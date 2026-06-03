#!/usr/bin/env python3
from pathlib import Path

DEVICES = ["student_14_5", "handheld_hybrid", "ds_xl_coder", "wearables_arena_set"]
ROOT = Path(__file__).resolve().parents[1]
READINESS = "H2"


def main() -> None:
    out_dir = ROOT / "results/device_reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    for d in DEVICES:
        contract = ROOT / "results/contracts" / f"{d}_hardware_profile.json"
        bom = ROOT / "bom" / d / "bom.csv"
        kicad = ROOT / "electrical" / d / "kicad" / f"{d}.kicad_sch"
        body = f"""# Device report — {d}

Readiness: **{READINESS}** (EVT-1 engineering package candidate)

## Evidence present
- KiCad stub: `{kicad.exists()}`
- BOM: `{bom.exists()}`
- Hardware contract: `{contract.exists()}`

## Not claimed
- Manufacture-ready (H3)
- FCC/CE certification
- Field validation
"""
        (out_dir / f"{d}_report.md").write_text(body, encoding="utf-8")
    print("Generated device reports")


if __name__ == "__main__":
    main()
