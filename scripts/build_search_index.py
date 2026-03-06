#!/usr/bin/env python3
"""Build a static JSON search index from FRUS TEI XML volumes."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
import sys
import xml.etree.ElementTree as ET


REPO_ROOT = Path(__file__).resolve().parents[1]
VOLUMES_DIR = REPO_ROOT / "data" / "frus" / "volumes"
OUTPUT_PATH = REPO_ROOT / "docs" / "search-index.json"


def local_name(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def normalize_text(text: str) -> str:
    return " ".join(text.split())


def extract_documents(xml_path: Path) -> list[dict[str, str]]:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    docs: list[dict[str, str]] = []

    for elem in root.iter():
        if local_name(elem.tag) != "div" or elem.attrib.get("type") != "document":
            continue

        title = ""
        for child in elem:
            if local_name(child.tag) == "head":
                title = normalize_text("".join(child.itertext()))
                break

        text = normalize_text("".join(elem.itertext()))
        docs.append(
            {
                "title": title,
                "text": text,
                "source": str(xml_path.relative_to(VOLUMES_DIR)),
            }
        )

    return docs


def main() -> int:
    documents: list[dict[str, str]] = []
    latest_source_mtime: float | None = None

    if not VOLUMES_DIR.exists():
        print(f"Warning: source directory not found: {VOLUMES_DIR}", file=sys.stderr)
    else:
        for xml_path in sorted(VOLUMES_DIR.rglob("*.xml")):
            file_mtime = xml_path.stat().st_mtime
            latest_source_mtime = (
                file_mtime
                if latest_source_mtime is None
                else max(latest_source_mtime, file_mtime)
            )
            try:
                documents.extend(extract_documents(xml_path))
            except ET.ParseError as exc:
                print(f"Warning: skipping malformed XML {xml_path}: {exc}", file=sys.stderr)
            except Exception as exc:  # pragma: no cover - defensive logging for build resilience
                print(f"Warning: failed to parse {xml_path}: {exc}", file=sys.stderr)

    generated_at = (
        datetime.fromtimestamp(latest_source_mtime, timezone.utc).isoformat()
        if latest_source_mtime is not None
        else None
    )

    payload = {
        "generated_at": generated_at,
        "total_documents": len(documents),
        "documents": documents,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(documents)} documents to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
