# Java EE / Jakarta EE

## Applicability
Använd när backend använder Java EE, Jakarta EE eller närliggande Java-baserade webb/API-mönster med JAX-RS, CDI, EJB, Servlet, JPA eller motsvarande.

## Security objectives
Granskningen ska verifiera att säkerhetskritiska backendkontroller ligger på serversidan, att data access sker säkert och att framework-/containerfunktioner används på ett sätt som inte skapar injektions-, deserialiserings-, XML-, SSRF-, fil- eller behörighetsrisker.

## High-value review areas
- autentisering och identitetspropagering
- metod-, endpoint- och objektbehörighet
- annotations och interceptors
- JAX-RS-resurser
- Servlet/filter
- JPA/JPQL/native SQL
- dynamiska queries
- deserialisering
- JSON/XML parsing
- XXE
- SSRF och outbound HTTP
- filuppladdning och filåtkomst
- path traversal
- command/process execution
- template/expression-injektion
- felhantering och informationsläckage
- logging av känsliga data
- secrets och datasource credentials
- TLS-/endpointkonfiguration
- CORS när satt i backend
- admin/management endpoints

## Code patterns
Leta särskilt efter:
- `@RolesAllowed`, `@PermitAll`, `@DenyAll`
- security constraints i `web.xml`
- custom interceptors/filters för authorization
- `SecurityContext`, `Principal`, container identity
- JAX-RS resources utan synlig authz-kontroll
- `EntityManager.createQuery`, `createNativeQuery`
- strängkonkatenering i JPQL/SQL
- `Statement`, `PreparedStatement`
- dynamisk sortering/fältnamn från klient
- `ObjectInputStream`
- Java serialization
- polymorf JSON-deserialisering med bred typupplösning
- XML parsers/factories
- externa entities/DTD
- `URL`, `URI`, `HttpClient`, REST clients med användarkontrollerade mål
- `Files.*`, `Paths.*`, `File`
- uppladdade filnamn som används i filesystem paths
- `Runtime.exec`, `ProcessBuilder`
- reflection/expression engines när input kan påverka uttryck
- stack traces eller exceptiondetaljer till klient
- loggning av tokens, credentials eller känsliga payloads

## Configuration patterns
Granska när underlag finns:
- `web.xml`
- `persistence.xml`
- MicroProfile/Jakarta config
- datasource-inställningar
- JAX-RS/security-konfiguration
- CORS
- TLS
- session/cookie-inställningar
- container security realms
- secrets-referenser
- feature flags för säkerhetskritiska funktioner
- management/admin endpoints

Skilj alltid repo-konfiguration från container-, gateway- eller runtimekonfiguration som kan ligga externt.

## Authentication and identity reasoning
Autentisering kan implementeras i:
- applikationen,
- container/runtime,
- reverse proxy/gateway,
- extern IdP.

Frånvaro av auth-kod i resursklassen är därför inte i sig ett confirmed finding.

Identifiera i stället:
1. hur identity når applikationen,
2. var autenticiteten verifieras,
3. hur principal/claims används,
4. om tilliten bygger på externa komponenter som inte finns i underlaget.

## Authorization reasoning
Prioritera server-side authorization.

Vanliga signaler:
- `@PermitAll` på skyddsvärd funktion
- resurs utan metod-/klassnivåkontroll där global kontroll inte kan verifieras
- användar-ID/objekt-ID från klient används utan verifiering mot principal
- roller kontrolleras bara i frontend
- custom authorization används men täcker inte alla kodvägar

Objektbehörighet ska granskas separat från funktionsbehörighet.

## JPA / SQL reasoning
Säkra mönster:
- bind parameters för datavärden
- `PreparedStatement` med parametrar
- statiska JPQL queries med parametrisering

Riskmönster:
- strängkonkatenering av användarinput till query
- dynamiska native queries
- okontrollerade kolumn-/sorteringsnamn
- dynamiska fragments som inte kan parametriseras och saknar allowlist

Viktigt: parametrisering skyddar datavärden men inte automatiskt dynamiska identifiers eller query fragments.

## Deserialization reasoning
Flagga inte all JSON-deserialisering.

Risk ökar vid:
- Java native serialization av otillförlitlig data
- bred polymorf typupplösning
- godtycklig klassinstansiering
- osäkra custom deserializers
- trust av signerad/extern payload utan verifierad signatur

## XML / XXE reasoning
Granska parserkonfiguration när XML kommer från extern eller otillförlitlig källa.

Riskindikatorer:
- DTD/external entity support aktiv
- parser skapas utan tydlig hardening
- external schema/entity resolution tillåts

Rapportera inte XXE enbart för att XML används.

## SSRF reasoning
För SSRF krävs normalt:
1. attacker-kontrollerad eller otillförlitlig URL/host,
2. server-side request,
3. otillräcklig allowlist/validering/nätverksbegränsning.

Rapportera inte SSRF för statiska integrations-URL:er.

## File handling reasoning
Granska:
- path traversal
- filnamn från användare
- temporärfiler
- uppladdningsbegränsningar
- content type kontra faktisk filtyp
- lagringsplats
- åtkomstkontroll vid nedladdning
- zip-slip-liknande extraction

Ett användarfilnamn är inte automatiskt path traversal; verifiera hur path byggs och normaliseras.

## Common weaknesses
- endpoint saknar verifierbar server-side authorization
- BOLA/IDOR genom att objekt hämtas via klient-ID utan ownership/role check
- SQL/JPQL byggs med strängkonkatenering
- native Java deserialization av otillförlitlig data
- osäker XML parser med externa entities
- outbound request till användarkontrollerad URL
- path traversal vid upload/download
- command injection via `Runtime.exec`/`ProcessBuilder`
- exception stack traces läcker internt till klient
- känsliga tokens i logg
- secrets i config-filer

## False-positive guards
Rapportera inte:
- avsaknad av `@RolesAllowed` som confirmed authz-brist om global interceptor/filter/containerpolicy kan verifieras
- `PreparedStatement` med parametrar som SQL injection
- all `createQuery()`-användning som injektion
- all JSON mapping som osäker deserialisering
- all XML-användning som XXE
- alla outbound HTTP-anrop som SSRF
- alla filuppladdningar som path traversal
- `Runtime.exec` med helt statiskt kommando som command injection
- interna stack traces i serverlogg som klientinformationsläckage, så länge de inte exponeras till användare och loggen hanteras korrekt

## Evidence expectations
För authorization finding:
- skyddsvärd operation/data,
- relevant endpoint/metod,
- verifierbar avsaknad eller otillräcklighet av serverkontroll.

För injection:
- otillförlitlig input,
- query/command/expression sink,
- avsaknad av parameterisering/allowlist/escaping som är relevant för just sinken.

För SSRF:
- kontrollerbar destination,
- server-side request,
- otillräcklig destinationskontroll.

För XXE:
- extern XML,
- parserinställning som tillåter riskfylld entity/DTD-resolution eller oklar parserhärdning med stark indikator.

## Manual verification triggers
- authn/authz implementeras i container/gateway utanför repo
- custom interceptors med komplex ordning
- objektbehörighet bygger på domänlogik
- JPA filters/multitenancy som påverkar dataisolering
- parserhardening ligger i shared bibliotek utanför underlag
- outbound access begränsas av nätverkspolicy
- filskanning/antivirus sker i extern tjänst
- management endpoints exponeras via separat nätverkszon

## Defensive reporting note

Behåll rotorsak, evidens, severity/confidence, remediation och defensivt verifieringsmål. Abstrahera exploitpayloads, steg-för-steg-angrepp, bypass-recept och attackkedjor om de inte behövs för defensiv förståelse.
