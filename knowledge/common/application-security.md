# Application security

## Applicability
Används som gemensam orienteringsmodul för alla applikationsgranskningar. Detaljerade regler ligger i domänprofilerna i samma katalog.

## Core domains
- authentication
- authorization
- input/output/injection
- secrets and cryptography
- logging and error handling
- API security
- dependency and supply chain
- sensitive data
- architecture and trust boundaries

## Review priority
Prioritera i första hand:
1. privilegierade och administrativa flöden,
2. autentisering och auktorisering,
3. känsliga data över trust boundaries,
4. attacker-kontrollerad input till farliga sinks,
5. secrets och säkerhetskritisk konfiguration,
6. externa integrationer och dependency/build-risker.

## Evidence expectations
Generiska mönster får inte rapporteras som konkreta fynd utan koppling till faktisk implementation, konfiguration eller dokumenterad arkitektur.

## Cross-cutting rule
Ett fynd kan spänna över flera profiler. Konsolidera då observationerna efter rotorsak och exploaterbar kedja i stället för att skapa separata checklistfynd.

## Manual verification triggers
Komplex behörighetslogik, externa säkerhetskontroller, runtime-IAM, dynamiska policyer, dataklassning och områden där relevant produktionskonfiguration saknas.
