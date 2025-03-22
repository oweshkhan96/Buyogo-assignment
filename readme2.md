## Sample Test Queries & Expected Answers

### Query 1: Cancellation Rate for Resort Hotel
**Request:**
```
{
  "query": "What is the cancellation rate for Resort Hotel?"
}
```
**Expected response:**
```
{
  "query": "What is the cancellation rate for Resort Hotel?",
  "answer": "27.80%"
}
```
### Query 2: Average Price of a Hotel Booking

```
{
  "query": "What is the average price of a hotel booking?"
}
```
**Expected Response:**
```
{
  "query": "What is the average price of a hotel booking?",
  "answer": "150.00"
}

```

### Query 3: Locations with Highest Booking Cancellations
**Request:**
```
{
  "query": "Which locations had the highest booking cancellations?"
}
```
**Expected Response:**

```
{
  "query": "Which locations had the highest booking cancellations?",
  "answer": "PRT"
}
```
### Short Report: Implementation Choices & Challenges

## Implementation Choices:

    Framework & Tools: Used Django for building REST APIs, Pandas and NumPy for data processing, FAISS for vector retrieval, and Ollama with llama3.1 as the local LLM.

    Modular Design: Separated the project into modules for data preprocessing, analytics, and the RAG pipeline to ensure clear separation of concerns.

    Prompt Engineering: Crafted prompts to instruct the LLM to return only a concise final answer (e.g., “27.80%”) without extra explanation.

    Fallback Mechanisms: Implemented logic to return computed values directly when the LLM’s response is ambiguous or incomplete.

## Challenges:

    Data Quality: Handling missing values and inconsistencies in the CSV data required robust preprocessing.

    Prompt Tuning: Iteratively refining prompts to consistently obtain short, direct answers from the LLM was a key challenge.

    LLM Integration: Ensuring reliable communication with the Ollama API and managing error handling was essential.

    Retrieval Accuracy: Using dummy embeddings with FAISS provided a baseline; integrating a proper embedding model is needed for improved retrieval in production.