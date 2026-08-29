# Releaseprocess

GitHub Release-taggen är canonical versionskälla för releaseartefakter. `VERSION` används för lokala utvecklingsbyggen.

En publicerad release bygger och laddar upp:
- Chat ZIP
- Custom GPT ZIP
- SHA-256-checksummor

CI kör dessutom ett release-liknande smoke-test med `v0.0.0-ci` för att fånga fel före publicering.
