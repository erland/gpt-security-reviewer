# PostgreSQL

## Applicability
Använd när applikationen eller arkitekturen använder PostgreSQL.

## Security objectives
Verifiera minsta privilegium, säker schema-/rollmodell, korrekt query-konstruktion och att PostgreSQL-specifika funktioner inte skapar oavsiktlig privilegie- eller dataexponering.

## High-value review areas
- roles och memberships
- schema privileges
- `search_path`
- `PUBLIC` privileges
- `SECURITY DEFINER`
- Row Level Security
- dynamisk SQL
- extensions
- database ownership
- credentials
- TLS
- audit/logging
- backup/restore
- replication credentials

## Code patterns
Leta efter:
- dynamisk SQL i funktioner
- `EXECUTE` i PL/pgSQL
- `format()` med `%s` för identifiers/data utan korrekt quoting
- `SECURITY DEFINER`
- funktioner som förlitar sig på osäker `search_path`
- tenantfilter som bara finns i applikationskod
- användarstyrda identifiers

## Configuration patterns
Granska:
- role grants
- schema ownership
- `search_path`
- RLS policies
- extensioner
- connection config
- SSL mode
- backup scripts
- replication users
- migrations som ger breda privileges

## Common weaknesses
- runtimekonto är owner/superuser
- `SECURITY DEFINER` med osäker `search_path`
- schema eller funktioner är skrivbara av onödigt bred grupp
- RLS antas finnas men är inte aktiverad/tvingad där modellen kräver det
- dynamisk SQL saknar korrekt quoting/allowlist
- credentials i repo

## False-positive guards
Rapportera inte:
- `SECURITY DEFINER` som brist utan kontext
- `search_path` som risk om objektresolution är hårt kontrollerad
- avsaknad av RLS som brist om applikationen inte förlitar sig på RLS för säkerhetsgräns
- standardrollen `PUBLIC` som risk utan att visa relevant privilegium

## Evidence expectations
Fynd ska visa relevant role/grant, funktion, policy eller connection-konfiguration.

## Manual verification triggers
- RLS/policies skapas centralt
- produktionsroller skiljer sig från migrationsmiljön
- TLS policy styrs på server/proxy
- backup/replication ligger utanför projektet
