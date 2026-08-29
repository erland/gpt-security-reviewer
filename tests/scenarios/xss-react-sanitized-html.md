# Scenario: React raw HTML efter verifierad sanering

## Class
negative

## Tags
react, xss, false-positive

## Input
Användartext saneras med en strikt allowlist-baserad sanitizer innan den skickas till `dangerouslySetInnerHTML`.

## Expected
Rapportera inte confirmed XSS. Om sanitizer-policy är tydligt verifierad ska inget XSS-fynd skapas.
