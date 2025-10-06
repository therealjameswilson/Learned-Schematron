# FRUS Annotation Style Notes — Volume 1981–1988, Book XXIV

This guide distils the annotation patterns that compilers should follow when working on
Volume XXIV (1981–1988) of *Foreign Relations of the United States*. The advice is derived
from the series-wide TEI conventions already documented in this repository and should be
verified against the XML of `frus1981-88v24.xml` when local access to the reference volume is
available.

> **How to use this memo.** Treat it as a checklist while encoding or reviewing documents.
> Each section summarises the target structure and the micro-formatting cues that appear
> consistently across published FRUS material. Differences specific to Volume XXIV should be
> confirmed by inspecting the TEI master once it can be downloaded.

## 1. Document wrappers

* Every diplomatic item lives inside `<div type="document" xml:id="doc-###">`. Preserve the
  running document number as it appears in print (for example, `Document 123` appears in the
  TEI as `<head>Document 123</head>` followed by the descriptive heading line).
* Record the descriptive heading verbatim. Retain genre labels (Memorandum, Telegram,
  Minutes, Letter), prepositions (From, To, Between), and internal punctuation. Small-cap
  treatments in print continue to use `<hi rend="smallcaps">`.
* Identify the document subtype where helpful. Telegrams use `@subtype="telegram"`, meeting
  records often use `@subtype="minutes"`, and intelligence summaries may use
  `@subtype="report"`. Only employ subtypes that are already recognised by the validation
  schematron.

## 2. Openers and datelines

* Combine place, full calendar date, and (when available) time into the `<opener>` element.
  Encode the machine-readable value in `@when` using ISO 8601 (`YYYY-MM-DD` or
  `YYYY-MM-DDThh:mmZ`). When the document reports both sent and received timestamps, keep
  them together in the source note rather than duplicating them in the dateline.
* Include the salutation block exactly as printed. For memoranda, the `To:` and `From:` lines
  are bolded (`<hi rend="bold">To:</hi>`). Telegrams frequently open with an addressee line in
  small caps; do not relocate that material to footnotes.

## 3. Body text and paragraph cues

* Preserve paragraph numbering and internal headings (`Summary`, `Action Requested`, etc.) as
  inline bold spans. Begin each numbered point at the start of a paragraph, matching spacing
  and punctuation from the source.
* Encode editorial bracketings that appear in the book (for example, `[name not declassified]`)
  verbatim. Do not expand acronyms or normalise capitalisation.
* Meeting minutes often include lists of participants at the top of the document. Maintain the
  line breaks with `<list rend="participants">` where they are typeset as a list; otherwise
  keep them as consecutive paragraphs.

## 4. Source notes

* Start the first note with `Source:` and mark the label in bold. Follow the hierarchy
  repository → collection → box/folder → physical format → classification. Use semicolons to
  separate clauses. Example pattern: `National Archives, RG 59, Central Foreign Policy Files;
  Telegram; Secret; Immediate.`
* Add drafting, clearance, and transmission statements after the archive citation but before
  classification details (`Drafted by ...; approved by ...;`). For telegrams, cable numbers and
  transmission data (`Sent ...; Received ...`) come immediately before the final
  classification clause.
* Keep the entire source note within a single paragraph, even when it is lengthy. Only use
  additional notes for purely editorial commentary.

## 5. Editorial notes and cross-references

* Editorial background paragraphs follow the source note in the body of the document. Attribute
  them with `@resp` when multiple editors contributed.
* Cross-references use `<note type="crossreference">See <ref target="#doc-###">Document ###</ref>.</note>`
  and should end with a period. When referencing multiple documents, join them with semicolons.
* Use `<hi rend="italic">` for published works and `<foreign>` for non-English titles inside
  editorial notes.

## 6. Footnotes and apparatus

* Footnote call-outs appear as `<ref target="#fn-1">1</ref>` directly in the running text.
  Store the note text in `<note xml:id="fn-1" place="foot" type="source">` or an appropriate
  type such as `editorial` or `crossreference`.
* Multi-paragraph footnotes are permissible. Use `<p>` wrappers inside the `<note>` element
  to preserve paragraph breaks.
* When a footnote cites another FRUS document, format the citation as
  `See Document 45.` using an inline `<ref>`.

## 7. Attachments and enclosures

* Treat annexes, tabs, and attachments as nested `<div type="attachment">` elements with their
  own headings and source notes when they were printed in the volume. Link them from the parent
  document using `<note type="source">Attached but not printed.</note>` if only a citation is
  provided.
* For attachments that are summarised rather than printed, encode the summary text in an
  editorial note and include the archival citation when available.

## 8. Validation workflow for compilers

1. Download `frus1981-88v24.xml` into a local `tei/` directory (network access may require
   running the command outside the sandboxed environment used for this note).
2. Execute `python scripts/learn_frus.py --tei tei --out schemas --reports reports` to regenerate
   the learned Schematron. This will verify that the observed annotation patterns in Volume XXIV
   align with the expectations captured here.
3. Run `jing` or `xmllint` with the updated Schematron to confirm that compiler-edited documents
   conform to the learned rules.
4. Review the generated reports (especially `reports/learned-summary.json`) for any new
   annotation features unique to this volume, and update this checklist accordingly.

## 9. Known access limitation

The project sandbox currently blocks outbound HTTPS traffic to `raw.githubusercontent.com` and
`static.history.state.gov`, preventing direct downloads of the reference TEI file. The curl
command below illustrates the 403 error:

```
curl -L https://raw.githubusercontent.com/HistoryAtState/frus/main/volumes/frus1981-88v24.xml -o /tmp/frus1981-88v24.xml
```

Run the download outside the sandbox or mirror the XML into the repository before repeating the
learning process.
