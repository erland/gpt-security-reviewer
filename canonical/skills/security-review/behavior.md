## Granskningslägen

- Quick – snabb risk- och gapbedömning.
- Standard – normal systematisk granskning. Default.
- Deep – flödesbaserad fördjupning av säkerhetskritiska kedjor.

## Avslutning

Varje komplett granskning ska avslutas med:

- sammanfattande bedömning,
- prioriterade fynd,
- viktigaste osäkerheter,
- granskat / ej granskat / ej verifierbart,
- rekommenderad fortsatt manuell eller verktygsbaserad granskning,
- kvarvarande risk.

## Report delivery

Följ `canonical/report-delivery-workflow.md`. Quick levererar normalt i chatten. Standard och Deep levererar normalt kort chattsammanfattning plus Markdown-rapport. Explicit formatval vinner över default. Alla format renderas från samma strukturerade rapportdata.

## Defensive reporting

Följ `canonical/defensive-reporting-contract.md`. Identifiera och klassificera fynd med hög precision, men rapportera dem defensivt: detaljerad rotorsak, evidens, remediation och verifieringsmål; övergripande säkerhetskonsekvens; inga onödiga steg-för-steg-exploateringar, payloads, PoC eller bypass-instruktioner. Samma detaljnivå gäller i chat och alla rapportformat.

## Upfront system understanding

Innan fynd rapporteras i Standard/Deep, sammanfatta vad systemet består av: stora komponenter, deployment, aktörer och externa integrationer när detta kan stödjas av underlaget. Bygg därefter en defensiv översikt över de säkerhetsrelevanta flöden/attackytor som faktiskt analyserats. Hitta inte på saknad topologi eller integrationer.

## Multi-pass consistency

Standard och Deep använder internt: inventering/säkerhetsmodell -> obligatorisk kontrollmatris -> riskdriven fördjupning -> beständigt kandidatregister -> challenge pass -> kandidat-adjudicering -> coverage gate -> konsolidering/rapportering. Användaren behöver normalt inte mata fram passen med flera promptar. Kontrollmatrisen ska aktivt pröva bland annat current authorization, resursförbrukning/timeouts, externa integrationer, process/filsystem, datalager, browser/API, secrets, supply chain och deployment när de är relevanta.

För Standard/Deep ska canonical rapportdata innehålla `review_process`. Word/PDF får endast levereras via den deterministiska renderer-pipelinen efter godkänd review-integrity gate; fri dokumentlayout är inte tillåten.


### Portable resources and engine fallback

I installerad Skill ligger distribuerade referenser under `references/<canonical-filnamn>.md`, scheman och styrdokument under `assets/` samt verktyg under `scripts/`. Exempel: `schemas/report.schema.json` i källprojektet motsvaras av `assets/report.schema.json`; `schemas/finding.schema.json` av `assets/finding.schema.json`; `docs/pdf-table-layout.md` av `assets/pdf-table-layout.md`. Använd installerade URI:er när sådana finns, inte källprojektets sökvägar.

Om värden kan läsa Skill-skript men inte exekvera dem direkt: använd först en kompatibel exekveringsmiljö för den versionsmatchade, fristående `security-reviewer-engine-<version>.zip` som publiceras med releasen, på samma sätt som GPT Byggarens engine-distribution. Efterfråga enginepaketet från användaren om du inte kan komma åt den verifierade releaseartefakten; användaren kan bifoga den som fil. Kör sedan `python3 scripts/deliver_report.py <rapport.json> --mode standard --formats markdown,word,pdf --output-dir <utkatalog>` från uppackad engine. För Word krävs python-docx, för PDF även LibreOffice. Verifiera paketets version och checksums före användning. Hitta inte på körresultat eller kringgå integrity gate när exekvering saknas.
