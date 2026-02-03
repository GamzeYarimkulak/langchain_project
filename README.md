# LangChain ile Sistem Odaklı LLM Projeleri

Bu repository, **LangChain** ve **LangGraph** kullanarak **sistem odaklı LLM uygulamaları** geliştirme sürecini adım adım ele alan bir proje koleksiyonudur.

Amaç; yalnızca tekil prompt veya basit zincirler kurmak değil, **karar verebilen**, **kendi çıktısını denetleyebilen** ve **gerektiğinde geri dönüp kendini düzeltebilen** LLM sistemleri tasarlamayı öğrenmektir.

Projeler, basit LangChain kullanımlarından başlayarak **Corrective RAG** gibi daha ileri seviye, **decision-based** mimarilere doğru ilerleyen bir öğrenme yolunu temsil eder.

---

## ⭐ Featured Project — CorrectiveRAGProject

Bu repository'nin merkezinde yer alan proje **CorrectiveRAGProject**'tir.

Bu proje, klasik RAG yaklaşımının sınırlamalarını ele alarak **kendi cevabını denetleyebilen** ve **gerekirse kendini düzelten** bir RAG sistemi kurmayı hedefler.

### Öne Çıkan Özellikler

- Query routing (vector store vs web search)
- Doküman relevance grading
- Kontrollü cevap üretimi (context-only generation)
- Self-check & corrective loop
- Bounded retries ile döngü kontrolü
- LangGraph ile state-based workflow

###  Çıktılar ve Görseller

- Workflow grafiği
- Web arayüzü (React)
- Terminal çıktıları

Detaylar için:  
`CorrectiveRAGProject/README.md`

---

##  Proje Listesi & Öğrenme Yolu

Projeler, **sistematik bir öğrenme akışını** yansıtacak şekilde sıralanmıştır:

### 1. SetupProject

LangChain ve OpenAI API kullanımı için temel ortam kurulumu.  
API anahtarlarının güvenli yönetimi için **python-dotenv** kullanımı.

**Öğrenilenler**
- Ortam değişkenleri yönetimi
- Güvenli API anahtarı kullanımı

---

### 2. LangchainFirstProject

LangChain kütüphanesine giriş.  
Temel bileşenlerin (LLM, Prompt, Parser) adım adım öğrenilmesi.

**Öğrenilenler**
- ChatOpenAI modeli kullanımı
- Prompt template'ler
- Output parser'lar
- LangServe ile API oluşturma

---

### 3. VectorStoreProject

Vektör veritabanı kullanımının temelleri.  
**Chroma** ile embedding ve semantic search.

**Öğrenilenler**
- Embedding kavramı
- Vector store kullanımı
- Semantic search

---

### 4. VectorStoreProject1

VectorStoreProject'in gelişmiş versiyonu.  
Kalıcı vector store ve temel **RAG pattern**'i.

**Öğrenilenler**
- Retriever kullanımı
- Kalıcı vector store
- RAG pattern'inin temelleri
- Chain yapıları

---

### 5. RAGProject

Gerçek dünya verisi ile RAG uygulaması.  
Web sayfasından doküman yükleme ve soru-cevap sistemi.

**Öğrenilenler**
- Web doküman yükleme
- Text splitting stratejileri
- LangChain Hub kullanımı
- Streaming response

---

### 6. MessagingHistory

Chat uygulamalarında mesaj geçmişi yönetimi.  
Session bazlı konuşma takibi.

**Öğrenilenler**
- Chat history yönetimi
- Session management
- Context-aware chat

---

### 7. AgentProject

**ReAct agent pattern**'i ile web araması yapabilen agent sistemi.

**Öğrenilenler**
- Agent pattern'i ve ReAct
- Tool kullanımı
- LangGraph checkpoint yapısı
- Streaming agent responses

---

### 8. CorrectiveRAGProject ⭐

Decision-based, self-correcting RAG sistemi.  
Web arayüzü (React) ve demo içerir.

**Öğrenilenler**
- LangGraph ile state machine yaklaşımı
- Conditional routing
- Multi-step RAG
- Self-correction & quality assurance katmanları

---

##  Proje Yapısı
```text
projects/
├── SetupProject/
├── LangchainFirstProject/
├── VectorStoreProject/
├── VectorStoreProject1/
├── RAGProject/
├── MessagingHistory/
├── AgentProject/
└── CorrectiveRAGProject/
```

---

## Genel Gereksinimler

- Python 3.8+
- OpenAI API anahtarı
- Tavily API anahtarı (AgentProject ve CorrectiveRAGProject için)

Her projenin kendi `requirements.txt` dosyası vardır.

---

## Kurulum (Genel)
```bash
cd <ProjectName>
pip install -r requirements.txt
```

`.env` dosyası oluşturun:
```bash
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
```

---

## Notlar

- Her proje bağımsız olarak çalıştırılabilir
- Projeler arası doğrudan bağımlılık yoktur
- API anahtarlarını `.env` dosyasında tutun ve GitHub'a eklemeyin
- Detaylı açıklamalar her projenin kendi `README.md` dosyasında yer alır
