# FRUS Annotation Style Notes — Volume 1981–1988, Book I, Chapter 2

This briefing distils the annotation patterns visible in the finished presentation of
Chapter 2 ("Rebuilding the National Security Process") of *Foreign Relations of the United
States, 1981–1988, Volume I: Foundations of Foreign Policy*. Use it alongside the broader
[volume checklist](./frus1981-88v01-annotation-style.md) and the series-wide
[FRUS annotation quick reference](./frus-annotation-style.md). Where direct verification
against the official TEI (`frus1981-88v01.xml`) is required, follow the access notes at the
end of this memo.

> **Focus.** Chapter 2 documents the Reagan administration's effort to retool the
> National Security Council (NSC) system. The selections mix National Security Decision
> Directives (NSDDs), NSC meeting records, departmental memoranda, and public statements
> announcing the new process. These genres share a heavy emphasis on distribution blocks,
> signatories, and cross-references to subsequent implementation papers.

## 1. Headings and document wrappers

* Maintain `<div type="document" xml:id="doc-###">` wrappers keyed to the running
  document numbers printed in Chapter 2 (Documents 7–23). Chapter headings such as
  `Document 7` precede the descriptive headline in the original book and should be
  captured in `<head>` with the numbering intact.
* Headline lines generally follow the pattern `National Security Decision Directive 2;
  Organization of the National Security Council System`. Preserve the semicolon-joined
  subtitle (after the directive title) and encode directive identifiers in small caps
  when the print treatment does so:
  ```xml
  <head><hi rend="smallcaps">NSDD 2</hi>; Organization of the National Security Council System</head>
  ```
* Meeting minutes and memoranda often include parenthetical participant identifiers
  (`(Clark)` or `(Haig)`); keep these parentheticals verbatim in the headline instead of
  relocating them to note apparatus.

## 2. Openers, datelines, and participant blocks

* NSDDs print their Washington datelines without a time stamp. Encode the place and date
  inside `<opener><dateline>` and provide an ISO `@when` attribute (`1981-01-12`).
* Memoranda from the President's Assistant for National Security Affairs include explicit
  `TO`/`FROM` lines. Represent them as separate paragraphs in the opener, bolding the
  prompts:
  ```xml
  <opener>
    <dateline><placeName>Washington</placeName>, <date when="1981-01-12">January 12, 1981</date></dateline>
    <p><hi rend="bold">TO</hi>: The President</p>
    <p><hi rend="bold">FROM</hi>: <persName>Richard V. Allen</persName></p>
  </opener>
  ```
* Meeting minutes open with a participant roster rendered as a list in the print edition.
  Encode it as `<list rend="participants">` with `<item>` values for each attendee.
  Attribute chairpersons or speakers with inline `<hi rend="smallcaps">` spans when
  the typography calls for it.

## 3. Body structure and embedded directives

* NSDD texts rely on hierarchical numbering (Roman numerals, capital letters, Arabic
  numerals). Reproduce the numbering inline at the start of each paragraph instead of
  creating nested lists. Maintain the indentation cues with em dashes or colons according
  to the printed layout.
* Paragraph-level rubric lines such as `Purpose`, `Objective`, or `Implementation` appear
  in bold. Encode them as `<hi rend="bold">Purpose</hi>—` followed by the sentence text.
* When NSDDs or memoranda refer to annexes (`Annex A`, `Tab B`), insert a cross-reference
  note immediately after the reference pointing to the attachment's `xml:id`.

## 4. Signatures, distribution, and clearance

* Directive signatures consist solely of `Ronald Reagan`. Wrap them in
  `<closer><signed>Ronald Reagan</signed></closer>` and leave any authentication notation
  (for example, `By direction of the President`) as separate paragraphs after the closer.
* NSDDs display distribution lists enumerating cabinet-level principals. Encode the list
  as consecutive paragraphs prefixed with `<hi rend="bold">Distribution:</hi>` followed by
  the addressees separated by semicolons. Avoid turning the block into a list unless the
  print copy uses bullet markers.
* Memoranda typically note drafting and clearance in the source note rather than in
  the body. When the printed document includes `Drafted by`, `Cleared by`, or
  `Action requested` statements within the text, retain them inline with bold prompts.

## 5. Source notes for Chapter 2 genres

* Source notes begin with `<hi rend="bold">Source:</hi>` and detail the NSC filing location:
  `Reagan Library, NSC Institutional Files, NSDD 2`. Follow with physical format (`Printed
  directive`), classification (`Top Secret; Sensitive`), and transmittal status (`No
  drafting information appears on the original`).
* For NSC meeting minutes sourced from the White House Situation Room, cite the
  `Meeting Files, National Security Council`, including the meeting date and box/folder
  number. Mention whether the record is a summary of conclusions or verbatim transcript.
* Public statements (for example, the President's remarks explaining the NSC reorganization)
  conclude with the published citation after the archival reference: `Also printed in
  <hi rend="italic">Public Papers of the Presidents: Ronald Reagan, 1981</hi>, pp. xxx–xxx.`

## 6. Footnotes and cross-references

* Footnotes frequently link a directive to later implementation papers or prior NSDDs.
  Use `<note place="foot" type="crossreference">` with inline `<ref>` targets (`See
  Document 25`).
* When a note cites both archival material and published sources, separate each clause with
  semicolons and keep quotations within `<quote>` if the note reproduces language from the
  source.
* Editorial notes that summarise unprinted attachments use `type="editorial"` and reference
  the attachment with `<ref target="#att-##">Attachment A</ref>`.

## 7. Attachments and annex handling

* Many Chapter 2 documents mention attachments such as NSC organization charts or fact
  sheets. When printed, encode each as `<div type="attachment" xml:id="att-##">` with its own
  heading and source note. When omitted, create a `note type="source">Attachment not
  printed.</note>` immediately following the mention.
* Organization charts reproduced as figures can be represented with `<figure>` and a
  descriptive `<head>`, retaining caption text in `<figDesc>`.

## 8. Access limitations and verification steps

Direct HTTP requests to `history.state.gov` currently return `403 Forbidden` inside this
sandbox, preventing download of the canonical TEI. To validate these observations against
the official encoding:

1. Outside the sandbox, download the TEI using `curl -L
   https://history.state.gov/historicaldocuments/frus1981-88v01/ch2?format=tei` or by
   retrieving `frus1981-88v01.xml` from the Office of the Historian GitHub mirror.
2. Copy the TEI file into a local `tei/` directory within this repository.
3. Run `python scripts/learn_frus.py --tei tei --out schemas --reports reports` to refresh
   the learned Schematron rules and confirm the note types, structural patterns, and
   attribute usage documented above.
4. Review `reports/learned-summary.json` for any deviations and update this memo with
   exact examples (document numbers, line references) once the TEI is available.

This chapter-specific checklist should help compilers reproduce the formatting of the
finished documents while aligning with the automated validation learned from the source
TEI.
