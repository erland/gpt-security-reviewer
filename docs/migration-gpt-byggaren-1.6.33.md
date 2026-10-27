# Migrering till GPT Byggaren 1.6.33

Status: **Inventering genomförd; implementation ej påbörjad**. Detta dokument är ett migrationsunderlag, inte ett godkännande för merge eller release.

## Utgångsläge (main, 2026-10-27)

- Senaste uttryckligt dokumenterade GPT Byggaren-nivå är **1.5.0** i `gpt-project.yaml`, `STATUS.md` och `PROJECT.md`.
- Projektet använder en monolitisk canonical instruktion i `canonical/runtime-contract.md`, med kompletterande styrande kontrakt i `canonical/`.
- Aktiva befintliga mål: Chat, historisk Custom GPT, OpenCode och OpenAI Plugin; Claude Projects bedöms reducerad/inaktiv.
- Standard/Deep kräver persistent `review_process`, flerpassgranskning, kandidatregister, challenge pass, coverage gate och `scripts/validate_review_integrity.py`.
- Markdown, Confluence, DOCX och PDF produceras från strukturerad rapportdata; binära exporter kräver deterministisk pipeline.
- Befintlig CI och release använder projektspecifika bygg-, lint- och distributionsskript. Deras funktionella ersättning är **inte verifierad**.

## Vald strategi

Beteendebevarande migration, i sex steg enligt GPT Byggaren 1.6.33. Skriv inte över tidigare godkänd status eller versionshistorik förrän relevant gate faktiskt passerat. Motorns version och projektets releaseversion ska hållas åtskilda. Den originalpaketerade motorn `gpt-byggaren-engine-1.6.33.zip` är ett externt, versionsbundet byggberoende — den ska inte kopieras in som en alternativ egen motor.

### 1. Inventering — klar

Inventera runtime, styrande kontrakt, användbara resurser, skript, scheman, tester, dokumentation och CI. Klar som analys, **inte** som migrerad leverans. Bifogad originalmotor 1.6.33 passerade sitt självtest utanför projektet (SHA-256, installerare och sex-arkiv-smoke); det visar inte att Security Reviewer byggts med motorn.

### 2. Projektmodell — återstår

Uppdatera `gpt-project.yaml` och `project-status.yaml` enligt 1.6.33 efter kontroll av motorns schema. Definiera exakt fem runtime-mål: `chat`, `plugin`, `claude_project`, `claude_skills`, `opencode`. Historisk `custom_gpt` arkiveras som kompatibilitet, inte sjätte byggmål. Fortsätt behandla alla runtime-mål som peers men beskriv hostberoende funktioner ärligt.

### 3. Motor — återstår

Installera originalmotorn i en separat arbetskopia; verifiera installation, version och integritet. Behåll projektspecifika validatorer, rapport- och reviewverktyg där motorn inte har funktionell ersättning. Inga egna ersättningsbyggare. Versionspinna extern motor i GitHub Actions och kontrollera release-taggen separat.

### 4. Fem distributioner — återstår

Utvärdera modulär Skill-design **före** uppdelningen. Föreslagen minimal delning:

- `canonical/core.md`: identitet, odata/prompt injection, evidensdisciplin, risk kontra confidence, lägen, övergripande report-/review-gates och säkerhetsprinciper.
- `canonical/skills/security-review/behavior.md`: inventering, attackytor, teknikspecifika granskningsprofiler, kontrollmatris, candidate retention och challenge/coverage.
- `canonical/skills/report-delivery/behavior.md`: rapportstruktur, defensiv rapportering, rapportmodell, uttryckligt formatval, export- och integritetsgates.

Denna fördelning är preliminär. Kontrollera aktiveringsvillkor, ansvar och källspårbarhet innan den fastställs. Undvik två kopior av samma canonical text. `skills.resource_policy: explicit` ska endast införas efter granskning av alla aktiva beroenden för respektive skill. Kritiska regler måste finnas i core eller direkt aktiverat Skill-beteende.

Producera Chat, OpenAI Plugin, Claude Projects, Claude Skills och OpenCode med originalmotorn. Markera eventuella begränsningar kring persistent review state, verktyg och binära exporter per host i parity-rapporten.

### 5. Dokumentation och filhygien — återstår

Jämför `README.md`, `PROJECT.md`, `STATUS.md`, `docs/development-plan.md`, `docs/release-checklist.md`, `project-status.yaml`, workflows och faktiska utdata. Uppdatera brutna referenser samt versions-/releaseinstruktioner. Ta inte bort befintliga build/validator-skript förrän alla anrop och projektspecifika beteenden verifierats ersatta.

### 6. Slutverifiering — återstår

Kör canonical lint, projektets egen säkerhets-/rapportregression, schema-/resource-validering, modellrobusthets-evals, fem byggmål och distribution validation. Kontrollera runtime parity, integrity/coverage gate, reproducerbarhet, CI-release smoke, hygiene och release readiness. Markera klart först därefter.

## Särskilda regressionsrisker

1. `review_process` och kandidatretention förloras i ny Skill-separation.
2. Rapportexport till DOCX/PDF byter deterministisk pipeline eller hoppar över review-integrity.
3. Målrepo behandlas som instruktion i stället för odata eller ändras trots read-only-default.
4. Claude/Plugin rapporteras ha ekvivalent exekvering utan state-/filesystem-/code-execution-stöd.
5. Projektspecifika rapportverktyg misstas för runtimeverktyg enbart för att de ligger under `scripts/`.

## Nästa konkreta steg

Genomför **steg 2: projektmodell och verifierbar Skill-uppdelning** i en arbetskopia med samtliga ursprungliga filer. Kör motorns schema-/migrationsvalidator före nästa PR-uppdatering. Fortsätt därefter med steg 3–6; merge först vid dokumenterad grön slutverifiering.
