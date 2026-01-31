"""
Corrective RAG web arayüzü backend.
Soru gönderir, grafik adımlarını toplar, cevabı ve süreci döner.
"""
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Graph ve ingestion import'ları (vectorstore için)
from graph.graph import app as graph_app
from graph.node_constants import RETRIEVE, GRADE_DOCUMENTS, WEBSEARCH, GENERATE


app = FastAPI(title="Corrective RAG", docs_url=None, redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adım etiketleri – sade, teknik olmayan
STEP_LABELS = {
    RETRIEVE: {
        "title": "Belge arşivinde aranıyor",
        "detail": "Kayıtlı belgelerde ilgili bölümler taranıyor.",
    },
    GRADE_DOCUMENTS: {
        "title": "Belgeler inceleniyor",
        "detail": "Soruyla ilişki kontrol ediliyor.",
    },
    WEBSEARCH: {
        "title": "Web'de arama yapılıyor",
        "detail": "Güncel kaynaklar taranıyor.",
    },
    GENERATE: {
        "title": "Cevap hazırlanıyor",
        "detail": "Metin oluşturuluyor.",
    },
}


class QueryRequest(BaseModel):
    question: str


def _get_generation_from_state(state) -> str:
    """State'ten metin cevabını al; AIMessage vs. varsa content çıkar."""
    gen = state.get("generation") or ""
    if hasattr(gen, "content"):
        return getattr(gen, "content", "") or str(gen)
    return str(gen) if gen else ""


@app.post("/api/query")
def query(req: QueryRequest):
    if not (req.question or req.question.strip()):
        raise HTTPException(status_code=400, detail="Soru boş olamaz.")
    question = req.question.strip()

    steps = []
    answer = ""

    try:
        for event in graph_app.stream(
            {"question": question, "attempts": 0},
            stream_mode="updates",
        ):
            for node_name, state_update in event.items():
                if node_name in STEP_LABELS:
                    steps.append({
                        "id": node_name,
                        "title": STEP_LABELS[node_name]["title"],
                        "detail": STEP_LABELS[node_name]["detail"],
                    })
                if node_name == GENERATE:
                    answer = _get_generation_from_state(state_update) or answer
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"İşlem sırasında hata: {str(e)}",
        )

    if steps:
        first_id = steps[0]["id"]
        if first_id == RETRIEVE:
            steps.insert(0, {
                "id": "route",
                "title": "Soru analiz edildi",
                "detail": "Yanıt için belge arşivine yönlendirildi.",
            })
        elif first_id == WEBSEARCH:
            steps.insert(0, {
                "id": "route",
                "title": "Soru analiz edildi",
                "detail": "Yanıt için web aramasına yönlendirildi.",
            })

    return {
        "question": question,
        "steps": steps,
        "answer": answer,
    }


@app.get("/")
def index():
    return {"message": "Corrective RAG API", "docs": "POST /api/query", "ui": "frontend/ klasöründe React uygulaması"}


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
