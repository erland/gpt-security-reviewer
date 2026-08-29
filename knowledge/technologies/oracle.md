# Oracle

## Applicability
Använd när applikationen eller arkitekturen använder Oracle Database.

## Security objectives
Verifiera att applikationen använder ett ändamålsenligt konto, att privilegier är begränsade och att Oracle-specifika mekanismer inte skapar onödig attackyta eller kringgår applikationens säkerhetsmodell.

## High-value review areas
- system/object privileges
- roller och direkt grants
- schemaägare kontra runtimekonto
- `EXECUTE` på packages/procedures
- dynamic SQL i PL/SQL
- definer rights / invoker rights
- database links
- sensitive data
- auditing
- credentials/wallets
- network services
- backup/export
- TLS-konfiguration när synlig

## Code patterns
Leta efter:
- `EXECUTE IMMEDIATE`
- `DBMS_SQL`
- dynamisk PL/SQL/SQL med extern input
- stored procedures som bygger query-strängar
- användning av mycket privilegierade konton
- databaslänkar
- privilegiehöjande packages
- klientinput till procedure-parametrar som senare används dynamiskt

## Configuration patterns
Granska när det finns:
- användare/roller
- grants
- schema ownership
- datasource credentials
- wallets
- TNS/connection config
- audit policies
- database links
- export/backup scripts

## Common weaknesses
- applikationen ansluter som schemaägare eller överprivilegierad användare
- dynamisk SQL i PL/SQL använder otillförlitlig input utan allowlist/bind
- `AUTHID DEFINER` kombineras med osäker input och kraftfulla privilegier
- databaslänk exponerar bred åtkomst
- credentials i config/repo
- känslig export hanteras osäkert

## False-positive guards
Rapportera inte:
- `EXECUTE IMMEDIATE` som injektion om inputen är statisk eller strikt allowlistad
- `AUTHID DEFINER` som brist i sig; bedöm privilegier och input
- schemaägare som runtimekonto om arkitekturen uttryckligen och säkert kräver detta utan att först bedöma faktisk risk
- saknade audit policies i repo som bevis på avsaknad i databasen

## Evidence expectations
Oracle-specifika fynd ska kopplas till faktisk PL/SQL, grant, connection-konfiguration eller dokumenterad runtimearkitektur.

## Manual verification triggers
- privilegier hanteras av DBA utanför repo
- VPD/FGAC eller andra policyer används
- wallets och network ACLs hanteras centralt
- auditing konfigureras i databasmiljön

## Defensive reporting note

Behåll rotorsak, evidens, severity/confidence, remediation och defensivt verifieringsmål. Abstrahera exploitpayloads, steg-för-steg-angrepp, bypass-recept och attackkedjor om de inte behövs för defensiv förståelse.
