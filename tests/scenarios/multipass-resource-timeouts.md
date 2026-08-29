# Resource and timeout pass

## Class
positive

## Tags
availability, timeouts, resources, multipass

## Input
Backend gör Git-processer, HTTP-anrop och repositoryinventering. Det finns samtidigt stark authn/authz och filvalidering.

## Expected
- Kontrollmatrisen ska separat pröva resource consumption, timeouts, cancellation och concurrency.
- Starka kontroller i andra domäner får inte tolkas som att availability-ytan är granskad.
- Saknade explicita budgetar/deadlines ska kunna bli kandidatfynd med proportionerlig severity.
