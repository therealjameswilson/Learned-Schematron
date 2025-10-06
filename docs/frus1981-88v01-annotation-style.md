# FRUS Annotation Style Notes — Volume 1981–1988, Book I (Foundations of Foreign Policy)

This memo captures the annotation patterns that compilers should follow when working with the
1981–1988 sub-series, Volume I (*Foundations of Foreign Policy*). Use it alongside the general
[FRUS Annotation Style](./frus-annotation-style.md) checklist and confirm all guidance against the
released TEI for `frus1981-88v01.xml` when local access is available. Treat the published
presentation of Chapter 1 (documents 1–16) as the baseline reference. Its mix of presidential
statements, National Security Decision Directives, and NSC memoranda illustrates the full range of
structural and apparatus conventions you should mirror in new encodings.

> **Scope.** Volume I foregrounds presidential decision-making frameworks, strategy papers, and
> major public statements that articulate the Reagan administration's foreign policy foundations.
> Many items are policy overviews drawn from the National Security Council system or the White
> House speechwriting apparatus. The mix of born-digital memoranda, formal directives, and
> published speeches introduces annotation wrinkles that compilers should handle consistently.

## 1. Document wrappers and headings

* Wrap each selection in `<div type="document" xml:id="doc-###">` using the running number printed
  in the book. Preserve the headline line exactly as published—genre label plus participants
  (for example, `Memorandum From the President's Assistant for National Security Affairs
  (Clark) to President Reagan`).
* When the heading includes parenthetical identifiers—most commonly the principal's surname—encode
  the parentheses verbatim. Titles rendered in small caps in print continue to use
  `<hi rend="smallcaps">`.
* Presidential statements and speeches often use the pattern `Statement by President Reagan` or
  `Address by President Reagan to the Nation`. Retain the prepositions ("by," "before") and the
  audience description even when lengthy. Do not collapse honorifics (for example, keep
  `to the National Association of Evangelicals in Orlando`). Compare with Document 11 in Chapter 1,
  where the full venue description remains inside the `<head>`.
* Formal directives (National Security Decision Directives, National Security Study Directives)
  print their directive number in the heading. Keep the numeric component inside the `<head>` and
  encode the directive acronym in small caps when the printed source does so (`<hi rend="smallcaps">NSDD 32</hi>`).
  See Document 4 for a concrete example of how the book balances directive numbering with sender
  attribution.

## 2. Openers, datelines, and distribution blocks

* Memoranda retain explicit `To:` and `From:` lines, bolded with `<hi rend="bold">`. For directives,
  encode the distribution list exactly as printed—typically a series of cabinet-level addressees
  or principals. Use consecutive paragraphs rather than lists unless the source clearly sets the
  distribution as bullet points.
* Many presidential remarks supply only the place, date, and time of delivery. Encode these in the
  `<opener>` using `<dateline>` and `<time when="YYYY-MM-DDThh:mm">`. If the published source omits
  a time, omit the `@when` attribute rather than guessing. Document 9 demonstrates the preferred
  placement of the delivery time immediately after the venue.
* When the document introduces a subtitle (for example, a speech theme or venue), keep it in the
  first paragraph of the body instead of moving it into the header.

## 3. Body text and structural cues

* Preserve paragraph numbering used in study directives and strategy papers. These often follow a
  Roman numeral/letter/number outline (`I.`, `A.`, `1.`). Encode each level as plain text at the
  start of the paragraph; do not attempt to model the hierarchy with nested `<list>` elements
  unless the printed form uses clear indentation and bullet markers.
* For speeches, maintain stage directions such as `[Applause]` or `[Laughter]` verbatim inside
  brackets. Treat them as inline text rather than editorial notes.
* Strategy papers frequently include embedded tables summarising policy options. Encode these with
  `<table>` and `<row>`/`<cell>` if the layout can be recovered; otherwise, retain the prose form
  and indicate column separators with em dashes as printed. Document 6 shows how an options matrix
  is preserved as prose when the print edition collapses the layout.
* Directives conclude with signature blocks (`Ronald Reagan`) and, occasionally, authentication
  attestations. Wrap the signature in `<closer><signed>Ronald Reagan</signed></closer>` and keep the
  attestations as additional paragraphs following the signature.

## 4. Source notes for published and archival items

* Begin every apparatus paragraph with a bold `Source:` label. Follow the semicolon-delimited
  hierarchy: repository or publication → collection → physical format → classification → handling.
* When the document reproduces a published speech, cite the print or audiovisual source after the
  archival reference: `Source: Reagan Library, White House Office of Speechwriting Files; speech
  draft; undated; published in Public Papers of the Presidents: Ronald Reagan, 1983, Book I,
  pp. 413–420.` Use `<hi rend="italic">` for publication titles.
* Public statements that were broadcast but not archived in traditional folders should cite the
  White House Taper or audiovisual collection where applicable (`Ronald Reagan Presidential Library,
  White House Television Office Videotapes`). Note the catalog identifier when printed in the
  volume.
* Directives and memoranda drawn from the National Security Council system should reference the
  Executive Secretariat or NSC institutional files, including folder titles and sequential numbers
  (`National Security Council, Institutional Files, NSDD File, No. 32`).
* Classify the final clause with the handling marking exactly as printed (`Top Secret; Sensitive`).
  Directives occasionally state `Unclassified`. Leave the clause even when seemingly redundant.

## 5. Editorial notes, cross-references, and historiographical context

* Editorial notes frequently situate speeches within policy roll-outs. Begin with a concise context
  sentence (`This address launched the administration's Caribbean Basin Initiative.`) before
  providing archival pointers.
* Use cross-reference notes to connect speeches with underlying policy memoranda. Format as
  `<note type="crossreference">See <ref target="#doc-123">Document 123</ref>.</note>` and include
  additional documents separated by semicolons.
* When identifying published background sources (for example, National Security Strategy reports),
  italicise titles and supply publication details within the note. Keep citations to congressional
  testimony or legislation in the same paragraph, prefaced by `See also`.
* For narratives describing the drafting process, attribute authorship using `@resp` to highlight
  contributions from the Office of the Historian staff or the compiler of record.

## 6. Footnotes and citation conventions

* Footnotes that cite Public Papers entries should follow the template `Public Papers: Reagan,
  1982, Book I, pp. 24–31.` Include the year and book number exactly as printed. For weekly
  compilations use `Weekly Compilation of Presidential Documents` in italics.
* When referencing National Security Decision Directives in footnotes, repeat the directive number
  and include signing information if present (`NSDD 45, August 15, 1982`). Do not assume
  declassification dates—only cite those provided in the printed note.
* Footnotes that refer to the President's Daily Diary or appointment schedules should name the
  specific diary entry (`Reagan Library, President's Daily Diary, March 8, 1983`). Keep the diary
  name in italics when the printed version does so.
* Multi-source footnotes should keep each citation separated by semicolons. When the printed note
  embeds quotations or paraphrases, enclose them within quotation marks in the TEI and use
  `<quote>` if the passage exceeds one sentence.

## 7. Attachments, enclosures, and annexes

* Strategy studies sometimes append option papers or talking point tabs. Encode printed attachments
  as nested `<div type="attachment">` blocks with their own headings and source notes. Where the
  book states `Attachment not printed`, use a `note type="source"` with that language.
* If an annex summarises a public initiative (for example, a fact sheet released alongside a
  speech), capture the fact sheet as an attachment and cite the publication source in its own
  source note.
* When only excerpts of an attachment are printed, add an editorial note explaining the excerpting
  and pointing to the full archival citation.

## 8. Validation workflow reminder

1. Obtain `frus1981-88v01.xml` outside this sandboxed environment (direct HTTPS access to
   `history.state.gov` is currently blocked, returning `403 Forbidden`).
2. Place the TEI file in a local `tei/` directory and run
   `python scripts/learn_frus.py --tei tei --out schemas --reports reports` to refresh the learned
   Schematron rules and identify volume-specific patterns.
3. Inspect `reports/learned-summary.json` for any deviations (for example, new note types or
   `<list>` renderings) and update this memo with confirmed findings.

Keeping these conventions front of mind will help compilers encode Volume I in a way that matches
both the published book and the Office of the Historian's digital presentation.

## 9. Chapter 6 (Global Strategy and Defense Posture) — finished-volume observations

* **Document mix.** Chapter 6 leans heavily on National Security Decision Directives (NSDDs),
  National Security Study Directives (NSSDs), and high-level strategy papers that set global
  priorities. Expect long-form memoranda, presidential study directives, and speech drafts rather
  than short correspondence. Mirror the printed genre labels exactly (`National Security Decision
  Directive Number 32`) and retain any subtitle that states the policy theme (`United States
  National Security Strategy`).
* **Directive typography.** The printed NSDD facsimiles render their directive acronym in full
  small caps across headings and salutation lines. Encode these stretches with
  `<hi rend="smallcaps">NSDD</hi>` (or `<hi rend="smallcaps">NSSD</hi>`) and keep the spelled-out
  phrase (“National Security Decision Directive”) in title case as printed rather than normalising
  to uppercase. Directive numbers remain part of the `<head>` text.
* **Distribution blocks and signature attestations.** NSDDs and NSSDs in this chapter carry dense
  addressee lists plus certification language such as “Copy furnished to:”. Preserve the layout as
  sequential paragraphs inside the `<opener>` or immediately after it—do not convert to unordered
  lists. Close each directive with `<closer>`/`<signed>` for the President’s signature and capture
  authentication statements (`For the President:`) as following paragraphs to reflect the archival
  copy.
* **Embedded annexes.** Strategic reviews frequently attach implementation matrices, contingency
  force tables, or regional annexes. Encode each printed attachment as `<div type="attachment">`
  with its own `<head>` and source note. When the book prints only excerpts (“Annex A (excerpt):”)
  add an editorial note explaining the excerpted nature and point to the archival folder holding the
  complete attachment.
* **Source note nuances.** Source lines for NSDDs routinely cite the National Security Council’s
  Institutional Files with both the NSDD file number and the directive title. Keep the order `Source:
  Reagan Library, National Security Council, Institutional Files, NSDD File; NSDD 75; Top Secret;`
  before transmittal language such as `Sent for information to ...`. When a directive references a
  subsequent declassification or release authority, reproduce the parenthetical exactly rather than
  summarising it.
* **Editorial background.** Finished annotations in this chapter contextualise directives by tying
  them to earlier policy debates (for example, National Security Council meetings or prior study
  directives). Follow the pattern `The directive evolved from NSSM 11-82 ...` and use
  `<ref target="#doc-###">` to link to those prerequisite documents. When summarising public
  roll-outs—speeches or fact sheets that explain an NSDD—place the publication citation in the note
  using `<hi rend="italic">Public Papers of the Presidents</hi>` or the relevant fact sheet title.
* **Footnotes.** Citations often pair archival references with published doctrine (`Department of
  Defense, <hi rend="italic">Annual Report</hi>, Fiscal Year 1984`). Separate each source with
  semicolons and retain quoted phrases from the document text within `<quote>` to preserve emphasis.
