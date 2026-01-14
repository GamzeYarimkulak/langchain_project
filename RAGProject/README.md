# RAGProject

Gerçek dünya verisi ile RAG (Retrieval Augmented Generation) uygulaması. Bu projede, web sayfasından doküman yükleyip RAG pattern'i uyguluyoruz.

## Amaç

Bu proje, gerçek bir web sayfasından veri çekip RAG sistemi oluşturmayı gösterir. Lilian Weng'in "Agent" blog yazısı yüklenir, işlenir ve soru-cevap sistemi oluşturulur.

## Özellikler

- Web sayfasından doküman yükleme (WebBaseLoader)
- BeautifulSoup ile HTML parsing
- Dokümanları chunk'lara bölme (RecursiveCharacterTextSplitter)
- LangChain Hub'dan hazır RAG prompt'u kullanma
- Streaming response ile anlık cevap üretme

## Kurulum

```bash
pip install -r requirements.txt
```

## Kullanım

```bash
python main.py
```

Proje çalıştığında:
1. Web sayfasından doküman yüklenir
2. Dokümanlar 1000 karakterlik chunk'lara bölünür (200 karakter overlap)
3. Chroma vector store oluşturulur
4. LangChain Hub'dan `rlm/rag-prompt` çekilir
5. "what is task decomposition" sorusu için streaming cevap üretilir

## Nasıl Çalışır?

1. **Document Loading**: WebBaseLoader ile web sayfası yüklenir
2. **Text Splitting**: Dokümanlar anlamlı parçalara bölünür
3. **Embedding**: Chunk'lar vektörleştirilir
4. **Storage**: Chroma vector store'a kaydedilir
5. **Retrieval**: Soruya göre ilgili chunk'lar getirilir
6. **Generation**: Context ve question birleştirilip LLM'e gönderilir
7. **Streaming**: Cevap anlık olarak kullanıcıya gösterilir

## Öğrenilenler

- Web scraping ve doküman yükleme
- Text splitting stratejileri (chunk size, overlap)
- LangChain Hub kullanımı
- RAG pattern'inin tam uygulaması
- Streaming response ile kullanıcı deneyimi

## Notlar

- Web sayfası yapısı değişirse, BeautifulSoup parsing ayarları güncellenebilir
- Chunk size ve overlap değerleri, doküman türüne göre ayarlanabilir
- LangChain Hub'dan farklı prompt'lar deneyebilirsiniz

