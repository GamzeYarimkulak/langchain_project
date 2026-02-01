# LangChain Projeleri

Bu repository, LangChain ekosistemini öğrenmek için oluşturulmuş bir dizi proje içerir. Her proje, LangChain'in farklı özelliklerini ve kullanım senaryolarını gösterir.

## Proje Listesi

### 1. SetupProject
LangChain ve OpenAI API kullanımı için temel ortam kurulumu. API anahtarlarının güvenli yönetimi için `python-dotenv` kullanımı.

**Öğrenilenler:** Ortam değişkenleri yönetimi, güvenli API anahtarı kullanımı

---

### 2. LangchainFirstProject
LangChain kütüphanesine giriş projesi. Temel bileşenlerin (LLM, Prompt, Parser) adım adım öğrenilmesi.

**Öğrenilenler:** 
- ChatOpenAI modeli kullanımı
- Output parser'lar
- Prompt template'ler
- LangServe ile API oluşturma

---

### 3. VectorStoreProject
Vektör veritabanı kullanımının temelleri. Chroma vector store ile embedding ve semantic search.

**Öğrenilenler:**
- Embedding kavramı
- Vector store kullanımı
- Semantic search

---

### 4. VectoreStoreProject1
VectorStoreProject'in gelişmiş versiyonu. Kalıcı vector store, retriever ve RAG pattern'inin temel uygulaması.

**Öğrenilenler:**
- Retriever kullanımı
- Kalıcı vector store
- RAG pattern'inin temelleri
- Chain yapıları

---

### 5. RAGProject
Gerçek dünya verisi ile RAG uygulaması. Web sayfasından doküman yükleme, işleme ve soru-cevap sistemi.

**Öğrenilenler:**
- Web scraping ve doküman yükleme
- Text splitting stratejileri
- LangChain Hub kullanımı
- Streaming response

---

### 6. MessagingHistory
Chat uygulamalarında mesaj geçmişi yönetimi. Session bazlı konuşma takibi ve context preservation.

**Öğrenilenler:**
- Chat history yönetimi
- Session management
- MessagesPlaceholder kullanımı
- Context-aware chat

---

### 7. AgentProject
ReAct agent pattern'i ile akıllı arama aracı. LangGraph kullanarak web araması yapabilen agent.

**Öğrenilenler:**
- Agent pattern'i ve ReAct
- LangGraph checkpoint mekanizması
- Tool kullanımı
- Streaming agent responses

---

### 8. CorrectiveRAGProject ⭐
Gelişmiş RAG sistemi. Self-reflection mekanizması ekleyen, kendi kendini düzelten soru-cevap sistemi. Web arayüzü (React) ve demo içerir.

**Öğrenilenler:**
- LangGraph ile state machine
- Conditional routing
- Multi-step RAG
- Self-correction pattern
- Quality assurance katmanları

📷 **Çıktılar ve görseller:** [CorrectiveRAGProject/README.md](CorrectiveRAGProject/README.md#çıktılar-ve-görseller) — workflow grafiği, web arayüzü ve terminal çıktıları.

---

## Proje Yapısı

```
pycharm_projects/
├── SetupProject/
├── LangchainFirstProject/
├── VectorStoreProject/
├── VectoreStoreProject1/
├── RAGProject/
├── MessagingHistory/
├── AgentProject/
└── CorrectiveRAGProject/
```

## Genel Gereksinimler

- Python 3.8 veya üzeri
- OpenAI API anahtarı (çoğu proje için)
- Tavily API anahtarı (AgentProject ve CorrectiveRAGProject için)
- Her projenin kendi `requirements.txt` dosyası vardır

## Kurulum

Her proje için ayrı ayrı kurulum yapılmalıdır:

```bash
cd [ProjeAdı]
pip install -r requirements.txt
```

Ortam değişkenleri için `.env` dosyası oluşturun:

```
OPENAI_API_KEY=your_api_key_here
TAVILY_API_KEY=your_tavily_api_key  # Gerekli projeler için
```

## Öğrenme Yolu

Projeler, öğrenme yolculuğunu yansıtacak şekilde sıralanmıştır:

1. **SetupProject**: Temel kurulum ve ortam hazırlığı
2. **LangchainFirstProject**: LangChain'in temel bileşenlerini öğrenme
3. **VectorStoreProject**: Embedding ve vector store kavramları
4. **VectoreStoreProject1**: RAG pattern'inin temelleri
5. **RAGProject**: Gerçek dünya RAG uygulaması
6. **MessagingHistory**: Chat uygulamaları için geçmiş yönetimi
7. **AgentProject**: Agent pattern'i ve tool kullanımı
8. **CorrectiveRAGProject**: Gelişmiş RAG sistemi ve self-reflection

## Önemli Notlar

- Her proje bağımsız olarak çalıştırılabilir
- Projeler arasında bağımlılık yoktur (CorrectiveRAGProject hariç, kendi içinde tamamlanmıştır)
- Her projenin kendi README dosyası vardır, detaylar için ilgili klasöre bakın
- API anahtarlarınızı güvende tutun, `.env` dosyasını Git'e eklemeyin

## Katkıda Bulunma

Bu projeler eğitim amaçlıdır. İyileştirme önerileri ve hata bildirimleri memnuniyetle karşılanır.

## Lisans

Bu projeler eğitim amaçlıdır.

