import { useState } from 'react'
import './ChatDemo.css'

const API_BASE = '' // Vite proxy: /api -> localhost:8000

function getSourceTags(steps) {
  if (!steps || !steps.length) return ['Belge Arşivi', 'Web Kaynağı']
  const ids = new Set(steps.map((s) => s.id))
  const tags = []
  if (ids.has('retrieve') || ids.has('grade_documents')) tags.push('Belge Arşivi')
  if (ids.has('websearch')) tags.push('Canlı Arama (Tavily)')
  if (tags.length === 0) tags.push('Web Kaynağı')
  return tags
}

export default function ChatDemo() {
  const [question, setQuestion] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [conversation, setConversation] = useState(null)

  async function handleSubmit(e) {
    e.preventDefault()
    const q = (question || '').trim()
    if (!q) return
    setLoading(true)
    setError(null)
    setConversation(null)
    try {
      const res = await fetch(`${API_BASE}/api/query`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: q }),
      })
      const data = await res.json().catch(() => ({}))
      if (!res.ok) {
        setError(data.detail || 'Bir hata oluştu.')
        return
      }
      setConversation({
        question: data.question,
        answer: data.answer || '',
        steps: data.steps || [],
      })
      setQuestion('')
    } catch (err) {
      setError('Sunucuya bağlanılamadı. Backend çalışıyor mu?')
    } finally {
      setLoading(false)
    }
  }

  const sourceTags = conversation ? getSourceTags(conversation.steps) : ['Belge Arşivi', 'Web Kaynağı']

  return (
    <section id="demo" className="chat-demo">
      <div className="chat-demo-inner">
        <h2 className="section-title">Canlı Demo</h2>
        <p className="section-subtitle">
          Bir soru yazın; sistem belge arşivini veya web aramasını kullanarak yanıt üretir.
        </p>

        <div className="chat-card">
          <div className="chat-messages">
            {!conversation && !loading && (
              <div className="chat-placeholder">
                Örn: Küresel sıcaklığın deniz seviyelerine etkisi nedir?
              </div>
            )}
            {conversation && (
              <>
                <div className="bubble user">
                  <p>{conversation.question}</p>
                </div>
                <div className="bubble assistant">
                  <p>{conversation.answer || 'Yanıt üretilemedi.'}</p>
                  <div className="source-tags">
                    {sourceTags.map((tag) => (
                      <span key={tag} className="source-tag">
                        {tag}
                      </span>
                    ))}
                  </div>
                  <div className="verified-badge">
                    <span className="verified-icon">✓</span>
                    Doğrulandı
                  </div>
                </div>
              </>
            )}
            {loading && (
              <div className="bubble assistant loading-bubble">
                <p>Yanıt hazırlanıyor…</p>
                <div className="loading-dots">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            )}
          </div>

          <form onSubmit={handleSubmit} className="chat-form">
            <input
              type="text"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="Sorunuzu yazın..."
              disabled={loading}
              className="chat-input"
            />
            <button type="submit" disabled={loading} className="chat-send">
              Gönder
            </button>
          </form>

          {error && <p className="chat-error">{error}</p>}
        </div>
      </div>
    </section>
  )
}
