// Sections.jsx — Hero, About (Over ons), Services (Diensten).

function Hero({ c }) {
  return (
    <section id="hero" className="section" aria-label="Introductie">
      <div className="container">
        <div className="hero-grid">
          <Reveal className="hero-content">
            <span className="hero-eyebrow">{c.heroEyebrow}</span>
            <h1 className="hero-headline">{c.heroHeadline}</h1>
            <p className="hero-sub">{c.heroSub}</p>
            <div className="hero-tags">
              {SHARED_TAGS.map((t) => <span className="tag" key={t}>{t}</span>)}
            </div>
            <a href="#contact" className="hero-cta">Opdracht bespreken<Arrow /></a>
          </Reveal>
          <Reveal className="hero-visual">
            {c.stats.map((s, i) => (
              <div className="hero-stat" key={i}>
                <div className="hero-stat-num">{s.num}</div>
                <div className="hero-stat-label">{s.label.split('\n').map((l, j) => <React.Fragment key={j}>{l}{j === 0 ? <br/> : null}</React.Fragment>)}</div>
              </div>
            ))}
          </Reveal>
        </div>
      </div>
    </section>
  );
}

function About({ c }) {
  return (
    <section id="over-mij" className="section section-alt" aria-labelledby="over-mij-title">
      <div className="container">
        <div className="about-grid">
          <Reveal className="about-text">
            <span className="section-label">Wie wij zijn</span>
            <h2 className="section-title" id="over-mij-title">
              {c.aboutTitle[0]}<br/><em>{c.aboutTitle[1]}</em>
            </h2>
            {c.aboutBody.map((p, i) => <p key={i}>{p}</p>)}
          </Reveal>
          <Reveal className="credentials">
            <p className="credentials-title">{c.credTitle}</p>
            {c.creds.map(([name, meta], i) => (
              <div className="credential-item" key={i}>
                <span className="cred-name">{name}</span>
                <span className="cred-meta">{meta}</span>
              </div>
            ))}
          </Reveal>
        </div>
      </div>
    </section>
  );
}

function Services({ c }) {
  return (
    <section id="diensten" className="section" aria-labelledby="diensten-title">
      <div className="container">
        <Reveal>
          <span className="section-label">Diensten</span>
          <h2 className="section-title" id="diensten-title">{c.dienstenTitle}</h2>
          <p className="section-intro">{c.dienstenIntro}</p>
        </Reveal>
        <Reveal className="diensten-grid">
          {c.diensten.map(([num, title, desc]) => (
            <article className="dienst-card" key={num}>
              <div className="dienst-num">{num}</div>
              <h3 className="dienst-title">{title}</h3>
              <p className="dienst-desc">{desc}</p>
            </article>
          ))}
        </Reveal>
      </div>
    </section>
  );
}

Object.assign(window, { Hero, About, Services });
