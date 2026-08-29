# Word and PDF export contract

## Purpose
Word och PDF ska rendera samma canonical rapportdata som Markdown och Confluence markup.

## Source of truth
`schemas/report.schema.json` och rapportens strukturerade JSON är sanningskällan.

## Word
DOCX är det redigerbara dokumentformatet.

Krav:
- professionell rapportlayout,
- tydliga Heading 1/2/3-nivåer,
- tabeller för metadata, fyndöversikt, åtgärder och fortsatt granskning,
- detaljerade fynd som egna avsnitt,
- sidhuvud/sidfot med rapporttitel och sidnummer när möjligt,
- läsbara fil- och evidensreferenser,
- inga semantiska förändringar jämfört med canonical data.

## PDF
PDF skapas från samma DOCX-rendering för att maximera layoutlikhet mellan Word och PDF.

Krav:
- samma rubrikordning och fynddata som Word,
- inga klippta tabeller eller överlapp,
- konsekventa sidbrytningar,
- renderingskontroll före leverans.

## Invariants
Varken Word- eller PDF-rendering får:
- ändra finding ID,
- ändra severity,
- ändra confidence,
- ändra status,
- ta bort coverage,
- ändra follow-up review type,
- lägga till fynd.
