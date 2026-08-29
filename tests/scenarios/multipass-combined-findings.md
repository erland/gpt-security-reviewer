# Multiple risk families retained in same review

## Class
positive

## Tags
multipass, consistency, findings

## Input
Samma system innehåller både en möjlig current-authorization-brist vid privilegierade externa skrivoperationer och saknade resursbudgetar/timeouts i Git-/repositoryflöden.

## Expected
- Kandidatfyndspasset ska behålla båda riskfamiljerna tills de var för sig är avförda eller konsoliderade.
- Prioritering av ett fynd får inte undantränga det andra.
- Challenge pass ska särskilt pröva både stale authorization och resource exhaustion/timeouts.
- Slutrapporten ska kunna innehålla båda om evidensen stödjer dem.
