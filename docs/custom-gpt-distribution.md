# Custom GPT distribution

Custom GPT-paketet byggs från samma canonical källor som Chat ZIP.

## Instruktioner
En särskild kompakt instruktion genereras från `custom-gpt/instructions-template.md`. Den innehåller endast styrande runtime-regler och ska hålla sig under konfigurerad teckengräns.

## Knowledge
Detaljlogiken paketeras i tematiska filer:
- granskningskärna,
- common,
- frontend,
- backend,
- data/search,
- architecture/deployment,
- två schemas.

Det håller både instruktionen och filantalet små.

## Validering
Builder och validator stoppar om:
- instruktionerna blir för stora,
- knowledge-filantalet blir för högt,
- obligatoriska regler saknas,
- checksummor eller manifest inte stämmer.
