# Scenario: React dangerouslySetInnerHTML

## Input
Serverdata från användargenererad profiltext förs direkt till `dangerouslySetInnerHTML` utan synlig sanering.

## Expected
XSS-fynd, normalt probable eller confirmed beroende på datakällans verifierbarhet.
