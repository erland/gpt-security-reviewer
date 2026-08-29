# Docker / Kubernetes / OpenShift

## Applicability
Använd när projektet innehåller Dockerfile, Kubernetes-manifest, Helm-liknande deploymentunderlag, OpenShift-resurser eller dokumenterad containerplattform.

## Security objectives
Bedöm applikationsnära runtime-säkerhet: identitet, privilegier, secrets, exponering, containerhardening och gränsen mellan applikationsrepo och plattformsstyrda kontroller.

Detta är inte en fullständig cluster-hardening-granskning.

## High-value review areas
- container user/root
- `runAsNonRoot`
- `runAsUser`
- `allowPrivilegeEscalation`
- Linux capabilities
- privileged containers
- hostPath
- hostNetwork/hostPID/hostIPC
- seccomp
- readOnlyRootFilesystem
- service accounts
- RBAC-bindningar när de finns
- automount av service account token
- secrets och ConfigMaps
- env-vars med credentials
- image tags/digests
- image pull policy
- exposed ports/services/routes/ingress
- TLS termination
- probes som exponerar känslig information
- management endpoints
- init containers och sidecars
- OpenShift SCC-relaterade antaganden när synliga

## Code patterns
Leta efter:
- `privileged: true`
- `allowPrivilegeEscalation: true`
- root user
- `hostPath`
- `hostNetwork: true`
- breda capabilities som `SYS_ADMIN`
- service account med bred RBAC
- `automountServiceAccountToken: true` när token inte behövs
- secrets direkt i manifest
- plaintext credentials i env
- flytande image tags i produktionsflöde
- service/route/ingress som exponerar managementport
- debug endpoints
- volymer med känslig host-åtkomst
- writable root filesystem när applikationen inte behöver det

## Configuration patterns
Granska:
- Deployment/StatefulSet/Pod
- Service
- Ingress/Route
- NetworkPolicy när den finns
- ServiceAccount
- Role/ClusterRole och bindings
- Secret-referenser
- ConfigMaps
- SecurityContext
- PodSecurity/SCC-indikatorer
- TLS/cert references
- image registry/repository
- probes
- namespace-/environment separation

## Common weaknesses
- privileged container utan tydligt behov
- root + writeable filesystem + onödiga capabilities
- hostPath till känslig host-data
- bred service account/RBAC
- managementendpoint exponerad externt
- plaintext secrets i manifest
- admin och användartrafik delar route utan lämplig accesskontroll
- service account token mountas i pod som inte behöver Kubernetes API
- debug/profiling endpoint nåbar i produktion

## False-positive guards
Rapportera inte `containerPort` som internetexponering, Kubernetes Secret reference som plaintext secret, avsaknad av NetworkPolicy som confirmed vulnerability om policy styrs centralt eller avsaknad av explicit seccomp/runAsNonRoot om OpenShift/SCC eller admission policy kan tvinga detta.

## Evidence expectations
Deploymentfynd ska peka på konkret manifest/config eller dokumenterad runtimepolicy. När skydd kan vara plattformscentralt och underlaget saknas ska confidence sänkas eller coverage markeras `not_verifiable`.

## Manual verification triggers
- SCC/Pod Security/admission policies hanteras centralt
- NetworkPolicy eller service mesh ligger i separat repo
- extern secret manager används
- cluster RBAC ligger utanför applikationsprojektet
- ingress/WAF/gateway sköts centralt
- image scanning/signering hanteras i CI/CD utanför underlaget
