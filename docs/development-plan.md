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

Aktivera Chat, Custom GPT och OpenCode. Claude Projects är reducerad tills dess tool/runtime-modell kan uppfylla hela kontraktet. OpenAI Plugin aktiveras senare som runtime-dependent peer när skills-first workspace/state/tool-projektionen är verifierad.

Inför Project ZIP, runtime contracts, delivery manifest, checksummor och release-readiness.

## Steg 5 – Slutregression, hygiene och release readiness

Verifiera full regression, runtime parity, workflow parity, project hygiene och reproducerbar leverans. Genererad `dist/` ska inte vara persistent källmaterial när motsvarande CI/release-output är verifierad.

## Aktuellt nästa steg

Alla migrationssteg 1–5 är klara och verifierade. Projektet är i maintenance-läge efter migreringen till GPT Byggaren 1.5.0.


## Steg 6 – OpenAI Plugin peer-distribution

Aktivera OpenAI Plugin som `equivalent_runtime_dependent` från samma canonical säkerhetskontrakt.

**Klart när:**
- Plugin-ZIP har `plugin.json`, `runtime-contract.json` och canonical `SKILL.md`,
- canonical kontrakt, Knowledge, schemas och runtime tool/support closure följer med,
- review state är workspace-authoritativt för Standard/Deep,
- målrepo är read-only som standard och Plugin/state/output exkluderas från source evidence,
- review-integrity kan inte hoppas över,
- script-resurser kräver inte MCP-wrapper,
- Plugin ingår i CI, release, checksums, delivery manifest och reproducibility.
