# Teststrategi

## Mål
Testsviten ska balansera:
- recall: verkliga problem hittas,
- precision: säkra mönster felklassificeras inte,
- uncertainty handling: saknat underlag leder till not_verifiable,
- recommendation quality: fortsatt granskning blir proportionerlig.

## Atomära evals
`tests/scenarios/index.json` är canonical register över atomära scenarier.

Äldre samlingsfiler i `tests/scenarios/` är tillåtna som referensmaterial och behöver inte följa det atomära formatet.

## CI
CI verifierar:
- scenarioformat,
- unika scenario-ID:n,
- klassificering,
- förekomst av positiva, negativa, uncertainty och recommendation-scenarier,
- canonical projektvalidering,
- distributionsbygge.

## Senare modell-evals
Samma scenariofiler kan senare användas som faktisk modell-eval där genererad output jämförs med `Expected`.
