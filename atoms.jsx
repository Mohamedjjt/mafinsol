// atoms.jsx — shared primitives + content data for the MA Solutions site kit.
const { useState, useEffect, useRef } = React;

/* ---- MA monogram wordmark (letters + coloured dot; dot = brand variable) ---- */
function Logo({ mode }) {
  const dot = mode === 'care' ? '#16a394' : '#c9a961';
  const line1 = mode === 'care' ? 'CARE' : 'FINANCIAL';
  return (
    <svg viewBox="0 0 220 56" xmlns="http://www.w3.org/2000/svg" aria-label={`MA ${line1} Solutions`}>
      <text x="4" y="38" fontFamily="'Helvetica Neue',Arial,sans-serif" fontSize="28" fontWeight="600" letterSpacing="-0.5" fill="var(--primary)">MA</text>
      <circle cx="54" cy="29" r="4" fill={dot}></circle>
      <text x="66" y="24" fontFamily="'Helvetica Neue',Arial,sans-serif" fontSize="10" fontWeight="500" letterSpacing="2.5" fill="var(--primary)">{line1}</text>
      <text x="66" y="38" fontFamily="'Helvetica Neue',Arial,sans-serif" fontSize="10" fontWeight="300" letterSpacing="2.5" fill="var(--muted)">SOLUTIONS</text>
    </svg>
  );
}

/* ---- The lone UI icon: a thin arrow, currentColor ---- */
function Arrow({ size = 16 }) {
  return (
    <svg width={size} height={size} viewBox="0 0 16 16" fill="none" aria-hidden="true">
      <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round"/>
    </svg>
  );
}

/* ---- Scroll-reveal wrapper: fade-up when scrolled into view.
   Uses a scroll-position check (robust across preview/iframe contexts where
   IntersectionObserver can be unreliable). ---- */
function Reveal({ children, className = '' }) {
  const ref = useRef(null);
  const [visible, setVisible] = useState(false);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    let done = false;
    const check = () => {
      if (done) return;
      const r = el.getBoundingClientRect();
      if (r.top < window.innerHeight * 0.9 && r.bottom > 0) {
        done = true; setVisible(true);
        window.removeEventListener('scroll', check);
        window.removeEventListener('resize', check);
      }
    };
    check();
    window.addEventListener('scroll', check, { passive: true });
    window.addEventListener('resize', check);
    return () => {
      window.removeEventListener('scroll', check);
      window.removeEventListener('resize', check);
    };
  }, []);
  return <div ref={ref} className={`fade-in ${visible ? 'visible' : ''} ${className}`}>{children}</div>;
}

/* ---- All Dutch copy, keyed by identity ---- */
const CONTENT = {
  finance: {
    heroEyebrow: 'Interim Finance · Nederland & Internationaal',
    heroHeadline: 'Finance expertise die direct inzetbaar is — waar uw organisatie het nodig heeft.',
    heroSub: 'MA Financial Solutions levert scherpe, resultaatgerichte finance professionals voor complexe vraagstukken. Van ERP-migraties tot internationale consolidatie — wij zorgen dat uw financiële processen kloppen, ook onder druk.',
    stats: [
      { num: '4+', label: 'jaar actief in\ninterim finance' },
      { num: 'Top 50', label: 'opdrachtgevers\nin portefeuille' },
      { num: 'SAP', label: 'S/4HANA · ECC · REFX\nmigratie-ervaring' },
    ],
    aboutTitle: ['Specialist in finance', 'die verder kijkt'],
    aboutBody: [
      'MA Financial Solutions is een gespecialiseerde interim finance dienstverlener met een scherp profiel: wij opereren op het snijvlak van financial accounting, procesoptimalisatie en ERP-implementatie.',
      'Wij geloven dat de beste finance professional niet alleen de cijfers beheerst, maar ook begrijpt hoe een organisatie werkt. Daarom leveren wij mensen die meteen waarde toevoegen — zonder inwerkperiode van weken.',
    ],
    credTitle: 'Kernkwaliteiten',
    creds: [
      ['International Financial Reporting', 'IFRS 16, consolidatie, multi-entity, Europese entiteiten'],
      ['ERP & Systemen', 'SAP S/4HANA, SAP ECC, RE-FX, Microsoft Dynamics'],
      ['Data & Procesverbetering', 'Power BI, Lean, RPA — van analyse tot implementatie'],
      ['Talen', 'Nederlands & Engels — zakelijk op hoog niveau'],
      ['Erkend & verzekerd', 'KvK 93664850 · Modelovereenkomst · Beroepsaansprakelijkheid'],
    ],
    dienstenTitle: 'Finance Solutions',
    dienstenIntro: 'Wij leveren finance expertise op de gebieden waar uw organisatie het meest behoefte aan heeft.',
    diensten: [
      ['01', 'Interim Financial Controlling', 'Periodieke afsluitingen, consolidatie van Europese entiteiten, SOX-controles en management reporting — ingezet waar continuïteit en nauwkeurigheid tellen.'],
      ['02', 'ERP-migratie & Procesoptimalisatie', 'Bewezen ervaring met complexe SAP-trajecten en procesherontwerp. Wij zorgen dat uw organisatie de overgang maakt zonder verlies van data-integriteit of snelheid.'],
      ['03', 'Financial Accounting & Reporting', 'Van GL-accounting tot IFRS 16 en internationale belastingaangiften — nauwkeurige verwerking en heldere rapportage als basis voor betere beslissingen.'],
      ['04', 'Data & Procesanalyse', 'Wij brengen financiële processen in kaart, identificeren bottlenecks en vertalen data naar inzicht — met Power BI, Lean en RPA als instrumenten.'],
      ['05', 'Automatisering & RPA', 'Wij identificeren repetitieve financiële processen en automatiseren deze met RPA-tooling — zodat uw team zich richt op werk dat er echt toe doet.'],
      ['06', 'Dashboarding & Rapportage', 'Van ruwe data naar heldere management dashboards in Power BI. Wij bouwen inzicht dat besluitvorming versnelt — real-time, visueel en op maat.'],
    ],
    refTitle: 'Vertrouwd door toonaangevende organisaties',
    refs: [
      { logo: 'jumbo.svg', org: 'Jumbo Supermarkten', desc: 'Een van de grootste retailers van Europa, actief in Nederland en België met meer dan 700 vestigingen.' },
      { logo: 'philips.svg', org: 'Philips IGTD', desc: 'Wereldwijd actief medisch-technologisch concern. Betrokken bij financiële processen in meerdere Europese landen.' },
      { logo: 'asml.svg', org: 'ASML', desc: 'Marktleider in lithografiesystemen voor de halfgeleiderindustrie, actief in meer dan 60 landen wereldwijd.' },
      { logo: 'van-loon-group.svg', org: 'Van Loon Group', desc: 'Toonaangevend familiebedrijf in transport en logistiek met Europees netwerk en diverse operationele entiteiten.' },
    ],
    footer: '© 2026 MA Financial Solutions',
  },
  care: {
    heroEyebrow: 'Persoonlijke Begeleiding · Maatschappelijke Zorg · Nederland',
    heroHeadline: 'Begeleiding die aansluit — op de cliënt, op uw organisatie, op de vraag.',
    heroSub: 'MA Care Solutions biedt gekwalificeerde begeleiders voor zorginstellingen die snel en flexibel willen schakelen. Warme, gestructureerde ondersteuning — voor cliënten die er echt op kunnen rekenen.',
    stats: [
      { num: 'Snel', label: 'inzetbaar — ook\nop korte termijn' },
      { num: '100%', label: 'gediplomeerd en\nverzekerd' },
      { num: 'Flex', label: 'ambulant, intramuraal\nof projectbasis' },
    ],
    aboutTitle: ['Zorgprofessionals die', 'direct het verschil maken'],
    aboutBody: [
      'MA Care Solutions is uw partner voor flexibele inzet van gekwalificeerde zorgprofessionals. Wij leveren mensen die direct aansluiten bij uw werkwijze, uw cliënten en uw team — zonder lange inwerktijd.',
      'Van ambulante begeleiding tot gehandicaptenzorg: zorginstellingen kiezen voor ons omdat wij snel schakelen, transparant communiceren en kwaliteit boven kwantiteit stellen.',
    ],
    credTitle: 'Wat wij bieden',
    creds: [
      ['Ambulante begeleiding', 'Thuis, op locatie of hybride — aansluitend bij uw zorgmodel'],
      ['Gehandicaptenzorg', 'Inzetbaar bij verstandelijke en lichamelijke beperkingen'],
      ['Vervanging & projectinzet', 'Flexibel beschikbaar, ook op korte termijn'],
      ['Rapportage & kwaliteit', 'Ondersteuningsplannen en dossiervorming conform uw standaard'],
      ['Erkend & verzekerd', 'KvK 93664850 · Modelovereenkomst · Beroepsaansprakelijkheid'],
    ],
    dienstenTitle: 'Care Solutions',
    dienstenIntro: 'Wij bieden zorginstellingen gekwalificeerde begeleiding — flexibel, betrouwbaar en snel inzetbaar.',
    diensten: [
      ['01', 'Ambulante Begeleiding', 'Onze begeleiders ondersteunen cliënten in hun eigen omgeving — bij zelfzorg, wonen en het opbouwen van dagstructuur die écht past.'],
      ['02', 'Gehandicaptenzorg', 'Begeleiding voor mensen met verstandelijke en/of lichamelijke beperkingen — gericht op participatie, zelfregie en kwaliteit van leven.'],
      ['03', 'Begeleidingsplannen & Rapportage', 'Wij leveren begeleiders die gestructureerd observeren, rapporteren en plannen opstellen — zodat uw dossiervoering op orde blijft.'],
      ['04', 'Vervanging & Projectinzet', 'Snel schakelen bij uitval of piekbelasting. Wij leveren continuïteit zonder lange procedures — zodat uw cliënten de aandacht krijgen die zij verdienen.'],
    ],
    refTitle: 'Ingezet bij gerenommeerde zorginstellingen',
    refs: [
      { logo: 'helderzorg.png', org: 'Helderzorg', desc: 'Ambulante zorgverlener in Apeldoorn, actief in Gelderland en Overijssel, gericht op herstel en zelfstandigheid van cliënten met complexe ondersteuningsvragen.' },
      { logo: null, org: 'Amor Zorg', desc: 'Zorgaanbieder gespecialiseerd in ambulante begeleiding en ondersteuning van mensen met een hulpvraag in de thuissituatie.' },
    ],
    footer: '© 2026 MA Care Solutions',
  },
};

const SHARED_TAGS = ['Snel inzetbaar', 'Gecertificeerd & verzekerd', 'Modelovereenkomst beschikbaar', 'Nationaal & internationaal'];

const WERKWIJZE = [
  ['01', 'Snel en gericht opstarten', 'Wij luisteren eerst. Een korte intake volstaat om te begrijpen wat uw organisatie nodig heeft — zodat de juiste professional meteen aan de slag kan.'],
  ['02', 'Resultaatgericht, niet uurgericht', 'Elke opdracht wordt vooraf helder afgebakend op resultaat. U weet wat u krijgt — en wij leveren het.'],
  ['03', 'Transparante samenwerking', 'Heldere overeenkomsten, geen verborgen kosten, geen verrassingen. Wij werken met modelovereenkomsten en zijn volledig compliant met actuele wet- en regelgeving.'],
  ['04', 'Aantoonbare expertise', 'Onze professionals zijn gecertificeerd, verzekerd en actief bijgeschoold. Van Power BI tot PBMZ4 — kennis die direct inzetbaar is.'],
  ['05', 'Flexibel in duur en omvang', 'Of het nu gaat om een project van vier weken of een langlopend traject — wij schalen mee met uw behoefte.'],
  ['06', 'Nationaal bereik', 'Wij zijn actief door heel Nederland en waar nodig internationaal — op locatie of remote, afhankelijk van wat de opdracht vraagt.'],
];

Object.assign(window, { Logo, Arrow, Reveal, CONTENT, SHARED_TAGS, WERKWIJZE });
