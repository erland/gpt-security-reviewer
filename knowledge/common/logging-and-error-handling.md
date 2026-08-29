# Logging and error handling

## Applicability
Använd för säkerhetsrelevant spårbarhet, audit, applikationsloggar och felhantering.

## Security objectives
- säkerhetskritiska händelser ska kunna följas upp,
- loggar ska inte läcka secrets eller onödigt känsliga uppgifter,
- fel ska inte exponera intern implementation till obehöriga,
- logginnehåll ska vara motståndskraftigt mot manipulation där relevant.

## High-value review areas
- login/auth failures,
- privilegie-/administrativa ändringar,
- behörighetsfel,
- kritiska dataändringar,
- exception handlers,
- stack traces till klient,
- token/credential/PII i loggar,
- audit correlation/user identity.

## Common weaknesses
- access-/adminhändelser saknar spårbarhet,
- credentials/tokens loggas,
- full stack trace eller SQL-detaljer exponeras,
- klientinput loggas rått på ett sätt som möjliggör log injection,
- audit kan raderas/manipuleras av samma privilegium utan kontroll.

## False-positive guards
- avsaknad av loggkod i applikationen är inte bevis för att plattform/audit saknas,
- detaljerad serverlogg är inte samma sak som informationsläckage till klient.

## Manual verification triggers
- central logging/SIEM ligger externt,
- retention/access control saknas i underlaget,
- compliance/auditkrav kräver verksamhetsbedömning.
