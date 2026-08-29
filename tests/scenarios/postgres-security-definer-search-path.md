# Scenario: PostgreSQL SECURITY DEFINER

## Input
En SECURITY DEFINER-funktion använder okvalificerade objektnamn och osäker search_path där mindre betrodd roll kan skapa objekt.

## Expected
Privilege escalation finding eller probable finding beroende på grants.
