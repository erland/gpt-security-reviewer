# Scenario: PostgreSQL PUBLIC utan relevant grant

## Class
negative

## Tags
postgresql, false-positive

## Input
Databasen har standardrollen PUBLIC men inga CREATE/EXECUTE-privilegier på skyddsvärda scheman/funktioner.

## Expected
Rapportera inte PUBLIC som risk utan relevant privilege-evidens.
