# Scenario: Normal identifierare i logg

## Class
negative

## Tags
logging, false-positive

## Input
Applikationen loggar internt användar-ID och request-ID för felsökning men inga tokens, passwords eller payloads.

## Expected
Rapportera inte känslig loggning enbart på denna grund.
