# Elasticsearch

## Applicability
Använd när systemet använder Elasticsearch för sök, indexering, analys eller lagring.

## Security objectives
Verifiera att index och API:er inte exponeras bredare än avsett, att autentisering/auktorisering är tydlig, att känslig data hanteras proportionerligt och att query-/snapshot-/clusterfunktioner inte introducerar onödig risk.

## High-value review areas
- nätverks- och API-exponering
- autentisering
- index-/document-level authorization
- roller och index privileges
- känslig indexerad data
- query construction
- scripts
- dynamic templates/mappings när säkerhetsrelevant
- snapshots
- remote clusters
- ingest pipelines
- credentials/API keys
- TLS
- audit logging
- admin/cluster privileges

## Code patterns
Leta efter:
- användarkontrollerad query DSL
- `query_string`/lucene query syntax från klient
- raw JSON query bodies
- scripts eller scripted fields
- generiska indexnamn från klient
- wildcard-index
- klientcredentials i repo
- administrativa klientanrop från vanlig applikationskod

## Configuration patterns
Granska när det finns:
- roles
- role mappings
- users/API keys
- index privileges
- document/field level security
- TLS
- cluster/network bindings
- snapshots/repositories
- remote clusters
- audit
- anonymous access
- Kibana/service integration

## Common weaknesses
- klient kan påverka query syntax på sätt som kringgår avsedda filter
- applikationen använder breda `all`/cluster privileges
- wildcard-index ger åtkomst till mer data än avsett
- känslig data indexeras utan behov eller tillräckligt skydd
- snapshot repository exponerar skyddsvärd data
- Elasticsearch är åtkomligt utan tillräcklig authn/authz
- API keys eller credentials ligger i repo
- adminfunktioner exponeras via applikationens runtimekonto

## Query reasoning
Elasticsearch query injection skiljer sig från SQL injection.

Risk uppstår när användaren kan påverka query-struktur eller query syntax på ett sätt som:
- kringgår avsedda filter,
- får åtkomst till andra fält/index,
- skapar oönskad script-exekvering,
- orsakar kostsam eller farlig query.

Att användartext skickas som ett värde i en strukturerad match-query är inte automatiskt injection.

## Sensitive data reasoning
Index är ofta sekundära kopior av data. Bedöm därför:
- om känslig data behöver indexeras,
- om fler fält indexeras än nödvändigt,
- om dokument-/fältbehörighet finns,
- om retention och snapshots matchar primärdatans skyddsnivå.

## False-positive guards
Rapportera inte:
- all user search text som query injection
- användning av wildcard i legitim intern adminfunktion som brist utan accesskontext
- avsaknad av security-config i app-repot som bevis på osäker clusterkonfiguration
- Elasticsearch som osäker enbart för att den används som sekundär lagring

## Evidence expectations
För accessfynd: visa faktisk roll/API key/config eller verifierbar oskyddad endpoint.
För queryfynd: visa att användaren kan påverka query-struktur/syntax och vilken kontroll som saknas.
För datafynd: visa att skyddsvärd data faktiskt indexeras.

## Manual verification triggers
- cluster security ligger i separat driftrepo
- index-/document-level security styrs centralt
- nätverksexponering ligger bakom service mesh/gateway
- snapshots hanteras av plattformsteam
- remote-cluster trust ligger utanför underlaget
