# Status – Säkerhetsgranskaren för IT-stöd

## Pågående migrering

Projektets runtime- och distributionsmodell har migrerats från GPT Byggaren 1.5 till originalmotorn **1.6.33** på PR #10. Den tidigare 1.5-migreringen finns dokumenterad i Git-historiken och i `docs/development-plan.md`.

## Runtime-mål

- Chat – aktiv distribution
- OpenAI Plugin – aktiv, med värdberoenden för exekvering och beständigt review state
- Claude Project – aktiv distribution, reducerad verktygsparitet
- Claude Skills – aktiv distribution, reducerad verktygsparitet
- OpenCode – aktiv distribution

Custom GPT är inte längre en aktiv distribution. Gemensam kärna finns i `canonical/core.md`, och Security Review Skill i `canonical/skills/security-review/behavior.md`. Legacy `canonical/runtime-contract.md` är tills vidare kvar för spårbarhet och kompatibilitet.

## CI och release

- Ursprunglig 1.6.33-motor används för sex arkiv: projektpaket och fem runtimepaket.
- Säkerhets- och rapportregression, integrity gate, flerpasskontroller och Word/PDF-export kontrolleras fortsatt.
- Release-smoke kontrollerar de sex arkiven, checksummor och reproducerbarhet.
- Senast verifierade gröna CI före borttagning av kvarvarande Custom GPT-resurser: körning 40574174463.
- En verklig GitHub Release med `release.published` har **inte** verifierats.

## Kvarstående slutkontroller

1. Kontrollera CI efter den sista städningen av Custom GPT-resurserna.
2. Granska Skillens resursclosure och distributionernas faktiska verktygsförmåga/hostbegränsningar.
3. Kontrollera slutlig releasekonfiguration och markera därefter PR redo för granskning.

PR #10 förblir draft tills samtliga dessa kontroller passerat.
