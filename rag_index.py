
import numpy as np
import faiss
from data_preprocessing import load_and_clean_data

def create_dummy_embeddings(texts, dim=128):
    
    np.random.seed(42)
    return np.random.random((len(texts), dim)).astype('float32')

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def create_textual_data(df):
    
    texts = df.apply(
        lambda row: f"{row['hotel']} booking: {row['country']}, arrival on {row['arrival_date'].date()}, lead time {row['lead_time']} days, cancellation: {row['is_canceled']}",
        axis=1
    )
    return texts.tolist()

if __name__ == '__main__':
    df = load_and_clean_data('hotel_bookings.csv')
    texts = create_textual_data(df)
    embeddings = create_dummy_embeddings(texts)
    index = build_faiss_index(embeddings)
    print("FAISS index built with", index.ntotal, "vectors.")
