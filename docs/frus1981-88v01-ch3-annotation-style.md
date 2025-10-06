# FRUS Annotation Close-Read — Volume 1981–1988, Book I, Chapter 3

Chapter 3 of *Foreign Relations of the United States, 1981–1988, Volume I (Foundations of Foreign Policy)*
presents the Reagan administration's effort to articulate a comprehensive national security
strategy during 1982–1984. The documents mix internal National Security Council (NSC) memoranda,
National Security Decision Directives (NSDDs), and major presidential addresses delivered in the
United States and abroad. The notes below distil the annotation patterns that recur in the printed
chapter so that compilers can mirror the published presentation when preparing TEI.

> **Use with the general Volume I memo.** Pair these reminders with
> [`frus1981-88v01-annotation-style.md`](./frus1981-88v01-annotation-style.md) for cross-volume rules on
> headings, source-note sequencing, and attachment handling. The bullets that follow highlight
> Chapter 3–specific wrinkles.

## 1. Document 13 — Memorandum from Clark to President Reagan (National Security Strategy Options)

* Retain the triple cue lines (`<hi rend="bold">To:</hi>`, `From:`, `Subject:`) inside the `<opener>` and
  keep "Subject: National Security Strategy" on its own paragraph. The printed memorandum uses
  bold cue labels followed by an em dash before the addressees; encode the dash as plain text.
* The body opens with a numbered options list (I, II, III) that is printed flush-left without
  additional indentation. Encode each option as a separate `<p>` beginning with the Roman numeral
  and period (for example, `I.`) rather than using `<list>`/`<item>`.
* Clark summarises interagency clearance in a closing paragraph (`State, Defense, and JCS concur`).
  Keep this sentence in the body instead of moving it into the source note.
* The source note follows the semicolon chain `Reagan Library, Executive Secretariat, NSC: National
  Security Decision Directive Files; memorandum; Top Secret; Sensitive.` Include any hand-written
  marginalia mentioned in the book as a trailing clause (`with marginal notes by the President`).

## 2. Document 14 — National Security Decision Directive 32 (U.S. National Security Strategy)

* The `<head>` prints the directive number in small caps (`<hi rend="smallcaps">NSDD 32</hi>`) followed
  by the topic line on a second line. Keep the Presidential signature block inside
  `<closer><signed>Ronald Reagan</signed></closer>` with the printed date.
* NSDD 32 contains hierarchical paragraph numbering (I.A.1). Encode the alphanumeric sequence as
  inline text at the start of each `<p>`. Only promote to nested `<list>` structures where the
  printed directive uses indentation plus bullet symbols (for example, `—` for subpoints).
* Attachments labelled "Annex A" and "Annex B" are not printed in the chapter. Represent each with a
  `note type="source"` containing the book's language (`Annexes not printed.`) rather than creating
  empty `<div type="attachment">` stubs.
* The source note cites the NSC Institutional Files with series and case-file numbers. Follow the
  printed ordering: repository (`Reagan Library, NSC Institutional Files`), collection (`NSDD File`),
  specific case (`No. 32`), document description (`directive`), and classification (`Top Secret`).

## 3. Document 15 — National Security Strategy of the United States (Public Version)

* This public statement reproduces the unclassified booklet released alongside NSDD 32. The
  `<head>` uses the genre `Paper` followed by the subtitle. Keep "The White House, Washington" in the
  dateline even though it repeats the repository.
* The printed pamphlet divides sections with `I.`, `II.`, etc., and italicised subtitles. Encode each
  as `<head>` elements nested inside `<div type="section">` wrappers to preserve the booklet's
  hierarchy. Use `<hi rend="italic">` for the italicised subtitles.
* When the text includes bullet-style strategic objectives, represent them as `<list rend="bulleted">`
  with `<item>` children. Each bullet begins with an em dash in print; preserve the dash inside the
  `<item>` content.
* The source note acknowledges both the NSC file copy and the published pamphlet. After the archival
  clause, add `Published as <hi rend="italic">National Security Strategy of the United States</hi>
  (Washington: The White House, January 1983).`

## 4. Document 16 — Address to the British Parliament ("Westminster Speech")

* The `<opener>` includes the venue (`Palace of Westminster`) and city (`London`). Encode the delivery
  date (`June 8, 1982`) in `@when` on the `<date>`, but leave the time attribute empty because the
  printed text does not provide clock time.
* Stage directions such as `[Applause]` occur mid-paragraph. Retain the brackets exactly as printed
  and avoid wrapping them in `<note>`. Treat the short italicised foreign phrases (for example,
  `pax Britannica`) with `<foreign xml:lang="la">` if the language is specified.
* The source note cites the Public Papers volume in addition to the speechwriting file. Follow the
  order: repository (`Reagan Library, White House Office of Speechwriting`), file information
  (folder title, draft status), publication clause (`Published in <hi rend="italic">Public Papers of
  the Presidents: Ronald Reagan, 1982, Book I</hi>, pp. ###–###.`), and broadcast credit if the book
  lists one.
* Footnotes often identify British press reactions or parliamentary procedure. Keep newspaper titles
  italicised and cite Hansard references with the chamber and column numbers as printed.

## 5. Document 17 — Remarks to the National Association of Evangelicals ("Evil Empire" Speech)

* Encode the dateline as `Orlando, Florida, March 8, 1983`. The speech prints a thematic subtitle
  on the first paragraph—`"The March of Freedom"`—which should remain within the opening `<p>`.
* This address contains multiple rhetorical quotations from the Founders. Wrap block quotations with
  `<quote>` elements when the text sets them off as separate paragraphs; leave inline quotations as
  plain text with quotation marks.
* When the printed book shows `[Laughter]` or `[Applause]`, maintain them verbatim. Combine multiple
  cues within a single set of brackets (`[Applause and laughter]`).
* The source note links the speechwriting files, the Public Papers citation, and the audiovisual
  release from the White House Television Office. Include the videotape identifier when listed in the
  published volume.

## 6. Document 18 — NSDD 75 (U.S. Relations with the Soviet Union)

* Headings follow the same pattern as Document 14, with `<hi rend="smallcaps">NSDD 75</hi>` preceding
  the topic line. The directive contains three major pillars—political, economic, and ideological—that
  the printed text sets off with capitalised labels. Represent each pillar as a separate paragraph
  beginning with `<hi rend="bold">Political:</hi>` etc.
* NSDD 75 includes embedded subparagraphs that begin with `(a)`, `(b)`, `(c)`. Preserve the parenthetical
  markers as plain text within the paragraph. Only convert to `<list>` when the original uses true
  bulleting.
* The book notes a lengthy annex on implementation measures that is not printed. Encode a source note
  after the directive text explaining the omission and pointing to the archival citation for the
  annex.
* The source note again references the NSC Institutional Files but emphasises the case file title
  (`Soviet Union (NSDD 75)`). Retain the classification clause `Top Secret; Sensitive.` exactly as
  printed.

## 7. Document 19 — National Security Strategy Decision Memorandum Covering Implementation

* This short memorandum conveys Presidential approval of implementation steps. It uses only `To:` and
  `From:` lines without a subject. Preserve the exact ordering of addressees (Vice President first,
  then Secretaries) and encode multiple recipients within the same paragraph separated by commas.
* The memorandum ends with an instruction paragraph (`Implementation will be coordinated by ...`). Keep
  this as part of the body rather than the source note.
* The source note references the NSC Executive Secretariat's "NSDD 75 Implementation" folder. Include
  the filing case number and classification (`Secret`).

## 8. Footnote Patterns Specific to Chapter 3

* Footnotes frequently cross-reference earlier documents in the chapter. Use
  `<ref target="#doc-14">Document 14</ref>` syntax and list multiple documents in a single footnote
  separated by semicolons.
* When citing the published `National Security Strategy of the United States`, italicise the title and
  include the publication month and year exactly as in print (January 1983). Subsequent references can
  shorten to `National Security Strategy, 1983` if the book does so.
* Diaries and appointment logs appear in notes that situate speeches within the President's schedule.
  Cite them as `Reagan Library, President's Daily Diary, March 8, 1983.` without additional
  punctuation before the classification clause.

Sticking to these document-specific cues will keep Chapter 3 encodings aligned with the finished
volume and ensure the learned Schematron captures the subtleties unique to the national security
strategy rollout.
