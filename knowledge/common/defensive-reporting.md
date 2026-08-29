# Defensive security reporting

## Objective
Rapportera säkerhetsbrister så att ett försvarsteam kan förstå, prioritera och åtgärda dem utan att rapporten samtidigt blir en praktisk exploateringsmanual.

## Preserve detail
Behåll relevant kod-/konfigurationsplats, rotorsak, saknad/felaktig kontroll, severity, confidence, status, säkerhetskonsekvens, remediation och defensiva testmål.

## Reduce detail
Abstrahera attacker-controlled parameter sequences, payload syntax, exploit chains, bypass recipes, credential/token replay procedures, scanning/enumeration procedures och data-exfiltration steps.

## Examples
### Authorization
Rapportera: "Backend saknar verifierbar objektnivåauktorisering. Kan medföra obehörig åtkomst till andra användares data."
Undvik instruktioner om exakt parameter-/ID-manipulation.

### Injection
Rapportera: "Extern input når en dynamiskt konstruerad querydel utan verifierbar bindning eller allowlist. Detta kan påverka queryns avsedda struktur."
Undvik konkret payload.

### SSRF
Rapportera: "Användarkontrollerad destination kan påverka serverns utgående HTTP-anrop utan verifierbar destinationsbegränsning."
Undvik konkreta interna mål.

### Path traversal
Rapportera: "Extern filidentifierare används i sökvägskonstruktion utan verifierbar begränsning till avsedd katalog."
Undvik konkreta traversalsträngar/systemfiler.

## Remediation
Remediation får vara mer detaljerad än problembeskrivningen: central authz-kontroll, parameter binding/allowlists, URL-allowlist och nätverksrestriktion, canonical path validation, säkra parserinställningar, least privilege och säkrare secrets-hantering.

## Verification
Föreslå negativa testfall och kontrollmål, men formulera dem som defensiv verifiering snarare än ett recept för verklig exploatering.
