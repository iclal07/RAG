import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import faiss
from app.models import load_model, search

# FAISS endeksini yükle
index = faiss.read_index('data/faiss_index.idx')

# Belgeleri tekrar yükle
with open('data/cleaned_documents.txt', 'r') as file:
    documents = file.readlines()

# Modeli yükle
model = load_model()

# Kullanıcıdan sorgu al
query = input("Sorgunuzu girin: ")

# Sorguyu çalıştır ve sonuçları getir
results = search(query, index, documents)

print("Sonuçlar:")
for result in results:
    print(result)

