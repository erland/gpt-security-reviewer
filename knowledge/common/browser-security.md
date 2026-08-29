# Browser security

## Applicability
Används tillsammans med frontend-profiler när browsern utgör en viktig del av säkerhetsmodellen.

## Security objectives
Bedöm browserns säkerhetsmekanismer som delar av en helhet, inte som isolerade checklistpunkter.

## High-value review areas
- cookies och attribut
- browser storage
- CSP
- CORS-antaganden
- redirects
- postMessage
- iframe/sandbox
- tredjepartsskript
- source maps/debugdata

## Evidence expectations
Frånvaro i frontend-repot är inte bevis för frånvaro i runtime. Ange `not_verifiable` när reverse proxy, gateway eller plattform kan sätta kontrollen.

## False-positive guards
CORS är inte autentisering eller auktorisering. CSP är defense-in-depth och frånvaro är inte automatiskt en sårbarhet. Ett public client-id är inte en secret.

## Manual verification triggers
När headers, cookies, gatewaypolicy eller IdP-konfiguration ligger utanför det analyserade materialet.
