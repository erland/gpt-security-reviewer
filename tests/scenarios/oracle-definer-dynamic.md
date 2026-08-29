# Scenario: Oracle AUTHID DEFINER + dynamisk SQL

## Input
En privilegierad package med definer rights bygger SQL från användarstyrt objektnamn utan allowlist.

## Expected
Högprioriterat privilege/injection finding.
