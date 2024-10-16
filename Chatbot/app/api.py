from fastapi import FastAPI
from app.models import search
from scripts.vectorize import load_documents, load_faiss_index
from app.models import load_model

app = FastAPI()

# FAISS endeksini ve belgeleri yükle
documents = load_documents()
index = load_faiss_index()
model = load_model()

@app.get("/chatbot/")
def get_response(query: str):
    """
    Sorguyu alır, en uygun cevabı döndürür.
    """
    results = search(query, model, index, documents)
    return {"response": results[0]}

