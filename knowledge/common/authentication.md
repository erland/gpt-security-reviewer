# Authentication

## Applicability
Använd när systemet autentiserar användare, tjänster eller maskinidentiteter, eller när autentisering sker i en extern IdP/gateway som påverkar applikationens säkerhet.

## Security objectives
- identiteter ska verifieras på rätt trust boundary,
- autentiseringsresultat ska inte kunna förfalskas av klienten,
- credentials/tokens ska hanteras säkert genom hela livscykeln,
- återautentisering och sessionsavslut ska vara proportionerliga mot risk.

## High-value review areas
- var autentisering faktiskt sker,
- hur backend etablerar vem användaren/tjänsten är,
- validering av token/signatur/issuer/audience/expiry,
- service-to-service identity,
- fallback-/bypass-vägar,
- sessionsskapande och logout,
- lösenordsflöden när applikationen själv hanterar lösenord,
- recovery/reset-flöden,
- MFA-indikationer för privilegierade flöden när relevant.

## Evidence indicators
Stark evidens kan vara verifieringskod, security configuration, filter/interceptors, tokenvalidering, endpointpolicy eller dokumenterad och konfigurerad extern kontroll.

## Common weaknesses
- backend litar på klientskickat användar-ID/roll,
- token parsas men verifieras inte fullständigt,
- fel issuer/audience-validering,
- oskyddad alternativ endpoint,
- långlivade tokens utan rimlig kontroll,
- session invalidation saknas där det är säkerhetsrelevant.

## False-positive guards
- frånvaro av lokal login-kod är inte en brist om autentisering sker externt,
- frontend guards är UX och får inte ensamma bedömas som backend-autentisering,
- saknad MFA-kod i repo är inte bevis för att MFA saknas om IdP:n ligger externt.

## Manual verification triggers
- IdP/gateway-konfiguration saknas,
- tokenpolicyer styrs utanför repo,
- recovery/MFA-flöden ligger hos extern part,
- produktionssessionsinställningar saknas.
