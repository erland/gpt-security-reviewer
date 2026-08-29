# START HERE

Detta är canonical projektkälla för **Säkerhetsgranskaren för IT-stöd**.

## Arbetsordning

1. Läs `canonical/runtime-contract.md`.
2. Läs `canonical/workflow.md`.
3. Läs `canonical/review-framework.md`.
4. Läs `canonical/reporting-contract.md`.
5. Aktivera endast relevanta teknikprofiler under `knowledge/`.
6. Validera projektet med `python3 scripts/validate_project.py`.

## Designprincip

Kärninstruktionen ska hållas kompakt. Teknikspecifik kunskap ska ligga i separata profiler så att GPT:n kan växa utan att runtime-kontraktet blir stort.

## Common security-profiler

Läs `knowledge/common/application-security.md` som orientering och aktivera därefter endast de domänprofiler som är relevanta för det identifierade systemet och granskningsscopet.

## Inför release
- `RELEASE-NOTES.md`
- `CHANGELOG.md`
- `docs/release-checklist.md`
- `docs/v1-quality-review.md`
