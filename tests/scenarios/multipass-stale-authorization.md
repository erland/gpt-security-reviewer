# Current authorization survives risk prioritization

## Class
positive

## Tags
authorization, github, multipass, challenge

## Input
Ett system sparar en tidigare verifierad repositorykoppling och använder senare en privilegierad App-/serviceidentitet för användarinitierade skrivoperationer. Samma granskning innehåller även flera tydliga availability-risker som lätt kan dominera analysen.

## Expected
- Current/stale authorization ska prövas separat i kontrollmatris/challenge pass.
- Ett availability-fynd får inte göra att repository-auktorisering implicit hoppas över.
- Om aktuell användarbehörighet inte återverifieras före privilegierad sidoeffekt ska det kunna bli eget kandidatfynd.
- Om underlaget inte räcker ska området explicit bli review-point/not_verifiable, inte försvinna.
