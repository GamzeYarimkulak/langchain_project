# SetupProject

Bu proje, LangChain ve OpenAI API kullanımı için temel ortam kurulumunu içerir. Projelerde güvenli bir şekilde API anahtarlarını yönetmek için `python-dotenv` kütüphanesi kullanılmaktadır.

## Özellikler

- Ortam değişkenlerini `.env` dosyasından yükleme
- API anahtarlarının güvenli yönetimi
- Ortam değişkenlerinin doğru yüklendiğini test etme

## Kurulum

1. Gerekli paketi yükleyin:
```bash
pip install -r requirements.txt
```

2. Proje kök dizininde `.env` dosyası oluşturun:
```
OPENAI_API_KEY=your_api_key_here
```

3. Projeyi çalıştırın:
```bash
python main.py
```

## Kullanım

Proje, `.env` dosyasından `OPENAI_API_KEY` değişkenini yükler ve konsola yazdırır. Bu sayede API anahtarlarınızı kod içinde hardcode etmeden güvenli bir şekilde kullanabilirsiniz.

## Notlar

- `.env` dosyasını asla versiyon kontrol sistemine (Git) eklemeyin
- `.gitignore` dosyasına `.env` eklemeyi unutmayın
- API anahtarlarınızı güvende tutun

