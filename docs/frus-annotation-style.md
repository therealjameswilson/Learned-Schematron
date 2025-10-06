# FRUS Annotation Style (Model Volumes frus1989-92v31 and frus1981-88v04)

For a compiler-focused checklist that applies the same conventions to Volume XXIV of the
1981–1988 sub-series, see
[`frus1981-88v24-annotation-style.md`](./frus1981-88v24-annotation-style.md).

Summary of annotation conventions observed in the two reference volumes
reviewed so far. Use this as the textual companion to the in-app quick
reference.

## Document headings

* Reproduce the printed heading verbatim inside `<head>` without
  normalising case or punctuation. In both volumes the pattern starts
  with the document genre—“Memorandum,” “Telegram,” “Letter,” “Minutes,”
  and so forth—followed by a chain of prepositions (“From,” “of,” “to,”
  “between”) that identify the participants.
* Identify each principal by name and role. Spell out titles (“Secretary
  of State Haig”) rather than using abbreviations. Where the print
  edition uses small caps for names, the TEI preserves this with `<hi
  rend="smallcaps">` wrapped around the full name or the surname.
* When a single person holds multiple offices, retain the comma-delimited
  list exactly as printed (“the Under Secretary of State for Political
  Affairs and the Director of Central Intelligence”). Multi-sender
  headings keep the conjunction “and” (not an ampersand).
* Subordinate qualifiers—such as parenthetical references to annexes or
  teleconference numbers—remain part of the heading text. Avoid moving
  them into notes; the head should give the researcher the same quick
  orientation as the printed book.

## Source notes

* Always begin with the literal `Source:` label (rendered bold in TEI via
  `<hi rend="bold">`).
* Follow the pattern: repository → record group or collection → document
  format → classification / dissemination.
* Expand repository names to their published form. For National Archives
  holdings spell out "National Archives" and include the record group (for
  example, `National Archives, RG 59, Central Foreign Policy Files`). For
  presidential libraries, cite the library first, then the office-level
  collection, box, and folder (`Jimmy Carter Library, National Security
  Affairs Staff, Country File, Box 12, Nigeria`). University archives and
  manuscript repositories follow the same hierarchy: institution → collection
  → box/folder identifiers.
* When referencing microfilm or digitised sets, identify both the physical
  archive and the reproduction series (`Eisenhower Library, Whitman File,
  Dulles-Herter Series; microfilm`). Note commercial databases or published
  compilations after the archive reference (`Reagan Library, Executive
  Secretariat, NSC: Head of State File; reproduced in Digital National
  Security Archive`).
* For born-digital materials cite the hosting archive and, if applicable, the
  web collection title and accession path (`Clinton Presidential Library,
  Electronic Records, National Security Council Email; FOIA collection
  2006-0995-F`).
* Keep content in a single paragraph and separate factual clauses with
  semicolons. Examples of final clauses:
  * `Secret; Nodis.`
  * `Confidential; Immediate.`
  * `Unclassified.`
* Frequently cite drafting / approval info in the middle clause:
  `Drafted by ...; approved by ...;`.
* When the physical description requires additional qualifiers—“Telegram,”
  “Memorandum of conversation,” “No. 12345”—treat each as a semicolon
  clause in the order witnessed in the volume. Cable numbers and handling
  tags appear immediately after the format clause, before classification.
* Transmission data such as “Sent ...” and “Received ...” stay in the same
  sentence. In the 1981–1988 volume they trail the classification, joined
  by semicolons (`Secret; Niact Immediate; Sent ...; Received ...`).

## Editorial annotations

* Provide narrative background immediately after the source note.
* Use multiple paragraphs for longer stories; simple annotations often
  stay within one paragraph.
* Link to related documents with `<ref target="#document-###">Document ###</ref>`.
* Introduce archival research cues with phrases like “The memorandum was
  drafted …”, “According to the President's diary …”.
* Carry `@resp` to attribute responsibility when multiple editors are
  involved.
* Italicise publication titles with `<hi rend="italic">` and wrap foreign
  language titles with `<foreign>`.

## Telegrams

* Identify the document with `@subtype="telegram"` on the enclosing
  `<div type="document">`. Heads follow the pattern “Telegram From … to …”
  and preserve the exact capitalization that appears in print.
* The body heading often includes the sending post and addressee exactly as
  printed (“Telegram From the Embassy in Islamabad to the Department of
  State”). Do not expand or contract geographic qualifiers—retain “in,”
  “to,” and references to bureaus such as “the Mission to the United
  Nations.”
* Include a full dateline in the `<opener>`, combining the origin city,
  calendar date, and Zulu time. Encode the clock value with `<time
  when="YYYY-MM-DDThh:mmZ">` so downstream tools can parse the send time.
* Capture all filing and handling metadata in the source note. After the
  archival citation, record the telegram/cable number, distribution tags
  (for example, “Immediate; Niact Immediate”), and the “Sent …; Received …”
  timestamps as discrete semicolon clauses.
* Preserve the telegraphic front matter as part of the transcription. The
  first paragraph usually begins with a bolded `Subject:` line rendered
  via `<hi rend="bold">Subject:</hi>`, followed by the subject text in the
  same paragraph.
* Keep the cable’s numbered points verbatim. Paragraph numbers (`1.`,
  `2.`) remain inline at the start of each `<p>`, occasionally paired with
  bolded cue words such as `<hi rend="bold">Summary</hi>` or `<hi
  rend="bold">Action Requested</hi>`.
* Close with the signature block inside `<closer>`/`<signed>`, reproducing
  the sender’s surname alone when that is how the original cable closed.
  If the telegram carried an “Cleared by …” line beneath the signature,
  encode it as an additional `<p>` so the clearance remains part of the
  document body.
* When telegrams include a repeat or information addressee list, encode it
  as printed inside the body—typically as an initial paragraph in small
  caps—rather than moving it into notes.

## Cross-reference notes

* Use `note/@type='crossreference'`.
* Begin with “See” / “See also” and include inline `<ref>` anchors.
* Usually appear alongside editorial notes, before or after them.
* End with a terminal period.

