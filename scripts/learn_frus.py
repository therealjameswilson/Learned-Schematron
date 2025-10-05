import argparse, re, json
from pathlib import Path
from lxml import etree
from collections import Counter

NS = {"tei": "http://www.tei-c.org/ns/1.0"}

def itertext(e):
    return "".join(e.itertext())

def analyze(path: Path):
    root = etree.parse(str(path))
    dls = root.findall(".//tei:div[@type='document']/tei:opener/tei:dateline", namespaces=NS)
    when_shapes = Counter()
    for dl in dls:
        date = dl.find("./tei:date", namespaces=NS)
        if date is not None and 'when' in date.attrib:
            w = date.attrib['when']
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", w): key="YYYY-MM-DD"
            elif re.fullmatch(r"\d{4}-\d{2}", w): key="YYYY-MM"
            elif re.fullmatch(r"\d{4}", w): key="YYYY"
            else: key="other"
            when_shapes[key]+=1

    notes = root.findall(".//tei:note", namespaces=NS)
    source_notes = []
    types = Counter()
    for n in notes:
        t = n.attrib.get('type')
        if t: types[t]+=1
        text = itertext(n).strip()
        if re.match(r"^\s*Source\s*:", text, re.I):
            source_notes.append(text)

    text_all = itertext(root.getroot())
    us = len(re.findall(r"\bUS\b", text_all))
    u_s = len(re.findall(r"\bU\.S\.\b", text_all))
    hy_ranges = len(re.findall(r"\b\d{2,4}-\d{2,4}\b", text_all))

    return {
        "file": path.name,
        "when_shapes": when_shapes,
        "note_types": types,
        "source_notes": source_notes[:50],
        "count_US": us,
        "count_U.S.": u_s,
        "hyphen_ranges": hy_ranges,
    }

def write_learned(schemas_dir: Path, reports_dir: Path, agg_when, types):
    schemas_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)
    preferred = None
    if agg_when:
        preferred = max(agg_when.items(), key=lambda x: x[1])[0]
    allowed_types = " ".join(sorted(types)) if types else "source editorial textual crossreference"
    default_type = next(iter(sorted(types))) if types else "editorial"

    sch = f"""<schema xmlns="http://purl.oclc.org/dsdl/schematron"
      xmlns:tei="http://www.tei-c.org/ns/1.0"
      xmlns:sqf="http://www.schematron-quickfix.com/validator/process"
      queryBinding="xslt2">
      <title>FRUS TEI House Style — Learned</title>
      <pattern id="date-when">
        <rule context="tei:div[@type='document']/tei:opener/tei:dateline/tei:date">
          <assert test="@when" sqf:fix="addWhen">Dateline <date> must have @when.</assert>
          <assert test="matches(@when,'^\\d{{4}}(-\\d{{2}}(-\\d{{2}})?)?$')" sqf:fix="shapeWhen">Use ISO @when.</assert>
          <sqf:fix id="addWhen"><sqf:add match="." node-type="attribute" target="when">YYYY-MM-DD</sqf:add></sqf:fix>
          <sqf:fix id="shapeWhen"><sqf:add match="." node-type="attribute" target="when">YYYY-MM-DD</sqf:add></sqf:fix>
        </rule>
      </pattern>
      <pattern id="note-type">
        <rule context="tei:note">
          <assert test="@type" sqf:fix="setType">note/@type is required.</assert>
          <assert test="@type and contains('{allowed_types}', @type)">note/@type should be one of: {allowed_types}.</assert>
          <sqf:fix id="setType"><sqf:add match="." node-type="attribute" target="type">{default_type}</sqf:add></sqf:fix>
        </rule>
      </pattern>
    </schema>
    """
    (schemas_dir / "frus-learned.sch").write_text(sch, encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tei", required=True, help="Folder with TEI volumes")
    ap.add_argument("--out", default="schemas")
    ap.add_argument("--reports", default="reports")
    args = ap.parse_args()

    tei_dir = Path(args.tei)
    schemas_dir = Path(args.out)
    reports_dir = Path(args.reports)

    agg_when = Counter()
    types = Counter()
    all_reports = []
    for xml in tei_dir.glob("*.xml"):
        r = analyze(xml)
        all_reports.append(r)
        agg_when.update(r["when_shapes"])
        types.update(r["note_types"])

    write_learned(schemas_dir, reports_dir, agg_when, list(types.elements()))
    (reports_dir / "learned-summary.json").write_text(json.dumps(all_reports, indent=2), encoding="utf-8")
    print("Learned Schematron written to", schemas_dir / "frus-learned.sch")

if __name__ == "__main__":
    main()
