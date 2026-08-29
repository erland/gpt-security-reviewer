# Review framework

## Syfte

Ramverket ska ge konsekventa säkerhetsbedömningar utan falsk precision. Varje slutsats ska separera:

1. vad som observerats,
2. hur väl observationen är belagd,
3. hur allvarlig konsekvensen kan vara,
4. vad som fortfarande behöver verifieras.

## Granskningsdomäner

Minst följande domäner ska övervägas när de är relevanta:

- autentisering
- auktorisering
- objektbehörighet
- sessionshantering
- inputvalidering
- output encoding
- injektion
- secrets
- kryptografi
- felhantering
- loggning och säkerhetsrelevant spårbarhet
- känslig information och dataminimering
- API-säkerhet
- externa integrationer
- datalager
- dependency/supply chain
- deployment och runtime-konfiguration
- arkitektur, trust boundaries och privilegiegränser

Domäner som inte är relevanta ska inte mekaniskt rapporteras som checklistpunkter.

## Fyndstatus

### confirmed

Använd endast när den säkerhetsrelevanta egenskapen kan beläggas direkt i tillgängligt material och ingen rimlig saknad kontroll i samma flöde sannolikt förändrar slutsatsen.

Typiska exempel:

- hemlighet finns direkt i repo,
- dynamisk SQL byggs från okontrollerad input utan parametrisering,
- en säkerhetskritisk endpoint saknar synlig accesskontroll och hela relevanta kontrollkedjan finns i underlaget.

### probable

Använd när evidensen starkt pekar på en brist men en relevant del av kontrollkedjan saknas eller kan ligga utanför det material som granskats.

Exempel:

- endpoint saknar lokal accesskontroll men gateway-/interceptor-konfiguration saknas,
- osäker standardkonfiguration är synlig men runtime override kan finnas.

### review-point

Använd när något behöver verifieras men materialet inte räcker för att påstå att en brist finns.

Review-point ska inte räknas eller kommuniceras som en verifierad sårbarhet.

## Severity

Severity beskriver möjlig säkerhetskonsekvens om fyndet är verkligt.

### critical

Använd restriktivt. Normalt krävs realistisk möjlighet till exempelvis:

- omfattande obehörig administrativ kontroll,
- storskalig exponering eller manipulation av mycket känslig information,
- fjärrkörning av kod eller motsvarande systemövertagande,
- säkerhetskontroll som helt kan kringgås med mycket stor påverkan.

### high

Betydande påverkan, exempelvis:

- obehörig åtkomst till känsliga data eller centrala funktioner,
- privilegieeskalering,
- exploaterbar injektion med betydande konsekvens,
- allvarlig brist i objekt- eller funktionsbehörighet.

### medium

Reell säkerhetsrisk med mer begränsad påverkan, högre exploateringskrav eller mindre exponering.

### low

Begränsad säkerhetspåverkan, defense-in-depth-brist eller problem som normalt kräver flera andra förutsättningar.

### informational

Relevant säkerhetsobservation utan identifierad exploaterbar brist.

## Faktorer för severity

Väg minst in när informationen finns:

- impact: confidentiality, integrity, availability och accountability,
- data sensitivity,
- affected scope,
- required privileges,
- user interaction,
- exposure/reachability,
- exploit complexity,
- möjlighet till kedjning med andra fynd.

Använd inte numeriska poäng om underlaget inte motiverar dem.

## Confidence

Confidence beskriver hur säker bedömningen är, inte hur allvarligt fyndet är.

### high

- direkt evidens,
- relevant kontrollkedja är tillgänglig,
- få eller inga rimliga alternativa förklaringar.

### medium

- tydlig evidens,
- men någon relevant komponent, runtime-inställning eller indirekt kontroll saknas.

### low

- svag eller indirekt indikator,
- stora delar av nödvändig kontext saknas,
- flera alternativa förklaringar är rimliga.

## Evidenskrav

Ett konkret fynd ska så långt möjligt ange:

- källa: fil, dokument eller konfiguration,
- komponent,
- rad, funktion, endpoint eller sektion när möjligt,
- observerat beteende eller konfiguration,
- säkerhetsrelevant data-/kontrollflöde,
- vilka delar av slutsatsen som är infererade.

Föredra flera korta evidenspunkter framför en lång generell beskrivning.

## Negativ evidens

Avsaknad av ett mönster är normalt inte bevis för att kontrollen saknas.

Exempel:

- ingen annotation betyder inte automatiskt att endpoint saknar behörighetskontroll,
- ingen secret i repo betyder inte att secret-hanteringen är korrekt,
- parameteriserade queries i ett stickprov betyder inte att alla queries är säkra.

## Fyndkonsolidering

Observationer ska slås ihop när de beskriver samma rotorsak eller samma exploaterbara kedja.

Konsolidera exempelvis:

- klientstyrt objekt-ID,
- backend som läser objektet,
- saknad objektbehörighetskontroll,

som ett sammanhållet BOLA/IDOR-fynd om evidensen stödjer kedjan.

Behåll separata fynd när:

- rotorsakerna skiljer sig,
- åtgärderna skiljer sig väsentligt,
- olika komponenter har självständiga risker,
- sammanslagning skulle dölja olika severity eller ägarskap.

## Dubblettregel

Samma rotorsak ska inte rapporteras flera gånger enbart för att den förekommer på många endpoints eller filer. Rapportera ett huvudfynd och lista representativa eller berörda förekomster.

## Coverage

För varje relevant område använd en av:

### reviewed

Tillräckligt relevant material har granskats för att göra en meningsfull bedömning.

### not_reviewed

Området ligger utanför uppdraget eller valdes bort.

### not_verifiable

Området är relevant men nödvändigt material eller runtime-information saknas.

Coverage ska bedömas per relevant säkerhetsområde, inte bara per filtyp.

## Overall assessment

Övergripande bedömning ska väga samman:

- högsta relevanta severity,
- confidence för de viktigaste fynden,
- systemets säkerhetskritikalitet när känd,
- coverage och granskningsluckor,
- förekomst av systematiska brister,
- kvarvarande risk.

En granskning med få fynd men stora `not_verifiable`-områden får inte beskrivas som starkt säker.

## Referensmappning

OWASP ASVS, OWASP Top 10, OWASP API Security och CWE får användas för struktur och klassificering när mappningen är rimlig. Mappningen ska inte ersätta den konkreta tekniska förklaringen.

## Defensive finding expression

Analysen får vara tekniskt precis. Presentationen ska vara defensiv. Ett fynd ska normalt kunna förstås och åtgärdas utan payload, PoC, exakt exploateringssekvens, instruktion för att kringgå kontroll eller kedjning till större angrepp. Abstrahera vid behov till kontrollbrist -> säkerhetskonsekvens -> remediation -> verifieringsmål.
