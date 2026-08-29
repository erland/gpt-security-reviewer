# Chat ZIP distribution

## Syfte
Chat ZIP är den runtime-orienterade distributionen som kan laddas upp och användas direkt som GPT-kontext i en konversation.

## Innehåll
- en rotplacerad `START-HERE.md`,
- fyra runtime-filer,
- common knowledge,
- teknikprofiler,
- fynd- och summary-schema,
- VERSION,
- MANIFEST med SHA-256 checksums.

## Exkluderas
Utvecklingsmaterial såsom:
- `.github/`
- `tests/`
- `scripts/`
- `docs/`
- canonical källkatalog
- byggartefakter

Detta minskar kontextbrus och gör Chat ZIP lättare för enklare modeller att använda.

## Version
Vid vanlig lokal utveckling används `VERSION`.
Vid GitHub Release används release-taggen via `RELEASE_VERSION`.

## Integrity
`MANIFEST.json` listar alla runtimefiler och checksums. `validate_distribution.py` verifierar paketets innehåll.
