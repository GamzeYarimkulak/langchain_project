CorrectiveRAGProject

CorrectiveRAGProject, klasik Retrieval Augmented Generation (RAG) yaklaşımının ötesine geçerek karar veren, kendini denetleyen ve gerektiğinde kendini düzelten bir soru–cevap sistemi kurmayı amaçlar.

Bu projede LLM, yalnızca cevap üreten bir bileşen değil; sistemin farklı aşamalarında değerlendirme yapan bir karar mekanizması olarak kullanılır. Akış, LangGraph ile state-based bir yapı halinde modellenmiştir.

Genel Bakış

Sistem, gelen bir soruyu uçtan uca şu prensiple ele alır:

“En uygun kaynağı seç → bağlamı topla → cevap üret → cevabı denetle → gerekirse geri dön.”

Bu yaklaşım, lineer RAG pipeline’larının aksine kontrollü ve döngüsel bir iş akışı oluşturur.

Temel Özellikler

Query Routing
Soru, vector store veya web search arasında otomatik olarak yönlendirilir.

Document Relevance Grading
Retriever’dan gelen dokümanlar, soruyla gerçekten ilgili olup olmadıklarına göre filtrelenir.

Web Search Fallback
Vector store yeterli değilse sistem otomatik olarak web aramasına yönelir.

Controlled Generation
LLM yalnızca verilen bağlama dayanarak cevap üretir.

Self-Check & Correction Loop
Üretilen cevap:

bağlama dayanıyor mu?

soruyu gerçekten yanıtlıyor mu?
sorularıyla kontrol edilir. Gerekirse sistem geri dönerek kendini düzeltir.

State-Based Workflow
Tüm akış LangGraph ile state machine olarak modellenmiştir.

Workflow Grafiği
![Workflow grafiği](./graph.png)

Aşağıdaki diyagram, sistemin karar odaklı akışını özetler:

Demo & Arayüz

Projede, sistemin davranışını gözlemleyebilmek için basit bir web arayüzü de bulunmaktadır.

Vector store üzerinden gelen cevap örneği:
![Web arayüzü - belgelerden gelen cevap](./görseller/webarayüzbelgelerdengelencevap.png)
![Backend çıktısı - belgelerden gelen cevap](./görseller/backend_kodçıktısıs_belgelerden_gelen%20cevap.png)

Web search fallback ile gelen cevap örneği:
![Web arayüzü - Tavily ile gelen cevap](./görseller/webarayüzweb-tavilydengelencevap.png)
![Backend çıktısı - web'den gelen cevap](./görseller/backend_kod_ciktisi_webdengelencevap.png)

Hızlı Başlangıç (Quick Run)
1. Bağımlılıkları Yükleyin
pip install -r requirements.txt

2. Ortam Değişkenleri

.env dosyası oluşturun:

OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key

3. Vector Store Oluşturma

İlk çalıştırmada belge indeksini oluşturun:

python ingestion.py

4. Sistemi Çalıştırma
python main.py

Proje Yapısı
CorrectiveRAGProject/
├── main.py          # Uygulama giriş noktası
├── ingestion.py     # Doküman yükleme ve vector store oluşturma
├── graph/
│   ├── graph.py     # LangGraph workflow tanımı
│   ├── state.py     # State yapısı
│   ├── nodes/       # Retrieve, generate, grade, web search adımları
│   └── chains/      # Router ve grader chain'leri
├── graph.png        # Workflow diyagramı
└── requirements.txt

Notlar

Proje bağımsız çalışır.

Döngüsel yapı bounded retries ile kontrol altındadır.

Amaç “en uzun cevabı” değil, en güvenilir cevabı üretmektir.

Detaylı mimari anlatım Medium yazısında ele alınmıştır.

Lisans

Bu proje eğitim ve öğrenme amaçlıdır.
