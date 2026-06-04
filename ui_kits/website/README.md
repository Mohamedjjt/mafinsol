# Website UI Kit — MA Solutions

A high-fidelity, interactive recreation of the live **mafinsol.nl** single-page site, rebuilt as modular React components. It demonstrates the dual-brand system end to end: the **Finance** (navy/gold) and **Care** (modern teal) identities, dark mode, scroll reveals, and a working contact form with confirmation modal.

> The Care identity here uses the **modernised teal palette** (deep teal `#0d4f5c` + warm teal `#16a394`), replacing the legacy sage-green/terracotta of the original repo — per the design brief.

## Run it

Open `index.html`. Loaded from CDN: React 18 + Babel (inline JSX) and Google Fonts (Playfair Display + Manrope). Tokens come from `../../colors_and_type.css`; component styling from `styles.css`. Client logos are pulled from `../../assets/logos/`.

## Interactive behaviour

- **Finance / Care pill** in the header swaps the palette (CSS custom-property rebind on `body.care`), the logo dot colour, all copy, the references shown, and the contact-form options. Smooth 350ms cross-fade.
- **Theme switch** (sun / moon) toggles `body.dark` for a true dark theme on either identity.
- **Sticky header** gains a shadow on scroll; sections **rise** into view as you scroll.
- **Contact form** validates required fields (name, email, description) and opens a confirmation **modal** on submit.

## Components

| File | Exports | Notes |
|---|---|---|
| `atoms.jsx` | `Logo`, `Arrow`, `Reveal`, `CONTENT`, `SHARED_TAGS`, `WERKWIJZE` | Monogram logo (mode-aware dot), the lone arrow icon, scroll-reveal wrapper, and all Dutch copy keyed by identity. |
| `Header.jsx` | `Header` | Logo, nav, mode pill, theme switch. |
| `Sections.jsx` | `Hero`, `About`, `Services` | Hero with stat panel; about + credentials; numbered service cards. |
| `Sections2.jsx` | `References`, `Workflow` | Client-logo reference cards; inverted-primary workflow grid. |
| `Contact.jsx` | `Contact`, `Footer` | Validated form + modal; footer with legal links. |
| `App.jsx` | — | Top-level identity + dark state; composes the page and mounts to `#root`. |
| `styles.css` | — | Component styles layered on the shared token file. |

## Notes for reuse

- Components share scope via `Object.assign(window, {...})` (Babel-in-browser pattern) — each file exports its components globally so later `<script>`s can use them.
- All copy lives in `atoms.jsx` `CONTENT` — edit there to change text for either identity.
- This is a cosmetic recreation: the form does not POST anywhere (the live site wires Netlify forms); validation + modal are simulated client-side.
- Scroll-reveal keeps content visible by default and animates a subtle rise on reveal — so content never depends on an animation completing to be seen.
