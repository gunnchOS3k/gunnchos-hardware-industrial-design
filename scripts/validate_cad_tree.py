#!/usr/bin/env python3
from pathlib import Path
import sys

REQUIRED = [
    "cad/openscad/common/dimensions.scad",
    "cad/openscad/student_14_5/student_14_5_concept.scad",
    "cad/openscad/handheld_hybrid/handheld_hybrid_concept.scad",
    "cad/openscad/ds_xl_coder/ds_xl_coder_concept.scad",
]

def main():
    missing = [r for r in REQUIRED if not Path(r).exists()]
    if missing:
        print("FAIL", missing)
        return 1
    print("PASS cad tree")
    return 0

if __name__ == "__main__":
    sys.exit(main())
