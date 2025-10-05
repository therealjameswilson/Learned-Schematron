# Contributing to Learned-Schematron

We welcome pull requests that improve FRUS style validation.

## How to propose a rule
1. Open/modify a Schematron file under `schemas/`.
2. Keep new constraints **gentle** at first (report + Quick Fix). Promote to strict asserts later.
3. Provide **examples** in `reports/` or link to TEI lines showing the pattern.
4. Run locally:
   - `make build` (re-learn from TEI samples if you added any to `tei/`)
   - `make validate` (checks `tei/sample.xml` if present)
5. Commit and open a PR with a **clear, concrete description** of the rule’s intent and known exceptions.

## House principles
- Prefer **Quick Fix** over destructive auto-rewrites.
- Any rule that might have exceptions should begin as **report-only**.
- Keep macros (Word) and Schematron (TEI) aligned conceptually.
- All logic must work **offline** for secure networks.

## Licensing
By contributing, you agree that your contributions are licensed under the repository’s MIT License.
