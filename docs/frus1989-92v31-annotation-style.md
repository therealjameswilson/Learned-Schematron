# FRUS Annotation Style Notes — Volume 1989–1992, Book XXXI

This memo distils the TEI annotation patterns visible in the published edition of
*Foreign Relations of the United States, 1989–1992, Volume XXXI, South and Central Asia*.
Use it as a compiler checklist when encoding or reviewing the XML master for this volume
(`frus1989-92v31.xml`). Many of the practices mirror the cross-volume rules documented in
[`frus-annotation-style.md`](./frus-annotation-style.md); the points below highlight
volume-specific tendencies worth double-checking.

> **How to read this guide.** Each section summarises the structural template observed in the
> reference XML. Keep it beside you while editing, and confirm edge cases directly against the
> authoritative TEI when possible.

## 1. Document containers and headings

* Wrap every item in `<div type="document" xml:id="doc-###">` using the printed running
  document number. The `<head>` should preserve the book’s two-line heading structure: the
  numeric document label on the first line and the descriptive heading (genre + participants)
  on the second.
* Retain the exact genre labels that open the descriptive heading—“Memorandum,” “Telegram,”
  “Minutes,” “Information Memorandum”—including capitalisation and punctuation. The preposition
  chain (“From … to …”) mirrors the print edition and must not be normalised.
* Where the book uses small caps for personal names, wrap those spans in `<hi rend="smallcaps">`.
  Initials remain spaced as printed (for example, “J. N. Dixit”).
* Meeting records frequently include a participant list in small caps immediately below the
  heading. Encode it as a paragraph with embedded `<hi rend="smallcaps">` rather than a list,
  reflecting how the lines appear in the book.

## 2. Openers, datelines, and salutations

* Combine city, full date, and time in the `<opener>`. Encode machine-readable values with the
  `@when` attribute using ISO 8601 (`YYYY-MM-DD` or `YYYY-MM-DDThh:mmZ`). Telegrams almost always
  supply Zulu times; memoranda often omit the time and only supply the date.
* Preserve the salutation block exactly as printed. Memoranda of conversation usually include
  bolded `To:` and `From:` lines, encoded with `<hi rend="bold">To:</hi>` and `<hi
  rend="bold">From:</hi>`. Information memoranda often follow with a `Subject:` line in the same
  paragraph.
* When the dateline contains parenthetical qualifiers—such as “(sent by facsimile)”—keep them in
  the opener rather than moving them to notes.

## 3. Body structure and paragraph cues

* Respect paragraph numbering and bold cue words (`Summary`, `Action Requested`, `Background`).
  Encode cue words with `<hi rend="bold">` and keep the numeral inline at the start of the
  paragraph (`1.`).
* Meeting minutes typically open with a narrative sentence summarising the setting, followed by
  labelled sections (`Discussion`, `Participants`). Retain the same paragraph sequence and
  headings as bold spans rather than converting them into structural elements.
* Bracketed declassification notes (`[name not declassified]`, `[text not declassified]`) remain in
  the body text and are not normalised.

## 4. Source notes

* Start the first note beneath each document body with `Source:` and bold the label using `<hi
  rend="bold">`.
* Follow the hierarchy `Repository; Collection; Box/Folder; Format; Classification.` Volume XXXI
  documents regularly cite National Archives record groups (for example, `National Archives, RG 59,
  Central Foreign Policy Files`) and presidential library holdings (`George H.W. Bush Library,
  National Security Council Files, Country File, Box ...`). Preserve the exact punctuation from the
  print edition.
* Drafting and clearance information sits between the format clause and the classification clause
  (`Drafted by ...; cleared by ...;`). Cable numbers and transmission data for telegrams are placed
  immediately before the classification clause (`Telegram; Islamabad 12345; Secret; Immediate; Sent
  ...; Received ...`).
* Keep the entire source note in a single paragraph. Subsequent notes handle editorial narration.

## 5. Editorial and cross-reference notes

* Narrative editorial notes follow the source note and stay within the document body. Attribute
  multi-editor contributions with `@resp` when the TEI provides responsibility data.
* Use `<note type="crossreference">See <ref target="#doc-###">Document ###</ref>.</note>` for
  cross-document pointers. When multiple documents are cited, join the references with semicolons
  inside a single note and conclude with a period.
* Italicise published works with `<hi rend="italic">` and wrap non-English titles inside
  `<foreign>`.

## 6. Footnotes and apparatus

* Inline footnote calls appear as `<ref target="#fn-#">#</ref>` placed directly after the relevant
  punctuation in the text. The referenced note uses `<note xml:id="fn-#" place="foot"
  type="source">` (or `type="editorial"` / `type="crossreference"` as appropriate) with each
  paragraph wrapped in `<p>`.
* When the printed book uses lettered footnote calls (common for attachments), encode the same
  letter inside the `<ref>` and ensure the note IDs match (`fn-a`, `fn-b`).
* Use inline `<ref>` elements for FRUS self-citations (`See Document 25.`) rather than plain text.

## 7. Attachments, annexes, and not printed material

* Attachments printed in full are modelled as nested `<div type="attachment">` elements carrying
  their own `<head>`, source notes, and body. Maintain the numbering or lettering system from the
  book (e.g., “Tab A”).
* For attachments noted but not printed, include a short `<note type="source">Attached but not
  printed.</note>` after the source note. When archival details are supplied, append them within the
  same note separated by semicolons.
* Memoranda often include covering notes that describe separate decision memoranda. Encode these as
  editorial notes rather than attachments when the text is summarised instead of transcribed.

## 8. Telegram specifics

* Mark telegram documents with `@subtype="telegram"`. The `<head>` follows the pattern “Telegram
  From the Embassy in [City] to the Department of State.” Retain prepositions and geographic
  qualifiers.
* The opener captures the origin city, date, and Zulu time. Populate `<time when="...Z">` so
  downstream tooling can read the timestamp.
* Preserve front-matter lines such as distribution lists (`Info: AmEmbassy New Delhi, AmConsulate
  Karachi`) inside the body as printed, often in small caps.
* Numbered paragraphs remain inline, and bold cue words like `Summary:` or `Action Requested:` use
  `<hi rend="bold">` within the same paragraph.
* Close with `<closer>` / `<signed>` containing the surname in small caps when printed that way.
  Clearance lines (`Cleared by ...`) appear as subsequent paragraphs within the body.

## 9. Workflow reminder for compilers

1. Download `frus1989-92v31.xml` into a local `tei/` directory outside the sandbox if network
   restrictions block direct access.
2. Run `python scripts/learn_frus.py --tei tei --out schemas --reports reports` to rebuild the
   learned Schematron profile and confirm that the volume-specific features above are captured in
   the validation rules.
3. Review `reports/learned-summary.json` for any anomalies or new annotation patterns that should be
   added to this memo.

## 10. Known access limitation

The sandbox environment returns `403 Forbidden` when requesting resources from
`https://history.state.gov/`. Perform any required downloads (including the TEI master) from an
external network or mirror the XML into the repository before running the learning scripts.
