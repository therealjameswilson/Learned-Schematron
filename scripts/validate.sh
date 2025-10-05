#!/usr/bin/env bash
set -euo pipefail
if [[ ! -f schemas/frus-learned.sch ]]; then
  echo "No schemas/frus-learned.sch found. Run: python scripts/learn_frus.py --tei tei --out schemas --reports reports"
  exit 1
fi
if [[ ! -f tei/sample.xml ]]; then
  echo "Place a sample TEI as tei/sample.xml"
  exit 0
fi
java -jar /usr/local/bin/schxslt.jar -s schemas/frus-learned.sch -i tei/sample.xml -o out-report.html || true
echo "Wrote out-report.html"
