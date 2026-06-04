// Sections2.jsx — References (Referenties) and Workflow (Werkwijze).

function References({ c }) {
  return (
    <section id="referenties" className="section section-alt" aria-labelledby="ref-title">
      <div className="container">
        <Reveal>
          <span className="section-label">Opdrachtgevers</span>
          <h2 className="section-title" id="ref-title">{c.refTitle}</h2>
        </Reveal>
        <Reveal className="referenties-grid">
          {c.refs.map((r, i) => (
            <article className="ref-card" key={i}>
              {r.logo && (
                <div className="ref-logo"><img src={`../../assets/logos/${r.logo}`} alt={`${r.org} logo`} /></div>
              )}
              <div className="ref-org">{r.org}</div>
              <p className="ref-desc">{r.desc}</p>
            </article>
          ))}
        </Reveal>
      </div>
    </section>
  );
}

function Workflow() {
  return (
    <section id="werkwijze" className="section" aria-labelledby="werkwijze-title">
      <div className="container">
        <Reveal>
          <span className="section-label">Onze werkwijze</span>
          <h2 className="section-title" id="werkwijze-title">Hoe wij werken — en waarom dat voor u het verschil maakt</h2>
          <p className="section-intro">Wij geloven in heldere afspraken, concrete resultaten en een samenwerking die echt werkt. Geen bureaucratie, geen onduidelijkheid — gewoon goede mensen op de juiste plek.</p>
        </Reveal>
        <Reveal className="werkwijze-grid">
          {WERKWIJZE.map(([num, title, desc]) => (
            <div className="werkwijze-item" key={num}>
              <div className="werkwijze-num">{num}</div>
              <h3 className="werkwijze-title">{title}</h3>
              <p className="werkwijze-desc">{desc}</p>
            </div>
          ))}
        </Reveal>
      </div>
    </section>
  );
}

Object.assign(window, { References, Workflow });
