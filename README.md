# mafinsol.nl — MA Financial Solutions & MA Care Solutions

Statische website (geen frameworks, geen build in de browser). Gehost op **GitHub Pages**, live op https://mafinsol.nl.

## Pagina's
| URL | Bestand | Inhoud |
|---|---|---|
| `/` | `index.html` | MA Financial Solutions (interim financial controller, SAP) |
| `/care/` | `care/index.html` | MA Care Solutions (ambulante begeleiding, gehandicaptenzorg) |
| `/privacyverklaring.html`, `/algemene-voorwaarden.html` | handmatig | juridisch |
| `/404.html`, `/robots.txt`, `/sitemap.xml` | gegenereerd | |

## Werken aan de teksten
`index.html`, `care/index.html`, `404.html`, `sitemap.xml` en `robots.txt` worden **gegenereerd** door:

```
python3 tools/build.py
```

Teksten staan in `tools/build.py` (blokken `FINANCE` en `CARE`), structured data in `tools/schema-*.json`. Pas daar aan en draai het script; bewerk de gegenereerde HTML niet met de hand. Er is geen andere afhankelijkheid dan Python 3.

## Opmaak en scripts
- `colors_and_type.css`: design tokens (Finance navy/goud, Care teal, donkere modus).
- `assets/css/site.css`: opmaak van de site. `assets/js/site.js`: donkere modus, menu, formulier (Formspree).
- `assets/fonts/`: Playfair Display en Manrope, lokaal gehost (geen Google Fonts-verzoeken).
- `assets/og-*.png`: deelafbeeldingen (1200×630), gemaakt met `tools/og-template.html`.
- Donkere modus volgt de voorkeur van het apparaat en onthoudt een handmatige keuze lokaal in de browser (geen persoonsgegevens).

## Oud
`_archief/` bevat de vorige React-versie (Babel in de browser). De volledige oude staat staat ook in git-tag `backup-voor-herontwerp-2026-10-06`.

`SKILL.md`, `preview/` en `_reference/` horen bij het design system en zijn ongewijzigd.
