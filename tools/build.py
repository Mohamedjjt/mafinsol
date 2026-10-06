#!/usr/bin/env python3
"""Bouwt de statische pagina's van mafinsol.nl (geen frameworks, geen build-stap in de browser).

Gebruik:  python3 tools/build.py
Schrijft: index.html (Finance), care/index.html, 404.html, sitemap.xml, robots.txt
Teksten staan hieronder in PAGES; pas ze daar aan en draai het script opnieuw.
"""
import html, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://mafinsol.nl"
EMAIL = "info@mafinsol.nl"
KVK = "93664850"
V = "8"  # cache-buster voor css/js
# TODO: btw-nummer en vestigingsadres hier als <li>-regels toevoegen (zie tools/TODO.md), bijv.
# EXTRA_CONTACT = '<li><strong>BTW</strong><span>NL...B01</span></li>'
EXTRA_CONTACT = ""
esc = html.escape

ICON_ARROW = '<svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_CHECK = '<svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8.5l3.2 3L13 4.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_MOON = '<svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'
ICON_SUN = '<svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M5 5l1.5 1.5M17.5 17.5L19 19M2 12h2M20 12h2M5 19l1.5-1.5M17.5 6.5L19 5"/></svg>'
ICON_MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'


def logo(line1):
    return (
        f'<svg viewBox="0 0 220 56" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MA {line1.title()} Solutions">'
        '<text class="l-main" x="4" y="38" font-family="\'Helvetica Neue\',Arial,sans-serif" font-size="28" font-weight="600" letter-spacing="-0.5">MA</text>'
        '<circle class="l-dot" cx="54" cy="29" r="4"/>'
        f'<text class="l-main" x="66" y="24" font-family="\'Helvetica Neue\',Arial,sans-serif" font-size="10" font-weight="500" letter-spacing="2.5">{line1}</text>'
        '<text class="l-sub" x="66" y="38" font-family="\'Helvetica Neue\',Arial,sans-serif" font-size="10" font-weight="300" letter-spacing="2.5">SOLUTIONS</text>'
        '</svg>'
    )


# --------------------------------------------------------------------------
# Inhoud per pagina
# --------------------------------------------------------------------------
FINANCE = dict(
    key="finance", path="/", file="index.html", body_class="", theme="#0a2342", brand="MA Financial Solutions",
    logo_line="FINANCIAL", favicon="assets/favicon.svg", og="assets/og-finance.png", locality="finance",
    title="Interim Financial Controller & SAP | MA Financial Solutions",
    desc="Interim financial controller en SAP S/4HANA-specialist in Eindhoven en heel Nederland. Ervaring bij ASML, Philips, Jumbo en Van Loon Group. Snel inzetbaar.",
    og_title="Interim Financial Controller & SAP-specialist | MA Financial Solutions",
    og_desc="Maandafsluitingen, consolidatie en SAP-migraties door een snel inzetbare interim finance professional. Ervaring bij ASML, Philips, Jumbo en Van Loon Group.",
    eyebrow="Interim finance · Eindhoven, Nederland & internationaal",
    h1="Interim Financial Controller en SAP-specialist die direct waarde levert",
    sub="Ik help finance-afdelingen met maandafsluitingen, consolidatie en SAP-migraties. Vanuit Eindhoven, op locatie of remote, in heel Nederland en internationaal.",
    cta="Opdracht bespreken",
    meta=["Snel inzetbaar", "Modelovereenkomst beschikbaar", "Nederlands en Engels"],
    stats=[("4+", "jaar actief als interim finance professional"),
           ("4", "grote opdrachtgevers: ASML, Philips, Jumbo en Van Loon Group"),
           ("SAP", "S/4HANA, ECC en RE-FX: ervaring met migraties")],
    proof_label="Ervaring bij",
    proof=[("asml.svg", "ASML"), ("philips.svg", "Philips"), ("jumbo.svg", "Jumbo"), ("van-loon-group.svg", "Van Loon Group")],
    about_label="Over mij",
    about_title=("Specialist in finance", "die verder kijkt"),
    about=[
        "Ik ben Mohamed, interim finance professional. Ik werk op het snijvlak van financial accounting, procesoptimalisatie en ERP-implementatie. Ik ben ruim vier jaar actief als interim en heb meer dan vijf jaar finance-ervaring bij grote organisaties.",
        "Een goede finance professional beheerst niet alleen de cijfers, maar begrijpt ook hoe een organisatie werkt. Daarom lever ik meteen waarde, zonder inwerkperiode van weken.",
    ],
    cred_title="Kernkwaliteiten",
    creds=[
        ("International Financial Reporting", "IFRS 16, consolidatie, multi-entity, Europese entiteiten"),
        ("ERP en systemen", "SAP S/4HANA, SAP ECC, RE-FX, Microsoft Dynamics"),
        ("Data en procesverbetering", "Power BI, Lean, RPA: van analyse tot implementatie"),
        ("Talen", "Nederlands en Engels, zakelijk op hoog niveau"),
        ("Zakelijk", f"KvK {KVK} · modelovereenkomst · beroepsaansprakelijkheid"),
    ],
    services_title="Finance-diensten",
    services_intro="Finance-expertise op de gebieden waar uw organisatie het meest behoefte aan heeft.",
    services=[
        ("Interim Financial Controlling", "Periodieke afsluitingen, consolidatie van Europese entiteiten, SOX-controles en management reporting, ingezet waar continuïteit en nauwkeurigheid tellen."),
        ("ERP-migratie en procesoptimalisatie", "Ervaring met complexe SAP-trajecten en procesherontwerp. Uw organisatie maakt de overgang zonder verlies van data-integriteit of snelheid."),
        ("Financial Accounting en Reporting", "Van GL-accounting tot IFRS 16, BTW/ICP-aangiften en internationale belastingaangiften: nauwkeurige verwerking en heldere rapportage."),
        ("Data- en procesanalyse", "Ik breng financiële processen in kaart, vind de bottlenecks en vertaal data naar inzicht, met Power BI, Lean en RPA als instrumenten."),
        ("Automatisering en RPA", "Repetitieve financiële processen automatiseer ik met RPA-tooling, zodat uw team zich richt op werk dat er echt toe doet."),
        ("Dashboarding en rapportage", "Van ruwe data naar heldere management dashboards in Power BI: inzicht dat besluitvorming versnelt, visueel en op maat."),
    ],
    chips_label="Systemen en methoden",
    chips=["SAP S/4HANA", "SAP ECC", "SAP RE-FX", "Microsoft Dynamics", "IFRS 16", "SOX-controles", "BTW/ICP", "Power BI", "Lean", "RPA"],
    refs_title="Opdrachtgevers",
    refs_intro="Een selectie van organisaties waar ik interim opdrachten heb uitgevoerd.",
    refs=[
        ("jumbo.svg", "Jumbo Supermarkten", "Een van de grootste retailers van Europa, actief in Nederland en België met meer dan 700 vestigingen."),
        ("philips.svg", "Philips IGTD", "Wereldwijd medisch-technologisch concern. Interim opdrachten uitgevoerd voor financiële processen in meerdere Europese landen."),
        ("asml.svg", "ASML", "Marktleider in lithografiesystemen voor de halfgeleiderindustrie, actief in meer dan 60 landen wereldwijd."),
        ("van-loon-group.svg", "Van Loon Group", "Toonaangevend familiebedrijf in transport en logistiek met Europees netwerk en diverse operationele entiteiten."),
    ],
    steps_title="Zo werk ik",
    steps_intro="Heldere afspraken, concrete resultaten en een samenwerking zonder omwegen.",
    steps=[
        ("Korte intake", "Ik luister eerst. Een korte intake volstaat om te begrijpen wat uw organisatie nodig heeft, zodat ik snel kan starten."),
        ("Afgebakend op resultaat", "Elke opdracht wordt vooraf helder afgebakend op resultaat. U weet wat u krijgt, en ik lever het."),
        ("Transparant samenwerken", "Heldere overeenkomsten zonder verborgen kosten. Ik werk met een modelovereenkomst."),
        ("Flexibel in duur en plaats", "Een project van enkele weken of een langlopend traject, op locatie of remote, afhankelijk van wat de opdracht vraagt."),
    ],
    faq=[
        ("Hoe snel kunt u starten?", "Na een korte intake kan ik op korte termijn beginnen. De exacte startdatum hangt af van mijn agenda. Neem contact op voor de actuele beschikbaarheid."),
        ("Werkt u op locatie of remote?", "Beide. Ik werk op locatie in Eindhoven, Noord-Brabant en de rest van Nederland, in België en internationaal, of remote. Dat hangt af van wat de opdracht vraagt."),
        ("Voor welke duur bent u beschikbaar?", "Van een project van enkele weken tot een langlopend traject. Samen bepalen we wat past bij de opdracht."),
        ("Werkt u met een modelovereenkomst?", f"Ja, een modelovereenkomst is beschikbaar. Ik werk als zelfstandige onder KvK-nummer {KVK}."),
        ("Met welke systemen heeft u ervaring?", "Met SAP S/4HANA, SAP ECC en SAP RE-FX (inclusief migraties), Microsoft Dynamics en Power BI, aangevuld met Lean en RPA voor procesverbetering."),
    ],
    contact_title="Een opdracht bespreken?",
    contact_lead="Laat uw gegevens achter of mail direct. Ik reageer binnen één werkdag.",
    form_types=[("finance-controlling", "Interim controlling"), ("finance-erp", "ERP en proces"), ("finance-reporting", "Reporting en data"), ("anders", "Anders")],
    form_placeholder="Beschrijf kort de opdracht, uw organisatie en wat u zoekt...",
    cross=("Zoekt u zorgbegeleiding?", "Naast finance ben ik actief als zorgbegeleider (ambulante begeleiding en gehandicaptenzorg) via MA Care Solutions.", "/care/", "Naar MA Care Solutions"),
)

CARE = dict(
    key="care", path="/care/", file="care/index.html", body_class="care", theme="#0d4f5c", brand="MA Care Solutions",
    logo_line="CARE", favicon="assets/favicon-care.svg", og="assets/og-care.png", locality="care",
    title="Ambulante begeleiding & gehandicaptenzorg | MA Care Solutions",
    desc="Zorgbegeleider (PBMZ4) voor ambulante begeleiding en gehandicaptenzorg in Noord-Brabant en Limburg. Flexibel en snel inzetbaar voor zorginstellingen.",
    og_title="Ambulante begeleiding & gehandicaptenzorg | MA Care Solutions",
    og_desc="Zorgbegeleider (PBMZ4) voor zorginstellingen in Noord-Brabant, Limburg en landelijk. Flexibel inzetbaar bij uitval, piekbelasting en projecten.",
    eyebrow="Persoonlijke begeleiding · Maatschappelijke zorg · Noord-Brabant & Limburg",
    h1="Ambulante begeleiding en gehandicaptenzorg die aansluit bij de cliënt",
    sub="Ik ben zorgbegeleider (PBMZ4) en ondersteun zorginstellingen die snel en flexibel willen schakelen, met warme, gestructureerde begeleiding voor cliënten die erop kunnen rekenen.",
    cta="Inzet bespreken",
    meta=["Snel inzetbaar, ook op korte termijn", "Modelovereenkomst beschikbaar", "Noord-Brabant, Limburg en landelijk"],
    stats=[("PBMZ4", "Persoonlijk Begeleider Maatschappelijke Zorg, mbo niveau 4"),
           ("Snel", "inzetbaar, ook op korte termijn"),
           ("Flex", "ambulant, intramuraal of op projectbasis")],
    proof_label="Ingezet bij",
    proof=[("helderzorg.png", "Helderzorg"), ("amor-zorg.svg", "Amor Zorg")],
    about_label="Over mij",
    about_title=("Zorgprofessional die", "direct het verschil maakt"),
    about=[
        "MA Care Solutions is mijn zorgpraktijk voor flexibele inzet bij zorginstellingen. Ik sluit direct aan bij uw werkwijze, uw cliënten en uw team, zonder lange inwerktijd.",
        "Van ambulante begeleiding tot gehandicaptenzorg: zorginstellingen kiezen voor mij omdat ik snel schakel, transparant communiceer en kwaliteit boven kwantiteit stel.",
    ],
    cred_title="Wat ik bied",
    creds=[
        ("Ambulante begeleiding", "Thuis, op locatie of hybride, passend bij uw zorgmodel"),
        ("Gehandicaptenzorg", "Begeleiding bij verstandelijke en lichamelijke beperkingen"),
        ("Vervanging en projectinzet", "Flexibel beschikbaar, ook op korte termijn"),
        ("Rapportage en kwaliteit", "Ondersteuningsplannen en dossiervorming conform uw standaard"),
        ("Zakelijk", f"KvK {KVK} · modelovereenkomst · beroepsaansprakelijkheid"),
    ],
    services_title="Care-diensten",
    services_intro="Gekwalificeerde begeleiding voor zorginstellingen: flexibel, betrouwbaar en snel inzetbaar.",
    services=[
        ("Ambulante begeleiding", "Ik ondersteun cliënten in hun eigen omgeving, bij zelfzorg, wonen en het opbouwen van een dagstructuur die echt past."),
        ("Gehandicaptenzorg", "Begeleiding van mensen met verstandelijke en/of lichamelijke beperkingen, gericht op participatie, zelfregie en kwaliteit van leven."),
        ("Begeleidingsplannen en rapportage", "Ik observeer en rapporteer gestructureerd en stel ondersteuningsplannen op, zodat uw dossiervoering op orde blijft."),
        ("Vervanging en projectinzet", "Snel schakelen bij uitval of piekbelasting. Zo blijft de continuïteit gewaarborgd en krijgen cliënten de aandacht die ze verdienen."),
    ],
    chips_label="Expertise",
    chips=["Ambulante begeleiding", "Gehandicaptenzorg", "PBMZ4", "Ondersteuningsplannen", "Zelfredzaamheid", "Dossiervorming"],
    refs_title="Ingezet bij zorginstellingen",
    refs_intro="Een selectie van zorgorganisaties waar ik begeleiding heb geleverd.",
    refs=[
        ("helderzorg.png", "Helderzorg", "Ambulante zorgverlener in Apeldoorn, actief in Gelderland en Overijssel, gericht op herstel en zelfstandigheid van cliënten met complexe ondersteuningsvragen."),
        ("amor-zorg.svg", "Amor Zorg", "Zorgaanbieder gespecialiseerd in ambulante begeleiding en ondersteuning van mensen met een hulpvraag in de thuissituatie."),
    ],
    steps_title="Zo werk ik",
    steps_intro="Duidelijke afspraken en een begeleider die aansluit op uw team.",
    steps=[
        ("Korte intake", "We bespreken de zorgvraag, het team en de cliënten, zodat ik direct kan aansluiten."),
        ("Afspraken vooraf", "Duur, uren en werkwijze leggen we vooraf vast. Er zijn geen verrassingen achteraf."),
        ("Begeleiden en rapporteren", "Ik begeleid, observeer en rapporteer volgens uw standaard en de afspraken in het ondersteuningsplan."),
        ("Flexibel opschalen", "Bij uitval of piekbelasting kan ik snel schakelen, voor een korte periode of een langer traject."),
    ],
    faq=[
        ("In welke regio bent u inzetbaar?", "Vooral in Noord-Brabant en Limburg, vanuit Eindhoven. Landelijke inzet is mogelijk in overleg."),
        ("Welke opleiding heeft u?", "Ik ben PBMZ4 (Persoonlijk Begeleider Maatschappelijke Zorg), een mbo-opleiding op niveau 4."),
        ("Voor welke doelgroepen werkt u?", "Voor mensen met verstandelijke en/of lichamelijke beperkingen en voor cliënten met een ondersteuningsvraag in de thuissituatie, ambulant of intramuraal."),
        ("Hoe snel kunt u beginnen?", "Ook op korte termijn, bijvoorbeeld bij uitval of piekbelasting. Neem contact op voor de actuele beschikbaarheid."),
        ("Werkt u met een modelovereenkomst?", f"Ja, een modelovereenkomst is beschikbaar. Ik werk als zelfstandige onder KvK-nummer {KVK}."),
    ],
    contact_title="Inzet bespreken?",
    contact_lead="Laat uw gegevens achter of mail direct. Ik reageer binnen één werkdag.",
    form_types=[("care-ambulant", "Ambulante begeleiding"), ("care-gehandicaptenzorg", "Gehandicaptenzorg"), ("care-vervanging", "Vervanging / project"), ("anders", "Anders")],
    form_placeholder="Beschrijf kort de zorgvraag, uw organisatie en de gewenste periode...",
    cross=("Zoekt u een interim finance professional?", "Naast zorgbegeleiding ben ik actief als interim financial controller en SAP-specialist via MA Financial Solutions.", "/", "Naar MA Financial Solutions"),
)


# --------------------------------------------------------------------------
# Onderdelen
# --------------------------------------------------------------------------
def header(p):
    cur_f = ' aria-current="page"' if p["key"] == "finance" else ""
    cur_c = ' aria-current="page"' if p["key"] == "care" else ""
    return f'''<header id="site-header" role="banner">
  <div class="header-inner">
    <a href="{p["path"]}" class="logo" aria-label="{p["brand"]}, naar boven">{logo(p["logo_line"])}</a>
    <nav class="nav" id="site-nav" aria-label="Paginanavigatie">
      <ul class="nav-links">
        <li><a href="#over-mij">Over mij</a></li>
        <li><a href="#diensten">Diensten</a></li>
        <li><a href="#referenties">Opdrachtgevers</a></li>
        <li><a href="#werkwijze">Werkwijze</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
    <div class="header-right">
      <nav class="pill-toggle" aria-label="Kies dienst">
        <a href="/"{cur_f}>Finance</a>
        <a href="/care/"{cur_c}>Care</a>
      </nav>
      <button type="button" class="icon-btn" id="theme-toggle" aria-pressed="false" aria-label="Schakel naar donkere modus">{ICON_MOON}{ICON_SUN}</button>
      <button type="button" class="icon-btn menu-btn" id="menu-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu">{ICON_MENU}</button>
    </div>
  </div>
</header>'''


def section_head(label, title, intro=None):
    out = f'<span class="eyebrow">{esc(label)}</span>\n        <h2 class="section-title">{title}</h2>'
    if intro:
        out += f'\n        <p class="section-intro">{esc(intro)}</p>'
    return out


def page(p):
    meta_items = "".join(f"<li>{ICON_CHECK}<span>{esc(m)}</span></li>" for m in p["meta"])
    stats = "".join(f'<div class="stat"><div class="stat-num">{esc(n)}</div><div class="stat-label">{esc(l)}</div></div>' for n, l in p["stats"])
    proof = "".join(f'<img src="/assets/logos/{f}" alt="{esc(n)}" loading="lazy">' for f, n in p["proof"])
    creds = "".join(f'<div class="cred"><span class="cred-name">{esc(n)}</span><span class="cred-meta">{esc(m)}</span></div>' for n, m in p["creds"])
    services = "".join(
        f'<article class="card"><div class="card-num">{i:02d}</div><h3>{esc(t)}</h3><p>{esc(d)}</p></article>'
        for i, (t, d) in enumerate(p["services"], 1))
    chips = "".join(f'<li class="chip">{esc(c)}</li>' for c in p["chips"])
    refs = "".join(
        f'<article class="ref-card"><div class="ref-logo"><img src="/assets/logos/{f}" alt="{esc(o)} logo" loading="lazy"></div>'
        f'<div class="ref-org">{esc(o)}</div><p>{esc(d)}</p></article>' for f, o, d in p["refs"])
    steps = "".join(
        f'<div class="step"><div class="step-num">{i:02d}</div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
        for i, (t, d) in enumerate(p["steps"], 1))
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in p["faq"])
    opts = "".join(f'<option value="{v}">{esc(l)}</option>' for v, l in p["form_types"])
    c_title, c_text, c_href, c_btn = p["cross"]
    other_logo_h = ""

    # structured data
    biz = json.loads((ROOT / "tools" / f"schema-{p['key']}.json").read_text(encoding="utf8"))
    graph = [biz, {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]}]
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))

    canonical = SITE + p["path"]
    og_img = f"{SITE}/{p['og']}"
    return f'''<!DOCTYPE html>
<html lang="nl" data-site="{p["brand"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["desc"])}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="{p["theme"]}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{esc(p["og_title"])}">
<meta property="og:description" content="{esc(p["og_desc"])}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{p["brand"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(p["og_title"])}">
<meta name="twitter:description" content="{esc(p["og_desc"])}">
<meta name="twitter:image" content="{og_img}">
<link rel="icon" type="image/svg+xml" href="/{p["favicon"]}">
<link rel="alternate" hreflang="nl" href="{canonical}">
<link rel="preload" href="/assets/fonts/Manrope-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/PlayfairDisplay-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/fonts/fonts.css?v={V}">
<link rel="stylesheet" href="/colors_and_type.css?v={V}">
<link rel="stylesheet" href="/assets/css/site.css?v={V}">
<script type="application/ld+json">{ld}</script>
</head>
<body class="{p["body_class"]}">
<script>document.documentElement.classList.add('js');try{{var t=localStorage.getItem('ma-theme');if(t==='dark'||(!t&&window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches))document.body.classList.add('dark')}}catch(e){{}}</script>
<a class="skip-link" href="#main">Naar de inhoud</a>
{header(p)}

<main id="main">
  <section class="hero" aria-label="Introductie">
    <div class="container hero-grid">
      <div class="reveal">
        <span class="eyebrow">{esc(p["eyebrow"])}</span>
        <h1>{esc(p["h1"])}</h1>
        <p class="hero-sub">{esc(p["sub"])}</p>
        <div class="hero-actions">
          <a class="btn" href="#contact">{esc(p["cta"])}{ICON_ARROW}</a>
          <a class="btn btn-ghost" href="mailto:{EMAIL}">Mail direct</a>
        </div>
        <ul class="hero-meta">{meta_items}</ul>
      </div>
      <aside class="stat-panel reveal" aria-label="In het kort">{stats}</aside>
    </div>
  </section>

  <section class="proof" aria-label="{esc(p["proof_label"])}">
    <div class="container proof-inner">
      <span class="proof-label">{esc(p["proof_label"])}</span>
      <div class="proof-logos">{proof}</div>
    </div>
  </section>

  <section id="over-mij" class="section" aria-labelledby="over-mij-title">
    <div class="container about-grid">
      <div class="about-text reveal">
        <span class="eyebrow">{esc(p["about_label"])}</span>
        <h2 class="section-title" id="over-mij-title">{esc(p["about_title"][0])} <em>{esc(p["about_title"][1])}</em></h2>
        {"".join(f"<p>{esc(t)}</p>" for t in p["about"])}
      </div>
      <div class="panel reveal">
        <p class="panel-title">{esc(p["cred_title"])}</p>
        {creds}
      </div>
    </div>
  </section>

  <section id="diensten" class="section section-alt" aria-labelledby="diensten-title">
    <div class="container">
      <div class="reveal">
        <span class="eyebrow">Diensten</span>
        <h2 class="section-title" id="diensten-title">{esc(p["services_title"])}</h2>
        <p class="section-intro">{esc(p["services_intro"])}</p>
      </div>
      <div class="cards cards-3 reveal">{services}</div>
      <p class="chips-label">{esc(p["chips_label"])}</p>
      <ul class="chips reveal">{chips}</ul>
    </div>
  </section>

  <section id="referenties" class="section" aria-labelledby="ref-title">
    <div class="container">
      <div class="reveal">
        <span class="eyebrow">Opdrachtgevers</span>
        <h2 class="section-title" id="ref-title">{esc(p["refs_title"])}</h2>
        <p class="section-intro">{esc(p["refs_intro"])}</p>
      </div>
      <div class="cards cards-refs reveal">{refs}</div>
    </div>
  </section>

  <section id="werkwijze" class="section section-alt" aria-labelledby="werkwijze-title">
    <div class="container">
      <div class="reveal">
        <span class="eyebrow">Werkwijze</span>
        <h2 class="section-title" id="werkwijze-title">{esc(p["steps_title"])}</h2>
        <p class="section-intro">{esc(p["steps_intro"])}</p>
      </div>
      <div class="steps reveal">{steps}</div>
    </div>
  </section>

  <section id="faq" class="section" aria-labelledby="faq-title">
    <div class="container">
      <div class="reveal">
        <span class="eyebrow">Veelgestelde vragen</span>
        <h2 class="section-title" id="faq-title">Goed om te weten</h2>
      </div>
      <div class="faq reveal">{faq}</div>
    </div>
  </section>

  <section class="section section-alt" aria-label="Andere dienst" style="padding-block: clamp(2.5rem, 5vw, 4rem)">
    <div class="container reveal" style="display:flex;flex-wrap:wrap;gap:1.25rem 2rem;align-items:center;justify-content:space-between">
      <div style="max-width:42rem">
        <h2 class="section-title" style="font-size:1.5rem;margin-bottom:.4rem">{esc(c_title)}</h2>
        <p style="margin:0;color:var(--muted)">{esc(c_text)}</p>
      </div>
      <a class="btn btn-ghost" href="{c_href}">{esc(c_btn)}{ICON_ARROW}</a>
    </div>
  </section>

  <section id="contact" class="contact" aria-labelledby="contact-title">
    <div class="container contact-grid">
      <div class="reveal">
        <span class="eyebrow">Contact</span>
        <h2 id="contact-title">{esc(p["contact_title"])}</h2>
        <p class="contact-lead">{esc(p["contact_lead"])}</p>
        <ul class="contact-list">
          <li><strong>E-mail</strong><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><strong>Plaats</strong><span>Eindhoven</span></li>
          <li><strong>KvK</strong><span>{KVK}</span></li>
          {EXTRA_CONTACT}
        </ul>
      </div>
      <div class="reveal">
        <form class="contact-form" id="contact-form" action="https://formspree.io/f/xwvjpzye" method="POST" novalidate aria-label="Contactformulier">
          <div class="form-row">
            <div class="field"><label for="naam">Naam *</label><input id="naam" name="naam" type="text" autocomplete="name" placeholder="Uw volledige naam" required><div class="field-error" id="err-naam" role="alert"></div></div>
            <div class="field"><label for="organisatie">Organisatie</label><input id="organisatie" name="organisatie" type="text" autocomplete="organization" placeholder="Bedrijfsnaam"></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="email">E-mail *</label><input id="email" name="email" type="email" autocomplete="email" placeholder="u@bedrijf.nl" required><div class="field-error" id="err-email" role="alert"></div></div>
            <div class="field"><label for="telefoon">Telefoon</label><input id="telefoon" name="telefoon" type="tel" autocomplete="tel" placeholder="+31 6 ..."></div>
          </div>
          <div class="field"><label for="opdracht-type">Type opdracht</label><select id="opdracht-type" name="opdracht-type">{opts}</select></div>
          <div class="field"><label for="beschrijving">Korte beschrijving *</label><textarea id="beschrijving" name="beschrijving" placeholder="{esc(p["form_placeholder"])}" required></textarea><div class="field-error" id="err-beschrijving" role="alert"></div></div>
          <div class="hp" aria-hidden="true"><label>Niet invullen<input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
          <p class="form-note">Met het versturen gaat u akkoord met de verwerking van uw gegevens, zoals beschreven in de <a href="/privacyverklaring.html">privacyverklaring</a>.</p>
          <button type="submit" class="btn"><span>Verstuur contactverzoek</span>{ICON_ARROW}</button>
          <div id="form-status" class="form-status" role="status" aria-live="polite"></div>
        </form>
      </div>
    </div>
  </section>
</main>

<footer role="contentinfo">
  <div class="footer-inner">
    <p>© 2026 {p["brand"]} · KvK {KVK}</p>
    <nav aria-label="Juridische links">
      <ul class="footer-links">
        <li><a href="/algemene-voorwaarden.html">Algemene voorwaarden</a></li>
        <li><a href="/privacyverklaring.html">Privacyverklaring</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      </ul>
    </nav>
  </div>
</footer>
<script src="/assets/js/site.js?v={V}" defer></script>
</body>
</html>
'''


def not_found():
    p = FINANCE
    return f'''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pagina niet gevonden | MA Solutions</title>
<meta name="robots" content="noindex">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="stylesheet" href="/assets/fonts/fonts.css?v={V}">
<link rel="stylesheet" href="/colors_and_type.css?v={V}">
<link rel="stylesheet" href="/assets/css/site.css?v={V}">
</head>
<body>
<script>try{{var t=localStorage.getItem('ma-theme');if(t==='dark'||(!t&&window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches))document.body.classList.add('dark')}}catch(e){{}}</script>
<main class="notfound">
  <div>
    <a href="/" class="logo" style="margin:0 auto 2rem;width:max-content" aria-label="MA Financial Solutions">{logo("FINANCIAL")}</a>
    <h1>Deze pagina bestaat niet</h1>
    <p>De pagina die u zoekt is verplaatst of bestaat niet meer.</p>
    <a class="btn" href="/">Naar de homepage{ICON_ARROW}</a>
  </div>
</main>
</body>
</html>
'''


def main():
    (ROOT / "care").mkdir(exist_ok=True)
    for p in (FINANCE, CARE):
        (ROOT / p["file"]).write_text(page(p), encoding="utf8")
    (ROOT / "404.html").write_text(not_found(), encoding="utf8")
    urls = [("/", "1.0"), ("/care/", "0.8"), ("/privacyverklaring.html", "0.2"), ("/algemene-voorwaarden.html", "0.2")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, pr in urls:
        sm.append(f"  <url><loc>{SITE}{u}</loc><lastmod>2026-10-06</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf8")
    print("gebouwd: index.html, care/index.html, 404.html, sitemap.xml, robots.txt")


if __name__ == "__main__":
    main()
