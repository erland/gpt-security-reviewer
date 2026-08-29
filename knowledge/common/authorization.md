# Authorization

## Applicability
Använd för alla funktioner och data där åtkomst beror på identitet, roll, ägarskap, attribut eller systemprivilegium.

## Security objectives
- kontroll ska ske på server-/trust-boundary-sidan,
- funktions- och objektbehörighet ska båda beaktas,
- default-deny ska eftersträvas för privilegierade resurser,
- behörighet ska tillämpas konsekvent genom alternativa vägar.

## High-value review areas
- endpoint/function authorization,
- object-level authorization (BOLA/IDOR),
- tenant-/organisationsisolering,
- administrativa funktioner,
- batch/export/search-funktioner,
- indirekta åtkomstvägar,
- servicekontons privilegier,
- policy/role mapping.

## Evidence indicators
Följ ett konkret flöde från inkommande identitet och resursidentifierare till faktisk kontroll innan data/funktion används.

## Common weaknesses
- kontroll endast i frontend,
- rollkontroll utan objektscope,
- klientstyrd tenant/user-id används direkt,
- admin-endpoint skyddas svagare än motsvarande UI,
- samma resurs nås via en alternativ endpoint utan kontroll,
- overly broad service account.

## False-positive guards
- saknad annotation är inte automatiskt saknad kontroll,
- kontroll kan ligga i interceptor/filter/service/policy engine,
- en frontend-guard ska inte räknas som backendkontroll men kan vara en ledtråd till förväntad policy.

## Manual verification triggers
- dynamiska policyer,
- ABAC/RBAC-konfiguration utanför repo,
- komplex ärvd rollmodell,
- flera tjänster delar ansvar för beslutet.

## Defensive reporting note

Behåll rotorsak, evidens, severity/confidence, remediation och defensivt verifieringsmål. Abstrahera exploitpayloads, steg-för-steg-angrepp, bypass-recept och attackkedjor om de inte behövs för defensiv förståelse.
