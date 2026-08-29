# React

## Applicability
Använd när frontend använder React eller React-baserat ramverk.

## Security objectives
React:s normala rendering ska bevara escaping. Fokusera på avsteg från modellen, autentiserings-/behörighetsantaganden och riskfylld browser-API-användning.

## High-value review areas
- `dangerouslySetInnerHTML`
- osäker DOM-manipulation utanför React
- länkar, redirects och URL-konstruktion
- tokenlagring
- klientbaserad authorization
- runtime/build-konfiguration
- tredjepartsbibliotek som renderar HTML/Markdown
- SSR/CSR-gränser när relevant
- hydration-data med känslig information

## Code patterns
Leta efter `dangerouslySetInnerHTML`, `ref.current.innerHTML`, `document.write`, `innerHTML`, `outerHTML`, `insertAdjacentHTML`, Markdown/WYSIWYG med rå HTML, dynamiska `href/src/iframe/window.open`, browser storage för tokens, UI-baserad rollkontroll och potentiella credentials i build/runtime config.

## Configuration patterns
Granska React-buildens miljövariabler och runtime-config, source maps, CSP/security headers när de finns, auth-relaterade cookieinställningar, externa scriptdomäner och SSR-konfiguration när ramverket använder serverrendering.

## Common weaknesses
- rå HTML via `dangerouslySetInnerHTML`
- tredjeparts-HTML renderer utan verifierbar sanering
- access token i persistent browser storage utan motiverad hotmodell
- UI-baserad rollkontroll utan backend enforcement
- privata nycklar/API-secrets i frontend config
- open redirect
- osäker `postMessage`

## False-positive guards
Vanlig JSX-interpolation som `<div>{userInput}</div>` ska inte rapporteras som XSS enbart för att input är användarkontrollerad. Rapportera inte route guards som sårbarhet när backend auktoriserar relevanta endpoints, publika API-base-URL:er/client IDs som secrets eller `dangerouslySetInnerHTML` som confirmed XSS när innehållet är statiskt eller robust sanerat.

## Evidence expectations
För XSS-fynd bör evidensen normalt visa otillförlitlig input, riskfylld sink och ingen verifierad säker sanering/encoding. För authz-fynd ska skyddsvärd funktion/data, klientkontroll och avsaknad av verifierbar serverkontroll framgå.

## Manual verification triggers
Saneringsbibliotek med oklar policy, Next.js/SSR-auth, extern gateway, tokenrotation/sessionrevocation som inte framgår samt komplex hydration/server-client dataöverföring.
