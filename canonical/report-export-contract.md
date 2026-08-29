# Report export contract

## Purpose
Alla exporter ska utgå från samma strukturerade rapportdata enligt `schemas/report.schema.json`.

## Canonical source
Den strukturerade rapportmodellen är sanningskällan. Markdown är canonical mänskligt läsbart format.

## Supported formats in step 15
- Markdown
- Confluence markup

## Invariants
Renderers får inte ändra finding ID, severity, confidence, finding status, coverage eller follow-up review type och får inte lägga till nya fynd.

## Empty sections
Obligatoriska canonical sektioner ska finnas även när de saknar poster. Använd en neutral text, exempelvis `Inga identifierade poster.`

## Finding order
Fynd sorteras efter severity: critical, high, medium, low, informational och därefter ID.

## Markdown
Markdown använder rubriker, sammanfattningstabeller och separata fyndavsnitt och ska fungera som direkt nedladdningsbar rapport.

## Confluence markup
Confluence-renderingen använder klassisk wiki markup med `h1.`, `h2.`, `h3.`, `||` för tabellhuvuden och `|` för tabellceller. Markdown-tabellsyntax får inte läcka in.

## File naming
- `sakerhetsgranskning-<system>.md`
- `sakerhetsgranskning-<system>.confluence.txt`
