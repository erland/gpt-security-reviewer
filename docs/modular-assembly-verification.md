# Exakt avsnittsassembly för modulära Skills

## Genomförd källtransformation

Den ursprungliga `canonical/runtime-contract.md` delades nu utan omskrivningar av en enda originalregel:

- `canonical/core.md`: ursprunglig ingress, Roll, Mål och Grundregler.
- `canonical/skills/security-review/behavior.md`: Granskningslägen, Avslutning, Report delivery, Defensive reporting, Upfront system understanding och Multi-pass consistency.
- `canonical/assembly.json`: ordnad ägarlista för exakt återställning av originalets nio avsnitt.

**PASS**: sammanfogning av manifestets nio ordnade avsnitt, inklusive ursprunglig ingress, är byte-för-byte identisk med den tidigare runtimeinstruktionen (4 096 tecken). Detta är starkare än den tidigare rubrikkontrollen.

## Viktig gräns

De modulära källorna är ännu inte aktiverade via `instructions.mode: modular_skills`. Den gamla källan och de gamla byggena är fortsatt aktiva. Nästa ändring måste införa `instructions.core`, `instructions.assembly`, `skills.definitions` och riktiga runtime-targets tillsammans med en verifierad resursclosure. Att bara ändra YAML utan originalmotorns projekttester räcker inte för att godkänna migreringen.

## Resursägarskap som måste verifieras

För Security Review-Skillen: samtliga `canonical/`-kontrakt som används under granskning och rapportleverans, schemas (`review-process`, `report`, `finding`, `review-summary`), teknik-/common-knowledge, samt `validate_review_integrity.py`, `deliver_report.py` och faktiska Python-importberoenden till rapport-renderers. DOCX/PDF kräver extern programvara och ska markeras hostberoende.

## Verifiering

- Exakt källassembly: PASS.
- Motor 1.6.33 självtest på motorns eget provprojekt: PASS (tidigare).
- Security Reviewer originalmotor-build: EJ KÖRD.
- Runtime parity, CI, dokumenthygien och release readiness: EJ GODKÄNDA.

## Nästa steg

Hämta/matera hela projektet i en exekverbar arbetsyta, inventera konkreta skill-referenser/assets/scripts, aktivera YAML-mappningen, kör originalmotorns `lint_gpt_project.py` och `validate_generated_delivery.py`, bygg alla fem runtimepaket och jämför den faktiska instruktionen mot `canonical/runtime-contract.md`. Behåll PR som draft.
