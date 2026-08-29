# Web frontend

## Applicability
Använd för webbaserade klienter oavsett om de är byggda med React, Angular eller annan modern frontendteknik.

## Security objectives
Frontend får aldrig betraktas som en säkerhetsgräns för auktorisering. Klientkod ska hantera data, DOM, autentiseringsartefakter och externa resurser på ett sätt som minimerar XSS, informationsläckage och tokenmissbruk.

## High-value review areas
- XSS och DOM-baserad XSS
- osäker HTML-injektion
- URL- och redirect-hantering
- token- och sessionslagring
- exponering av secrets eller känslig konfiguration
- klientbaserade behörighetskontroller
- CSP
- CORS-antaganden
- tredjepartsskript
- frontendloggning
- känsliga data i browser storage
- postMessage och cross-window-kommunikation

## Code patterns
Leta särskilt efter explicit HTML-injektion, `innerHTML`, `outerHTML`, `insertAdjacentHTML`, dynamiska URL:er, redirects, browser storage för tokens, `postMessage` utan origin-kontroll och klientkod som avgör åtkomst utan motsvarande serverkontroll.

## Configuration patterns
Granska när underlag finns CSP, CORS, cookie-flaggor, runtime-config, exponerade miljövariabler, source maps, tredjepartsdomäner, security headers och build-time secrets.

## Common weaknesses
- HTML från användare renderas utan tillräcklig sanering
- tokens lagras på sätt som förstärker konsekvensen av XSS
- frontend guards används som enda auktorisering
- känslig konfiguration byggs in i klientpaketet
- CSP är mycket tillåtande
- `postMessage` accepterar godtyckligt origin
- open redirects

## False-positive guards
Rapportera inte automatiskt all `localStorage`-användning som kritisk, alla klientguards som brist när backendkontroll finns, all dynamisk HTML som XSS när säker sanering kan verifieras eller publika frontendvärden som secrets utan autentiserande värde.

## Evidence expectations
Ett konkret fynd ska visa en kontrollerbar eller otillförlitlig källa, relevant sink eller säkerhetskritisk användning och avsaknad eller otillräcklighet av skydd när detta kan verifieras.

## Manual verification triggers
Extern IdP, reverse proxy/gateway som sätter headers, saknad backend för verifiering, tredjepartsskript med hög dataåtkomst och komplex cross-origin-kommunikation.
