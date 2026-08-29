# Scenario: path traversal

## Input
`Paths.get(uploadDir, uploadedFilename)` används direkt med användarens filnamn och ingen normalisering/allowlist visas.

## Expected
Path traversal-fynd eller probable finding beroende på övrig validering.
