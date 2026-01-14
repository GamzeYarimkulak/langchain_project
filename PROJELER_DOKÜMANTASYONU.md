# Projeler Dokümantasyonu

Bu doküman, pycharm_projects klasöründeki tüm projelerin detaylı açıklamasını içermektedir. Özellikle **CorrectiveRAGProject** projesi üzerinde durulmuştur.

---

## 📁 Proje Klasörleri Genel Bakış

### 1. SetupProject
### 2. LangchainFirstProject
### 3. VectorStoreProject
### 4. VectoreStoreProject1
### 5. RAGProject
### 6. MessagingHistory
### 7. AgentProject
### 8. **CorrectiveRAGProject** ⭐ (Ana Proje)

---

## 1. SetupProject

### Amaç
LangChain projeleri için temel ortam kurulumu ve yapılandırması.

### Yapılanlar
- `.env` dosyasından ortam değişkenlerini yükleme (`python-dotenv` kullanarak)
- `OPENAI_API_KEY` gibi API anahtarlarının güvenli bir şekilde yönetilmesi
- Ortam değişkenlerinin doğru şekilde yüklendiğini test etme

### Dosya: `main.py`
```python
from dotenv import load_dotenv, dotenv_values

load_dotenv()

print(dotenv_values(".env").get("OPENAI_API_KEY"))
print(dotenv_values(".env"))
```

### Öğrenilenler
- Ortam değişkenlerinin güvenli yönetimi
- `.env` dosyası kullanımı
- API anahtarlarının kod içinde hardcode edilmemesi gerektiği

---

## 2. LangchainFirstProject

### Amaç
LangChain kütüphanesinin temel kullanımını öğrenmek ve adım adım gelişmek.

### Yapılanlar

#### a) `simplemessage.py` - Temel Mesajlaşma
- OpenAI ChatOpenAI modeli ile basit mesaj gönderme
- System ve Human mesajları kullanımı
- Model çağrısı ve yanıt alma

#### b) `simplemessagewithoutputparser.py` - Output Parser Ekleme
- `StrOutputParser` kullanarak model çıktısını string'e dönüştürme
- Chain yapısı oluşturma (`model | parser`)
- Daha temiz ve kullanılabilir çıktı alma

#### c) `simplemessagewithtemplates.py` - Prompt Template Kullanımı
- `ChatPromptTemplate` ile dinamik prompt'lar oluşturma
- Parametreli prompt'lar (örneğin: `{language}`, `{text}`)
- Tam chain yapısı: `prompt_template | model | parser`

#### d) `serve.py` - FastAPI ile Servis Oluşturma
- LangChain chain'ini FastAPI ile servis haline getirme
- `langserve` kullanarak REST API oluşturma
- Çeviri uygulaması örneği

### Öğrenilenler
- LangChain'in temel bileşenleri (LLM, Prompt, Parser)
- Chain yapısı ve pipe operatörü (`|`)
- Prompt template'lerin kullanımı
- LangServe ile API servisi oluşturma

---

## 3. VectorStoreProject

### Amaç
Vektör veritabanı (vector store) kullanımını öğrenmek.

### Yapılanlar
- Chroma vektör veritabanı kurulumu
- OpenAI embeddings kullanarak dokümanları vektörleştirme
- Benzerlik araması (similarity search) yapma

### Dosya: `main.py`
- 5 adet örnek doküman oluşturuldu (köpek, kedi, balık, papağan, tavşan hakkında)
- `OpenAIEmbeddings` ile dokümanlar vektörleştirildi
- Chroma vectorstore'a kaydedildi
- "dog" kelimesi için benzerlik araması yapıldı

### Öğrenilenler
- Embedding kavramı
- Vektör veritabanı kullanımı
- Semantic search (anlamsal arama)

---

## 4. VectoreStoreProject1

### Amaç
VectorStoreProject'in gelişmiş versiyonu - Retriever ve Chain yapısı.

### Yapılanlar
- Chroma vectorstore'un kalıcı hale getirilmesi (`persist_directory`)
- Retriever oluşturma ve `RunnableLambda` kullanımı
- Retriever + LLM + Prompt ile tam bir RAG chain'i oluşturma
- Context ve question'ı birleştirerek cevap üretme

### Dosya: `main.py`
- Dokümanlar kalıcı olarak `chroma_store` klasörüne kaydedildi
- Retriever, k=1 ile en benzer dokümanı getiriyor
- Custom prompt template ile context ve question birleştirildi
- Chain: `{"context": retriever, "question": RunnablePassthrough()} | prompt | llm`

### Öğrenilenler
- Retriever kavramı ve kullanımı
- RAG (Retrieval Augmented Generation) pattern'i
- Context ve question'ın birleştirilmesi
- Kalıcı vectorstore oluşturma

---

## 5. RAGProject

### Amaç
Gerçek dünya verisi ile RAG uygulaması oluşturmak.

### Yapılanlar
- Web sayfasından doküman yükleme (`WebBaseLoader`)
- BeautifulSoup ile HTML parsing
- Dokümanları chunk'lara bölme (`RecursiveCharacterTextSplitter`)
- LangChain Hub'dan hazır RAG prompt'u çekme
- Streaming response ile cevap üretme

### Dosya: `main.py`
- Lilian Weng'in "Agent" blog yazısı yüklendi
- Dokümanlar 1000 karakterlik chunk'lara bölündü (200 karakter overlap ile)
- LangChain Hub'dan `rlm/rag-prompt` kullanıldı
- Streaming ile kullanıcıya anlık cevap gösterildi

### Öğrenilenler
- Web scraping ve doküman yükleme
- Text splitting stratejileri
- LangChain Hub kullanımı
- Streaming response

---

## 6. MessagingHistory

### Amaç
Chat uygulamalarında mesaj geçmişi yönetimi.

### Yapılanlar
- `InMemoryChatMessageHistory` ile mesaj geçmişi saklama
- `RunnableWithMessageHistory` ile chain'e geçmiş ekleme
- Session ID bazlı geçmiş yönetimi
- `MessagesPlaceholder` ile dinamik mesaj geçmişi

### Dosya: `main.py`
- Her session için ayrı geçmiş saklanıyor
- Kullanıcı ve AI mesajları otomatik olarak geçmişe ekleniyor
- Interactive chat loop oluşturuldu

### Öğrenilenler
- Chat history yönetimi
- Session bazlı konuşma takibi
- `MessagesPlaceholder` kullanımı

---

## 7. AgentProject

### Amaç
ReAct agent pattern'i ile akıllı arama aracı oluşturmak.

### Yapılanlar
- Tavily Search API entegrasyonu
- LangGraph checkpoint mekanizması (`SqliteSaver`)
- ReAct agent oluşturma (`create_react_agent`)
- Agent executor ile streaming response
- Thread ID bazlı checkpoint yönetimi

### Dosya: `main.py`
- Tavily search tool'u agent'a eklendi
- LangChain Hub'dan ReAct prompt'u çekildi
- Memory checkpoint ile konuşma geçmişi saklandı
- Streaming ile kullanıcıya anlık düşünce süreci gösterildi

### Öğrenilenler
- Agent pattern'i ve ReAct
- Tool kullanımı
- Checkpoint ve memory yönetimi
- Streaming agent responses

---

## 8. CorrectiveRAGProject ⭐

### Genel Bakış
**CorrectiveRAGProject**, gelişmiş bir RAG (Retrieval Augmented Generation) sistemidir. Bu proje, LangGraph kullanarak karmaşık bir decision-making workflow'u oluşturur. Sistem, soruları otomatik olarak yönlendirir, dokümanları değerlendirir, web araması yapar ve üretilen cevapları doğrular.

### Mimari
Proje, **state machine** (durum makinesi) pattern'i kullanır. Her node (düğüm) belirli bir görevi yerine getirir ve sistem, conditional routing (koşullu yönlendirme) ile akıllı kararlar verir.

### Proje Yapısı

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
└── requirements.txt
```

---

### Detaylı Bileşen Açıklamaları

#### 1. State Yönetimi (`graph/state.py`)

**GraphState** sınıfı, workflow boyunca taşınan verileri tanımlar:

```python
class GraphState(TypedDict):
    question: str          # Kullanıcı sorusu
    generation: str        # LLM tarafından üretilen cevap
    web_search: bool      # Web araması yapılması gerekip gerekmediği
    documents: List[str]   # İlgili dokümanlar
```

**Önemi**: State, tüm node'lar arasında veri paylaşımını sağlar. Her node, state'i okuyup güncelleyebilir.

---

#### 2. Ingestion (`ingestion.py`)

**Amaç**: Vectorstore'u oluşturmak ve retriever'ı hazırlamak.

**Yapılanlar**:
- 3 farklı web sayfasından doküman yükleme:
  - Agent blog yazısı
  - Prompt engineering blog yazısı
  - Adversarial attacks on LLMs blog yazısı
- Dokümanları 250 karakterlik chunk'lara bölme (overlap: 0)
- Chroma vectorstore oluşturma ve kalıcı hale getirme
- Retriever oluşturma

**Özellikler**:
- `tiktoken` encoder kullanarak token bazlı splitting
- `.chroma` klasörüne kalıcı kayıt
- `rag-chroma` collection adı ile organize edilmiş

---

#### 3. Node'lar (`graph/nodes/`)

##### a) Retrieve Node (`retrieve.py`)

**Görev**: Kullanıcı sorusuna göre vectorstore'dan ilgili dokümanları getirmek.

**İşleyiş**:
```python
def retrieve(state: GraphState) -> Dict[str, Any]:
    question = state["question"]
    documents = retriever.invoke(question)
    return {"question": question, "documents": documents}
```

- Vectorstore'dan semantic search yapar
- En ilgili dokümanları döndürür
- State'e dokümanları ekler

---

##### b) Grade Documents Node (`grade_documents.py`)

**Görev**: Getirilen dokümanların soruyla ilgili olup olmadığını değerlendirmek.

**İşleyiş**:
- Her doküman için `retrieval_grader` chain'i çalıştırılır
- LLM, dokümanın soruyla ilgili olup olmadığını "yes" veya "no" olarak değerlendirir
- İlgili olmayan dokümanlar filtrelenir
- Eğer hiç ilgili doküman kalmazsa, `web_search` flag'i `True` yapılır

**Önemi**: Bu adım, gereksiz veya yanlış dokümanların cevap üretiminde kullanılmasını önler.

---

##### c) Web Search Node (`web_search.py`)

**Görev**: Vectorstore'da yeterli bilgi yoksa web'de arama yapmak.

**İşleyiş**:
- Tavily Search API kullanılır
- Kullanıcı sorusu için web'de arama yapılır
- En iyi 3 sonuç alınır
- Sonuçlar Document formatına dönüştürülür ve mevcut dokümanlara eklenir

**Özellikler**:
- Tavily'nin farklı response formatlarını handle eder
- Web sonuçları doküman listesine eklenir
- Metadata ile kaynak bilgisi saklanır

---

##### d) Generate Node (`generate.py`)

**Görev**: Context ve question'ı kullanarak LLM ile cevap üretmek.

**İşleyiş**:
- Tüm dokümanlar birleştirilerek context oluşturulur
- LangChain Hub'dan `rlm/rag-prompt` kullanılır
- LLM'e context ve question gönderilir
- Üretilen cevap state'e eklenir

---

#### 4. Chain'ler (`graph/chains/`)

##### a) Router Chain (`router.py`)

**Görev**: Soruyu analiz edip vectorstore veya web search'e yönlendirmek.

**Yapı**:
- Structured output ile `RouteQuery` modeli kullanılır
- LLM, sorunun vectorstore'daki konularla ilgili olup olmadığını değerlendirir
- Vectorstore konuları: agents, prompt engineering, adversarial attacks on LLMs
- Diğer konular için web search'e yönlendirilir

**Önemi**: Gereksiz web aramalarını önler ve performansı artırır.

---

##### b) Retrieval Grader Chain (`retrieval_grader.py`)

**Görev**: Bir dokümanın soruyla ilgili olup olmadığını değerlendirmek.

**Yapı**:
- `GradeDocuments` structured output modeli
- Binary score: "yes" veya "no"
- Her doküman için ayrı ayrı değerlendirme yapılır

---

##### c) Hallucination Grader Chain (`hallucination_grader.py`)

**Görev**: Üretilen cevabın dokümanlara dayalı olup olmadığını kontrol etmek.

**Yapı**:
- `GradeHallucination` structured output modeli
- Binary score: "yes" (grounded) veya "no" (hallucination)
- Dokümanlar ve üretilen cevap karşılaştırılır

**Önemi**: LLM'in kendi bilgisinden uydurma yapmasını önler.

---

##### d) Answer Grader Chain (`answer_grader.py`)

**Görev**: Üretilen cevabın soruyu gerçekten cevaplayıp cevaplamadığını kontrol etmek.

**Yapı**:
- `GradeAnswer` structured output modeli
- Binary score: "yes" (answers question) veya "no" (doesn't answer)
- Soru ve cevap birlikte değerlendirilir

**Önemi**: Cevabın soruyla alakalı olmasını garanti eder.

---

##### e) Generation Chain (`generation.py`)

**Görev**: RAG prompt'u ile cevap üretmek.

**Yapı**:
- LangChain Hub'dan `rlm/rag-prompt` çekilir
- LLM ve StrOutputParser ile chain oluşturulur
- Context ve question parametreleri kullanılır

---

#### 5. Ana Workflow (`graph/graph.py`)

**Workflow Yapısı**:

```
[Entry Point]
    |
    v
[Route Question] ──┬──> [Web Search] ──> [Generate]
    |              |
    └──> [Retrieve] ──> [Grade Documents] ──┬──> [Generate]
                                             |
                                             └──> [Web Search] ──> [Generate]
                                                                        |
                                                                        v
                                                              [Grade Generation]
                                                                        |
                                                                        ├──> "useful" ──> [END]
                                                                        ├──> "not useful" ──> [Web Search]
                                                                        └──> "not supported" ──> [Web Search]
```

**Routing Fonksiyonları**:

1. **`route_question`**: İlk yönlendirme
   - Soruyu analiz eder
   - Vectorstore veya Web Search'e yönlendirir

2. **`decide_to_generate`**: Doküman değerlendirmesi sonrası
   - Eğer ilgili doküman varsa → Generate
   - Yoksa → Web Search

3. **`grade_generation_grounded_in_documents_and_question`**: Cevap değerlendirmesi
   - Hallucination kontrolü
   - Soru cevaplama kontrolü
   - 3 durum döner:
     - `"useful"`: Cevap kabul edilebilir → END
     - `"not useful"`: Cevap soruyu cevaplamıyor → Web Search
     - `"not supported"`: Cevap dokümanlara dayalı değil → Web Search

**Özellikler**:
- Conditional edges ile akıllı yönlendirme
- Self-correction mekanizması (cevap yetersizse tekrar web search)
- Graph görselleştirmesi (`graph.png`)

---

### Workflow Akış Senaryoları

#### Senaryo 1: Vectorstore'da Bilgi Var
1. Soru gelir → `route_question` → Vectorstore'a yönlendirilir
2. `retrieve` → İlgili dokümanlar getirilir
3. `grade_documents` → Dokümanlar değerlendirilir
4. İlgili dokümanlar varsa → `generate` → Cevap üretilir
5. `grade_generation` → Cevap kontrol edilir
6. Cevap yeterliyse → END

#### Senaryo 2: Vectorstore'da Bilgi Yok
1. Soru gelir → `route_question` → Vectorstore'a yönlendirilir
2. `retrieve` → Dokümanlar getirilir
3. `grade_documents` → Hiç ilgili doküman yok → `web_search = True`
4. `web_search` → Web'de arama yapılır
5. `generate` → Web sonuçlarıyla cevap üretilir
6. `grade_generation` → Cevap kontrol edilir
7. Cevap yeterliyse → END

#### Senaryo 3: Web Search Gerekli
1. Soru gelir → `route_question` → Web Search'e yönlendirilir (konu dışı)
2. `web_search` → Web'de arama yapılır
3. `generate` → Cevap üretilir
4. `grade_generation` → Cevap kontrol edilir
5. Cevap yeterliyse → END

#### Senaryo 4: Self-Correction
1. Cevap üretilir
2. `grade_generation` → Cevap yetersiz bulunur
3. `web_search` → Tekrar web araması yapılır
4. `generate` → Yeni cevap üretilir
5. Tekrar kontrol edilir

---

### Kullanılan Teknolojiler

- **LangGraph**: State machine ve workflow yönetimi
- **LangChain**: LLM chain'leri ve prompt yönetimi
- **Chroma**: Vector database
- **OpenAI**: Embeddings ve LLM
- **Tavily**: Web search API
- **LangChain Hub**: Hazır prompt'lar

---

### Projenin Güçlü Yönleri

1. **Akıllı Yönlendirme**: Sorular otomatik olarak en uygun kaynağa yönlendirilir
2. **Kalite Kontrolü**: Çoklu değerlendirme katmanları (document grading, hallucination check, answer grading)
3. **Self-Correction**: Yetersiz cevaplar otomatik olarak düzeltilir
4. **Esneklik**: Farklı veri kaynakları (vectorstore + web) entegre edilmiştir
5. **Modüler Yapı**: Her bileşen bağımsız olarak test edilebilir

---

### Öğrenilenler

1. **LangGraph ile State Machine**: Karmaşık workflow'ların yönetimi
2. **Conditional Routing**: Koşullu yönlendirme ile akıllı karar verme
3. **Structured Output**: LLM'den yapılandırılmış çıktı alma
4. **Multi-Step RAG**: Geleneksel RAG'in ötesinde, çok adımlı doğrulama
5. **Self-Correction Pattern**: Sistemin kendi hatalarını düzeltmesi
6. **Quality Assurance**: Çoklu kontrol katmanları ile kalite garantisi

---

### Kullanım

```python
from graph.graph import app

result = app.invoke(input={"question": "What is your name?"})
print(result)
```

---

### Geliştirme Önerileri

1. **Retry Mekanizması**: Başarısız denemeler için retry limit eklenebilir
2. **Caching**: Aynı sorular için cache mekanizması
3. **Logging**: Detaylı loglama ve monitoring
4. **Error Handling**: Daha kapsamlı hata yönetimi
5. **Testing**: Unit testler ve integration testler
6. **UI**: Web arayüzü veya API endpoint'leri

---

## Sonuç

Bu projeler, LangChain ekosistemini adım adım öğrenmek için tasarlanmıştır. **CorrectiveRAGProject**, bu öğrenme yolculuğunun zirvesidir ve gerçek dünya uygulamalarında kullanılabilecek gelişmiş bir RAG sistemidir.

Her proje, bir öncekinin üzerine inşa edilmiş ve yeni konseptler eklenmiştir. Bu yaklaşım, karmaşık sistemlerin nasıl parçalara ayrılıp yönetilebileceğini gösterir.



