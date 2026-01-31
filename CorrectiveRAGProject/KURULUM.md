# Corrective RAG – Kurulum

## 1. Sanal ortam (venv)

Proje klasöründe:

```powershell
cd C:\Users\LENOVO\Desktop\llm\langchain_project\CorrectiveRAGProject
python -m venv venv
venv\Scripts\activate
```

## 2. Bağımlılıklar

```powershell
pip install -r requirements.txt
```

## 3. API anahtarları (.env)

`.env` dosyası projede hazır. İçindeki boş değerleri doldur:

| Değişken | Nereden alınır | Zorunlu |
|----------|----------------|---------|
| **OPENAI_API_KEY** | https://platform.openai.com/api-keys | Evet |
| **TAVILY_API_KEY** | https://tavily.com (ücretsiz hesap) | Evet |
| **USER_AGENT** | İsteğe bağlı (zaten dolu) | Hayır |

- **OPENAI_API_KEY**: OpenAI hesabından “API keys” bölümünde yeni anahtar oluştur; kopyalayıp `.env` içinde `OPENAI_API_KEY=` satırının sonuna yapıştır.
- **TAVILY_API_KEY**: Tavily’de kayıt ol, dashboard’dan API key al; `.env` içinde `TAVILY_API_KEY=` satırının sonuna yapıştır.

Örnek (gerçek anahtarları kendin yaz):

```
OPENAI_API_KEY=sk-proj-xxxx...
TAVILY_API_KEY=tvly-xxxx...
USER_AGENT=CorrectiveRAG/1.0
```

## 4. Vectorstore (ilk kez)

Belge arşivini oluşturmak için bir kez çalıştır:

```powershell
python ingestion.py
```

## 5. Çalıştırma

- Komut satırı: `python main.py`
- Web arayüzü: `python serve.py` → tarayıcıda http://localhost:8000
