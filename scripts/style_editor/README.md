# FRUS Style Guide Editor (UI)

A simple FastAPI + Jinja app that loads learned style info from `/reports`,
lets editors tweak rules (preferred `@when` shape, `note/@type` set, and
Source note patterns), and exports an updated Schematron file to `/schemas/frus-style-guide-editor.sch`.

## Run (inside Codespaces or Dev Container)
```bash
pip install -r tools/requirements.txt
uvicorn scripts.style_editor.app:app --reload --host 0.0.0.0 --port 8000
```
Open http://localhost:8000/
