"""Reference guidelines for FRUS annotation markup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class AnnotationExample:
    """A single curated reminder about a FRUS annotation pattern."""

    heading: str
    description: str
    cues: list[str]
    sample: str


def iter_annotation_guidelines() -> Iterable[AnnotationExample]:
    """Yield annotation reminders distilled from the model FRUS volume."""

    yield AnnotationExample(
        heading="Source notes",
        description=(
            "Source notes begin with the literal label “Source:” followed by repository, location, and metadata about "
            "drafting, transmission, and classification.  The 1989–1992 model volume keeps the whole note inside a "
            "single paragraph, separated by semicolons, and always closes with a terminal period."
        ),
        cues=[
            "`<note type='source'>` with one `<p>` child",
            "Bold label rendered via `<hi rend='bold'>Source:</hi>`",
            "Repository phrases such as “Department of State, Central Files” or “George Bush Presidential Library”",
            "Classification string (“Secret; Nodis.”, “Confidential.”, “Unclassified.”) at the end of the sentence",
            "Intermediate semicolon phrases for drafting, approval, and transmission details",
        ],
        sample=(
            "<note type=\"source\">\n"
            "  <p>\n"
            "    <hi rend=\"bold\">Source:</hi> Department of State, Central Files, 320.1/2-2890; telegram, Secret; Nodis.\n"
            "  </p>\n"
            "</note>"
        ),
    )

    yield AnnotationExample(
        heading="Editorial annotations",
        description=(
            "Editorial annotations contextualise the document and cite related material.  They typically appear "
            "immediately after the source note, make use of `<ref>` elements for cross references, and can carry `@resp` "
            "pointers to identify the editor."
        ),
        cues=[
            "`<note type='editorial'>` often with `@resp` (e.g. `resp='#o1'`)",
            "Multiple `<p>` children when the annotation narrates events",
            "Introductory cues like “The memorandum was drafted by …” or “See Document …”",
            "Inline `<ref target='#...'>Document 123</ref>` cross references",
            "Use of `<foreign>` for non-English titles and `<hi rend='italic'>` for publication names",
        ],
        sample=(
            "<note type=\"editorial\" resp=\"#o1\">\n"
            "  <p>The memorandum was drafted by Scowcroft for President Bush after the NSC meeting.</p>\n"
            "  <p>See also <ref target=\"#document-234\">Document 234</ref> and the President's diary entry for February 14.</p>\n"
            "</note>"
        ),
    )

    yield AnnotationExample(
        heading="Cross-reference notes",
        description=(
            "Cross-reference notes provide navigational links to other FRUS documents or previously published material. "
            "The canonical text starts with “See” or “See also” and points to numbered documents using `<ref>`."
        ),
        cues=[
            "`<note type='crossreference'>` positioned before or after editorial notes",
            "Initial keyword “See” (capitalised) followed by the referenced item",
            "`<ref>` targets that resolve to `#document-XXX` anchors within the volume",
            "Terminal period to close the sentence",
        ],
        sample=(
            "<note type=\"crossreference\">\n"
            "  <p>See <ref target=\"#document-198\">Document 198</ref> for the final version transmitted to Moscow.</p>\n"
            "</note>"
        ),
    )


def guidelines_as_dict() -> list[dict[str, object]]:
    """Return guidelines formatted for JSON/Jinja consumption."""

    return [
        {
            "heading": example.heading,
            "description": example.description,
            "cues": example.cues,
            "sample": example.sample,
        }
        for example in iter_annotation_guidelines()
    ]


__all__ = ["AnnotationExample", "guidelines_as_dict", "iter_annotation_guidelines"]

