#!/usr/bin/env python3
"""Top-level hardware validate."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "validate_bom_schema.py",
    "validate_cad_tree.py",
    "validate_schematics.py",
]


def main() -> int:
    for s in SCRIPTS:
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / s)], cwd=ROOT)
        if r.returncode:
            return r.returncode
    print("PASS validate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
