#!/usr/bin/env python3
"""Audit NXP-0 package inventory and print gate token block."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NXP = ROOT / "hardware_v1" / "open_custom_nxp"


def main() -> int:
    if not NXP.is_dir():
        print("FAIL: open_custom_nxp missing")
        return 1

    files = sorted(p.relative_to(ROOT).as_posix() for p in NXP.rglob("*") if p.is_file())
    print(f"NXP-OPEN AUDIT: {len(files)} files under hardware_v1/open_custom_nxp/")
    for f in files:
        print(f"  {f}")

    gates_path = NXP / "NXP2_GATES.json"
    if not gates_path.exists():
        gates_path = NXP / "NXP0_GATES.json"
    if not gates_path.exists():
        print("FAIL: NXP2_GATES.json / NXP0_GATES.json missing")
        return 1
    g = json.loads(gates_path.read_text())
    keys = [
        "NXP_OPEN_CUSTOM_TRACK_IMPLEMENTATION_STARTED",
        "NXP_PUBLIC_COLLATERAL_INDEX_COMPLETE",
        "NXP_PUBLIC_PINMAP_UNDERSTOOD",
        "NXP_PUBLIC_POWER_ARCHITECTURE_UNDERSTOOD",
        "NXP_PUBLIC_MEMORY_TOPOLOGY_UNDERSTOOD",
        "CPB0_OPEN_SCHEMATIC_STARTED",
        "CPB0_OPEN_SCHEMATIC_ERC_PASS",
        "CPB0_OPEN_PCB_STARTED",
        "CPB0_OPEN_PCB_DRC_PASS",
        "CPB0_OPEN_READY_FOR_FAB",
        "EVT_PENDING",
        "DVT_PENDING",
        "PVT_PENDING",
        "PHYSICAL_HARDWARE_VALIDATED",
        "NEXT_HARDWARE_ACTION",
        "NEXT_OWNER_ACTION",
    ]
    print("--- token block ---")
    for k in keys:
        v = g.get(k)
        if isinstance(v, bool):
            print(f"{k}={str(v).lower()}")
        else:
            print(f"{k}={v}")
    print("--- end ---")
    print("NXP-OPEN AUDIT PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
