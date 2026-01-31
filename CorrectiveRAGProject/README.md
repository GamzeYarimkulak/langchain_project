# CorrectiveRAGProject

Gelişmiş RAG (Retrieval Augmented Generation) sistemi. Bu proje, LangGraph kullanarak self-reflection mekanizması ekleyen, kendi kendini düzelten bir soru-cevap sistemi oluşturur.

## Genel Bakış

CorrectiveRAGProject, geleneksel RAG sistemlerinin ötesine geçer. Sistem, soruları otomatik olarak yönlendirir, dokümanları değerlendirir, web araması yapar ve üretilen cevapları çoklu katmanlarda kontrol eder. Eğer cevap yetersizse, sistem otomatik olarak kendini düzeltir.

## Temel Özellikler

- **Akıllı Yönlendirme**: Sorular otomatik olarak vectorstore veya web search'e yönlendirilir
- **Doküman Değerlendirme**: Getirilen dokümanların soruyla ilgili olup olmadığı kontrol edilir
- **Web Arama Entegrasyonu**: Vectorstore'da yeterli bilgi yoksa otomatik web araması yapılır
- **Çoklu Kalite Kontrolü**: Hallucination check, answer quality check gibi katmanlar
- **Self-Correction**: Yetersiz cevaplar otomatik olarak düzeltilir
- **State Machine**: LangGraph ile karmaşık workflow yönetimi

## Proje Yapısı

```
CorrectiveRAGProject/
├── main.py                 # Ana uygulama giriş noktası
├── ingestion.py            # Veri yükleme ve vectorstore oluşturma
├── graph/
│   ├── graph.py           # Ana workflow grafiği
│   ├── state.py           # State tanımlamaları
│   ├── node_constants.py  # Node isimleri
│   ├── nodes/             # İş mantığı node'ları
│   │   ├── generate.py
│   │   ├── retrieve.py
│   │   ├── grade_documents.py
│   │   └── web_search.py
│   └── chains/            # LLM chain'leri
│       ├── router.py
│       ├── retrieval_grader.py
│       ├── hallucination_grader.py
│       ├── answer_grader.py
│       └── generation.py
├── graph.png              # Workflow görselleştirmesi
└── requirements.txt
```

## Kurulum

### 1. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 2. Ortam Değişkenlerini Ayarlayın

`.env` dosyası oluşturun:

```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 3. Vectorstore'u Oluşturun

İlk çalıştırmada vectorstore'u oluşturmanız gerekir:

```bash
python ingestion.py
```

Bu komut:
- 3 farklı web sayfasından doküman yükler
- Dokümanları chunk'lara böler
- Chroma vectorstore oluşturur
- `.chroma` klasörüne kalıcı olarak kaydeder

## Kullanım

### Temel Kullanım

```bash
python main.py
```

Bu komut, örnek bir soru ile sistemi test eder.

### Web arayüzü

Soruyu yazıp süreci (belge mi, web mi kullanıldığı) ve cevabı görmek için:

```bash
pip install fastapi uvicorn
python serve.py
```

Tarayıcıda http://localhost:8000 adresine gidin. Sorunuzu yazıp gönderin; sayfada önce süreç adımları (soru analizi, belge arşivi / web araması, cevap hazırlama) listelenir, en altta cevap metni görünür.

### Özelleştirilmiş Kullanım

`main.py` dosyasını düzenleyerek farklı sorular sorabilirsiniz:

```python
result = app.invoke(input={"question": "Your question here"})
print(result)
```

## Workflow Açıklaması

### 1. Query Analysis (Soru Analizi)

Sistem, gelen soruyu analiz eder ve en uygun yolu seçer:

- **Vectorstore'a yönlendir**: Soru, index'teki konularla ilgiliyse (agents, prompt engineering, adversarial attacks)
- **Web Search'e yönlendir**: Soru, index dışındaysa

### 2. Retrieve (Doküman Getirme)

Vectorstore'dan semantic search yaparak ilgili dokümanlar getirilir.

### 3. Grade Documents (Doküman Değerlendirme)

Getirilen dokümanların soruyla ilgili olup olmadığı kontrol edilir:

- Her doküman için LLM ile değerlendirme yapılır
- İlgisiz dokümanlar filtrelenir
- Eğer hiç ilgili doküman yoksa → Web search tetiklenir

### 4. Generate (Cevap Üretme)

Context ve question birleştirilerek LLM ile cevap üretilir.

### 5. Hallucination Check (Halüsinasyon Kontrolü)

Üretilen cevabın dokümanlara dayalı olup olmadığı kontrol edilir:

- Cevap dokümanlara dayalı değilse → Re-write question → Retrieve (döngü)

### 6. Answer Quality Check (Cevap Kalite Kontrolü)

Cevabın soruyu gerçekten cevaplayıp cevaplamadığı kontrol edilir:

- Cevap yetersizse → Re-write question → Retrieve (döngü)
- Cevap yeterliyse → END

### 7. Web Search (Web Arama)

Gerekli durumlarda Tavily API ile web'de arama yapılır ve sonuçlar dokümanlara eklenir.

## Bileşenler

### State Yönetimi

`GraphState` sınıfı, workflow boyunca taşınan verileri tanımlar:

```python
class GraphState(TypedDict):
    question: str          # Kullanıcı sorusu
    generation: str        # LLM tarafından üretilen cevap
    web_search: bool      # Web araması yapılması gerekip gerekmediği
    documents: List[str]   # İlgili dokümanlar
```

### Node'lar

#### Retrieve Node
Vectorstore'dan semantic search yapar ve ilgili dokümanları getirir.

#### Grade Documents Node
Her dokümanı değerlendirir ve ilgili olanları filtreler. İlgili doküman yoksa web search'i tetikler.

#### Generate Node
Context ve question'ı birleştirerek LLM ile cevap üretir.

#### Web Search Node
Tavily API kullanarak web'de arama yapar ve sonuçları dokümanlara ekler.

### Chain'ler

#### Router Chain
Soruyu analiz edip vectorstore veya web search'e yönlendirir. Structured output kullanır.

#### Retrieval Grader Chain
Bir dokümanın soruyla ilgili olup olmadığını değerlendirir.

#### Hallucination Grader Chain
Üretilen cevabın dokümanlara dayalı olup olmadığını kontrol eder.

#### Answer Grader Chain
Cevabın soruyu gerçekten cevaplayıp cevaplamadığını kontrol eder.

#### Generation Chain
LangChain Hub'dan RAG prompt'u çekerek cevap üretir.

## Örnek Senaryolar

### Senaryo 1: Vectorstore'da Bilgi Var

1. Soru gelir → Query Analysis → Vectorstore'a yönlendirilir
2. Retrieve → İlgili dokümanlar getirilir
3. Grade Documents → Dokümanlar değerlendirilir
4. Generate → Cevap üretilir
5. Hallucination Check → Cevap kontrol edilir
6. Answer Quality Check → Cevap yeterliyse END

### Senaryo 2: Vectorstore'da Bilgi Yok

1. Soru gelir → Query Analysis → Vectorstore'a yönlendirilir
2. Retrieve → Dokümanlar getirilir
3. Grade Documents → Hiç ilgili doküman yok → Web Search tetiklenir
4. Web Search → Web'de arama yapılır
5. Generate → Web sonuçlarıyla cevap üretilir
6. Kontroller → Cevap yeterliyse END

### Senaryo 3: Self-Correction

1. Cevap üretilir
2. Hallucination Check → Cevap dokümanlara dayalı değil
3. Re-write question → Soru yeniden yazılır
4. Retrieve → Yeni dokümanlar getirilir
5. Generate → Yeni cevap üretilir
6. Tekrar kontrol edilir

## Gereksinimler

- Python 3.8+
- OpenAI API anahtarı
- Tavily API anahtarı (web search için)
- Tüm bağımlılıklar `requirements.txt` dosyasında listelenmiştir

## Özelleştirme

### Farklı Veri Kaynakları

`ingestion.py` dosyasındaki URL'leri değiştirerek farklı veri kaynakları ekleyebilirsiniz:

```python
urls = [
    "https://your-url-1.com",
    "https://your-url-2.com",
    # ...
]
```

### Chunk Ayarları

Chunk size ve overlap değerlerini ayarlayabilirsiniz:

```python
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250,  # İstediğiniz boyut
    chunk_overlap=0   # Overlap miktarı
)
```

### Router Ayarları

`graph/chains/router.py` dosyasındaki system prompt'u düzenleyerek router'ın hangi konuları vectorstore'a yönlendireceğini belirleyebilirsiniz.

## Sorun Giderme

### Vectorstore Bulunamıyor

Eğer vectorstore bulunamazsa, önce `ingestion.py` dosyasını çalıştırın.

### Tavily API Hatası

Tavily API anahtarınızın `.env` dosyasında doğru ayarlandığından emin olun.

### Import Hataları

Tüm bağımlılıkların yüklendiğinden emin olun:

```bash
pip install -r requirements.txt
```

## Geliştirme Notları

- Her node bağımsız olarak test edilebilir
- State yönetimi LangGraph tarafından otomatik yapılır
- Conditional routing ile akıllı karar verme sağlanır
- Self-correction mekanizması döngüsel iyileştirme yapar

## Gelecek Geliştirmeler

- Retry mekanizması eklenebilir
- Caching mekanizması eklenebilir
- Detaylı logging ve monitoring
- Web arayüzü veya API endpoint'leri
- Farklı LLM modelleri ile test

## Lisans

Bu proje eğitim amaçlıdır.

