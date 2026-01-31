import './Hero.css'

export default function Hero() {
  return (
    <section className="hero">
      <div className="hero-inner">
        <div className="hero-content">
          <h1 className="hero-title">
            <span className="hero-title-accent">Güvenilir</span>{' '}
            <span className="hero-title-white">Yapay Zeka</span>{' '}
            <span className="hero-title-gradient">Yanıtları</span>
          </h1>
          <p className="hero-subtitle">
            Doğrulanmış, temellendirilmiş ve halüsinasyonsuz yapay zeka yanıtları.
            Otomatik hızda ve canlı web araması ile akıllı RAG sistemi.
          </p>
          <div className="hero-buttons">
            <a href="#demo" className="btn-hero btn-primary">
              <span className="btn-icon">▶</span>
              Demo İzle
            </a>
          </div>
        </div>
      </div>
    </section>
  )
}
