Hotel Booking Analytics & Q&A API
This project processes hotel booking data, extracts insights, and enables retrieval-augmented question answering (RAG) using a local instance of the Ollama-powered llama3.1 model. The system provides analytics (e.g., revenue trends, cancellation rate, geographical distribution, booking lead time distribution) and answers natural language queries about hotel booking data.

Features
Data Preprocessing:
Cleans and structures hotel booking data (CSV or database).

Analytics & Reporting:

Revenue trends over time

Cancellation rate as percentage of total bookings

Geographical distribution of bookings

Booking lead time distribution

Retrieval-Augmented Question Answering (RAG):
Uses FAISS for vector indexing and a local LLM (llama3.1 via Ollama) for answering queries.

API Endpoints:

POST /analytics: Returns analytics reports.

POST /ask: Answers booking-related queries.

GET /health: Returns the health status of the system.

Bonus Features (Optional):

Real-time data updates via a database (e.g., SQLite, PostgreSQL)

Query history tracking

Health check endpoint

Prerequisites
Python 3.8+

Virtual environment (recommended)

Ollama installed and running with the llama3.1 model on port 11434

Required Python packages:

Django

pandas

numpy

matplotlib

seaborn

faiss-cpu

requests

Setup Instructions

1. Clone the Repository

```git clone <repo-url>
cd <repo-directory>
```

2. Create and Activate a Virtual Environment

```
python -m venv venv
```

On Windows:
```
venv\Scripts\activate
```

On macOS/Linux:
```
source venv/bin/activate
```

3. Install Required Packages
```
pip install -r requirements.txt
```

4. Setup the Django Project

Change into the Django project directory (e.g., hotelapi) and run the migrations:
```
python manage.py makemigrations
python manage.py migrate
```

5. Load Sample Data

Place your hotel_bookings.csv file in the root directory (or update the file path in data_preprocessing.py).

6. Run the Django Development Server

```
python manage.py runserver
```
Your server will run at http://127.0.0.1:8000/.

API Endpoints
POST /analytics
Description: Returns analytics reports including revenue trends, cancellation rate, geographical distribution, and booking lead time distribution.

Request Example:
```
curl -X POST http://127.0.0.1:8000/analytics
```
Response Example:
```
{
  "revenue_trends": [ /* Array of revenue records */ ],
  "cancellation_rate": 27.80,
  "geographical_distribution": [ /* Array of records by country */ ],
  "lead_time_distribution_summary": { /* Statistical summary */ }
}```

POST /ask
Description: Answers booking-related queries using the RAG pipeline.

Request Example (using Postman or curl):
```
curl -X POST http://127.0.0.1:8000/ask -H "Content-Type: application/json" -d '{"query": "What is the average price of a hotel booking?"}'
```
Response Example:
```
{
  "query": "What is the average price of a hotel booking?",
  "answer": "150.00"
}```


GET /health
Description: Checks the overall health of the system including database connection, LLM (Ollama) availability, and FAISS index status.

Request Example:

bash
Copy
Edit
curl -X GET http://127.0.0.1:8000/health
Response Example:

json
Copy
Edit
{
  "status": "up",
  "components": {
    "database": "up",
    "llm": "up",
    "faiss_index": "up"
  }
}
RAG Pipeline and LLM Integration
FAISS:
Used to index and retrieve relevant documents from hotel booking data (using dummy embeddings by default).

LLama3.1 via Ollama:
The system calls http://localhost:11434/api/generate to generate concise answers.

Prompt Instructions:
The prompts instruct the model to return only the final answer (e.g., "27.80%" for cancellation rate) without additional explanation.

Bonus Features
Real-Time Data Updates
Booking data is stored in a database (via Django models).

The system retrieves the latest data on each request, ensuring real-time updates.

Query History Tracking
Each query and its answer are stored in the QueryHistory model for auditing and debugging purposes.

Health Check Endpoint
The /health endpoint performs internal checks on the database, LLM, and FAISS index.

Testing the API
Use Postman or curl to test the endpoints. Example queries include:

Cancellation Rate:
{"query": "What is the cancellation rate for Resort Hotel?"}

Average Price:
{"query": "What is the average price of a hotel booking?"}

Revenue Trends:
{"query": "Show me total revenue for July 2017"}

Health Check:
GET http://127.0.0.1:8000/health

Troubleshooting
LLM Issues:
Ensure Ollama is running on http://localhost:11434 and the llama3.1 model is correctly loaded.

Data Issues:
Verify that hotel_bookings.csv contains all necessary fields (e.g., adr for average price).

API Errors:
Check the Django server logs for error details.

License
[Include license details here.]

Acknowledgements
Thanks to Ollama for the llama3.1 integration.

Thanks to Django, Pandas, FAISS, and other libraries.