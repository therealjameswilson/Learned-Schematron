# FRUS Annotation Style (Model Volume frus1989-92v31)

Summary of annotation conventions observed in the reference volume. Use
this as the textual companion to the in-app quick reference.

## Source notes

* Always begin with the literal `Source:` label (rendered bold in TEI via
  `<hi rend="bold">`).
* Follow the pattern: repository → record group or collection → document
  format → classification / dissemination.
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

## Cross-reference notes

* Use `note/@type='crossreference'`.
* Begin with “See” / “See also” and include inline `<ref>` anchors.
* Usually appear alongside editorial notes, before or after them.
* End with a terminal period.

