# Motor- och källkontroll, migrationssteg 3 (2026-10-27)

## Resultat

**PASS – originalmotor:** användarbifogad `gpt-byggaren-engine-1.6.33(3).zip` kontrollerades i ett lokalt isolerat workspace. Originalscript `scripts/selftest_distribution_engine.py --source /mnt/data/security-engine` returnerade `ok: true`. Stegen source (62 filer), materialize (62), integrity (SHA-256 för 62), installer samt build (ett projektarkiv + fem peer-distributioner) passerade. Smoke-testet bygger motorns testprojekt, **inte** Security Reviewer.

**PASS – källspårbarhet:** samtliga nio rubriker i tidigare `canonical/runtime-contract.md` har en motsvarighet i `canonical/core.md` respektive `canonical/skills/security-review/behavior.md`. Fyra kritiska uttryck för odata, flerpassmodell, coverage gate och risk/confidence finns i dessa kandidatkällor.

**NOT RUN – projektbuild:** projektet är inte lokalt klonat i detta steg och Security Reviewers egna fullständiga build-, schema-, verktygs- och regressionskontroller har inte körts. Nya källor är därför **staged, not activated**.

## Ändrade filer

- `canonical/core.md` – kärnbeteende och obligatoriska gates
- `canonical/skills/security-review/behavior.md` – exklusiv granskning/rapportleverans med tydliga beroenden
- Ursprunglig `canonical/runtime-contract.md` behålls oförändrad som aktiv källa tills atomisk aktivering är verifierad

## Nästa blockerande gate

1. Skaffa komplett projektarbetskopia inklusive alla tester och dependencies.
2. Kör originalmotorns migrerings-/resursanalys för den föreslagna Skill-arkitekturen.
3. Dokumentera explicit resource closure (references/assets/scripts), uppdatera `instructions.mode`, `skills.definitions` och runtime-målen atomiskt.
4. Kör full regression inklusive `validate_review_integrity.py`, all rapportexport, portable skill validation och fem distributionsbyggen.
5. Först efter PASS får legacy-build och CI/release ersättas och PR lämna draft.
