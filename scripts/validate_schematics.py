#!/usr/bin/env python3
"""Validate KiCad project stubs exist per device."""
from pathlib import Path
import sys

DEVICES = ["student_14_5", "handheld_hybrid", "ds_xl_coder", "wearables_arena_set"]
ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    missing = []
    for d in DEVICES:
        base = ROOT / "electrical" / d / "kicad"
        for ext in (".kicad_pro", ".kicad_sch", ".kicad_pcb"):
            p = base / f"{d}{ext}"
            if not p.exists():
                missing.append(str(p))
    if missing:
        print("FAIL schematics", missing)
        return 1
    print("PASS validate-schematics (EVT-1 stubs — ERC/DRC pending for H3)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
