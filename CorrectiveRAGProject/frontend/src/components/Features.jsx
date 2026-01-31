import './Features.css'

const FEATURES = [
  {
    id: 'loop',
    title: 'Kendi Kendine Düzeltme Döngüsü',
    desc: 'Yanıt yetersiz veya kaynaklara dayalı değilse sistem otomatik olarak web araması veya yeniden üretim yapar.',
    visual: 'loop',
  },
  {
    id: 'hallucination',
    title: 'Halüsinasyon Önleme',
    desc: 'Üretilen metnin yalnızca sunulan belgelere dayalı olup olmadığı kontrol edilir; dayalı değilse yeniden yönlendirilir.',
    visual: 'shield',
  },
  {
    id: 'source',
    title: 'Kaynak Odaklı Yanıtlar',
    desc: 'Yanıtlar belge arşivi (Chroma) veya canlı web araması (Tavily) ile desteklenir; hangi yolun kullanıldığı süreçte görülür.',
    visual: 'chain',
  },
  {
    id: 'websearch',
    title: 'Canlı Web Araması (Tavily)',
    desc: 'Belgelerde yeterli bilgi yoksa veya soru arşiv dışındaysa Tavily ile web araması yapılıp sonuçlar cevaba eklenir.',
    visual: 'clock',
  },
]

export default function Features() {
  return (
    <section id="ozellikler" className="features">
      <div className="features-inner">
        <div className="features-header">
          <h2 className="features-title">
            <span className="features-title-accent">Özellikler</span>
          </h2>
        </div>

        <div className="features-grid">
          {FEATURES.map((f) => (
            <div key={f.id} className="feature-card">
              <div className={`feature-visual feature-visual--${f.visual}`}>
                {f.visual === 'loop' && (
                  <div className="loop-icon">
                    <span className="loop-ring" />
                    <span className="loop-ring" />
                    <span className="loop-ring" />
                    <span className="loop-core">↻</span>
                  </div>
                )}
                {f.visual === 'shield' && <span className="shield-icon">✓</span>}
                {f.visual === 'chain' && <span className="chain-icon">S</span>}
                {f.visual === 'clock' && <span className="clock-icon">◷</span>}
              </div>
              <h3 className="feature-title">{f.title}</h3>
              <p className="feature-desc">{f.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
