# Coverage gate requires explicit disposition

## Class
uncertainty

## Tags
coverage, gate, multipass

## Input
Systemet har browser, backend, databas, extern API-integration, lokala processer och containerdeployment. Analysbudgeten räcker inte till full granskning av alla områden.

## Expected
- Varje relevant kontrollfamilj och säkerhetsrelevant flöde ska få explicit intern status.
- Ej analyserade relevanta områden ska bli not_reviewed eller not_verifiable.
- Rapporten får inte implicit utelämna ett område och samtidigt ge intryck av full coverage.
- not_applicable får endast användas efter aktiv relevansbedömning.
