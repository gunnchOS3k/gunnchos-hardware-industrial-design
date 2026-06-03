#!/usr/bin/env python3
import csv
from pathlib import Path
import sys

def main():
    paths = list(Path("bom").glob("**/*.csv"))
    if not paths:
        paths = list(Path("devices").glob("**/bom_target.csv"))
    for p in paths:
        rows = list(csv.reader(p.open()))
        if not rows:
            print("FAIL empty", p)
            return 1
    print("PASS bom schema")
    return 0

if __name__ == "__main__":
    sys.exit(main())
