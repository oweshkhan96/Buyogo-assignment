
import numpy as np
import requests
from rag_index import create_dummy_embeddings, build_faiss_index, create_textual_data
from data_preprocessing import load_and_clean_data

def llama3_1_generate(prompt):
    url = "http://localhost:11434/api/generate"  
    payload = {
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        
        return data.get("response", "").strip()
    except Exception as e:
        return f"Error calling Ollama API: {str(e)}"

class RAGPipeline:
    def __init__(self, df):
        self.df = df
        
        self.texts = create_textual_data(df)
        
        self.embeddings = create_dummy_embeddings(self.texts)
        self.index = build_faiss_index(self.embeddings)
    
    def get_relevant_docs(self, query, k=3):
        
        np.random.seed(0)
        query_embedding = np.random.random((1, self.embeddings.shape[1])).astype("float32")
        distances, indices = self.index.search(query_embedding, k)
        relevant_texts = [self.texts[i] for i in indices[0]]
        return relevant_texts

    def answer_query(self, query):
        query_lower = query.lower()
        if "resort hotel" in query_lower:
            
            resort_df = self.df[self.df["hotel"].str.contains("Resort Hotel", case=False)]
            if resort_df.empty:
                return "No Resort Hotel records found."
            
            total = len(resort_df)
            cancelled = resort_df["is_canceled"].sum()
            cancellation_rate = (cancelled / total) * 100
            
            
            prompt = (
                f"Total bookings: {total}\n"
                f"Total cancellations: {cancelled}\n"
                f"Cancellation rate: {cancellation_rate:.2f}%\n\n"
                "Provide only the final answer as a percentage rounded to two decimal places, with no explanation.\nFinal Answer:"
            )
            llm_answer = llama3_1_generate(prompt)
            
            if not llm_answer or "%" not in llm_answer:
                return f"{cancellation_rate:.2f}%"
            else:
                return llm_answer
        elif "average price" in query_lower or "average cost" in query_lower:
            
            if "adr" not in self.df.columns:
                return "Price data is not available."
            avg_price = self.df["adr"].mean()
            prompt = (
                f"Calculated average price (adr) for hotel bookings: {avg_price:.2f}.\n\n"
                "Provide only the final answer as a number rounded to two decimal places with no explanation.\nFinal Answer:"
            )
            llm_answer = llama3_1_generate(prompt)
            if not llm_answer or not any(char.isdigit() for char in llm_answer):
                return f"{avg_price:.2f}"
            else:
                return llm_answer
        else:
            
            relevant_docs = self.get_relevant_docs(query)
            context = "\n".join(relevant_docs)
            prompt = (
                f"Question: {query}\n"
                f"Context:\n{context}\n\n"
                "Provide only the final answer with no explanation.\nFinal Answer:"
            )
            return llama3_1_generate(prompt)

if __name__ == '__main__':
    
    df = load_and_clean_data("hotel_bookings.csv")
    rag_pipeline = RAGPipeline(df)
    
    
    query = "What is the average price of a hotel booking?"
    answer = rag_pipeline.answer_query(query)
    print("Query:", query)
    print("Answer:", answer)
