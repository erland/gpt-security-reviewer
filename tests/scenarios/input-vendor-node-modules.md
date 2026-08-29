# Scenario: node_modules innehåller riskmönster

## Class
negative

## Tags
repository, vendor, false-positive

## Input
Ett React-projekt innehåller node_modules med tredjepartskod som använder innerHTML. Applikationens förstapartskod använder inte mönstret.

## Expected
Skapa inte application finding enbart från node_modules. Använd dependency manifests/SCA för tredjepartsrisker.
