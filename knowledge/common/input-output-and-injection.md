# Input, output and injection

## Applicability
Använd där data passerar trust boundaries eller används i interpreters, queries, templates, HTML, kommandon, sökfrågor, filvägar eller externa anrop.

## Security objectives
- skilj validering från kontextuell escaping/encoding,
- använd parametriserade eller typade API:er,
- undvik att bygga exekverbara uttryck med ostrukturerad input,
- validera på betrodd sida.

## High-value sinks
- SQL/JPQL/native queries,
- Elasticsearch query construction,
- HTML/DOM/template rendering,
- shell/process invocation,
- XPath/XML parsers,
- expression languages,
- file paths/archive extraction,
- URL/host targets för server-side requests.

## Evidence indicators
För ett injektionsfynd bör dataflödet från attacker-kontrollerad källa till farlig sink vara synligt och relevanta neutraliseringskontroller saknas eller vara otillräckliga.

## Common weaknesses
- strängkonkatenerad query,
- osäker HTML-rendering,
- path traversal,
- SSRF via okontrollerad URL,
- command injection,
- osäker XML-parserkonfiguration.

## False-positive guards
- användning av en farlig API-funktion utan attacker-kontrollerad input är inte i sig exploaterbarhet,
- validering av format kan reducera risk men ersätter inte alltid parametrisering/encoding,
- parametriserad query ska normalt inte rapporteras som SQL-injektion.

## Manual verification triggers
- dataflow är utspritt över flera moduler,
- sanitizer/validator är egenutvecklad,
- runtime-template/query engine-konfiguration saknas.
