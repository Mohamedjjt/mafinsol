/* MA Solutions: kleine, afhankelijkheidsvrije scripts (thema, menu, reveal, formulier). */
(function () {
  'use strict';
  var body = document.body;

  /* ---- Donkere modus (voorkeur blijft lokaal in de browser, geen persoonsgegevens) ---- */
  var themeBtn = document.getElementById('theme-toggle');
  function syncThemeBtn() {
    if (!themeBtn) return;
    var dark = body.classList.contains('dark');
    themeBtn.setAttribute('aria-pressed', String(dark));
    themeBtn.setAttribute('aria-label', dark ? 'Schakel naar lichte modus' : 'Schakel naar donkere modus');
  }
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      body.classList.toggle('dark');
      try { localStorage.setItem('ma-theme', body.classList.contains('dark') ? 'dark' : 'light'); } catch (e) {}
      syncThemeBtn();
    });
    syncThemeBtn();
  }

  /* ---- Menu op mobiel ---- */
  var menuBtn = document.getElementById('menu-toggle');
  var nav = document.getElementById('site-nav');
  if (menuBtn && nav) {
    var setMenu = function (open) {
      nav.classList.toggle('open', open);
      menuBtn.setAttribute('aria-expanded', String(open));
    };
    menuBtn.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
    nav.addEventListener('click', function (e) { if (e.target.tagName === 'A') setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  /* ---- Header-schaduw bij scrollen ---- */
  var hdr = document.getElementById('site-header');
  if (hdr) {
    var onScroll = function () { hdr.classList.toggle('scrolled', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---- Reveal bij scrollen ---- */
  var items = [].slice.call(document.querySelectorAll('.reveal'));
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---- Contactformulier (Formspree) ---- */
  var form = document.getElementById('contact-form');
  if (form) {
    var status = document.getElementById('form-status');
    var btn = form.querySelector('button[type="submit"]');
    var required = ['naam', 'email', 'beschrijving'];
    var show = function (cls, html) { status.className = 'form-status ' + cls; status.innerHTML = html; };
    var emailOk = function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v); };

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      status.className = 'form-status'; status.textContent = '';
      var bad = null;
      required.forEach(function (name) {
        var el = form.elements[name];
        var err = document.getElementById('err-' + name);
        var ok = el.value.trim() !== '' && (name !== 'email' || emailOk(el.value.trim()));
        el.setAttribute('aria-invalid', ok ? 'false' : 'true');
        err.textContent = ok ? '' : (name === 'email' ? 'Vul een geldig e-mailadres in.' : 'Dit veld is verplicht.');
        if (!ok && !bad) bad = el;
      });
      if (bad) { bad.focus(); return; }
      if (form.elements._gotcha && form.elements._gotcha.value) return; /* bot */

      var data = {};
      [].forEach.call(form.elements, function (el) { if (el.name && el.name !== '_gotcha') data[el.name] = el.value; });
      data._subject = 'Nieuw contactverzoek via mafinsol.nl (' + (document.documentElement.getAttribute('data-site') || 'website') + ')';

      btn.disabled = true;
      var label = btn.querySelector('span'); var old = label.textContent; label.textContent = 'Versturen...';
      fetch(form.action, { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) {
          if (!r.ok) throw new Error('http ' + r.status);
          form.reset();
          show('ok', '<strong>Bedankt, uw aanvraag is verstuurd.</strong> Ik neem binnen één werkdag contact met u op.');
        })
        .catch(function () {
          show('err', 'Versturen is niet gelukt. Stuur uw aanvraag direct naar <a href="mailto:info@mafinsol.nl">info@mafinsol.nl</a>.');
        })
        .then(function () { btn.disabled = false; label.textContent = old; });
    });
  }
})();
