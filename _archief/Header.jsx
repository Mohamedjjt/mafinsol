// Header.jsx — sticky header with logo, nav, Finance/Care pill, dark toggle.
const { useState: useStateH, useEffect: useEffectH } = React;

function Header({ mode, setMode, dark, setDark }) {
  useEffectH(() => {
    const hdr = document.getElementById('site-header');
    const onScroll = () => { if (hdr) hdr.classList.toggle('scrolled', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  const nav = [
    ['#over-mij', 'Over ons'], ['#diensten', 'Diensten'],
    ['#referenties', 'Referenties'], ['#werkwijze', 'Werkwijze'], ['#contact', 'Contact'],
  ];

  return (
    <header id="site-header" role="banner">
      <div className="header-inner">
        <a href="#hero" className="logo"><Logo mode={mode} /></a>
        <nav aria-label="Paginanavigatie">
          <ul className="nav-links">
            {nav.map(([href, label]) => <li key={href}><a href={href}>{label}</a></li>)}
          </ul>
        </nav>
        <div className="header-right">
          <div className="pill-toggle" role="tablist" aria-label="Wissel tussen Finance en Care">
            <span className="pill-indicator" aria-hidden="true"></span>
            <button type="button" className={`pill-option ${mode === 'finance' ? 'active' : ''}`}
              role="tab" aria-selected={mode === 'finance'} onClick={() => setMode('finance')}>Finance</button>
            <button type="button" className={`pill-option ${mode === 'care' ? 'active' : ''}`}
              role="tab" aria-selected={mode === 'care'} onClick={() => setMode('care')}>Care</button>
          </div>
          <button className="dark-toggle" aria-label="Schakel donkere modus" onClick={() => setDark(d => !d)}>
            {dark
              ? <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
              : <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M5 5l1.5 1.5M17.5 17.5L19 19M2 12h2M20 12h2M5 19l1.5-1.5M17.5 6.5L19 5"/></svg>}
          </button>
        </div>
      </div>
    </header>
  );
}
Object.assign(window, { Header });
