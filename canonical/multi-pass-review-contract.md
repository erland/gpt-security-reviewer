# Multi-pass review contract

## Syfte

Standard och Deep ska inte genomföras som ett enda fritt analysvarv. Granskningen ska använda flera separata interna pass så att viktiga kontrollfamiljer och trust boundaries inte trängs undan av de fynd som råkar upptäckas först.

Användaren behöver normalt inte skriva `fortsätt` mellan passen. Passen är en intern arbetsordning och kan levereras som en sammanhållen rapport.

## Pass 1 - inventering och säkerhetsmodell

Identifiera:

- förstapartskomponenter och teknikprofiler,
- deploymentenheter,
- aktörer och externa system,
- trust boundaries,
- säkerhetsrelevanta data- och kontrollflöden,
- administrativa och privilegierade sidoeffekter,
- material som saknas eller inte är verifierbart.

Resultatet ska styra nästa pass; det är inte bara rapporttext.

## Pass 2 - obligatorisk kontrollmatris

För varje relevant kontrollfamilj och identifierad säkerhetsrelevant yta sätt exakt en intern status:

- `reviewed` - tillräckligt material har analyserats,
- `not_reviewed` - relevant men medvetet bortvald inom scope/budget,
- `not_verifiable` - relevant men underlag/runtime saknas,
- `not_applicable` - kontrollfamiljen är inte relevant för det observerade systemet.

Minst följande kontrollfamiljer ska aktivt bedömas för relevans:

- authentication/session,
- authorization/object ownership/current authorization,
- input/archive/path handling,
- injection/output/browser sinks,
- secrets/cryptography,
- external HTTP/API integrations,
- local process/Git/file-system operations,
- data stores,
- resource consumption/timeouts/concurrency,
- error handling/logging/audit,
- dependency/supply chain,
- deployment/runtime/network exposure,
- architecture/trust boundaries/privilege boundaries.

`not_applicable` ska inte fyllas mekaniskt i slutrapporten. Det är ett internt kvitto på att relevansfrågan faktiskt har prövats.

## Pass 3 - riskdriven fördjupning

Fördjupa de flöden där konsekvens, privilegier, extern exponering eller osäkerhet är störst. Standard använder riktade stickprov; Deep följer fler kedjor genom flera lager.

Fynd i detta pass får inte göra att övriga relevanta rader i kontrollmatrisen lämnas obehandlade.

## Pass 4 - kandidatfynd

Samla alla rimligt underbyggda kandidatfynd innan prioritering. Kandidater kan senare:

- bli `confirmed`, `probable` eller `review-point`,
- slås ihop med samma rotorsak,
- avföras efter motbevisande evidens,
- omklassificeras till coverage-gap.

Prioritera inte bort ett kandidatfynd bara för att ett allvarligare fynd redan finns.

## Pass 5 - challenge pass

Gör ett separat motgranskningspass innan fyndbilden låses. Kontrollera uttryckligen:

- stale/current authorization vid privilegierade externa sidoeffekter,
- privilegie- och trust-boundary mismatch,
- resource exhaustion, timeouts, cancellation och concurrency,
- osäkra default-/deploymentantaganden,
- klientdistribuerade credentials/capabilities,
- filsystem-, process- och repositorygränser,
- missade authn/authz-kontroller mellan lager,
- supply-chain och immutable release identity,
- om positiva kontroller verkligen täcker hela relevanta kedjan.

Challenge-passet ska försöka falsifiera både fynd och antagandet att en yta är säker.

## Pass 6 - coverage gate

En komplett Standard/Deep-rapport får inte slutföras förrän:

1. varje identifierad säkerhetsrelevant trust boundary/flöde har en granskningsstatus,
2. varje relevant kontrollfamilj har en status i kontrollmatrisen,
3. viktiga `not_reviewed` och `not_verifiable` är representerade i coverage eller fortsatt granskning,
4. varje kandidatfynd har konsoliderats, avförts med skäl eller blivit review-point,
5. challenge-passet är genomfört.

Om analysbudgeten inte räcker ska rapporten hellre markera `not_reviewed` än att implicit utelämna området.

## Pass 7 - konsolidering och defensiv rapportering

Först efter coverage gate:

- konsolidera dubbletter,
- bedöm severity och confidence separat,
- prioritera åtgärder,
- formulera defensiva fynd,
- generera rapporten.

## Reproducerbarhet

Målet är inte identisk ordalydelse mellan körningar. Målet är att samma relevanta kontrollfamiljer och säkerhetsgränser alltid prövas, så att viktiga fynd inte försvinner enbart därför att analysen råkade börja i ett annat område.
