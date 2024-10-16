from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Llama 3.2 modelini yerel dizinden yükleme
def load_llama_model(local_model_path: str):
    """
    Llama 3.2 modelini ve tokenizer'ı yerel dosya yolundan yükler.
    """
    print(f"Loading Llama model from local path: {local_model_path}")
    device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")
    
    # Model ve tokenizer'ı yerel dizinden yükle
    model = AutoModelForCausalLM.from_pretrained(local_model_path).to(device)
    tokenizer = AutoTokenizer.from_pretrained(local_model_path)
    
    return model, tokenizer

# Sorguyu Llama modeliyle cevaplama
def generate_response_llama(model, tokenizer, query: str):
    """
    Llama modeliyle verilen sorguya cevap üretir.
    """
    device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")
    
    # Sorguyu modelin anlayabileceği formatta tokenize et
    inputs = tokenizer(query, return_tensors="pt").to(device)
    
    # Model ile yanıt oluştur
    outputs = model.generate(**inputs, max_new_tokens=100)
    
    # Yanıtı tokenize edip string olarak döndür
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response

from sentence_transformers import SentenceTransformer

# Vektörleştirme modeli (Sentence-Transformers) yükleme
def load_vectorizer_model(model_name: str = 'all-MiniLM-L6-v2'):
    """
    Sentence-Transformers modelini yükler. Bu model belgeleri vektörleştirmek için kullanılır.
    """
    print(f"Loading vectorizer model: {model_name}")
    model = SentenceTransformer(model_name)
    return model

