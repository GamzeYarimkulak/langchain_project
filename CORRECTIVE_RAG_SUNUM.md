# CorrectiveRAG Project: Sunum Dokümanı
## RAG + Self-Reflection Workflow ile Akıllı Soru-Cevap Sistemi

---

## 📋 İçindekiler

1. [LangChain Nedir?](#langchain-nedir)
2. [RAG (Retrieval Augmented Generation) Kavramı](#rag-kavramı)
3. [Proje Mimarisi: RAG + Self-Reflection](#proje-mimarisi)
4. [Workflow Detayları](#workflow-detayları)
5. [LangChain'in Rolü](#langchainin-rolü)
6. [Sonuç ve Öğrenilenler](#sonuç)

---

## 1. LangChain Nedir? 🤖

### Tanım
**LangChain**, büyük dil modelleri (LLM) ile uygulamalar geliştirmek için kullanılan açık kaynaklı bir framework'tür.

### Ne İşe Yarar?

#### 🔗 Chain Yapıları
- LLM çağrılarını birbirine bağlar
- Karmaşık iş akışlarını modüler parçalara ayırır
- `prompt | llm | parser` gibi zincirler oluşturur

#### 📚 Veri Entegrasyonu
- Vector store'larla entegrasyon (Chroma, Pinecone, vb.)
- Doküman yükleme ve işleme
- Embedding oluşturma ve semantic search

#### 🧠 Akıllı Yönlendirme
- Conditional routing (koşullu yönlendirme)
- Agent pattern'leri (ReAct, Plan-and-Execute)
- Tool kullanımı ve function calling

#### 🔄 State Yönetimi
- Workflow state'lerini yönetir
- Memory ve chat history
- Checkpoint mekanizmaları

### LangChain'in Temel Bileşenleri

```
┌─────────────┐
│   Prompt    │ → Kullanıcı girdisini formatlar
└──────┬──────┘
       │
┌──────▼──────┐
│     LLM     │ → Model çağrısı yapar
└──────┬──────┘
       │
┌──────▼──────┐
│   Parser    │ → Çıktıyı formatlar
└─────────────┘
```

**Örnek Kullanım:**
```python
chain = prompt_template | llm | parser
response = chain.invoke({"question": "What is RAG?"})
```

---

## 2. RAG Kavramı 📖

### RAG Nedir?
**Retrieval Augmented Generation (RAG)**, LLM'lerin kendi eğitim verileri dışındaki bilgilere erişmesini sağlayan bir tekniktir.

### Neden RAG?

#### ❌ LLM'lerin Sınırlamaları
- Eğitim verileriyle sınırlıdır
- Güncel bilgilere erişemez
- Domain-specific bilgileri içermeyebilir
- Hallucination (halüsinasyon) yapabilir

#### ✅ RAG'in Avantajları
- Güncel bilgilere erişim
- Domain-specific bilgi kullanımı
- Daha doğru ve güvenilir cevaplar
- Kaynak referansları

### Basit RAG Akışı

```
1. Question → 2. Retrieve → 3. Context → 4. Generate → 5. Answer
```

**Sorun:** Bu basit akış yeterli değil!
- İlgisiz dokümanlar getirilebilir
- Cevap dokümanlara dayalı olmayabilir
- Cevap soruyu tam cevaplamayabilir

**Çözüm:** **CorrectiveRAG** - Self-reflection ve kalite kontrolü ekleyen gelişmiş RAG!

---

## 3. Proje Mimarisi: RAG + Self-Reflection 🏗️

### Genel Bakış

CorrectiveRAGProject, **self-reflection** (kendi kendini değerlendirme) mekanizması ekleyerek geleneksel RAG'i geliştirir.

### Temel Fark

| Geleneksel RAG | CorrectiveRAG |
|----------------|---------------|
| Retrieve → Generate → Answer | Retrieve → Grade → Generate → Check → Correct |
| Tek yönlü akış | Döngüsel, kendi kendini düzelten |
| Kalite kontrolü yok | Çoklu kalite kontrol katmanları |

### Mimari Şeması

```
                    ┌─────────────────────────────────────┐
                    │     RAG + Self-Reflection            │
                    └─────────────────────────────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │   Query Analysis              │
                    │   (Soruyu Analiz Et)          │
                    └───────────────┬───────────────┘
                                    │
            ┌───────────────────────┼───────────────────────┐
            │                       │                       │
    [related to index]    [unrelated to index]    [Optional]
            │                       │                       │
            ▼                       ▼                       ▼
    ┌───────────────┐      ┌──────────────┐      ┌─────────────┐
    │   Retrieve    │      │  Web Search  │      │   Optional  │
    │   (Node)      │      │              │      │             │
    └───────┬───────┘      └──────┬───────┘      └─────────────┘
            │                     │
            ▼                     ▼
    ┌───────────────┐      ┌──────────────┐
    │     Grade     │      │   Generate   │
    │   (Node)      │      │   (Node)     │
    └───────┬───────┘      └──────┬───────┘
            │                     │
            ▼                     │
    ┌───────────────┐             │
    │ Docs relevant?│             │
    └───────┬───────┘             │
            │                     │
    ┌───────┴───────┐             │
    │               │             │
   Yes             No             │
    │               │             │
    ▼               ▼             │
┌─────────┐  ┌──────────────┐    │
│Generate │  │Re-write      │    │
│(Node)   │  │question      │────┘
└────┬────┘  │(Node)        │
     │       └──────┬────────┘
     │              │
     ▼              │
┌───────────────┐   │
│ Hallucinations?│   │
└───────┬───────┘   │
        │           │
   ┌────┴────┐      │
  Yes       No      │
   │         │      │
   ▼         ▼      │
┌───────┐ ┌──────────────┐
│Re-write│ │Answers      │
│question│ │question?    │
│(Node)  │ └──────┬──────┘
└───┬────┘        │
    │        ┌────┴────┐
    │       Yes       No
    │        │         │
    │        ▼         ▼
    │   ┌─────────┐ ┌──────────────┐
    │   │ Answer  │ │Re-write      │
    │   │         │ │question      │
    │   └─────────┘ │(Node)        │
    │               └──────┬────────┘
    │                      │
    └──────────────────────┘
```

---

## 4. Workflow Detayları 🔄

### Adım 1: Query Analysis (Soru Analizi)

**Görev:** Gelen soruyu analiz edip en uygun yolu seçmek.

**LangChain Kullanımı:**
- **Structured Output**: LLM'den yapılandırılmış çıktı alma
- **Router Chain**: Soruyu kategorize etme

```python
class RouteQuery(BaseModel):
    datasource: Literal["vectorstore", "websearch"]

question_router = route_prompt | structured_llm_router
```

**Karar Noktaları:**
- ✅ **Vectorstore'a yönlendir**: Soru, index'teki konularla ilgiliyse
  - Agents, Prompt Engineering, Adversarial Attacks
- 🌐 **Web Search'e yönlendir**: Soru, index dışındaysa
- 🔄 **Optional**: Diğer özel durumlar

**Neden Önemli?**
- Gereksiz web aramalarını önler
- Performansı artırır
- Doğru kaynağa yönlendirir

---

### Adım 2: Retrieve (Doküman Getirme)

**Görev:** Vectorstore'dan soruyla ilgili dokümanları getirmek.

**LangChain Kullanımı:**
- **Chroma Vectorstore**: Embedding tabanlı arama
- **Retriever**: Semantic search yapma

```python
retriever = Chroma(
    collection_name="rag-chroma",
    embedding_function=OpenAIEmbeddings()
).as_retriever()

documents = retriever.invoke(question)
```

**Nasıl Çalışır?**
1. Soru embedding'e dönüştürülür
2. Vectorstore'da benzerlik araması yapılır
3. En ilgili dokümanlar döndürülür

---

### Adım 3: Grade Documents (Doküman Değerlendirme)

**Görev:** Getirilen dokümanların gerçekten soruyla ilgili olup olmadığını kontrol etmek.

**LangChain Kullanımı:**
- **Structured Output**: Binary scoring
- **Retrieval Grader Chain**: Her dokümanı değerlendirme

```python
class GradeDocuments(BaseModel):
    binary_score: str  # "yes" veya "no"

retrieval_grader = grade_prompt | structured_llm_grader
```

**İşleyiş:**
```
Her doküman için:
  ├─ LLM'e sor: "Bu doküman soruyla ilgili mi?"
  ├─ "yes" → Dokümanı tut
  └─ "no" → Dokümanı filtrele
```

**Kritik Kontrol:**
- Eğer hiç ilgili doküman yoksa → `web_search = True`
- Bu, sistemin web araması yapmasını tetikler

**Neden Önemli?**
- İlgisiz dokümanlar yanlış cevaplara yol açar
- Kalite kontrolünün ilk katmanı
- Self-correction mekanizmasının başlangıcı

---

### Adım 4: Generate (Cevap Üretme)

**Görev:** Context ve question'ı kullanarak cevap üretmek.

**LangChain Kullanımı:**
- **LangChain Hub**: Hazır RAG prompt'u
- **Generation Chain**: Prompt + LLM + Parser

```python
prompt = hub.pull("rlm/rag-prompt")
generation_chain = prompt | llm | StrOutputParser()

context = "\n\n".join([d.page_content for d in documents])
generation = generation_chain.invoke({
    "context": context,
    "question": question
})
```

**RAG Prompt Yapısı:**
```
Context: [Retrieved documents]
Question: [User question]

Answer based on the context only.
```

---

### Adım 5: Hallucination Check (Halüsinasyon Kontrolü)

**Görev:** Üretilen cevabın dokümanlara dayalı olup olmadığını kontrol etmek.

**LangChain Kullanımı:**
- **Hallucination Grader Chain**: Grounding kontrolü

```python
class GradeHallucination(BaseModel):
    binary_score: bool  # Grounded mi?

hallucination_grader = hallucination_prompt | structured_llm_grader
```

**Kontrol:**
```
LLM'e sor: "Bu cevap, verilen dokümanlara dayalı mı?"
├─ "yes" → Cevap güvenilir, devam et
└─ "no" → Hallucination var! → Re-write question → Retrieve
```

**Neden Kritik?**
- LLM'ler bazen kendi bilgilerinden uydurma yapabilir
- Bu, yanlış bilgi üretimine yol açar
- Self-correction mekanizması devreye girer

---

### Adım 6: Answer Quality Check (Cevap Kalite Kontrolü)

**Görev:** Cevabın soruyu gerçekten cevaplayıp cevaplamadığını kontrol etmek.

**LangChain Kullanımı:**
- **Answer Grader Chain**: Relevance kontrolü

```python
class GradeAnswer(BaseModel):
    binary_score: bool  # Soruyu cevaplıyor mu?

answer_grader = answer_prompt | structured_llm_grader
```

**Kontrol:**
```
LLM'e sor: "Bu cevap, soruyu cevaplıyor mu?"
├─ "yes" → Cevap kabul edilebilir → END
└─ "no" → Cevap yetersiz → Re-write question → Retrieve
```

**Self-Correction Döngüsü:**
```
Cevap yetersiz
    ↓
Re-write question (Soru yeniden yazılır)
    ↓
Retrieve (Yeni dokümanlar getirilir)
    ↓
Generate (Yeni cevap üretilir)
    ↓
Check again (Tekrar kontrol edilir)
```

---

### Adım 7: Web Search (Web Arama)

**Görev:** Vectorstore'da yeterli bilgi yoksa web'de arama yapmak.

**LangChain Kullanımı:**
- **Tavily Search Tool**: Web arama API'si
- **Tool Integration**: LangChain tool wrapper

```python
web_search_tool = TavilySearchResults(k=3)
docs = web_search_tool.invoke({"query": question})
```

**Ne Zaman Kullanılır?**
1. Query Analysis → Soru index dışındaysa
2. Grade Documents → İlgili doküman yoksa
3. Self-Correction → Cevap yetersizse

---

## 5. LangChain'in Rolü 🎯

### LangChain Bileşenleri ve Kullanımları

#### 1. **LangGraph** - Workflow Yönetimi

**Ne İşe Yarar?**
- State machine oluşturma
- Conditional routing
- Node'lar arası veri akışı

**Projede Kullanımı:**
```python
workflow = StateGraph(GraphState)

# Node'ları ekle
workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(GENERATE, generate)

# Conditional routing
workflow.add_conditional_edges(
    GRADE_DOCUMENTS,
    decide_to_generate,
    {WEBSEARCH: WEBSEARCH, GENERATE: GENERATE}
)
```

**Faydaları:**
- Karmaşık workflow'ları yönetmek kolay
- Görselleştirilebilir (graph.png)
- Modüler ve test edilebilir

---

#### 2. **Structured Output** - Yapılandırılmış Çıktı

**Ne İşe Yarar?**
- LLM'den JSON formatında çıktı alma
- Type-safe veri yapıları
- Pydantic modelleri ile entegrasyon

**Projede Kullanımı:**
```python
class RouteQuery(BaseModel):
    datasource: Literal["vectorstore", "websearch"]

structured_llm_router = llm.with_structured_output(RouteQuery)
```

**Kullanıldığı Yerler:**
- Router: Soru yönlendirme
- Retrieval Grader: Doküman değerlendirme
- Hallucination Grader: Grounding kontrolü
- Answer Grader: Cevap kalite kontrolü

**Faydaları:**
- Güvenilir veri yapıları
- Hata kontrolü kolay
- Type safety

---

#### 3. **Vector Stores** - Embedding ve Arama

**Ne İşe Yarar?**
- Dokümanları vektörleştirme
- Semantic search
- Benzerlik araması

**Projede Kullanımı:**
```python
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=OpenAIEmbeddings(),
    persist_directory="./.chroma"
)

retriever = vectorstore.as_retriever()
```

**Faydaları:**
- Anlamsal arama (keyword değil, meaning)
- Hızlı ve ölçeklenebilir
- Kalıcı depolama

---

#### 4. **Chains** - İş Akışı Zincirleri

**Ne İşe Yarar?**
- Prompt + LLM + Parser kombinasyonları
- Modüler iş akışları
- Reusable bileşenler

**Projede Kullanımı:**
```python
# Generation chain
generation_chain = prompt | llm | StrOutputParser()

# Router chain
question_router = route_prompt | structured_llm_router
```

**Faydaları:**
- Kod tekrarını önler
- Test edilebilir
- Kolay bakım

---

#### 5. **Tools** - Harici Servisler

**Ne İşe Yarar?**
- Web arama, API çağrıları
- Function calling
- Agent'lar için araçlar

**Projede Kullanımı:**
```python
web_search_tool = TavilySearchResults(k=3)
docs = web_search_tool.invoke({"query": question})
```

**Faydaları:**
- LLM'in yeteneklerini genişletir
- Güncel bilgilere erişim
- Esnek entegrasyon

---

#### 6. **LangChain Hub** - Hazır Prompt'lar

**Ne İşe Yarar?**
- Community tarafından paylaşılan prompt'lar
- Best practice'ler
- Hızlı prototipleme

**Projede Kullanımı:**
```python
prompt = hub.pull("rlm/rag-prompt")
```

**Faydaları:**
- Zaman tasarrufu
- Test edilmiş prompt'lar
- Kolay güncelleme

---

### LangChain Olmadan Ne Olurdu?

#### ❌ Zorluklar:
- Her bileşeni manuel yazmak gerekirdi
- State yönetimi karmaşık olurdu
- LLM entegrasyonu zor olurdu
- Vector store entegrasyonu manuel olurdu
- Workflow yönetimi zor olurdu

#### ✅ LangChain ile:
- Modüler ve temiz kod
- Kolay entegrasyonlar
- Best practice'ler
- Hızlı geliştirme
- Ölçeklenebilir yapı

---

## 6. Sonuç ve Öğrenilenler 🎓

### Projenin Başarıları

#### ✅ Akıllı Yönlendirme
- Sorular otomatik olarak en uygun kaynağa yönlendirilir
- Gereksiz işlemler önlenir

#### ✅ Çoklu Kalite Kontrolü
- 3 farklı kontrol katmanı:
  1. Document relevance
  2. Hallucination check
  3. Answer quality

#### ✅ Self-Correction
- Sistem kendi hatalarını düzeltebilir
- Döngüsel iyileştirme mekanizması

#### ✅ Esnek Mimari
- Vectorstore + Web Search kombinasyonu
- Modüler ve genişletilebilir yapı

---

### LangChain'in Değeri

#### 🔧 Geliştirme Hızı
- Haftalar sürecek işler günler içinde tamamlandı
- Hazır bileşenler kullanıldı

#### 🏗️ Mimari Kalite
- Best practice'ler uygulandı
- Modüler ve bakımı kolay kod

#### 📈 Ölçeklenebilirlik
- Yeni node'lar kolayca eklenebilir
- Farklı LLM'lerle değiştirilebilir

#### 🧪 Test Edilebilirlik
- Her bileşen bağımsız test edilebilir
- Mock'lar kolay oluşturulabilir

---

### Öğrenilen Konseptler

1. **State Machine Pattern**
   - Karmaşık workflow'ları yönetme
   - Conditional routing

2. **RAG Pattern**
   - Retrieval + Generation kombinasyonu
   - Context injection

3. **Self-Reflection Pattern**
   - Sistemin kendini değerlendirmesi
   - Iterative improvement

4. **Structured Output**
   - LLM'den güvenilir veri alma
   - Type safety

5. **Multi-Step Reasoning**
   - Karmaşık problemleri adımlara ayırma
   - Her adımda kontrol

---

### Gelecek Geliştirmeler

#### 🚀 Öneriler:
1. **Retry Mekanizması**
   - Başarısız denemeler için limit
   - Exponential backoff

2. **Caching**
   - Aynı sorular için cache
   - Performans artışı

3. **Monitoring**
   - Detaylı logging
   - Metrics toplama

4. **UI/API**
   - Web arayüzü
   - REST API endpoints

5. **Fine-tuning**
   - Domain-specific fine-tuning
   - Daha iyi sonuçlar

---

## 📊 Özet

### CorrectiveRAGProject Ne Yapar?

1. **Soruyu Analiz Eder** → En uygun kaynağı seçer
2. **Dokümanları Getirir** → Vectorstore veya Web
3. **Dokümanları Değerlendirir** → İlgili olanları filtreler
4. **Cevap Üretir** → Context ile generation
5. **Cevabı Kontrol Eder** → Hallucination ve quality check
6. **Gerekirse Düzeltir** → Self-correction döngüsü

### LangChain'in Katkısı

- **Workflow Yönetimi**: LangGraph
- **LLM Entegrasyonu**: ChatOpenAI, Structured Output
- **Veri Yönetimi**: Vector Stores, Embeddings
- **Araçlar**: Tavily Search, Tools
- **Prompt Yönetimi**: Templates, Hub

### Sonuç

**CorrectiveRAGProject**, LangChain ekosistemini kullanarak:
- ✅ Geleneksel RAG'in ötesine geçer
- ✅ Self-reflection ekler
- ✅ Çoklu kalite kontrolü yapar
- ✅ Kendi kendini düzeltir
- ✅ Production-ready bir sistem oluşturur

---

## 🎯 Ana Mesaj

**LangChain**, LLM uygulamaları geliştirmeyi:
- **Kolaylaştırır** (modüler bileşenler)
- **Hızlandırır** (hazır çözümler)
- **Kaliteli hale getirir** (best practices)
- **Ölçeklenebilir yapar** (esnek mimari)

**CorrectiveRAGProject**, bu gücü kullanarak:
- Geleneksel RAG'in sınırlamalarını aşar
- Self-reflection ile akıllı bir sistem oluşturur
- Production-ready bir çözüm sunar

---

## 📚 Kaynaklar

- LangChain Documentation: https://python.langchain.com
- LangGraph Documentation: https://langchain-ai.github.io/langgraph
- RAG Papers: Retrieval-Augmented Generation
- CorrectiveRAG Pattern: Self-Reflection in RAG Systems

---

**Hazırlayan:** [İsminiz]  
**Tarih:** [Tarih]  
**Proje:** CorrectiveRAGProject



