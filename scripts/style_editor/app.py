from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import json
from .rules_model import StyleConfig, load_learned_defaults
from .generator import generate_schematron

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORTS_DIR = REPO_ROOT / "reports"
SCHEMAS_DIR = REPO_ROOT / "schemas"

app = FastAPI(title="FRUS Style Guide Editor")
app.mount("/static", StaticFiles(directory=(Path(__file__).parent / "static")), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    learned = load_learned_defaults(REPORTS_DIR)
    return request.app.state.templates.TemplateResponse("index.html", {"request": request, "learned": learned.dict()})

@app.post("/save", response_class=RedirectResponse)
async def save(
    request: Request,
    prefer_when: str = Form("YYYY-MM-DD"),
    allowed_note_types: str = Form("source editorial textual crossreference"),
    repo_presidential_pattern: str = Form(""),
    repo_nara_pattern: str = Form(""),
    repo_dos_pattern: str = Form(""),
    repo_cia_pattern: str = Form(""),
    require_terminal_period: str = Form("on"),
    prefer_semicolons: str = Form("on"),
):
    cfg = StyleConfig(
        prefer_when=prefer_when.strip(),
        allowed_note_types=[t for t in allowed_note_types.split() if t],
        source_patterns={
            "presidential_library": repo_presidential_pattern.strip(),
            "nara_rg": repo_nara_pattern.strip(),
            "state_dept": repo_dos_pattern.strip(),
            "cia": repo_cia_pattern.strip(),
        },
        source_simple_fixes={
            "terminal_period": (require_terminal_period == "on"),
            "prefer_semicolons": (prefer_semicolons == "on"),
        }
    )
    # Save config snapshot
    SCHEMAS_DIR.mkdir(parents=True, exist_ok=True)
    (SCHEMAS_DIR / "style-config.json").write_text(cfg.json(indent=2), encoding="utf-8")
    # Generate schematron
    sch_text = generate_schematron(cfg)
    (SCHEMAS_DIR / "frus-style-guide-editor.sch").write_text(sch_text, encoding="utf-8")
    return RedirectResponse(url="/", status_code=303)

@app.get("/api/learned")
async def api_learned():
    learned = load_learned_defaults(REPORTS_DIR)
    return JSONResponse(learned.dict())

def init_templates(app: FastAPI):
    from fastapi.templating import Jinja2Templates
    templates_dir = Path(__file__).parent / "templates"
    app.state.templates = Jinja2Templates(directory=str(templates_dir))

init_templates(app)
