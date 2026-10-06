// Contact.jsx — contact form with Formspree submit, modal, plus Footer.
const { useState: useStateC } = React;

function Contact({ mode }) {
  const [modal, setModal] = useStateC(null); // null | {naam, email} | {error: true}
  const [errors, setErrors] = useStateC({});
  const [sending, setSending] = useStateC(false);

  async function submit(e) {
    e.preventDefault();
    const f = e.target;
    const naam = f.naam.value.trim(), email = f.email.value.trim(), beschrijving = f.beschrijving.value.trim();
    const err = {};
    if (!naam) err.naam = true;
    if (!email) err.email = true;
    if (!beschrijving) err.beschrijving = true;
    setErrors(err);
    if (Object.keys(err).length) return;

    setSending(true);
    try {
      const response = await fetch('https://formspree.io/f/xwvjpzye', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({
          naam: f.naam.value,
          organisatie: f.organisatie.value,
          email: f.email.value,
          telefoon: f.telefoon.value,
          'opdracht-type': f['opdracht-type'].value,
          beschrijving: f.beschrijving.value,
        })
      });
      if (response.ok) {
        setModal({ naam, email });
        f.reset();
      } else {
        setModal({ error: true });
      }
    } catch {
      setModal({ error: true });
    } finally {
      setSending(false);
    }
  }

  const opts = mode === 'care'
    ? [['care-ambulant', 'Ambulante begeleiding'], ['care-gehandicaptenzorg', 'Gehandicaptenzorg'], ['care-vervanging', 'Vervanging / Project']]
    : [['finance-controlling', 'Interim Controlling'], ['finance-erp', 'ERP & Proces'], ['finance-reporting', 'Reporting & Data']];

  return (
    <section id="contact" className="section" aria-labelledby="contact-title">
      <div className="container">
        <div className="contact-grid">
          <Reveal>
            <span className="contact-cta-label">Contact</span>
            <h2 className="contact-cta-title" id="contact-title">Een opdracht bespreken? Laat uw gegevens achter — wij reageren binnen één werkdag.</h2>
            <div className="contact-details">
              <div className="contact-detail"><strong>E-mail</strong><a href="mailto:info@mafinsol.nl">info@mafinsol.nl</a></div>
              <div className="contact-detail"><strong>KvK</strong><span>93664850</span></div>
            </div>
          </Reveal>
          <Reveal className="">
            <form className="contact-form" onSubmit={submit} noValidate aria-label="Offerte aanvragen">
              <div className="form-row">
                <div className="form-group"><label htmlFor="naam">Naam *</label>
                  <input id="naam" name="naam" type="text" placeholder="Uw volledige naam" style={{ borderColor: errors.naam ? '#e05252' : '' }} /></div>
                <div className="form-group"><label htmlFor="organisatie">Organisatie</label>
                  <input id="organisatie" name="organisatie" type="text" placeholder="Bedrijfsnaam" /></div>
              </div>
              <div className="form-row">
                <div className="form-group"><label htmlFor="email">E-mail *</label>
                  <input id="email" name="email" type="email" placeholder="u@bedrijf.nl" style={{ borderColor: errors.email ? '#e05252' : '' }} /></div>
                <div className="form-group"><label htmlFor="telefoon">Telefoon</label>
                  <input id="telefoon" name="telefoon" type="tel" placeholder="+31 6 ..." /></div>
              </div>
              <div className="form-group"><label htmlFor="opdracht-type">Type opdracht</label>
                <select id="opdracht-type" name="opdracht-type">
                  {opts.map(([v, l]) => <option key={v} value={v}>{l}</option>)}
                  <option value="anders">Anders</option>
                </select>
              </div>
              <div className="form-group"><label htmlFor="beschrijving">Korte beschrijving *</label>
                <textarea id="beschrijving" name="beschrijving" placeholder="Beschrijf kort de opdracht, uw organisatie en wat u zoekt..." style={{ borderColor: errors.beschrijving ? '#e05252' : '' }}></textarea></div>
              <button type="submit" className="btn-submit" disabled={sending}>
                {sending ? 'Versturen...' : 'Verstuur contactverzoek'}<Arrow />
              </button>
            </form>
          </Reveal>
        </div>
      </div>

      <div className={`modal-overlay ${modal ? 'open' : ''}`} role="dialog" aria-modal="true" onClick={(e) => { if (e.target.classList.contains('modal-overlay')) setModal(null); }}>
        <div className="modal-box">
          <h3 className="modal-title">{modal && modal.error ? 'Er ging iets mis' : 'Aanvraag ontvangen'}</h3>
          <div className="modal-body">
            {modal && (modal.error
              ? <p>Stuur uw aanvraag direct naar <a href="mailto:info@mafinsol.nl" style={{ color: 'var(--accent)' }}>info@mafinsol.nl</a>.</p>
              : <React.Fragment>
                  <p>Bedankt, <strong>{modal.naam}</strong>! Uw aanvraag is verstuurd.</p>
                  <p style={{ marginTop: '.75rem', fontSize: '.88rem' }}>Wij nemen binnen één werkdag contact met u op via <strong>{modal.email}</strong>.</p>
                </React.Fragment>
            )}
          </div>
          <button className="modal-close" onClick={() => setModal(null)}>Sluiten</button>
        </div>
      </div>
    </section>
  );
}

function Footer({ c }) {
  return (
    <footer role="contentinfo">
      <div className="footer-inner">
        <p className="footer-copy">{c.footer}</p>
        <nav aria-label="Juridische links">
          <ul className="footer-links">
            <li><a href="algemene-voorwaarden.html">Algemene Voorwaarden</a></li>
            <li><a href="privacyverklaring.html">Privacyverklaring</a></li>
          </ul>
        </nav>
        <p className="footer-kvk">KvK 93664850</p>
      </div>
    </footer>
  );
}

Object.assign(window, { Contact, Footer });
