# FRUS Annotation Style Notes — Volume 1981–1988, Book V

This memo summarises the annotation cues that compilers should watch for when
working on the fifth volume (Book V) of the 1981–1988 *Foreign Relations of the
United States* sub-series. It builds on the series-wide conventions captured in
[`frus-annotation-style.md`](./frus-annotation-style.md) and the targeted
checklist for Volume XXIV. Treat these points as a quick companion while
reviewing or encoding documents from this book.

> **Reference access.** The Office of the Historian hosts the PDF and HTML
> presentation at <https://history.state.gov/historicaldocuments/frus1981-88v05>.
> Network egress from the project sandbox currently returns HTTP 403 when
> attempting to download the PDF or the underlying TEI, so plan to fetch the
> reference files outside this environment and mirror them into the workspace
> before running validation scripts.

## 1. Document wrappers and headings

* Continue to wrap each item in `<div type="document" xml:id="doc-###">`,
  preserving the printed document number.
* Reproduce descriptive headings verbatim. Volume V frequently prints genre
  cues such as “Memorandum of Conversation,” “Talking Points,” and “National
  Security Council Meeting.” Keep prepositions (“From,” “To,” “Between”) and
  roles (“the Secretary of State,” “Assistant to the President for National
  Security Affairs”) exactly as they appear.
* Multi-line headings in this volume often include parenthetical qualifiers
  (for example, “(S)” or “with attached Talking Points)”). Retain those
  parenthetical notes inside the `<head>` instead of moving them to source
  notes.
* Identify telegrams with `@subtype="telegram"`, meeting minutes with
  `@subtype="minutes"`, and intelligence or directive material with
  `@subtype="report"` or `@subtype="directive"` when those values already exist
  in the schematron rule set.

## 2. Openers, datelines, and participant lists

* Capture full datelines in `<opener>` blocks. When the print version supplies
  both the venue and time zone (for example, “Washington, June 10, 1983,
  9:30 a.m.”), encode the machine-readable value using `@when="YYYY-MM-DDThh:mm"`
  and add `@type="approx"` if the printed time is approximate.
* Memoranda of conversation regularly begin with a participant roster. Encode
  structured lists with `<list rend="participants">` and individual attendees
  in `<item>` elements. Where the printed text uses a paragraph run-on, keep the
  roster as consecutive `<p>` elements instead.
* Preserve printed briefing headers like `<hi rend="bold">SUBJECT</hi>`,
  `<hi rend="bold">PARTICIPANTS</hi>`, and `<hi rend="bold">SUMMARY</hi>` at the
  top of memoranda. These appear in uppercase in the book and should remain in
  uppercase within the TEI.

## 3. Body text patterns unique to Volume V

* Talking points and briefing papers often contain ordered sections introduced
  by capitalised cue phrases (for example, “BACKGROUND,” “OBJECTIVES,”
  “RECOMMENDATION”). Encode each cue word in bold (`<hi rend="bold">`) and begin
  a new paragraph when the printed document inserts extra spacing.
* Presidential memcons include interjections (for example, “The President:” / “The
  Prime Minister:”). Represent these as `<hi rend="smallcaps">` speakers
  followed by the colon and transcript text, mirroring the print layout.
* National Security Decision Directives (NSDDs) in the volume retain their
  formal numbering (for example, “NSDD-75”). Encode the identifier verbatim and
  keep paragraph numbering exactly as printed.
* Attachments that are printed in full should be nested inside
  `<div type="attachment">` wrappers with their own `<head>` and source note.
  When the volume describes an attachment without reproducing it, annotate the
  reference with `<note type="source">Attached but not printed.</note>` or a more
  specific description provided in the book.

## 4. Source notes and classification data

* Begin source notes with a bold `Source:` label. Volume V relies heavily on the
  Reagan Presidential Library, the Department of State Central Foreign Policy
  Files, and National Security Council staff paper collections. Follow the
  hierarchy `Repository; collection; series; box/folder; format; classification`.
* Many items include drafting and clearance chains—`Drafted by …; cleared by …;`
  Record each clause in the order it appears, joined by semicolons within the
  same paragraph.
* For telegrams, include cable numbers and transmission data after the archival
  citation and before the final classification clause (`Telegram 12345; Secret;
  Immediate; Sent ...; Received ...`).
* When the printed source note lists the document’s control number (for example,
  “No. 8405163”) or directive status (for example, “NSC# 12345”), preserve it as
  another semicolon-delimited clause.

## 5. Editorial notes, cross-references, and footnotes

* Place narrative editorial notes immediately after the source paragraph. Use
  `@resp` attributes to credit compilers when there are multiple editors.
* Cross-references begin with “See”/“See also” and rely on `<ref>` links to
  `#doc-###` ids. End each cross-reference with a period.
* Volume V contains dense contextual footnotes that cite prior negotiations or
  intelligence estimates. Store footnotes in `<note place="foot">` containers.
  Multi-paragraph notes should wrap each paragraph in `<p>`.
* When footnotes reference published legislation (for example, the Goldwater–
  Nichols Act) or international agreements, italicise titles with `<hi rend="italic">`
  and include publication details as printed.
* Encode bracketed redaction cues (for example, `[name not declassified]`,
  `[less than 1 line not declassified]`) verbatim.

## 6. Validation workflow

1. Download `frus1981-88v05.xml` or the published PDF outside the sandboxed
   environment (see the note on access above) and place it in a local `tei/`
   directory alongside other reference volumes.
2. Run `python scripts/learn_frus.py --tei tei --out schemas --reports reports`
   to regenerate the learned schematron rules, confirming that Volume V aligns
   with the existing constraints.
3. Inspect `reports/learned-summary.json` for new constructs (for example,
   additional note types or subtype values) and update this memo if new patterns
   appear.
4. Validate compiler-produced TEI with `jing` or `xmllint` against the refreshed
   schematron before submitting changes upstream.

## 7. Open questions for follow-up review

* Confirm whether Volume V introduces any new `<note type="">` values (such as
  `type="presidential-diary"`) when the TEI becomes available.
* Verify the handling of handwritten marginalia; the print volume occasionally
  flags “handwritten notation” lines that may map to `<note type="handwritten">`.
* Determine whether the volume encodes translated attachments with `<foreign>`
  blocks or separate `<div type="translation">` wrappers.

Document updates should be appended here as soon as the TEI source can be
cross-checked.
