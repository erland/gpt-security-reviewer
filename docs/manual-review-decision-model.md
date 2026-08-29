# Beslutsmodell för fortsatt säkerhetsgranskning

## Syfte

Modellen styr när GPT:n ska rekommendera ytterligare mänsklig eller verktygsbaserad granskning.

## Beslutsordning

1. Finns ett viktigt säkerhetsområde som inte kan verifieras?
2. Kan osäkerheten reduceras med ett enkelt stickprov?
3. Krävs semantisk mänsklig förståelse?
4. Krävs bred automatisk kod-/dependency-täckning?
5. Krävs runtimeverifiering?
6. Motiverar systemets exponering/skyddsvärde ett oberoende penetrationstest?
7. Krävs specialistkompetens utanför GPT:ns kärnscope?

## Proportionalitetsprincip

Välj den minst omfattande aktivitet som ger tillräcklig riskreduktion.

Exempel:

- oklar accesskontroll på två kritiska endpoints → manuell granskning/spot-check före full penetrationstest,
- stor dependency-yta utan aktuell status → SCA,
- okänd runtime-gatewaypolicy → configuration-review,
- internetexponerad applikation med komplex auth och höga skyddsvärden → penetration-test kan vara motiverat.
