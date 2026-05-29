import csv
from pathlib import Path

def test_bom_headers():
    for p in Path("bom").glob("*.csv"):
        row = next(csv.reader(p.open()))
        assert "ref" in row[0].lower() or row[0] == "ref"
