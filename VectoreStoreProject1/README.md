# VectoreStoreProject1

VectorStoreProject'in gelişmiş versiyonu. Bu projede, vector store'u kalıcı hale getirip retriever ve chain yapısı oluşturuyoruz.

## Farklar

VectorStoreProject'ten farklı olarak:
- Vector store kalıcı olarak kaydediliyor (`persist_directory`)
- Retriever oluşturuluyor
- LangChain chain yapısı kullanılıyor
- Custom prompt template ile RAG pattern'i uygulanıyor

## Özellikler

- Kalıcı vector store oluşturma
- Retriever ile doküman getirme
- RunnableLambda kullanımı
- Custom prompt template
- RAG (Retrieval Augmented Generation) pattern'i

## Kurulum

```bash
pip install -r requirements.txt
```

## Kullanım

```bash
python main.py
```

Proje çalıştığında:
1. Dokümanlar `chroma_store` klasörüne kalıcı olarak kaydedilir
2. Retriever oluşturulur ve en benzer doküman getirilir (k=1)
3. Custom prompt ile context ve question birleştirilir
4. LLM'e gönderilir ve cevap üretilir

## Proje Yapısı

- Dokümanlar kalıcı olarak `chroma_store/` klasörüne kaydedilir
- Retriever, k=1 parametresi ile en benzer dokümanı getirir
- Chain yapısı: `{"context": retriever, "question": RunnablePassthrough()} | prompt | llm`

## Öğrenilenler

- Retriever kavramı ve kullanımı
- Kalıcı vector store oluşturma
- RAG pattern'inin temel uygulaması
- Context ve question'ın birleştirilmesi
- RunnableLambda ve RunnablePassthrough kullanımı

