# Corrective RAG – Landing Page (Frontend)

React + Vite ile yazılmış, dark-mode ağırlıklı landing page. Backend (FastAPI) ile Chat Demo bölümü üzerinden entegre çalışır.

## Gereksinimler

- Node.js 18+
- npm veya yarn

## Kurulum

```bash
cd frontend
npm install
```

## Geliştirme

Frontend ve backend birlikte çalışmalı:

1. **Backend** (bir terminalde):
   ```bash
   cd ..
   python serve.py
   ```
   Backend http://localhost:8000 üzerinde çalışır.

2. **Frontend** (başka bir terminalde):
   ```bash
   npm run dev
   ```
   Frontend http://localhost:5173 üzerinde açılır. `/api` istekleri Vite proxy ile otomatik olarak `localhost:8000`'e yönlendirilir.

Tarayıcıda http://localhost:5173 adresine gidin.

## Build

```bash
npm run build
```

Üretilen dosyalar `dist/` klasöründe olur. Backend'den statik olarak sunmak için `dist` çıktısını FastAPI'ye mount edebilirsiniz.

## Bölümler

- **Header**: Logo, Özellikler / Nasıl Çalışır / Demo, API Erişimi, Başla
- **Hero**: Başlık, alt metin, Demo İzle / GitHub'da Nasıl
- **Chat Demo**: Soru gönder, backend `/api/query` ile yanıt al, kaynak etiketleri ve Doğrulandı badge
- **How It Works**: Arama, Skor, Test, Canlı, Cevap adımları
- **Features**: Self-healing loop, Halüsinasyon önleme, Kaynak doğrulama, Güven skoru, Gerçek zamanlı güncelleme

## Teknik

- React 18, Vite 5
- CSS modülleri yerine bileşen bazlı `.css` dosyaları
- API: `POST /api/query` → `{ question }` → `{ question, steps, answer }`
