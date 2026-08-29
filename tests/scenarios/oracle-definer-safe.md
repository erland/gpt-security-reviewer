# Scenario: Oracle definer rights med säkert API

## Class
negative

## Tags
oracle, false-positive

## Input
Package använder `AUTHID DEFINER`, statiska SQL-satser och strikt parametrisering. EXECUTE är endast grantad till applikationsrollen.

## Expected
Rapportera inte privilege escalation enbart på grund av AUTHID DEFINER.
