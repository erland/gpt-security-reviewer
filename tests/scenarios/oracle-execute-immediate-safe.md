# Scenario: Oracle statisk EXECUTE IMMEDIATE

## Input
`EXECUTE IMMEDIATE` används med helt statisk DDL utan extern input.

## Expected
Rapportera inte SQL injection enbart på grund av EXECUTE IMMEDIATE.
