# Rapportworkflow

Default:
- Quick: chat
- Standard: chat + Markdown
- Deep: chat + Markdown

Explicit användarval kan vara Markdown, Confluence markup, Word, PDF eller flera format samtidigt.

`plan_report_delivery.py` bestämmer planen, `deliver_report.py` renderar från samma report JSON och `render_chat_summary.py` skapar den korta chattsammanfattningen.

Steg 16 ansvarar för faktisk DOCX/PDF-rendering och visuell QA. Steg 17 ansvarar för leveranslogik och semantisk enhetlighet.
