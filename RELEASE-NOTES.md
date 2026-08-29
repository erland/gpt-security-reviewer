# Release notes – v0.1.0-rc.1

Första releasekandidaten för V1 av Säkerhetsgranskaren för IT-stöd.

## Huvudfunktioner
- Riskdriven säkerhetsgranskning av källkod, konfiguration och arkitekturdokumentation.
- Stöd för React, Angular, Java EE/Jakarta EE, Oracle, PostgreSQL, Elasticsearch samt Docker/Kubernetes/OpenShift.
- Separat severity och confidence samt fyndstatus `confirmed`, `probable`, `review-point`.
- Coverage som Granskat, Ej granskat och Ej verifierbart.
- Quick, Standard och Deep.
- Rapporter i Markdown, Confluence markup, Word och PDF.
- Chat ZIP och Custom GPT från samma canonical kontrakt.
- Release-taggen styr releaseversionen.

## Rapportöversikt

- Standard/Deep inleds nu med en systemöversikt över verifierade huvudkomponenter, deployment, aktörer och externa integrationer.
- Rapporten visar analyserade säkerhetsrelevanta flöden/attackytor med granskningsfokus och coverage-status.
- Saknad deploymenttopologi eller integration fylls inte i genom antaganden.
- Attackyteöversikten följer defensive reporting-kontraktet och innehåller inte exploateringssteg.

## Robusthet
Falskpositivskydd finns bland annat för frontend guards, säker React/Angular-interpolation, parameteriserad SQL, Kubernetes `containerPort`, `secretKeyRef`, externa IAM-/plattformskontroller, prompt injection i granskningsmaterial samt vendor/generated content som `node_modules`.

## Kända begränsningar
- GPT:n ersätter inte fullständigt penetrationstest.
- Infrastruktur-/clusterhardening utanför applikationsnära scope kan kräva specialistgranskning.
- Aktuell CVE-status ska verifieras med SCA/aktuell källa.
- Externa gateway-/IAM-/plattformskontroller kan kräva manuell verifiering.

## Steg 25
- Beständigt candidate finding register med explicit adjudicering.
- Standard/Deep delivery gate validerar review_process före rendering.
- DOCX/PDF max tre textkolumner och blocklayout för åtgärder/follow-up.
- Deterministisk canonical JSON -> renderer-pipeline.
