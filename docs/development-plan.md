# Development plan – migrering av Säkerhetsgranskaren för IT-stöd

**Målversion:** GPT Byggaren 1.5.0  
**Migrationstyp:** existing-project, behavior-preserving  
**Modellrobusthet:** `stateful`

## Mål

Modernisera projekt- och runtime-modellen utan att förändra den befintliga evidensbaserade, defensiva säkerhetsgranskningen.

Befintliga canonical kontrakt, schemas, rapportpipeline och deterministiska validatorer är auktoritativa och ska återanvändas.

## Steg 1 – GPT Byggaren 1.5 projektmodell och stateful kontrakt

Inför:

- `gpt-project.yaml`,
- strukturerad projektstatus och migrationsplan,
- capability-, artifact-, workspace/state- och tool-kontrakt,
- explicit bedömning av alla fem peer-runtimes,
- `stateful` modellrobusthet,
- `schemas/review-process.schema.json` som auktoritativ state-modell för Standard/Deep.

**Klart när:** befintlig canonical logik är oförändrad och alla nuvarande projekt-/rapport-/Chat-/Custom-valideringar passerar tillsammans med ny 1.5-lint.

## Steg 2 – 1.5 testmanifest och model-robustness evals

Registrera befintliga deterministic gates i ett 1.5-testmanifest och komplettera med instruction-adherence-evals för prompt injection, kandidatförlust, coverage gate, falsk säkerhetsconfidence och defensiv rapportering.

## Steg 3 – OpenCode peer-distribution

Bygg OpenCode från samma canonical regler, Knowledge, schemas och relevanta verktyg. Målrepo ska hållas separat från assistantens runtimefiler. Normal säkerhetsgranskning ska vara read-only mot målrepo.

## Steg 4 – Runtime parity och modern releasekedja

Jämför fem registrerade runtimes över behavior, capability, artifact, workspace/state och tool.

Aktivera Chat, Custom GPT och OpenCode. Dokumentera Claude Projects och OpenAI Plugin som reducerade tills deras tool/runtime-modell kan uppfylla hela kontraktet.

Inför Project ZIP, runtime contracts, delivery manifest, checksummor och release-readiness.

## Steg 5 – Slutregression, hygiene och release readiness

Verifiera full regression, runtime parity, workflow parity, project hygiene och reproducerbar leverans. Genererad `dist/` ska inte vara persistent källmaterial när motsvarande CI/release-output är verifierad.

## Aktuellt nästa steg

**Steg 1 – GPT Byggaren 1.5 projektmodell och stateful kontrakt.**
