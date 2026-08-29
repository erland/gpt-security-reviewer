# Architecture security

## Applicability
Används när arkitekturdokumentation, systembeskrivning, diagram, integrationsbeskrivningar eller kodstruktur ger underlag för att förstå systemets säkerhetsmodell.

## Security objectives
Identifiera var systemet litar på externa aktörer, komponenter, nätverk och identiteter. Bedöm om säkerhetskontroller ligger vid rätt trust boundaries och om dokumenterad arkitektur stämmer med implementationen.

## High-value review areas
- system boundaries
- trust boundaries
- externa aktörer
- identity boundaries
- administrativa gränssnitt
- integrationspunkter
- externa API:er
- känsliga dataflöden
- persistens
- asynkrona flöden
- privilegierade komponenter
- management/control plane
- internetexponering
- interna tjänster som felaktigt betraktas som betrodda
- säkerhetskritiska beroenden
- datareplikering och sekundärlagring
- fail-open/fail-closed beteenden

## Architecture reasoning
För varje viktig data- eller kontrollkedja bör GPT:n försöka identifiera källa/aktör, trust boundary, mottagande komponent, autentisering, auktorisering, datakänslighet, transportskydd, persistens, vidare spridning och administrativ kontrollpunkt.

## Documentation versus implementation
När både dokumentation och kod finns ska GPT:n jämföra dokumenterad kontroll med implementerad kontroll och rapportera säkerhetsrelevanta avvikelser.

## Common weaknesses
- trust boundary saknar tydlig autentisering eller validering
- intern tjänst litar på spoofbar header/identitet
- administrativt gränssnitt delar samma exponeringsyta som vanlig användartrafik
- känslig data skickas till sekundär tjänst utan motsvarande skydd
- säkerhetskritisk kontroll finns endast i diagram men saknas i implementation
- implicit nätverkstillit används där stark identitet krävs
- extern integration har bredare dataåtkomst än funktionellt nödvändigt
- fail-open vid otillgänglig auth/policytjänst

## False-positive guards
Rapportera inte varje integrationspunkt som risk, varje intern tjänst som osäker eller frånvaro av detalj i ett hög-nivådiagram som bevis på avsaknad i implementation.

## Evidence expectations
Arkitekturfynd ska kopplas till diagram, dokumentsektion, kodstruktur eller verifierbar konfiguration. Om en kontroll sannolikt ligger utanför underlaget ska detta markeras som `not_verifiable` eller `review-point`.

## Manual verification triggers
- IAM-policyer ligger i extern plattform
- nätverkssegmentering kan inte verifieras
- gateway/service mesh hanterar identity eller policy
- administrativa vägar är separat driftkonfigurerade
- dokumentation är äldre än implementationen
