# Open punten voor Mohamed (herontwerp mafinsol.nl)

Het herontwerp staat live (branch `main`). Dit moet jij nog invullen of bevestigen.

## Verplicht / juridisch
- [ ] **Btw-nummer** toevoegen (contactblok + footer). Staat als HTML-commentaar in `tools/build.py` (zoek "TODO").
- [ ] **Vestigingsadres** (straat, postcode, plaats) toevoegen. Nu staat alleen "Eindhoven".
- [ ] **Claims controleren** (staan niet meer als "100% gediplomeerd", "Erkend", "volledig compliant"): modelovereenkomst, beroepsaansprakelijkheid (verzekering?), PBMZ4-diploma.
- [ ] **Logo's** van ASML, Philips, Jumbo, Van Loon, Helderzorg en Amor Zorg: toestemming om ze te tonen? Anders alleen de naam in tekst.
- [ ] Privacyverklaring: Formspree noemen als verwerker (contactformulier) en bewaartermijn controleren. Teksten zijn niet aangepast.

## Inhoud
- [ ] "ik" in plaats van "wij": past bij een eenmanszaak. Bevestig dat dit zo moet (ook voor Care).
- [ ] Controleer de cijfers: "4+ jaar interim", "meer dan 5 jaar finance-ervaring bij grote organisaties", "4 grote opdrachtgevers".
- [x] Telefoonnummer is op verzoek van Mohamed van de site en uit de structured data gehaald (2026-10-06).
- [ ] Foto van jou + korte bio (grote winst voor vertrouwen).
- [ ] 2 of 3 cases met probleem, aanpak en resultaat (geen klantgegevens die niet mogen).
- [ ] LinkedIn-profiel koppelen (URL ontbreekt).

## Techniek na livegang
- [ ] Google Search Console: sitemap `https://mafinsol.nl/sitemap.xml` indienen.
- [ ] Google Bedrijfsprofiel aanmaken (Eindhoven).
- [ ] DMARC van `p=none` naar `p=quarantine` zodra alle legitieme mail geverifieerd is. CAA-record overwegen (bij mijndomein.nl).
