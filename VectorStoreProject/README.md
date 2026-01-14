# VectorStoreProject

Vektör veritabanı (vector store) kullanımını öğrenmek için basit bir örnek proje. Bu projede, Chroma vector store kullanarak dokümanları vektörleştirip semantic search yapıyoruz.

## Amaç

Bu proje, embedding ve vector store kavramlarını öğrenmek için tasarlanmıştır. Örnek dokümanlar oluşturup bunları vektör veritabanına kaydediyor ve benzerlik araması yapıyoruz.

## Özellikler

- Chroma vector store kurulumu
- OpenAI embeddings kullanımı
- Dokümanları vektörleştirme
- Semantic search (anlamsal arama) yapma

## Kurulum

```bash
pip install -r requirements.txt
```

## Kullanım

```bash
python main.py
```

Proje çalıştığında, örnek dokümanlar (köpek, kedi, balık, papağan, tavşan hakkında) oluşturulur, vektörleştirilir ve "dog" kelimesi için benzerlik araması yapılır.

## Nasıl Çalışır?

1. Örnek dokümanlar oluşturulur
2. OpenAI embeddings kullanılarak dokümanlar vektörleştirilir
3. Chroma vector store'a kaydedilir
4. "dog" kelimesi için semantic search yapılır
5. En benzer dokümanlar döndürülür

## Öğrenilenler

- Embedding kavramı ve önemi
- Vector store kullanımı
- Semantic search'in keyword search'ten farkı
- Chroma vector store'un temel kullanımı

