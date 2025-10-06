# FRUS Footnote-Annotation Training Data (Volumes 1981-88 and 1989-92)

## Purpose

The Foreign Relations of the United States (FRUS) series uses footnotes to provide source citations and editorial annotations for each document. These notes are one of the key value-added tasks performed by compilers because they identify archival sources, clarify context and link to other documents. The TEI markup for FRUS files must encode footnotes consistently so that the notes render correctly on the Office of the Historian web site and in ebooks. This training guide extracts examples from released volumes of Volume I (Foundations of Foreign Policy) and Volume III (Soviet Union) in the 1981–1988 sub-series and demonstrates how to encode them. The same principles apply to later volumes (1989–1992) when they become available.

## 1. Structure of Footnote Encoding

FRUS documents are encoded in TEI. A document (`<div type="document">`) contains a series of paragraphs and footnote call-outs. Each footnote call-out is a `<ref>` element with the `@target` attribute pointing to the `xml:id` of the footnote. The actual footnote text is stored in a `<note>` element in the same document with `@xml:id` matching the target ID and `@place="foot"`. The following simplified pattern covers most cases:

```xml
<div type="document">
  <p>Paragraph text with a <ref target="#fn-1">1</ref> footnote call-out.</p>
  <note xml:id="fn-1" place="foot">Footnote text that appears at the bottom of the document.</note>
</div>
```

