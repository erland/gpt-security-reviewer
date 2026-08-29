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

## Distribution

Både Chat ZIP och Custom GPT ska byggas från samma canonical material.

Versionsnummer ska i releaseflödet tas från GitHub Release-taggen.

## Chat ZIP

Chat-distributionen byggs med:

```bash
python3 scripts/build_chat_zip.py
python3 scripts/validate_distribution.py
```

Den resulterande ZIP-filen innehåller endast runtime-relevant material och en rotplacerad `START-HERE.md`.

## Custom GPT

```bash
python3 scripts/build_custom_gpt.py
python3 scripts/validate_custom_gpt.py
python3 scripts/package_custom_gpt.py
```

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
