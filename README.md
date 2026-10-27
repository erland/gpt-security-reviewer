# Säkerhetsgranskaren för IT-stöd

GPT-projekt för evidensbaserad säkerhetsgranskning av verksamhetsnära IT-stöd.

## V1-scope

Primärt stöd:

- React
- Angular
- Java EE / Jakarta EE
- Oracle
- PostgreSQL
- Elasticsearch
- applikationsnära Docker/Kubernetes/OpenShift-konfiguration
- arkitekturdokumentation

GPT:n ska:

1. inventera underlaget,
2. identifiera teknikstack och säkerhetskritiska flöden,
3. välja relevanta granskningsprofiler,
4. identifiera fynd med spårbar evidens,
5. skilja risknivå från evidensstyrka,
6. redovisa vad som granskats, inte granskats och inte kunnat verifieras,
7. rekommendera proportionerlig manuell eller verktygsbaserad fortsatt granskning.

## Viktig princip

GPT:n är ett gransknings- och beslutsstöd. Den ersätter inte penetrationstest, fullständig infrastruktursäkerhetsgranskning eller specialistbedömning där sådant behövs.

## Projektstruktur

- `canonical/` – styrande runtime-kontrakt
- `knowledge/` – gemensamma och teknikspecifika granskningsprofiler
- `schemas/` – maskinläsbara fynd- och sammanfattningsscheman
- `scripts/` – validering och byggstöd
- `.github/workflows/` – CI och release
- `tests/` – scenarier och fixtures

## Distributioner (GPT Byggaren 1.6.33)

Originalmotorn 1.6.33 installerar en gemensam byggare och tar fram sex ZIP-arkiv:
projektpaket samt **Chat, OpenAI Plugin, Claude Project, Claude Skills och OpenCode**.
Custom GPT är en historisk kompatibilitetsdistribution och ingår inte i denna release.

Gemensam styrning finns i `canonical/core.md`; granskningsbeteendet i
`canonical/skills/security-review/behavior.md`. Den gamla
`canonical/runtime-contract.md` är kvar för bakåtkompatibilitet och spårbarhet.

I CI installeras den versionslåsta originalmotorn från GitHub Release v1.6.33.
Den installeras även i det publicerade releaseflödet, innan testning och bygge.
Build/validation körs med originalmotorns `scripts/build_distributions.py`
och `scripts/validate_distributions.py` samt leveranskontroll.

Säkerhetsgranskningens särskilda regressionskontroller för integrity gate,
coverage, rapportmodell och Word/PDF körs fortfarande före release.

Claude-distributionerna har dokumenterade värdberoenden: lokal deterministisk
integritetskontroll och Word/PDF-export kräver en kompatibel exekveringsmiljö.
Releaseversionen härleds från GitHub Release-taggen och manifest samt SHA-256
levereras tillsammans med paketen.

## Rapportering

Markdown är canonical mänskligt läsbart rapportformat. Standard och Deep ska normalt skapa fullständig Markdown-rapport. Quick levererar primärt resultat i chatten. Confluence markup, PDF och Word ska renderas från samma rapportmodell.

## Rapportexport

Markdown och Confluence markup genereras från samma strukturerade rapportdata enligt `schemas/report.schema.json`.

## Word och PDF

DOCX och PDF kan renderas från samma canonical rapportdata. PDF byggs via DOCX för att hålla layouten konsekvent.

## Rapportworkflow

Default: Quick → chat, Standard → chat + Markdown, Deep → chat + Markdown. Explicit formatval kan vara Markdown, Confluence markup, Word, PDF eller flera format.

## V1 release candidate

Step 18 genomför en samlad V1-kvalitetsgranskning. Se `docs/v1-quality-review.md`. Granskningsmaterial behandlas som odata; prompt injection i repository/dokumentation får inte styra GPT:n. Genererat/vendor-material deprioriteras i manuell granskning.

## Release candidate

Aktuell projektversion: **0.1.0-rc.1**.

Avsedd GitHub Release-tagg: `v0.1.0-rc.1`. Release-taggen är canonical versionskälla vid release och vinner över `VERSION`.

Se `RELEASE-NOTES.md`, `CHANGELOG.md`, `docs/release-checklist.md`, `docs/release-process.md` och `docs/v1-quality-review.md`.

## Defensiv rapportering

GPT:n behåller hög teknisk detaljnivå för rotorsak, evidens, remediation och defensiv verifiering, men abstraherar onödiga exploateringssteg, payloads, PoC, bypass-recept och attackkedjor. Detta gäller chat, Markdown, Confluence markup, Word och PDF.

## System- och attackyteöversikt

Standard- och Deep-rapporter ger nu tidigt en verifierad systembild med huvudkomponenter, deployment, aktörer och externa integrationer. Därefter visas analyserade säkerhetsrelevanta flöden/attackytor med granskningsfokus och coverage-status. Saknad topologi eller integration fylls inte i genom antaganden.

## Steg 24 - flerpassgranskning och robust PDF-layout

Standard/Deep använder nu en obligatorisk kontrollmatris, challenge pass och coverage gate innan rapportering. Word/PDF använder samtidigt adaptiv tabellayout med färre texttunga kolumner och diskreta horisontella radavskiljare. Se `canonical/multi-pass-review-contract.md`, `docs/multi-pass-review.md` och `docs/pdf-table-layout.md`.

## Steg 25 - kandidatregister och deterministisk leverans
Standard/Deep använder nu ett beständigt kandidatregister med obligatorisk slutdisposition och en leveransgate före rapportgenerering. DOCX/PDF renderas deterministiskt från canonical JSON; texttunga tabeller begränsas till tre kolumner och åtgärds-/follow-up-sektioner använder blocklayout.


## GPT Byggaren 1.6.33 – runtime-distributioner

De fem aktiva distributionerna är Chat, OpenAI Plugin, Claude Project, Claude Skills och OpenCode. GitHub Release använder originalmotorn 1.6.33 och publicerar sex ZIP-arkiv inklusive projektpaketet, `SHA256SUMS.txt` och `DELIVERY-MANIFEST.json`.

Runtime-kontrakten är gemensamma, men verktygspariteten är värdberoende: framför allt Claude-distributionerna kräver en host som erbjuder beständigt review state och deterministisk exekvering för att kunna slutföra Standard/Deep och binär rapportexport. De två registrerade domänverktygen är `review-integrity` och `report-delivery`.

Verifiering sker i CI mot originalmotorns builder, distributionsvalidator och leveransvalidator. Säkerhets-, coverage- och rapporttester bibehålls. En faktisk publicerad GitHub Release återstår att verifiera separat.
