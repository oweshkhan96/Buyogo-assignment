import json
import requests
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.db import connections
from django.db.utils import OperationalError
from .models import Booking, QueryHistory
from data_preprocessing import load_and_clean_data
from analytics import revenue_trends, cancellation_rate, geographical_distribution, lead_time_distribution
from rag import RAGPipeline

def get_all_bookings():
    return list(Booking.objects.all().values())

def get_booking_dataframe():

    bookings = get_all_bookings()
    if bookings:
        df = pd.DataFrame(bookings)
    else:
        # Fallback: load from CSV if database is empty
        CSV_PATH = 'hotel_bookings.csv'
        df = load_and_clean_data(CSV_PATH)
    return df

df = get_booking_dataframe()
rag_pipeline = RAGPipeline(df)

# --- API Endpoints ---

@csrf_exempt
def analytics_view(request):

    if request.method == 'POST':
        rev_trends = revenue_trends(df)
        cancel_rate = cancellation_rate(df)
        geo_dist = geographical_distribution(df)
        lead_time = lead_time_distribution(df)
        
        response_data = {
            "revenue_trends": rev_trends.to_dict(orient='records') if rev_trends is not None else "ADR data not available",
            "cancellation_rate": cancel_rate,
            "geographical_distribution": geo_dist.to_dict(orient='records'),
            "lead_time_distribution_summary": lead_time.describe().to_dict()
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

@csrf_exempt
def ask_view(request):

    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            query = body.get('query', '')
            if not query:
                return JsonResponse({"error": "Query not provided"}, status=400)
            answer = rag_pipeline.answer_query(query)
            QueryHistory.objects.create(query_text=query, answer_text=answer)
            return JsonResponse({"query": query, "answer": answer})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

def check_database():

    db_conn = connections['default']
    try:
        db_conn.cursor()
    except OperationalError:
        return False
    return True

def check_llm():

    test_prompt = "Hello"
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.1",
        "prompt": test_prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        if data.get("response", "").strip():
            return True
    except Exception:
        return False
    return False

@require_GET
def health_view(request):

    health_status = {
        "database": "up" if check_database() else "down",
        "llm": "up" if check_llm() else "down",
        "faiss_index": "up"  
    }
    overall_status = all(status == "up" for status in health_status.values())
    return JsonResponse({"status": "up" if overall_status else "down", "components": health_status})
