# Learned Schematron

This repository hosts documentation and tooling experiments for the FRUS annotation workflow. For detailed guidance on footnote encoding, see [FRUS Footnote-Annotation Training Data](docs/frus-footnote-annotation-training.md). Volume-specific checklists are available for [Volume XXIV (1981–1988)](docs/frus1981-88v24-annotation-style.md) and [Volume XLIV, Part 1 (1981–1988, South Asia)](docs/frus1981-88v44p1-annotation-style.md).

## GitHub Pages search

The GitHub Pages site under `docs/` now auto-loads `docs/search-index.json` at page load, so repository corpus search works with no manual upload.

That index is generated from XML files under `data/frus/volumes/**` by:

```bash
python scripts/build_search_index.py
```

A GitHub Actions workflow (`.github/workflows/build-pages-index.yml`) regenerates and commits `docs/search-index.json` automatically on pushes to `main` when FRUS corpus data or related search code changes.

## Server-hosted app

The Flask app and related server-hosted workflows still exist for deployments that need a backend. The GitHub Pages search experience remains fully static and does not require server-side XML upload handling.
