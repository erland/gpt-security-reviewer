# Project – Säkerhetsgranskaren för IT-stöd

## Syfte

Projektet ger evidensbaserad, defensiv och spårbar säkerhetsgranskning av källkod, konfiguration, deploymentunderlag och arkitekturdokumentation.

## Canonical beteende

Befintligt canonical-lager är fortsatt auktoritativt. Migreringen till GPT Byggaren 1.5.0 ändrar inte granskningslogik, rapporteringsregler eller säkerhetsklassificering.

Viktiga styrande filer:

- `canonical/runtime-contract.md`
- `canonical/workflow.md`
- `canonical/multi-pass-review-contract.md`
- `canonical/review-framework.md`
- `canonical/reporting-contract.md`
- `canonical/defensive-reporting-contract.md`
- `schemas/review-process.schema.json`

## Modellrobusthet

`stateful`

Standard/Deep använder redan strukturerat state genom kontrollmatris, kandidatregister, challenge pass och coverage gate. `review_process` är därför auktoritativ state-modell under en granskning.

## Runtime-strategi

- ChatGPT Chat – ready / active
- ChatGPT Custom – ready / active
- OpenCode – ready / active
- Claude Projects – reduced / inactive
- OpenAI Plugin – equivalent_runtime_dependent / active

OpenCode är referensruntime för lokal full parity. OpenAI Plugin använder samma canonical state/tool-modell som skills-first peer runtime; full Standard/Deep-parity är beroende av hostens repository-workspace, persistent filesystem och code execution.

## Projektkällor

- Projektkontrakt: `gpt-project.yaml`
- Strukturerad projektstatus: `project-status.yaml`
- Utvecklingsplan: `docs/development-plan.md`
- Runtime state-schema: `schemas/review-process.schema.json`

- Runtime parity: `runtime-parity.yaml`
- Runtime contracts: `runtime-contracts/`
