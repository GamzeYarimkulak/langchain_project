# AgentProject

ReAct agent pattern'i ile akıllı arama aracı. Bu projede, LangGraph kullanarak web araması yapabilen bir agent oluşturuyoruz.

## Amaç

Bu proje, LangGraph ve ReAct agent pattern'ini öğrenmek için tasarlanmıştır. Agent, kullanıcı sorularını analiz edip gerekirse web'de arama yaparak cevap üretir.

## Özellikler

- Tavily Search API entegrasyonu
- LangGraph checkpoint mekanizması (SqliteSaver)
- ReAct agent oluşturma
- Agent executor ile streaming response
- Thread ID bazlı checkpoint yönetimi
- Konuşma geçmişi saklama

## Kurulum

```bash
pip install -r requirements.txt
```

Ayrıca Tavily API anahtarına ihtiyacınız var. `.env` dosyasına ekleyin:
```
TAVILY_API_KEY=your_api_key_here
```

## Kullanım

```bash
python main.py
```

Proje çalıştığında interaktif bir agent başlar. Sorularınızı yazabilir, agent düşünce sürecini ve arama sonuçlarını anlık olarak gösterir.

## Nasıl Çalışır?

1. Kullanıcı sorusu alınır
2. Agent, soruyu analiz eder
3. Gerekirse Tavily ile web araması yapar
4. Sonuçları değerlendirir
5. Cevap üretir ve streaming olarak gösterir
6. Konuşma geçmişi checkpoint'e kaydedilir

## Özellikler

- **ReAct Pattern**: Reasoning + Acting kombinasyonu
- **Tool Usage**: Tavily search tool'u kullanımı
- **Checkpoint**: SQLite ile konuşma geçmişi saklama
- **Streaming**: Anlık düşünce süreci gösterimi
- **Memory**: Thread ID bazlı hafıza yönetimi

## Öğrenilenler

- Agent pattern'i ve ReAct
- LangGraph checkpoint mekanizması
- Tool kullanımı ve entegrasyonu
- Streaming agent responses
- Memory ve state yönetimi

## Notlar

- Tavily API anahtarı gereklidir (ücretsiz tier mevcut)
- Checkpoint SQLite kullanıyor, production'da farklı bir backend kullanılabilir
- Thread ID sabit kodlanmış, gerçek uygulamada dinamik olmalı

