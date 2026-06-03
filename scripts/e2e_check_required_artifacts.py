#!/usr/bin/env python3
from pathlib import Path
import sys

DEVICES = ["student_14_5", "handheld_hybrid", "ds_xl_coder", "wearables_arena_set"]
ROOT = Path(__file__).resolve().parents[1]

REQ = [
    "docs/00_START_HERE.md",
    "REQUIREMENTS.md",
    "results/e2e/hardware_e2e_report.md",
    "rf_wireless/common/WIRELESS_ROADMAP.md",
    "compliance/common/COMPLIANCE_MASTER_MATRIX.md",
    "shared_contracts/hardware_os_device_profile.schema.json",
]

for d in DEVICES:
    REQ += [
        f"results/device_reports/{d}_report.md",
        f"results/contracts/{d}_hardware_profile.json",
        f"results/manufacturing/{d}_package_index.md",
        f"electrical/{d}/kicad/{d}.kicad_sch",
        f"bom/{d}/bom.csv",
    ]


def main() -> int:
    missing = [p for p in REQ if not (ROOT / p).exists()]
    if missing:
        print("FAIL", missing)
        return 1
    print("PASS hardware e2e")
    return 0


if __name__ == "__main__":
    sys.exit(main())
