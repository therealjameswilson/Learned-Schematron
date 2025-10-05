    .PHONY: build validate
    build:
	python scripts/learn_frus.py --tei tei --out schemas --reports reports

    validate:
	java -jar /usr/local/bin/schxslt.jar -s schemas/frus-learned.sch -i tei/sample.xml -o out-report.html || true
