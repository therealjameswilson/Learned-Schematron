# FRUS Annotation Style Notes — Volume 1981–1988, Book XLIV, Part 1

These notes summarise the annotation and encoding habits visible in the published volume
[*Foreign Relations of the United States, 1981–1988, Volume XLIV, Part 1, South Asia*](https://history.state.gov/historicaldocuments/frus1981-88v44p1).
Use them as a quick reference when preparing or reviewing TEI for this book. They are meant to
complement the series-wide checklist in [`frus-annotation-style.md`](./frus-annotation-style.md)
by highlighting patterns unique to this volume.

> **How to read this memo.** Each numbered section calls out structure or formatting that occurs
> consistently across the volume. Pay particular attention to the semicolon order in source notes,
> the placement of editorial background paragraphs, and the way attachments are described, as
> these three areas show the clearest patterns in Part 1.

## 1. Document wrappers and numbering

* Each document appears inside `<div type="document" xml:id="doc-###">` where the running
  number matches the print book (“Document 123”). The `<head>` opens with the running number on
  its own line, followed by the descriptive heading in the next block-level element.
* Genre labels are spelled out (“Memorandum”, “Telegram”, “Letter”, “Minutes”) and are followed by
  a chain of prepositional phrases that identify the participants. Keep commas and hyphenated job
  titles exactly as printed. Small caps for names persist via `<hi rend="smallcaps">`.
* Documents derived from intelligence reporting (`National Intelligence Daily`, `Special National
  Intelligence Assessment`) generally add `@subtype="report"` on the `<div>` wrapper. Meeting
  records often use `@subtype="minutes"`, while situation room logs rely on `@subtype="summary"`.

## 2. Openers, datelines, and salutations

* The `<opener>` contains the dateline. Diplomatic cables combine origin city, calendar date,
  and Zulu time; memoranda omit the time unless it was printed. Encode machine-readable values in
  `@when` (`YYYY-MM-DD` or `YYYY-MM-DDThh:mmZ`).
* Memoranda use bold cue labels for addressing lines—`<hi rend="bold">To:</hi>` and `<hi
  rend="bold">From:</hi>`—each on its own paragraph. When a memorandum includes a `Subject:` line
  it stays in the opener, also bolded, separated from the addressee block by a blank line.
* Meeting minutes and intelligence summaries often start with a participant list. Encode it using
  `<list rend="participants">` when laid out as bullet-style entries; otherwise preserve the
  lineation as successive paragraphs within the opener.

## 3. Body structure, emphasis, and redactions

* Numbered paragraphs in telegrams keep the number inline at the start of each `<p>` (`1.` `2.`)
  followed by a space. Cue phrases such as “Summary” or “Action Requested” appear in bold via `<hi
  rend="bold">` directly after the number.
* Editorial brackets that appear in print (`[name not declassified]`, `[less than 1 line not
  declassified]`) are preserved verbatim. Do not expand abbreviations or modernise spelling.
* Within intelligence reporting, tables and bullet lists are rare; when they appear, encode them as
  `<table>` or `<list>` elements so the hierarchical structure matches the printed presentation.

## 4. Source notes and archival citations

* Source notes begin with `<hi rend="bold">Source:</hi>` followed by semicolon-delimited clauses
  in this sequence:
  1. Repository (expanded to the full printed form—“Reagan Library”, “National Archives”,
     “Washington National Records Center”).
  2. Collection, series, box, and folder identifiers, each separated by commas.
  3. Physical description of the item (“Telegram”, “Memorandum”, “Paper prepared in the Department
     of State”).
  4. Handling information (`Secret; Nodis.` `Confidential; Immediate.` `Unclassified.`).
* Drafting, clearance, and distribution statements live between the physical description and the
  classification clause (`Drafted by ...; cleared by ...;`). For telegrams, cable numbers and
  transmission data (`Sent ...; Received ...`) follow the format clause but precede classification.
* When an item originated outside the U.S. Government—such as foreign ministry notes or speeches—
  the source note cites the originating institution after the repository (`American Institute in
  Taiwan; memorandum; Confidential.`).

## 5. Editorial notes and cross-references

* Narrative background paragraphs follow the source note and stay inside the document body, not the
  footnotes. Attribute shared work using `@resp` when more than one editor contributed.
* Cross-references use `<note type="crossreference">See <ref target="#doc-###">Document ###</ref>.</note>`
  and end with a period. Multiple targets are separated with semicolons inside the same note.
* Substantive editorial notes italicise published works (`<hi rend="italic">Asian Survey</hi>`) and
  enclose non-English quotations in `<foreign>`.

## 6. Footnote apparatus

* Footnote callouts appear inline as `<ref target="#fn-1">1</ref>` and reference a corresponding
  `<note xml:id="fn-1" place="foot" type="editorial">` (or `type="source"` when relaying
  archival citations). Multi-paragraph notes wrap each paragraph in `<p>`.
* When footnotes point to related FRUS documents, use `See <ref target="#doc-###">Document ###</ref>.`
  Names of foreign publications or agreements inside footnotes follow the same italicisation rules
  as the main body.

## 7. Attachments, annexes, and not printed references

* Printed attachments are nested within the parent document as `<div type="attachment">` elements
  with their own headings, openers, and source notes. Maintain the running order indicated in the
  book (Annex A, Tab B, etc.).
* When the book notes an attachment that is not printed, encode a source note or editorial note in
  the parent document: `<note type="source">Attached but not printed.</note>` Include a brief
  summary when the volume supplies one.
* Intelligence compilations that collect multiple enclosures may present them as numbered tabs.
  Represent each tab as its own attachment division, mirroring the nested numbering and keeping the
  descriptive heading verbatim.

## 8. Suggested validation workflow

1. Download `frus1981-88v44p1.xml` to a local `tei/` folder (download outside this sandbox if
   necessary).
2. Run `python scripts/learn_frus.py --tei tei --out schemas --reports reports` to retrain the
   learned Schematron on the new TEI.
3. Inspect `reports/learned-summary.json` for unexpected constructs (new note types, uncommon
   `@rend` values) and incorporate any confirmed patterns back into this checklist.
4. Validate edited TEI with `jing` or another Schematron processor before submission to ensure the
   document-level rules captured here remain satisfied.
