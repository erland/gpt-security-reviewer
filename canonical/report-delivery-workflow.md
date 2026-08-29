# Report delivery workflow

## Purpose
Detta kontrakt kopplar granskningsläge till hur resultat ska levereras.

## Quick
Default: resultat i chatten och ingen fil automatiskt. Om användaren begär fil kan valfritt stödformat genereras.

## Standard
Default: kort sammanfattning i chatten samt fullständig Markdown-rapport som fil.

## Deep
Default: kort sammanfattning i chatten samt fullständig Markdown-rapport med Deep-nivåns mer detaljerade evidens och metodredovisning.

## Supported formats
- markdown
- confluence
- word
- pdf

Flera format får begäras samtidigt.

## Format selection rules
1. Explicit användarval vinner över default.
2. Quick utan format -> chat.
3. Standard utan format -> Markdown.
4. Deep utan format -> Markdown.
5. Flera format renderas från samma report JSON.
6. Analysen görs inte om separat per format.
7. Exportfel får inte ändra rapportdata eller fynd.

## Chat completion message
När filer skapats ska chatten kort ange att granskningen är klar, viktigaste bedömningen, fynd per relevant severity, viktiga not_verifiable-områden och skapade filer.

## No-finding case
Om inga fynd identifierats får GPT:n inte säga att systemet är säkert. Coverage och not_verifiable ska fortfarande redovisas och fortsatt granskning rekommenderas proportionerligt.

## Standard/Deep delivery gate
Innan någon filrendering sker ska canonical report JSON vara färdig och `scripts/validate_review_integrity.py` passera. Kandidatregister, challenge pass och coverage gate är därmed en precondition för leverans.

Word/PDF får inte skapas som fristående dokumentutkast. De ska renderas från samma canonical JSON via projektets renderer. Detta låser rubrikordning och layoutregler oberoende av hur analysen formulerades i chatten.
