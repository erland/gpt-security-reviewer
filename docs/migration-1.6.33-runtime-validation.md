# 1.6.33 – verifieringsresultat efter aktivering av runtime-modellen

Datum: 2026-10-27

## Genomfört på PR-branchen

- `instructions.mode: modular_skills`, gemensam kärna och en Security Review Skill är aktiverade i projektkontraktet.
- `build_system.targets` och `build_system.runtime_targets` deklarerar projektpaket samt exakt fem runtime-mål: chat, plugin, claude_project, claude_skills, opencode.
- Historisk `runtime.custom_gpt.enabled` är `false` enligt originalmotorns installerarkontrakt.
- `runtime.plugin` har lagts till utan att radera det äldre `runtime.openai_plugin`; legacy-konfigurationen är tills vidare kvar för spårbarhet.
- `runtime.claude.enabled` är `true` som distributionsmål, **inte** ett påstående om verifierad funktionell hostparitet.
- Projektspecifika säkerhets-/rapportverktyg och ursprunglig instruktion är ännu inte borttagna.

## Kontroller

- PASS: 1.6.33-originalmotorns själtest, inklusive source, materialize, integrity, installer och provbygge av sex arkiv. Detta test är för originalmotorn, inte Security Reviewer.
- PASS: byte-exakt återställning av den äldre runtimeinstruktionen från den modulära assembly-manifesten.
- EJ KÖRD: originalmotorns `install_distribution_engine.py` mot hela Security Reviewer-repot.
- EJ KÖRD: originalmotorns lint och full distribution build/validation för Security Reviewer.
- EJ KÖRD: säkerhetsgranskarens regressionssvit och alla rapport-/DOCX-/PDF-validatorer.
- EJ VERIFIERAT: resursclosure för den nya Skillens references/assets/scripts.
- EJ GODKÄND: release readiness och runtimeparitet.

## Känd inkompatibilitet att lösa före merge

Legacy `scripts/lint_gpt_project.py` kräver uttryckligen den gamla uppsättningen runtime-kandidater och ett aktivt historiskt Custom GPT-mål, medan originalmotorn 1.6.33 kräver inaktiverad `runtime.custom_gpt` och en ny `runtime.plugin`. Denna konflikt måste lösas genom byte till originalmotorns installations-/valideringsflöde **med bibehållna projektspecifika testgates**; det är inte tillräckligt att kringgå eller stänga av den gamla linten.

## Nästa steg

Kör migreringen och samtliga tester mot hela repositoryt i en exekverbar projektarbetskopia. Uppdatera CI/release till versionspinnad motor 1.6.33 efter verifierad installerare, och ta först därefter bort ersatta legacybyggare. PR ska vara draft tills dessa kontroller är gröna.
