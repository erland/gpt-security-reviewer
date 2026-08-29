# API security

## Applicability
Använd för REST/HTTP-API:er och andra applikationsgränssnitt som exponeras över trust boundaries.

## Security objectives
- varje endpoint ska ha korrekt autentisering och auktorisering,
- resurser och funktioner ska ha server-side access control,
- input/output ska begränsas till avsett schema,
- missbruk och överexponering ska reduceras proportionerligt.

## High-value review areas
- endpoint inventory och oavsiktligt exponerade routes,
- BOLA/IDOR,
- broken function-level authorization,
- mass assignment/property binding,
- excessive data exposure,
- rate/resource abuse när relevant,
- CORS som browser-policy, inte auth-kontroll,
- admin/debug/management endpoints,
- versionerade/legacy endpoints.

## Common weaknesses
- objekt-ID utan ägarskapskontroll,
- bindning direkt till domänobjekt med känsliga fält,
- bred DTO/response med onödigt känsliga attribut,
- admin-route med endast UI-skydd,
- gammal API-version kvar med svagare policy.

## False-positive guards
- CORS påverkar browseråtkomst men ersätter inte authn/authz,
- rate limiting kan ligga i gateway och blir då `not_verifiable` om konfigurationen saknas,
- en endpoint behöver inte vara publik bara för att route-koden saknar lokala annotations.

## Manual verification triggers
- API gateway/policy saknas,
- externa konsumenter och scopes är oklara,
- business logic abuse kräver domänkunskap,
- runtime rate limiting eller schema enforcement ligger externt.
