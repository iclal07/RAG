import re

def clean_text(text):
    # Gereksiz karakterleri temizle
    text = re.sub(r'\s+', ' ', text)  # Fazla boşlukları temizle
    text = re.sub(r'\W+', ' ', text)  # Noktalama işaretlerini kaldır
    return text.lower()  # Hepsini küçük harfe çevir

# Belgeleri yükle
with open('data/documents.txt', 'r') as file:
    documents = file.readlines()

# Belgeleri temizle
cleaned_documents = [clean_text(doc) for doc in documents]

# Temizlenmiş belgeleri kaydet
with open('data/cleaned_documents.txt', 'w') as file:
    for doc in cleaned_documents:
        file.write(doc + '\n')

print("Belgeler temizlendi ve kaydedildi.")
