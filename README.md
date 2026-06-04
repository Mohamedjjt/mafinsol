# mafinsol.nl — MA Solutions

De live website voor **MA Financial Solutions** en **MA Care Solutions**: twee professionele diensten van één Nederlandse ZZP'er, gepresenteerd op één site met een Finance/Care toggle in de header.

Gehost op **GitHub Pages** via `mohamedjjt.github.io` — live op **https://mafinsol.nl**.

> De Care identiteit gebruikt het **moderne teal palet** (diep teal `#0d4f5c` + warm teal `#16a394`), ter vervanging van het originele salie-groen/terracotta.

## Hoe werkt het

Open `index.html` in je browser of push naar de `main` branch — GitHub Pages deployt automatisch binnen ~30 seconden.

Geladen via CDN: React 18 + Babel (inline JSX) en Google Fonts (Playfair Display + Manrope). Tokens komen uit `colors_and_type.css`; componentstijlen uit `styles.css`. Client logos worden geladen uit `assets/logos/`.

## Interactief gedrag

- **Finance / Care pill** in de header wisselt het palet (CSS custom-property rebind op `body.care`), de logo dot kleur, alle tekst en de getoonde referenties. Soepele 350ms cross-fade.
- **Thema-schakelaar** (zon / maan) togglet `body.dark` voor een echt donker thema op beide identiteiten.
- **Sticky header** krijgt een schaduw bij scrollen; secties **rijzen** in beeld bij scrollen.
- **Contactformulier** valideert verplichte velden (naam, e-mail, omschrijving) en toont een bevestigingsmodal bij verzenden.

## Componenten

| Bestand | Exports | Toelichting |
|---|---|---|
| `atoms.jsx` | `Logo`, `Arrow`, `Reveal`, `CONTENT`, `SHARED_TAGS`, `WERKWIJZE` | Monogram logo (mode-aware dot), het pijlicoon, scroll-reveal wrapper, en alle Nederlandse tekst per identiteit. |
| `Header.jsx` | `Header` | Logo, navigatie, mode pill, thema-schakelaar. |
| `Sections.jsx` | `Hero`, `About`, `Services` | Hero met stat paneel; over ons + kernkwaliteiten; genummerde dienstkaarten. |
| `Sections2.jsx` | `References`, `Workflow` | Referentiekaarten met klantlogo's; werkwijze grid op geïnverteerde achtergrond. |
| `Contact.jsx` | `Contact`, `Footer` | Gevalideerd formulier + modal; footer met juridische links. |
| `App.jsx` | — | Hoofdcomponent — beheert identiteit en dark state; composeert de pagina en mount naar `#root`. |
| `styles.css` | — | Componentstijlen gelaagd op de gedeelde token file. |

## Bestandsstructuur

| Bestand | Inhoud |
|---|---|
| `index.html` | Hoofdpagina — laadt alle componenten, bevat SEO, title en meta tags |
| `colors_and_type.css` | Kleur- en typografie tokens voor beide identiteiten + dark mode |
| `styles.css` | Componentstijlen gelaagd op de tokens |
| `atoms.jsx` | Logo, pijlicoon, scroll-reveal, en alle Nederlandse tekst per identiteit |
| `Header.jsx` | Logo, navigatie, mode pill, thema-schakelaar |
| `Sections.jsx` | Hero met stat paneel, over ons, dienstkaarten |
| `Sections2.jsx` | Referentiekaarten met klantlogo's, werkwijze grid |
| `Contact.jsx` | Contactformulier + modal, footer met juridische links |
| `App.jsx` | Hoofdcomponent — beheert identiteit en dark state |
| `assets/` | Logo's (MA merk + klanten), favicons |
| `_reference/` | Originele index.html voor referentie (legacy groen Care palet) |
| `preview/` | Design system preview cards (kleuren, typografie, componenten) |
| `CNAME` | Koppelt mafinsol.nl aan GitHub Pages |

## SEO

`index.html` bevat volledige SEO in de `<head>`:
- Title, meta description, keywords
- Open Graph (LinkedIn, WhatsApp, Facebook)
- Twitter Card
- Canonical URL
- Structured Data (JSON-LD) met twee ProfessionalService entiteiten: Finance en Care

## Tekst aanpassen

Alle Nederlandse tekst per identiteit staat in `atoms.jsx` in het `CONTENT` object — pas daar aan voor wijzigingen in kopij.

## Technische notities

- Componenten delen scope via `Object.assign(window, {...})` (Babel-in-browser patroon) — elk bestand exporteert zijn componenten globaal zodat latere `<script>`s ze kunnen gebruiken.
- Alle tekst staat in `atoms.jsx` `CONTENT` — daar aanpassen voor beide identiteiten.
- Het contactformulier POST momenteel niet — validatie en modal zijn client-side gesimuleerd.
- Scroll-reveal houdt content altijd zichtbaar en animeert een subtiele opkomst bij reveal — content is nooit afhankelijk van een animatie om zichtbaar te zijn.

## Hosting

- **Platform:** GitHub Pages
- **Domein:** mafinsol.nl (via MijnDomein DNS → GitHub Pages IP's)
- **HTTPS:** actief via Let's Encrypt (Enforce HTTPS ingeschakeld)
- **Deploy:** automatisch bij elke push naar `main`
