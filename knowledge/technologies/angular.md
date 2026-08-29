# Angular

## Applicability
Använd när frontend använder Angular.

## Security objectives
Angular sanerar/escapar många template-bindningar. Fokusera på bypass av ramverkets säkerhetsmodell, direkt DOM-användning och klient/server-auktorisering.

## High-value review areas
- `DomSanitizer`
- `bypassSecurityTrustHtml`
- `bypassSecurityTrustScript`
- `bypassSecurityTrustStyle`
- `bypassSecurityTrustUrl`
- `bypassSecurityTrustResourceUrl`
- direkt DOM-manipulation
- `[innerHTML]`
- route guards
- HTTP interceptors och tokenhantering
- browser storage
- dynamiska URL:er
- runtime environment/config
- tredjepartswidgets

## Code patterns
Leta efter alla `bypassSecurityTrust*`, `ElementRef.nativeElement`, direkt `innerHTML`, `document/window`, manuella DOM-API:er, `[innerHTML]`, route guards som enda synliga kontroll, tokeninjektion i interceptors, browser storage, credentials i environment/runtime-config och dynamiska redirects.

## Configuration patterns
Granska `environment*.ts`, runtime-config, auth-relaterade interceptor-/providerinställningar, CSP/security headers när de finns, source maps och externa resursdomäner. Skilj build-time config från verklig runtimepolicy.

## Common weaknesses
- osäker användning av `bypassSecurityTrust*`
- direkt DOM-manipulation med otillförlitlig data
- route guards som enda authorization
- tokenlagring som förvärrar XSS-konsekvens
- hemligheter i frontend environment
- dynamiska resource URLs utan tillräcklig kontroll
- open redirects

## False-positive guards
Normal Angular interpolation ska inte flaggas som XSS. `[innerHTML]` ska inte kallas confirmed XSS om Angular:s sanering är aktiv och ingen bypass sker. Route guards är inte en brist om backendkontroll verifieras. Alla värden i `environment.ts` är inte secrets.

## Evidence expectations
För bypass-relaterat fynd: identifiera bypass-anropet, spåra datakällan, avgör om data kan påverkas av användare/extern källa och kontrollera om separat sanering finns.

## Manual verification triggers
Custom sanitizer, komplexa `SafeHtml/SafeUrl`-flöden, auth via gateway/IdP, server-side rendering och dynamiska microfrontends.
