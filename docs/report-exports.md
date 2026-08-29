# Rapportexporter

## Markdown
`python3 scripts/render_report_markdown.py report.json -o report.md`

## Confluence markup
`python3 scripts/render_report_confluence.py report.json -o report.confluence.txt`

## Gemensam export
`python3 scripts/export_report.py report.json --format both --output-dir out`

Renderers får inte ändra fyndens semantik.
