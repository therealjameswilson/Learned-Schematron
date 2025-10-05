# FRUS Annotation Style Notes

## Access to Reference Volume

Attempts to download the model volume `frus1981-88v01.xml` from the HistoryAtState repository were blocked by the sandbox's outbound network policy (HTTP 403). This prevented a direct inspection of that specific volume during this session. The curl command below shows the failure state.

```
curl -L https://raw.githubusercontent.com/HistoryAtState/frus/master/volumes/frus1981-88v01.xml -o /tmp/frus1981-88v01.xml
```

## Inferences from the Existing Learning Script

The `scripts/learn_frus.py` utility bundled with this project encodes several assumptions about FRUS TEI annotation practice:

- **Dateline dating uses ISO-formatted `@when` attributes.** The analyzer visits every `<div type="document">` dateline and records the shape of each `date/@when` value, categorising them into `YYYY`, `YYYY-MM`, `YYYY-MM-DD`, or other patterns. The generated Schematron requires that `@when` be present and conform to one of these ISO formats.
- **Notes carry controlled `@type` values.** All `<note>` elements are expected to have a `type` attribute, and the generated Schematron constrains the value to a known whitelist collected from the observed volumes (defaulting to `source`, `editorial`, `textual`, and `crossreference` if no data are available). When the analyzer runs, it also inventories the free-text content, flagging entries that begin with "Source:"—an indicator that source notes follow a standard introductory formula.
- **Lexical consistency checks matter.** The script aggregates counts of plain `US`, punctuated `U.S.`, and numeric ranges such as `12-13`, signaling that FRUS style guidance may regulate spelling and hyphenation patterns across the corpus.

These behaviors collectively outline the annotation style expectations that the learned Schematron enforces. Once the reference volume is reachable, running `python scripts/learn_frus.py --tei tei --out schemas --reports reports` with the volume inside `tei/` will populate detailed frequency tables for the dateline shapes, note types, and source note phrasings.

## Next Steps When the Volume Is Available

1. Place `frus1981-88v01.xml` into a `tei/` directory at the project root.
2. Run the learning script as shown above to collect observed annotation patterns and regenerate `schemas/frus-learned.sch`.
3. Review `reports/learned-summary.json` for concrete counts of each annotation practice, then update this document with explicit examples drawn from the volume.
