from pydantic import BaseModel, Field
from pathlib import Path
import json

class StyleConfig(BaseModel):
    prefer_when: str = Field("YYYY-MM-DD", description="Preferred date/@when shape")
    allowed_note_types: list[str] = Field(default_factory=lambda: ["source","editorial","textual","crossreference"])
    source_patterns: dict = Field(default_factory=dict)
    source_simple_fixes: dict = Field(default_factory=dict)

def load_learned_defaults(reports_dir: Path) -> StyleConfig:
    # Try to load learned files if present; otherwise return defaults
    learned_path = reports_dir / "frus-source-learned.json"
    try:
        if learned_path.exists():
            data = json.loads(learned_path.read_text(encoding="utf-8"))
            patterns = data.get("suggested_regex_blocks", {})
            fixes = data.get("simple_fixes", {})
            return StyleConfig(
                prefer_when="YYYY-MM-DD",
                allowed_note_types=["source","editorial","textual","crossreference"],
                source_patterns=patterns,
                source_simple_fixes=fixes
            )
    except Exception:
        pass
    return StyleConfig()
