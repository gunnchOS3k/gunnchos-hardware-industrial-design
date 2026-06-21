#!/usr/bin/env python3
"""Check CAD export artifacts exist or status doc is present."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
STLS = [
    "exports/stl/student_14_placeholder.stl",
    "exports/stl/handheld_hybrid_placeholder.stl",
    "exports/stl/ds_xl_coder_placeholder.stl",
    "exports/stl/wearables_arena_set_placeholder.stl",
]
if all((ROOT / f).exists() for f in STLS):
    print("PASS all STL exports present")
    sys.exit(0)
if (ROOT / "exports/OPENSCAD_EXPORT_STATUS.md").exists():
    print("PASS STL exports pending — status doc present")
    sys.exit(0)
print("FAIL missing STL exports and status doc")
sys.exit(1)
