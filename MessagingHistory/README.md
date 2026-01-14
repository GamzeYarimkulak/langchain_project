# MessagingHistory

Chat uygulamalarında mesaj geçmişi yönetimi projesi. Bu projede, LangChain'in message history özelliklerini kullanarak konuşma geçmişini yönetiyoruz.

## Amaç

Bu proje, chat uygulamalarında mesaj geçmişinin nasıl yönetileceğini gösterir. Her session için ayrı geçmiş tutulur ve konuşma bağlamı korunur.

## Özellikler

- InMemoryChatMessageHistory ile mesaj geçmişi saklama
- RunnableWithMessageHistory ile chain'e geçmiş ekleme
- Session ID bazlı geçmiş yönetimi
- MessagesPlaceholder ile dinamik mesaj geçmişi
- Interactive chat loop

## Kurulum

```bash
pip install -r requirements.txt
```

## Kullanım

```bash
python main.py
```

Proje çalıştığında interaktif bir chat döngüsü başlar. Her mesajınız geçmişe eklenir ve AI, önceki konuşmaları da dikkate alarak cevap verir.

## Nasıl Çalışır?

1. Her session için ayrı bir message history oluşturulur
2. Kullanıcı mesajı gönderilir
3. Mesaj geçmişi otomatik olarak chain'e eklenir
4. LLM, geçmişi dikkate alarak cevap üretir
5. AI cevabı geçmişe eklenir
6. Döngü devam eder

## Özellikler

- **Session Management**: Her session ID için ayrı geçmiş
- **Context Preservation**: Önceki mesajlar otomatik olarak korunur
- **Memory Store**: In-memory dictionary ile geçmiş saklama
- **Interactive Loop**: Sürekli konuşma imkanı

## Öğrenilenler

- Chat history yönetimi
- Session bazlı konuşma takibi
- MessagesPlaceholder kullanımı
- RunnableWithMessageHistory pattern'i
- Context-aware chat uygulamaları

## Notlar

- Bu örnekte in-memory storage kullanılıyor. Production'da database kullanılmalı
- Session ID'ler sabit kodlanmış, gerçek uygulamada dinamik olmalı
- Geçmiş uzunluğu sınırlanabilir (token limit'i için)

