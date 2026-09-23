# Status – Säkerhetsgranskaren för IT-stöd

## Sammanfattning

Migrering till **GPT Byggaren 1.5.0** har startat.

Befintligt canonical säkerhetsbeteende, flerpassgranskning, rapportpipeline och nuvarande Chat/Custom GPT-distributioner bevaras medan projekt- och runtime-modellen moderniseras.

## Migrationssteg

- [x] Steg 1 – GPT Byggaren 1.5 projektmodell och stateful kontrakt
- [x] Steg 2 – 1.5 testmanifest och model-robustness evals
- [x] Steg 3 – OpenCode peer-distribution
- [ ] Steg 4 – Runtime parity och modern releasekedja
- [ ] Steg 5 – Slutregression, hygiene och release readiness

## Runtime-status

- ChatGPT Chat: ready / active
- ChatGPT Custom: ready / active
- OpenCode: ready / active
- Claude Projects: reduced / inactive
- OpenAI Plugin: reduced / inactive

## Verifiering av steg 1

CI passerade den nya GPT Builder stateful-linten tillsammans med befintliga projekt-, workflow-, RC-, rapport-, multi-pass-, review-integrity-, export-, defensive-reporting- och distributionsvalidatorer. Chat/Custom-build samt release-smoke är fortsatt gröna.

## Verifiering av steg 2

CI passerade testmanifestregistreringen och blockerande model-robustness evals för prompt injection i granskningsmaterial, kandidatretention, coverage gate, falsk säkerhetsconfidence och defensiv rapportering. Samtidigt passerade hela den befintliga säkerhets-, rapport-, export- och distributionskedjan.

## Verifiering av steg 3

OpenCode-distributionen bygger och validerar i både full CI och release-smoke. Paketet håller runtimefiler under `.opencode/security-reviewer/`, review state under `.security-reviewer-state/` och rapporter under `security-review-output/`. Målrepots källfiler är read-only som standard och assistant/state/output-yta exkluderas från source evidence.

## Aktuellt steg

**Steg 4 – Runtime parity och modern releasekedja.**
