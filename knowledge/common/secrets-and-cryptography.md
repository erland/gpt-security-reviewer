# Secrets and cryptography

## Applicability
Använd för credentials, API-nycklar, tokens, privata nycklar, kryptering, signering, hashing och annan kryptografisk säkerhetsfunktion.

## Security objectives
- hemligheter ska inte lagras i källkod eller distribueras till obehöriga klienter,
- nycklar/algoritmer ska användas för avsett syfte,
- egen kryptografisk design ska undvikas,
- skydd i vila och transport ska bedömas där underlag finns.

## High-value review areas
- hårdkodade secrets,
- frontend-exponerade credentials,
- secret injection/references,
- key management-indikationer,
- hashning av lösenord,
- signaturverifiering,
- TLS verification,
- svaga/deprecated algoritmer eller modes,
- deterministisk/återanvänd nonce/IV där relevant.

## Evidence indicators
En faktisk credential/private key i repo är normalt direkt evidens. En miljövariabelreferens är däremot inte bevis på vare sig säker eller osäker lagring.

## Common weaknesses
- committed secrets,
- secrets i loggar/felmeddelanden,
- disabled certificate validation,
- egenimplementerad kryptering,
- reversible lagring av lösenord,
- kryptografisk nyckel som delas med frontend.

## False-positive guards
- namn som `password` eller `secret` kan vara placeholders/testvärden,
- base64 är inte kryptering men är inte alltid en brist,
- frånvaro av nyckelmaterial i repo verifierar inte produktionshantering.

## Manual verification triggers
- extern secrets manager,
- HSM/KMS,
- certifikatrotation,
- produktions-TLS-policy,
- kryptografiska krav med hög skyddsnivå.
