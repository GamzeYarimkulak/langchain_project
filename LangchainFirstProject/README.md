# LangchainFirstProject

LangChain kütüphanesine giriş projesi. Bu projede, LangChain'in temel bileşenlerini adım adım öğreniyoruz.

## Proje Yapısı

Proje, LangChain öğrenme yolculuğunun farklı aşamalarını gösteren dört örnek içerir:

### 1. simplemessage.py
En basit LangChain kullanımı. OpenAI modeli ile doğrudan mesaj gönderme.

**Öğrenilenler:**
- ChatOpenAI modeli kullanımı
- SystemMessage ve HumanMessage oluşturma
- Model çağrısı ve yanıt alma

### 2. simplemessagewithoutputparser.py
Output parser ekleyerek model çıktısını daha kullanılabilir hale getirme.

**Öğrenilenler:**
- StrOutputParser kullanımı
- Chain yapısı oluşturma (pipe operatörü `|`)
- Çıktıyı string formatına dönüştürme

### 3. simplemessagewithtemplates.py
Prompt template kullanarak dinamik prompt'lar oluşturma.

**Öğrenilenler:**
- ChatPromptTemplate ile template oluşturma
- Parametreli prompt'lar (örneğin: `{language}`, `{text}`)
- Tam chain yapısı: `prompt | model | parser`

### 4. serve.py
LangChain chain'ini FastAPI ile servis haline getirme.

**Öğrenilenler:**
- LangServe kullanımı
- FastAPI entegrasyonu
- REST API oluşturma
- Çeviri uygulaması örneği

## Kurulum

```bash
pip install -r requirements.txt
```

## Kullanım

Her dosyayı ayrı ayrı çalıştırabilirsiniz:

```bash
python simplemessage.py
python simplemessagewithoutputparser.py
python simplemessagewithtemplates.py
python serve.py
```

`serve.py` dosyasını çalıştırdığınızda, FastAPI sunucusu `http://localhost:8000` adresinde başlar. API dokümantasyonuna `http://localhost:8000/docs` adresinden erişebilirsiniz.

## Gereksinimler

- Python 3.8+
- OpenAI API anahtarı (`.env` dosyasında)
- Tüm bağımlılıklar `requirements.txt` dosyasında listelenmiştir

