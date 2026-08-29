# PDF ska använda deterministisk renderer

## Class
recommendation

## Tags
- reporting
- pdf
- layout

## Input
Standardgranskningen ska levereras som PDF och innehåller långa åtgärdstexter, systemkomponenter och follow-up review.

## Expected
Analysen ska först låsas i canonical JSON. Standard/Deep-leverans ska gå genom review integrity gate och deterministic DOCX/PDF renderer. Texttunga tabeller får högst tre kolumner; rekommenderade åtgärder och fortsatt granskning ska renderas som block och canonical rubrikordning ska bevaras.
