# Relationsdatabaser

## Applicability
Använd när applikationen använder relationsdatabas via JDBC, JPA, ORM, stored procedures eller motsvarande.

## Security objectives
Databasen ska behandlas som en skyddsvärd säkerhetsgräns med minsta privilegium, säker query-konstruktion, kontrollerad åtkomst till känsliga data och tydlig ansvarsfördelning mellan applikation och databas.

## High-value review areas
- parametrisering
- dynamisk SQL
- dynamiska identifiers/fragments
- servicekonton och privilegier
- schema-/objektbehörigheter
- credentials
- känsliga data
- audit/loggning
- krypteringsindikatorer
- backup/export
- multi-tenant/dataisolering
- stored procedures
- migrations och privilegier

## Code patterns
Leta efter:
- strängkonkatenering i SQL
- native queries
- dynamiska tabell-/kolumnnamn
- användarstyrd sortering/filter
- stored procedure-anrop med dynamiska delar
- administratörskonton i connection strings
- credentials i repo
- generiska databasanvändare med breda rättigheter

## Configuration patterns
Granska:
- datasource-användare
- connection strings
- SSL/TLS-parametrar
- schema
- migrations
- grants
- read/write-separation
- auditinställningar när de finns
- backup/exportkonfiguration

## Common weaknesses
- applikationskonto har onödigt höga privilegier
- användarinput når query-fragment utan allowlist
- känsliga data exponeras via för breda queries
- credentials lagras i repo
- databasåtkomst sker utan TLS där hotmodellen kräver skydd
- backup/export innehåller skyddsvärd data utan motsvarande skydd
- tenantfilter kan kringgås

## False-positive guards
Rapportera inte:
- alla ORM-anrop som SQL injection
- alla administrativa DB-användare som brist utan att verifiera faktisk användning
- avsaknad av DB-grants i repo som bevis på för breda privilegier
- frånvaro av TLS-inställning i applikationen om TLS termineras/krävs externt

## Evidence expectations
För injektion: visa kontrollerbar input, query construction och otillräckligt skydd.
För privilegier: visa faktisk credential/roll/grant eller tydlig runtimekonfiguration.
För känslig data: visa vilken data som hanteras och varför exponeringen är otillräckligt skyddad.

## Manual verification triggers
- grants hanteras utanför repo
- DB-policyer/RLS används
- tenantisolering implementeras i databasen
- TLS krävs av plattformen
- backup/audit hanteras centralt
