# FRUS Annotation Style (Model Volume frus1981-88v13)

This quick reference distills the annotation patterns that compilers
should verify when working from **Foreign Relations of the United States,
1981–1988, Volume XIII**. The guidance assumes access to the TEI edition of
the volume and pairs field observation with the general FRUS style rules
already captured in `docs/frus-annotation-style.md`.

> **Access note**: The sandbox used for this training guide currently
> blocks outbound HTTPS requests to `raw.githubusercontent.com`, so the
> XML edition of the volume cannot be inspected directly from this
> environment. Download the TEI file outside the sandbox and place it in
> the repository’s `tei/` directory before running the learning scripts
> or verifying the examples described below.

## Review workflow

1. **Acquire the TEI file**. Save `frus1981-88v13.xml` to `tei/` and run
   `python scripts/learn_frus.py --tei tei --out schemas --reports reports`
   to regenerate the learned Schematron and frequency reports.
2. **Inspect the heading inventory** in `reports/learned-summary.json` to
   confirm the balance between memoranda, telegrams, intelligence reports,
   and presidential correspondence. This shapes the document templates you
   prioritise for QA checks.
3. **Sample ten documents per genre** to verify that the observed patterns
   match the summaries captured below. Adjust the Schematron or update the
   style notes if you encounter deviations.

## Document headings and front matter

* Expect long multi-clause headings that identify both the author and the
  chain of recipients. Volume XIII focuses on Caribbean Basin diplomacy,
  so many memoranda name inter-agency actors (State, Defense, NSC, CIA) and
  regional bureaus. Preserve punctuation exactly as printed and include all
  role qualifiers (for example, “Assistant Secretary of State for Inter-
  American Affairs”).
* Presidential decisions and National Security Decision Directives appear
  as memoranda or annexes. Retain the numbered directive identifiers in the
  `<head>` text and cross-reference them in annotations where necessary.
* Telegram headers include origin posts such as the Department of State,
  Embassies in Caribbean capitals, and the US Mission to the OAS. Capture
  the Zulu time component in `<time when="…Z">` to support chronology
  queries.

## Source notes

* Primary repositories include the Ronald Reagan Presidential Library,
  National Archives (especially RG 59 Central Foreign Policy File and
  Lot Files), and Department of Defense records. Spell out repository
  names and stack the citation elements with semicolons: repository →
  collection → box/folder → classification and handling (`Secret; Nodis;`
  `Immediate` tags, etc.).
* Intelligence attachments from the CIA or DIA often cite microfilm reels
  or published intelligence summaries. Identify both the originating
  agency and the reproduction medium when present (`CIA Records, Job
  XXX; microfiche`).
* Memoranda that circulated within the White House frequently carry routing
  data (“Sent for action,” “Returned to NSC”). Encode those phrases in the
  source note after the archival citation but before the classification
  clause.

## Editorial notes and cross-references

* Editorial annotations frequently clarify economic assistance programs
  (for example, the Caribbean Basin Initiative), covert operations, or the
  Grenada intervention timeline. Summarise these contexts in coherent
  paragraphs and link related documents using `<ref target="#document-###">`.
* Use cross-reference notes (`@type="crossreference"`) to direct readers to
  National Security Decision Directives, intelligence estimates, or prior
  memoranda that shaped the policy decision under discussion.
* When quoting statutes or presidential statements, italicise publication
  titles with `<hi rend="italic">` and identify public law numbers or NSDD
  identifiers in the text of the note.

## Attachments and supplemental material

* Attachments often include intelligence assessments, talking points, or
  draft public statements. Encode each attachment as a nested `<div`>
  within the parent document, preserving the attachment title verbatim in
  `<head>` and carrying over any classification markings.
* Statistical tables associated with economic assistance packages should
  remain in `<table>` form rather than being flattened into paragraphs.
  Where the printed edition uses column headers in small caps, translate
  them with `<hi rend="smallcaps">`.
* When annexes reproduce National Intelligence Estimates or Interagency
  Group reports, check that `@type` (for example, `report`, `intelligence`) is
  applied consistently and that the signature block includes agency
  acknowledgments.

## Footnotes

* Footnote numbering restarts for each document. Ensure each `<note
  place="foot">` is linked to the correct call-out via matching `xml:id`
  targets.
* Source notes inside footnotes (common when an attachment has its own
  archival trail) should retain the `Source:` label and follow the same
  semicolon-separated structure as the main source note.
* Editorial footnotes often synthesize intelligence reporting or economic
  data. Use multiple paragraphs within a single `<note>` when the printed
  annotation contains bulleted or enumerated context.

## Quality-assurance checklist

* Confirm that every telegram includes `@subtype="telegram"` and captures
  the send/receive times within the source note.
* Ensure that classification strings match the printed order (`Secret;
  Sensitive; Exclusively Eyes Only` rather than rearranging the tags).
* Validate that references to intelligence code names or operations remain
  unexpanded; FRUS retains the printed cover terms unless the annotation
  explains them explicitly.
* Cross-check that attachments flagged as “Tab A/B/C” in memoranda carry
  matching `xml:id` anchors so editors can reference them in notes.

Following this workflow keeps compilers aligned with the annotation style
established in Volume XIII while remaining interoperable with the broader
FRUS TEI corpus.
