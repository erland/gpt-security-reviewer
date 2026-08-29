# Scenario: dynamisk sorteringskolumn

## Input
Klientens `sort` konkateneras direkt till `ORDER BY` i native SQL.

## Expected
Injection/control finding om ingen allowlist eller säker mapping finns. Parameterbindning av datavärden löser inte identifier-problemet.
