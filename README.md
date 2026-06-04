# MA Solutions — Design System

A dual-brand design system for **MA Financial Solutions** and **MA Care Solutions**: two professional service identities operated by a single Dutch ZZP (independent professional), presented on one website and toggled with a Finance / Care pill switch in the header.

This folder gives a design agent everything needed to produce on-brand interfaces, mockups, slides and assets for either identity — colours, type, logos, client logos, CSS tokens, and a full UI-kit recreation of the live site.

---

## 1. Company & product context

**One person, two services, two brands, one site.**

| | **MA Financial Solutions** | **MA Care Solutions** |
|---|---|---|
| **What** | Interim finance consultancy | Interim care / social-support staffing |
| **Specialisms** | SAP S/4HANA, SAP ECC, RE-FX · ERP migration · financial controlling · IFRS 16 · Power BI dashboarding · RPA automation · consolidation | Ambulante begeleiding (ambulatory guidance) · gehandicaptenzorg (disability care) · support plans & reporting · replacement/project staffing |
| **Credential** | KvK 93664850 · model agreement · professional liability | KvK 93664850 · **PBMZ4** (MBO niveau 4) · model agreement · liability |
| **Region** | Netherlands & international (Eindhoven base, EU) | Noord-Brabant, Limburg & nationwide |
| **Clients / references** | ASML, Philips IGTD, Jumbo Supermarkten, Van Loon Group | Helderzorg, Amor Zorg |
| **Brand colour** | Deep **navy** + **gold** dot | Deep **teal** + **warm teal** dot |

**Audience.** CFOs, finance managers, controllers, directors and recruiters at large corporates (Finance); care institutions, zorginstellingen and team leads needing qualified staff fast (Care). The tone throughout is premium, serious and trustworthy — closer to a McKinsey / Deloitte Digital consultancy than a gig-economy marketplace.

**The site** is a single Dutch-language page with sticky header and these sections: **hero → over ons (about) → diensten (services) → referenties (references) → werkwijze (workflow) → contact (form)**, plus a footer with a dark-mode toggle and links to legal pages. The Finance/Care pill swaps copy, palette, logo dot colour and the references shown — the layout stays identical.

### Sources used to build this system

- **GitHub repo:** `Mohamedjjt/mafinsol` (private) — `https://github.com/Mohamedjjt/mafinsol`
  - `index.html` — the entire live single-page site (structure, copy, CSS tokens, JS, inline client logos). **This was the primary source of truth.**
  - `favicon.svg`, `ASML…svg`, `Philips…svg`, `Jumbo_Supermarkten…svg`, `Van_Loon_Group…svg`, `Helderzorg_Logo.png` — logo assets, imported into `assets/`.
  - `algemene-voorwaarden.html`, `privacyverklaring.html` — legal pages (not rebuilt here).
  - Live domain referenced in the code: `https://mafinsol.nl/`.

  Readers with access can explore the repo for the authoritative source — recreating designs from the real `index.html` will always beat working from screenshots.

### What this revision changes vs. the live repo

The brief asked for the **Care identity to be modernised**. The live repo dresses Care in a sage-green (`#5c6f5c`) + terracotta (`#b8704c`) palette. **This system replaces that with a modern teal palette** (deep teal `#0d4f5c` primary, warm teal `#16a394` accent, teal-white `#f0f7f7` background) for a cleaner, contemporary Dutch-healthcare feel. Finance (navy/gold) is preserved exactly as built.

---

## 2. Content fundamentals

How MA writes. Match this voice in any new copy.

- **Language: Dutch (NL), formal register.** The site addresses the reader as **"u"** (formal you), never "je". Always plural-professional **"wij"** ("we") for MA itself — even though it's one person, the brand speaks as an organisation. English appears only as embedded technical terms (SAP S/4HANA, IFRS 16, Power BI, RPA, reporting).
- **Tone: confident, precise, reassuring — never salesy.** Claims are concrete and outcome-led, not hyped. e.g. *"Resultaatgericht, niet uurgericht"* ("Result-driven, not hour-driven"); *"Geen bureaucratie, geen onduidelijkheid — gewoon goede mensen op de juiste plek."*
- **Sentence rhythm uses the em-dash (`—`) heavily** as a thinking pause / reframe. This is a signature. e.g. *"Begeleiding die aansluit — op de cliënt, op uw organisatie, op de vraag."* Use real `&mdash;` / `—`, surrounded by spaces.
- **Headlines are serif, sentence case, often a single idea + an em-dash qualifier.** Sub-clauses sometimes set in italic serif for emphasis (*"Specialist in finance die verder kijkt"* — the second line italicised).
- **Section eyebrows are short uppercase labels** ("Wie wij zijn", "Diensten", "Opdrachtgevers", "Onze werkwijze", "Contact"). Body intros are one or two calm sentences.
- **Service cards** are numbered `01–06`, with a 2–4 word serif title and a 1–2 sentence description that names the *value to the client*, not just the activity.
- **Casing:** Title-case is avoided for body; headlines are sentence case. Uppercase is reserved for labels, nav, buttons and tags (with wide letter-spacing). Buttons read as imperatives: *"Opdracht bespreken"*, *"Verstuur contactverzoek"*.
- **No emoji. No exclamation hype. No first-person "ik".** Trust signals are stated plainly: *"Gecertificeerd & verzekerd"*, *"KvK 93664850"*, *"Modelovereenkomst beschikbaar"*.
- **Care vs Finance voice.** Finance leans on rigor and systems ("nauwkeurigheid", "data-integriteit", "consolidatie"). Care leans on warmth-with-structure ("warme, gestructureerde ondersteuning", "kwaliteit boven kwantiteit", "cliënten die er echt op kunnen rekenen"). Same formality, different emphasis.

---

## 3. Visual foundations

The brand reads as **premium consultancy minimalism**: lots of whitespace, a tight neutral palette warmed by a single metallic/teal accent, serif display over clean sans body, and sharp (not pill) corners.

### Colour
- **Two palettes, identical structure** (see `colors_and_type.css`). Each has: a deep `primary`, a single `accent`, a light page `bg`, white `surface`, a hairline `border`, a `muted` secondary text, a near-black-brand `dark-bg`, and a `tag-bg` chip tint.
- **Finance:** navy `#0a2342` + gold `#c9a961` on cool grey `#f4f6fa`.
- **Care (modernised):** deep teal `#0d4f5c` + warm teal `#16a394` on teal-white `#f0f7f7`.
- **Accent is used sparingly** — eyebrows/labels, the logo dot, serif stat numerals on dark panels, the tag checkmark, the 3px left rule on service cards, and the Care/Finance submit button. Never as a large fill.
- **Dark mode** desaturates and deepens both palettes (page `~#0d1520` navy / `~#0a1416` teal). It's a true theme, toggled and persisted in `localStorage`, not a media query.

### Type
- **Playfair Display** (serif) for all headings, hero numerals and stat figures — gives the premium editorial feel. Weights 400/600/700, with an italic used for emphasis fragments.
- **Manrope** (sans) for body, UI, nav, labels and forms. Weights 300–700. *(The monogram wordmark itself is set in Helvetica Neue inside the logo SVG.)* The brief mentioned Inter / Helvetica Neue for body — the live product ships **Manrope**, so that is what this system uses. Flag if you'd prefer a swap.
- **Uppercase + wide tracking** (`0.08em`–`0.18em`) is the signature treatment for every label, eyebrow, nav item and button.
- Body line-height is generous (`1.7`, prose `1.9`).

### Spacing & layout
- **1180px max content width**, centred, with fluid side padding `clamp(1.25rem, 4vw, 2.5rem)`.
- **Vertical section rhythm** is large and fluid: `clamp(4rem, 8vw, 8rem)` top/bottom.
- Cards and grids use **CSS grid with `gap`** and `auto-fit minmax(260–300px, 1fr)` — responsive without media queries.
- Generous whitespace is the point; density is low.

### Backgrounds
- **Flat solid fills only** — no photography, no illustration, no texture, no gradients as decoration. Page is the light `bg`; alternate sections use white `surface`; the **workflow** section inverts to the solid `primary`; **contact** uses the deepest `dark-bg`.
- Two subtle decorative shapes only: a faint (`opacity 0.04`) primary-colour **circle** bleeding off the hero's right edge, and a small accent circle (`opacity 0.15`) in the corner of the hero stat panel. These are the only "graphics".

### Corners, borders, cards
- **Sharp by default.** `2px` radius on buttons, tags, inputs; `4px` on cards, panels and the modal. The **only** soft element is the `6px` mode-toggle pill. **No fully-rounded pill buttons anywhere.**
- **Cards:** white `surface`, `1px` solid `border`, `4px` radius, no shadow at rest. Service cards add a `3px` accent-colour rule down the left edge and a faint oversized serif numeral.
- **Borders are hairline** (`1px`, low-contrast `border` token). Dividers inside panels are the same.

### Shadows & elevation
- **Almost flat.** No resting shadows on cards. Shadow appears **only on hover/active** and on the sticky header once scrolled (`0 2px 16px rgba(0,0,0,.08)`). Hover shadows are soft and large: `0 8–12px 24–36px rgba(0,0,0,.06–.15)`.

### Motion
- **Restrained and professional.** Scroll-reveal fade-up (`opacity` + `translateY(24px)`, `0.7s ease`) via IntersectionObserver. Brand/theme switches cross-fade colours over `350ms ease`. The pill indicator slides with `cubic-bezier(0.4,0,0.2,1)`. No bounce, no spring, no looping/decorative animation.

### Hover & press states
- **Buttons & cards:** lift `translateY(-2px to -4px)` + gain a soft shadow on hover. CTAs nudge their arrow icon `translateX(4px)`.
- **Nav links:** colour shifts `muted → primary` and grow a `2px` accent bottom-border.
- **Links in dark sections:** accent colour, `opacity 0.8` on hover.
- No explicit shrink/scale-down press state; the lift + colour shift carries interaction.

### Transparency & blur
- Used only for the **modal scrim** (`rgba(0,0,0,.6)` + `backdrop-filter: blur(4px)`) and for white-on-dark text tiers (`rgba(255,255,255, .85/.65/.6/.5/.35/.15)`) inside the navy/teal panels. No frosted cards in the light UI.

### Imagery vibe
- There is **no photography or illustration** in the product — the aesthetic is purely typographic + flat colour. If imagery is ever added, keep it cool, corporate and restrained to match (no warm grain, no playful illustration). Client/reference logos are shown on small **white tiles** (`4px` radius, `1px` border) so multi-colour brand marks sit on a consistent ground.

---

## 4. Iconography

MA uses **almost no icons** — this is a deliberately type-led brand. Document and respect that restraint.

- **No icon library, font, or sprite is used.** There is no Lucide/Heroicons/Font Awesome dependency in the source.
- **Inline SVG, hand-placed, minimal.** The only UI icons are:
  - A small **arrow** (`→`, 16×16, 1.75 stroke, round caps) inside CTAs and the submit button — drawn inline, `currentColor`.
  - The **select chevron**, embedded as a tiny data-URI SVG in the dropdown background.
  - The footer **dark-mode toggle** uses two **Unicode glyphs** — 🌙 (`&#127769;`) and ☀ (`&#9728;`) — not SVG icons.
- **The "✓" tag bullet** is a CSS `content: '✓'` pseudo-element in the accent colour — a text glyph, not an icon asset.
- **No emoji** anywhere in content; the only Unicode pictographs are the two dark-mode glyphs above.
- **Logos are the real iconography.** The MA monogram (letters **MA** + a coloured **dot**: gold for Finance, teal for Care) and the client logos (ASML, Philips, Jumbo, Van Loon Group, Helderzorg) are the brand's visual marks. All are vector SVG (Helderzorg is a PNG). They live in `assets/logos/`.

**Guidance for new work:** if an interface genuinely needs icons, introduce a **thin line set at ~1.75px stroke, round caps, `currentColor`** to match the lone existing arrow — and use them sparingly. Prefer numerals (`01–06`) and type over iconography, as the brand does. Flag any icon-set addition to the user.

---

## 5. Index / manifest

Root files:

| File | What it is |
|---|---|
| `README.md` | This document — context, voice, visual foundations, iconography, manifest. |
| `colors_and_type.css` | The foundation: both brand palettes, dark-mode overrides, type scale, radius/motion tokens, and `.ds-*` semantic type classes. Import this into any new design. |
| `SKILL.md` | Agent-Skill front-matter wrapper so this folder works as a downloadable Claude skill. |
| `assets/` | Brand + client logos, favicons. See below. |
| `preview/` | Small HTML specimen cards that populate the Design System tab (colours, type, spacing, components, brand). Reference, not building blocks. |
| `ui_kits/website/` | High-fidelity, interactive recreation of the live mafinsol.nl site — the main reusable kit. |
| `_reference/original-site.html` | The imported, unmodified live `index.html` for source-of-truth reference (note: contains the *legacy* green Care palette). |

`assets/` contents:

| File | Use |
|---|---|
| `logos/ma-financial-solutions.svg` / `…-light.svg` | MA Financial wordmark (gold dot) — dark-on-light and white-on-dark. |
| `logos/ma-care-solutions.svg` / `…-light.svg` | MA Care wordmark (teal dot) — dark-on-light and white-on-dark. |
| `logos/asml.svg`, `philips.svg`, `jumbo.svg`, `van-loon-group.svg`, `helderzorg.png` | Client / reference logos. |
| `favicon.svg` | Finance favicon (navy tile, MA, gold dot). |
| `favicon-care.svg` | Care favicon (teal tile, MA, teal dot). |

`ui_kits/website/`:

| File | What it is |
|---|---|
| `index.html` | Interactive demo: full site with working Finance/Care toggle, dark mode, scroll reveals and contact modal. |
| `README.md` | Kit overview + component list. |
| `*.jsx` | Modular React components (header, hero, services, references, workflow, contact, footer, primitives). |

---

*Built from `Mohamedjjt/mafinsol`. Explore that repository for the authoritative source when recreating or extending these designs.*
