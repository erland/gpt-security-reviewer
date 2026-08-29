# Scenario: Access token loggas

## Class
positive

## Tags
logging, token, positive

## Input
HTTP-filter skriver hela `Authorization`-headern till applikationsloggen vid debug.

## Expected
Skapa confirmed sensitive logging finding. Rekommendera borttagning/redaction och bedöm behov av tokenrotation/loggrensning.
