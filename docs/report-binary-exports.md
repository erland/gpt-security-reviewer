# Word- och PDF-export

## Word

```bash
python3 scripts/render_report_docx.py report.json -o report.docx
```

DOCX är den redigerbara rapportversionen och använder samma sektioner och data som Markdown.

## PDF

```bash
python3 scripts/render_report_pdf.py report.json -o report.pdf
```

PDF skapas från DOCX-renderingen med LibreOffice för att hålla layouten så nära Word som möjligt.

## Alla format

```bash
python3 scripts/export_report.py report.json --format all --output-dir out
```

## Kvalitetsprincip
Word och PDF ska renderingskontrolleras visuellt före faktisk leverans till användare.
