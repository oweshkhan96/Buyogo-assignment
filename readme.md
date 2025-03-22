Hotel Booking Analytics & Q&A API


This project processes hotel booking data, extracts insights, and enables retrieval-augmented question answering (RAG) using a local instance of the Ollama-powered llama3.1 model. The system provides analytics (e.g., revenue trends, cancellation rates, geographical distribution, booking lead time distribution) and answers natural language queries about hotel booking data through a REST API built with Django.

Features:-

Data Preprocessing & Analytics:
```
Load, clean, and process hotel booking data from a CSV file.

Generate insights such as revenue trends, cancellation rates, geographical distribution, and booking lead time statistics.
```

Retrieval-Augmented Q&A (RAG):
```
Uses FAISS for vector indexing (with dummy embeddings by default).

Integrates with a local LLM (llama3.1 via Ollama) to answer booking-related questions with concise answers.
```

API Endpoints:
```
POST /analytics: Returns analytics reports.
```
```
POST /ask: Answers natural language queries about the data.
```
```
GET /health: Checks the overall health of the system (database, LLM, FAISS index).
```

Bonus Features:
```
Real-time data updates using a database (e.g., SQLite, PostgreSQL).

Query history tracking.

Health check endpoint.
```

Prerequisites
```
Python 3.8+

Virtual Environment (recommended)

Ollama installed and running with the llama3.1 model on port 11434
```

Required Python packages:
```
Django

pandas

numpy

matplotlib

seaborn

faiss-cpu

requests
```

Repository Setup Instructions

1. Clone the Repository
```
git clone https://github.com/oweshkhan96/Buyogo-assignment
cd Buyogo-assignment
```

2. Create and Activate a Virtual Environment

On Windows:
```
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```
python -m venv venv
source venv/bin/activate
```

3. Install Required Packages

```
pip install -r requirements.txt
```

4. Setup the Django Project

Navigate to your Django project directory (e.g., hotelapi) and run the migrations:
```
python manage.py makemigrations
python manage.py migrate
```

5. Load Sample Data

Place your hotel_bookings.csv file in the root directory (or update the file path in data_preprocessing.py accordingly).


Ollama & llama3.1 Setup
```
Install Ollama:
Follow the installation instructions on Ollama's website (for your operating system).
```

Pull the llama3.1 Model:

Open your terminal and run:
```
ollama pull llama3.1
```

This will download the llama3.1 model. Verify it's installed by running:

```
ollama list
```

Run Ollama:

Start Ollama to serve the API (default port is 11434):
```
ollama serve
```
Confirm it's running by visiting http://localhost:11434 in your browser.

API Endpoint Verification:
Verify that the API endpoint is accessible by using Postman (see below) or by issuing a test command. The project is configured to call the endpoint at http://localhost:11434/api/generate.

Running the Django Server
Once all setup steps are complete, start your Django development server:

```
python manage.py runserver
```
Your API will be available at http://127.0.0.1:8000/.

API Endpoints

```
POST /analytics
Description: Returns analytics reports (revenue trends, cancellation rate, geographical distribution, and booking lead time distribution).
```
```
POST /ask
Description: Answers booking-related natural language queries (e.g., "What is the average price of a hotel booking?") using the RAG pipeline and the locally integrated LLM.
```
```
GET /health
Description: Returns the overall health status of the system including the database, LLM, and FAISS index.
```

Testing the API Using Postman
1. Download & Install Postman
```
If you haven't installed Postman yet, download it from Postman’s website and install it on your system.
```
2. Launch Postman
```
Open the Postman application.
```
3. Setting Up Requests

A. Testing POST /analytics Endpoint

Create a New Request:

Click New > Request.

Name the request (e.g., "Hotel Analytics") and save it in a collection.

Configure the Request:
```
Method: Select POST.
```
```
URL: Enter http://127.0.0.1:8000/analytics.
```

Headers:
```
Go to the Headers tab.

Add a header:

Key: Content-Type

Value: application/json
```

Body:

Leave it empty

Expected Response: A JSON object with analytics data (e.g., revenue trends, cancellation rate, geographical distribution, and booking lead time summary).

B. Testing POST /ask Endpoint

Create a New Request:

Click New > Request.

Name it (e.g., "Hotel Q&A") and save it in a collection.

Configure the Request:
```
Method: Select POST.
```
```
URL: Enter http://127.0.0.1:8000/ask.
```
Headers:
```
In the Headers tab, add:

Key: Content-Type

Value: application/json
```
Body:
```
Click on the Body tab.

Select raw.

Choose JSON from the dropdown.

Enter a JSON payload with your query. For example:

{
  "query": "What is the average price of a hotel booking?"
}
```
Send the Request:

Click Send.

Expected Response: A JSON object with your query and a concise final answer (e.g., "150.00") returned by the RAG pipeline.

C. Testing GET /health Endpoint

Create a New Request:

Click New > Request.

Name it (e.g., "Health Check") and save it in a collection.

Configure the Request:
```
Method: Select GET.
```
```
URL: Enter http://127.0.0.1:8000/health.
```
Headers:
```
Optionally, add a header:

Key: Content-Type

Value: application/json
```
Send the Request:

Click Send.

Expected Response: A JSON object indicating the health status of each component (e.g., database, LLM, FAISS index):
```
{
  "status": "up",
  "components": {
    "database": "up",
    "llm": "up",
    "faiss_index": "up"
  }
}
```

Troubleshooting
Ollama / LLM Issues:

Ensure Ollama is running on http://localhost:11434 and the llama3.1 model is loaded.

Use Postman to test the LLM endpoint directly if needed.

Data Issues:

Verify that your hotel_bookings.csv file contains all required fields (e.g., adr for average price).

API Errors:

Check the Django server logs for error messages.

Ensure you are using the correct URL and request method in Postman.