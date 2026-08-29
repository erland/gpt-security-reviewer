# Scenario: dokumenterad kontroll saknas i implementation

## Input
Arkitekturdokumentet säger att alla admin-API:er kräver separat adminroll. Koden visar `@PermitAll` på ett admin-endpoint och ingen global kontroll täcker det.

## Expected
Säkerhetsfynd med både dokumentations- och kodevidens. Avvikelsen stärker confidence.
