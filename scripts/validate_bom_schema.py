#!/usr/bin/env python3
import csv
from pathlib import Path
import sys

def main():
    for p in Path("bom").glob("*.csv"):
        rows = list(csv.reader(p.open()))
        if not rows:
            print("FAIL empty", p)
            return 1
    print("PASS bom schema")
    return 0

if __name__ == "__main__":
    sys.exit(main())
