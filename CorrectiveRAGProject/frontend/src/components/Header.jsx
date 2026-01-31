import './Header.css'

export default function Header() {
  return (
    <header className="header">
      <div className="header-inner">
        <a href="#" className="logo">
          <span className="logo-icon">R</span>
          <span className="logo-text">Corrective RAG</span>
        </a>
        <nav className="nav">
          <a href="#ozellikler">Özellikler</a>
          <a href="#nasil-calisir">Nasıl Çalışır</a>
          <a href="#demo">Demo</a>
        </nav>
      </div>
    </header>
  )
}
