import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models import load_model, create_faiss_index
import faiss
import numpy as np

# Belgeleri temizlenmiş dosyadan yükle
with open('data/cleaned_documents.txt', 'r') as file:
    documents = file.readlines()

# Modeli yükle (MiniLM veya Llama gibi bir model kullanabilirsin)
model = load_model()

# Belgeleri vektörleştir
document_embeddings = model.encode(documents)

# FAISS endeksini oluştur
index = create_faiss_index(np.array(document_embeddings))

# FAISS endeksini kaydet
faiss.write_index(index, 'data/faiss_index.idx')

print("Belgeler vektörleştirildi ve FAISS endeksi oluşturuldu.")
