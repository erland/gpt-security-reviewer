# Security Review – Skill-beteende

> Migreringskandidat för GPT Byggaren 1.6.33, inte aktiverad. Gemensamma regler ligger i `canonical/core.md`. Vid aktivering ska ursprungsbeteendet verifieras mot `canonical/runtime-contract.md`.

## Aktivering

Aktivera vid användarens begäran att säkerhetsgranska källkod, konfiguration, deployment, API:er, beroenden eller arkitekturdokumentation. Följ alltid gemensam kärna.

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

## Detaljerade arbetskontrakt

- `canonical/workflow.md`: åtta granskningsfaser.
- `canonical/review-framework.md`: säkerhetskontroller, evidens och riskbedömning.
- `canonical/multi-pass-review-contract.md`: kontrollmatris, kandidatregister, challenge pass och coverage gate.
- `canonical/reporting-contract.md` och `canonical/report-model.md`: rapportstruktur och canonical rapportdata.
- `canonical/report-delivery-workflow.md` och `canonical/report-export-contract.md`: formatval och leverans.
- `canonical/defensive-reporting-contract.md` och `canonical/report-binary-export-contract.md`: defensiva rapporter och deterministisk export.
- `schemas/review-process.schema.json`: auktoritativt strukturerat granskningsstate.

## Körbara runtimeverktyg

Endast `scripts/validate_review_integrity.py` och `scripts/deliver_report.py` definieras som top-level-verktyg i projektkontraktet. Övriga skript är beroenden eller validerings-/buildstöd och blir inte automatiskt agentverktyg.
