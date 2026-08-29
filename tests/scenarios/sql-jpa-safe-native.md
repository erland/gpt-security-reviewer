# Scenario: Native SQL med bind parameters

## Class
negative

## Tags
java, sql, false-positive

## Input
Native SQL använder statisk query och bind parameter för samtliga datavärden. Inga dynamiska identifiers eller fragments används.

## Expected
Rapportera inte SQL injection.
