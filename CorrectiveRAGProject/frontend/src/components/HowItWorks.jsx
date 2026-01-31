import './HowItWorks.css'

const STEPS = [
  {
    id: 'search',
    title: 'Arama',
    desc: 'Dahili Chroma veri tabanında hızlı semantik arama',
    icon: 'DB',
    gradient: 'var(--gradient-teal)',
  },
  {
    id: 'score',
    title: 'Skor',
    desc: 'Bulunan bilgilerin değerlendirilmesi',
    icon: '✓',
    gradient: 'var(--gradient-blue)',
  },
  {
    id: 'test',
    title: 'Test',
    desc: 'Otomatik halüsinasyon kontrolü',
    icon: '◈',
    gradient: 'var(--gradient-purple)',
  },
  {
    id: 'live',
    title: 'Canlı',
    desc: 'Gerektiğinde Tavily ile web araması',
    icon: '◇',
    gradient: 'linear-gradient(135deg, #f97316, #eab308)',
  },
  {
    id: 'answer',
    title: 'Cevap',
    desc: 'Doğrulanmış ve kaynak destekli yanıt',
    icon: '★',
    gradient: 'var(--gradient-purple)',
  },
]

export default function HowItWorks() {
  return (
    <section id="nasil-calisir" className="how">
      <div className="how-inner">
        <h2 className="section-title">Nasıl Çalışır</h2>
        <p className="section-subtitle">
          Sorudan cevaba kadar adım adım işleyen RAG pipeline.
        </p>

        <div className="how-steps">
          {STEPS.map((step, i) => (
            <div key={step.id} className="how-step">
              <div
                className="how-step-icon"
                style={{ background: step.gradient }}
              >
                {step.icon}
              </div>
              <div className="how-step-content">
                <h3 className="how-step-title">
                  {i + 1}. {step.title}
                </h3>
                <p className="how-step-desc">{step.desc}</p>
              </div>
              {i < STEPS.length - 1 && <div className="how-step-connector" />}
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
