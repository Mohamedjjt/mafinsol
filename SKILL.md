---
name: ma-solutions-design
description: Use this skill to generate well-branded interfaces and assets for MA Financial Solutions & MA Care Solutions (a Dutch dual-brand finance + care consultancy), either for production or throwaway prototypes/mocks/etc. Contains essential design guidelines, colors, type, fonts, logos, and a website UI kit for prototyping. Covers both the navy/gold Finance identity and the teal Care identity.
user-invocable: true
---

Read the `README.md` file within this skill, and explore the other available files.

If creating visual artifacts (slides, mocks, throwaway prototypes, etc), copy assets out and create static HTML files for the user to view. If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand.

Key files:
- `README.md` — context, content/voice rules, visual foundations, iconography, manifest.
- `colors_and_type.css` — both brand palettes (Finance navy/gold, Care teal), dark mode, type scale, radius/motion tokens. Import this first.
- `assets/logos/` — MA wordmarks (Finance + Care, light + dark variants) and client logos.
- `ui_kits/website/` — interactive recreation of the live site with reusable JSX components.
- `preview/` — specimen cards for the foundations.

Two identities, one system: bind Finance by default; add the `.care` class to switch to the teal palette. Add `.dark` for dark mode. Default copy language is **Dutch, formal ("u" / "wij")**. Sharp corners (2–4px), serif (Playfair Display) headings over Manrope body, heavy use of em-dashes, no emoji, minimal icons.

If the user invokes this skill without any other guidance, ask them what they want to build or design, ask some questions, and act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need.
