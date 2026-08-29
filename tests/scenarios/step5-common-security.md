# Step 5 – common security scenarios

## S5-01 Client-side authorization only
React döljer adminfunktion men backend-endpoint saknar synlig kontroll och hela backendflödet finns.
Förväntning: auktoriseringsfynd; frontend guard räknas inte som backendkontroll.

## S5-02 Authorization may be external
Endpoint saknar annotation men runtime anger att extern gateway används; gatewaypolicy saknas.
Förväntning: inte confirmed enbart på frånvaro av annotation; probable/review-point eller not_verifiable beroende på övrig evidens.

## S5-03 Parameterized query
Attackerstyrd input skickas genom parameteriserad query.
Förväntning: inget SQL-injektionsfynd på denna evidens.

## S5-04 Hard-coded real secret
Produktionslik API-nyckel finns i repo och används i runtimekod.
Förväntning: confirmed secret exposure med hög confidence; secrets-scan kan rekommenderas för bredare coverage.

## S5-05 Environment secret reference
Konfiguration använder env-var/secret reference, inget secretvärde finns.
Förväntning: inte ett fynd i sig; runtime secret storage kan vara not_verifiable.

## S5-06 Token parsed without full validation
Backend läser claims ur JWT men evidens visar ingen signatur/issuer/audience-verifiering i komplett kontrollkedja.
Förväntning: autentiseringsfynd proportionerligt till exponering och användning.

## S5-07 Current CVE unknown
Package-version syns men ingen aktuell sårbarhetsdatakälla finns.
Förväntning: GPT:n får inte påstå aktuell CVE; rekommendera SCA när relevant.

## S5-08 Sensitive data in logs
Access token eller tydligt känsligt data loggas i vanlig applikationslogg.
Förväntning: konkret logging/data-exposure-fynd.

## S5-09 Rate limit external
API är internetexponerat men rate limiting hanteras enligt arkitektur av gateway; gatewaykonfiguration saknas.
Förväntning: not_verifiable och eventuell configuration-review/DAST, inte automatiskt brist.

## S5-10 Business authorization complexity
Objektåtkomst styrs av flera roller, tenant och delegation över flera tjänster.
Förväntning: manuell granskning kan rekommenderas även om inget confirmed-fynd finns, eftersom kontrollkedjan är komplex.
