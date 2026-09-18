#!/usr/bin/env python3
"""Fail-closed digital fab-release auditor for CPB0-O (NXP-1)."""
from __future__ import annotations
import csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NXP = ROOT / "hardware_v1" / "open_custom_nxp"

def main() -> int:
    errors: list[str] = []
    gates_path = NXP / "NXP1_GATES.json"
    if not gates_path.exists():
        print("FAIL: missing NXP1_GATES.json"); return 1
    gates = json.loads(gates_path.read_text())

    # Exact SoC
    if "MIMX9596" not in str(gates.get("selected_soc_opn", "")):
        errors.append("selected_soc_opn missing MIMX9596*")
    if not gates.get("NXP_EXACT_SOC_OPN_FROZEN"):
        errors.append("NXP_EXACT_SOC_OPN_FROZEN not true")

    # Pinmap
    ball = NXP / "CPB0_OPEN_SOC_BALLMAP.csv"
    if not ball.exists():
        errors.append("missing CPB0_OPEN_SOC_BALLMAP.csv")
    else:
        rows = list(csv.DictReader(ball.open(encoding="utf-8")))
        unr = [r for r in rows if str(r.get("unresolved","")).lower() in {"true","1","yes"}]
        if unr:
            errors.append(f"{len(unr)} unresolved ballmap rows")
        if gates.get("NXP_PUBLIC_PINMAP_UNDERSTOOD") and unr:
            errors.append("pinmap gate true with unresolved rows")

    # Memory rules
    ddr = NXP / "CPB0_OPEN_DDR_LENGTH_RULES.csv"
    if ddr.exists():
        drows = list(csv.DictReader(ddr.open(encoding="utf-8")))
        if any(r.get("status") == "UNRESOLVED" for r in drows):
            if gates.get("NXP_PUBLIC_MEMORY_TOPOLOGY_UNDERSTOOD"):
                errors.append("memory topology gate true with unresolved DDR rules")
            errors.append("required memory length rules unresolved")

    # Schematic / ERC / footprints / PCB / DRC / stackup / SI-PI / BOM / DFx / release / bringup
    checks = [
        ("CPB0_OPEN_SCHEMATIC_READY", gates.get("CPB0_OPEN_SCHEMATIC_READY")),
        ("CPB0_OPEN_SCHEMATIC_ERC_PASS", gates.get("CPB0_OPEN_SCHEMATIC_ERC_PASS")),
        ("CPB0_OPEN_FOOTPRINT_LIBRARY_VALIDATED", gates.get("CPB0_OPEN_FOOTPRINT_LIBRARY_VALIDATED")),
        ("CPB0_OPEN_PCB_READY", gates.get("CPB0_OPEN_PCB_READY")),
        ("CPB0_OPEN_PCB_DRC_PASS", gates.get("CPB0_OPEN_PCB_DRC_PASS")),
        ("CPB0_OPEN_STACKUP_DEFINED", gates.get("CPB0_OPEN_STACKUP_DEFINED")),
        ("CPB0_OPEN_BOM_AVL_DIGITAL_PASS", gates.get("CPB0_OPEN_BOM_AVL_DIGITAL_PASS")),
        ("CPB0_OPEN_DFM_DFA_DFT_PASS", gates.get("CPB0_OPEN_DFM_DFA_DFT_PASS")),
        ("CPB0_OPEN_BRINGUP_ENGINEERING_READY", gates.get("CPB0_OPEN_BRINGUP_ENGINEERING_READY")),
        ("NXP_OPEN_NO_NDA_BOUNDARY_PASS", gates.get("NXP_OPEN_NO_NDA_BOUNDARY_PASS")),
    ]
    for name, val in checks:
        if name in {"CPB0_OPEN_STACKUP_DEFINED","CPB0_OPEN_DFM_DFA_DFT_PASS","CPB0_OPEN_BRINGUP_ENGINEERING_READY","NXP_OPEN_NO_NDA_BOUNDARY_PASS"}:
            if not val:
                errors.append(f"{name} must be true for fab audit")
        else:
            if not val:
                errors.append(f"{name} is not true")

    # Release outputs
    manifest = NXP / "release" / "cpb0_open" / "A0" / "MANIFEST.json"
    if manifest.exists():
        man = json.loads(manifest.read_text())
        if man.get("fab_outputs_present") is True:
            errors.append("manifest claims fab outputs present without proof")
    else:
        errors.append("missing release MANIFEST.json")

    # Physical claims forbidden
    if gates.get("PHYSICAL_HARDWARE_VALIDATED") is True:
        errors.append("PHYSICAL_HARDWARE_VALIDATED must be false")
    if gates.get("NDA_ACCEPTED") is True:
        errors.append("NDA_ACCEPTED must be false")

    # Document existence alone must not set READY_FOR_FAB
    ready = gates.get("CPB0_OPEN_READY_FOR_FAB") is True
    audit_pass = len(errors) == 0
    if ready and not audit_pass:
        errors.append("READY_FOR_FAB true but audit failed")

    # Update gate file honesty for audit token
    gates["CPB0_OPEN_DIGITAL_FAB_AUDIT_PASS"] = False  # always false while errors
    if audit_pass:
        gates["CPB0_OPEN_DIGITAL_FAB_AUDIT_PASS"] = True
    # do not write gates here — reporter owns tokens; print only

    if errors:
        print("CPB0-OPEN FAB AUDIT FAIL")
        for e in errors:
            print(f"  - {e}")
        print("CPB0_OPEN_DIGITAL_FAB_AUDIT_PASS=false")
        print("CPB0_OPEN_READY_FOR_FAB=false")
        return 1
    print("CPB0-OPEN FAB AUDIT PASS")
    print("CPB0_OPEN_DIGITAL_FAB_AUDIT_PASS=true")
    return 0

if __name__ == "__main__":
    sys.exit(main())
