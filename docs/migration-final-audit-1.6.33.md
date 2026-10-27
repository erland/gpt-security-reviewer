# Slutgranskning av övergången 1.5 → 1.6.33

Datum: 2026-10-27. PR #10, granskad commit f873989.

## Verifierad baslinje

CI-körning 40568989996 avslutades med `success`. Det innefattar både Security Reviewers befintliga rapport-/integritetstester och originalmotorns 1.6.33-installation, projektlint, sex arkiv, distributionsvalidering och leveranskontroll. Detta bevisar däremot inte att en riktig publicerad GitHub Release har körts.

## Kvarvarande 1.5-beroenden (inventering)

| Komponent | Verifierat kvarvarande beroende | Bedömning |
| --- | --- | --- |
| `scripts/validate_release_readiness.py` | Kräver fem äldre arkiv, inklusive Custom GPT, och äldre filnamn | Legacy release smoke; får inte användas som 1.6.33-release-gate |
| `scripts/verify_reproducible_build.py` | Kör åtta äldre bygg-/paketeringsskript och jämför deras artefakter | Testar endast legacy-reproducerbarhet |
| `scripts/validate_project.py` | Kräver Custom GPT-resurser, äldre byggskript och runtimespecifika kontrakt | Kräver kontrollerad nedtrappning, inte blind radering |
| `scripts/validate_workflow_parity.py` | CI:s release-smoke kräver fortfarande gamla bygg- och checksummekanisismen | Dubbla modeller; separation krävs |
| `scripts/validate_runtime_parity.py` | Spårbarhet för Chat, Plugin och OpenCode genom äldre runtime-contract JSON; Claude har enbart hostbegränsningsdeklarationer | Skilj statisk projektparitet från faktisk paketparitet |
| `scripts/project_hygiene.py` | Kräver fortsatt tidigare runtimekontrakt | Behöver migreras tillsammans med `validate_project.py` |
| `project-status.yaml` och dokumentation | Äldre 1.5-underlag anger historiskt release-ready och äldre Custom GPT-leverans | Måste avslutas utan att felaktigt hävda att en 1.6.33-release genomförts |

## För att avsluta PR #10 utan regression

1. **Paketa och testa mot verkliga kanoniska artefakter.** Kontrollera Skillens `references`, `scripts`, policy och faktisk resursclosure i Chat/Plugin/Claude/OpenCode. Det gröna CI-jobbet säkerställer motorns leveranskontroll men ersätter inte manuell funktionell granskning av hostspecifika verktyg.
2. **Migrera legacy-validatorerna samordnat.** Byt bygg-/checksum-/manifestspecifika referenser i `validate_project.py`, `validate_release_readiness.py`, `verify_reproducible_build.py` och CI:s `release-smoke` till motorns kanoniska flöde. Bevara granskningens scheman, coverage gate, report delivery och PDF/DOCX-tester.
3. **Städa endast efter grön ny CI.** Ta då bort onödiga legacybyggare och Custom GPT-resurser; anpassa `project_hygiene.py` och övriga korsreferenser i samma commit.
4. **Verifiera publicerad release separat.** Den uppdaterade `release.yml` är kodgranskad/CI-paritetskontrollerad men har inte exekverats av ett verkligt `release.published`-event i denna granskning.

## Rekommendation

Fortsätt med steg 2 samordnat i PR #10. Merg inte enbart därför att CI för migrationsbranchen är grön; en viktig del av release-smoke bygger fortfarande legacydistributionerna.
