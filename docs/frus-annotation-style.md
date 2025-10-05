# FRUS Annotation Style (Model Volume frus1989-92v31)

Summary of annotation conventions observed in the reference volume. Use
this as the textual companion to the in-app quick reference.

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

## Cross-reference notes

* Use `note/@type='crossreference'`.
* Begin with “See” / “See also” and include inline `<ref>` anchors.
* Usually appear alongside editorial notes, before or after them.
* End with a terminal period.

