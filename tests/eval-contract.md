# Eval contract

## Purpose
Testsviten ska verifiera både recall och precision.

GPT:n ska:
- hitta verkliga och underbyggda säkerhetsproblem,
- skilja confirmed/probable/review-point,
- avstå från generiska eller felaktiga fynd,
- markera not_verifiable när underlaget saknas,
- ge proportionerliga rekommendationer.

## Scenario classes
- `positive` – konkret fynd ska identifieras
- `negative` – GPT:n ska avstå från fynd
- `uncertainty` – GPT:n ska markera osäkerhet/not_verifiable
- `architecture` – arkitektur/trust-boundary-resonemang
- `recommendation` – proportionerlig fortsatt granskning

## Atomic eval format
Endast scenarier registrerade i `tests/scenarios/index.json` räknas som atomära eval-scenarier.

Varje registrerat scenario ska innehålla:
- `## Class`
- `## Tags`
- `## Input`
- `## Expected`

Äldre samlingsfiler får ligga kvar i katalogen som referensmaterial men ska inte automatiskt tolkas som atomära evals.
