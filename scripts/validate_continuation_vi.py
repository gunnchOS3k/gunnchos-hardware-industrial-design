#!/usr/bin/env python3
"""Static validation for Continuation VI public-engineerability + EDA closure."""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def need(path: Path, msg: str | None = None) -> None:
    if not path.exists():
        ERRORS.append(msg or f"missing {path.relative_to(ROOT)}")


def main() -> int:
    need(ROOT / "docs/full_product_family/PUBLIC_ENGINEERABILITY_GATE.md")
    need(ROOT / "docs/full_product_family/OPEN_DOCUMENTATION_ALTERNATIVE_AUDIT.md")
    need(ROOT / "docs/full_product_family/PLACEHOLDER_SCAN_CONTINUATION_VI.md")
    need(ROOT / "docs/full_product_family/CERT_DIGITAL_PREP.md")
    need(ROOT / "docs/full_product_family/TOKENS.md")
    need(ROOT / "scripts/run_family_kicad_cli.sh")

    tokens = (ROOT / "docs/full_product_family/TOKENS.md").read_text(encoding="utf-8")
    for tok in [
        "STUDENT_BLOCKED_NDA",
        "DSXL_BLOCKED_NDA",
        "HANDHELD_PUBLIC_PINOUT_EDA_COMPLETE",
        "DOCK_TB4_EDA_COMPLETE",
        "RING_EDA_DT_PARITY_NOTES_COMPLETE",
        "PUBLIC_ENGINEERABILITY_GATE_OPTION3_ADLINK_NDA_EXTERNAL",
    ]:
        if tok not in tokens:
            ERRORS.append(f"TOKENS.md missing {tok}")

    not_claimed = tokens.split("Explicitly NOT claimed", 1)
    if len(not_claimed) < 2 or "FULL_HARDWARE_DESIGN_RELEASE_COMPLETE" not in not_claimed[1]:
        ERRORS.append("FULL_HARDWARE_DESIGN_RELEASE_COMPLETE must remain explicitly not claimed")

    pin_csv = ROOT / "device_designs/handheld_hybrid/docs/radxa_nx5_public_pinout_table.csv"
    need(pin_csv)
    if pin_csv.exists():
        rows = list(csv.DictReader(pin_csv.open(encoding="utf-8")))
        if len(rows) != 260:
            ERRORS.append(f"handheld pinout csv expected 260 rows, got {len(rows)}")
        if any(r.get("evidence") != "PUBLIC_PINOUT" for r in rows):
            ERRORS.append("all handheld pin rows must be PUBLIC_PINOUT")

    net_path = ROOT / "device_designs/handheld_hybrid/manufacturing/netlist.json"
    need(net_path)
    if net_path.exists():
        net = json.loads(net_path.read_text(encoding="utf-8"))
        if net.get("evidence_class") != "PUBLIC_PINOUT":
            ERRORS.append("handheld netlist evidence_class must be PUBLIC_PINOUT")
        if net.get("pin_count") != 260:
            ERRORS.append("handheld netlist pin_count must be 260")

    dock_path = ROOT / "device_designs/dock/manufacturing/netlist.json"
    need(dock_path)
    if dock_path.exists():
        dock = json.loads(dock_path.read_text(encoding="utf-8"))
        if dock.get("controller_mpn") != "JHL8440" or dock.get("retimer_mpn") != "JHL9040R":
            ERRORS.append("dock controller/retimer MPNs incorrect")
        if "JHL9480" not in dock.get("forbidden", []):
            ERRORS.append("dock must forbid JHL9480")

    gate = ROOT / "docs/full_product_family/PUBLIC_ENGINEERABILITY_GATE.md"
    if gate.exists():
        gtxt = gate.read_text(encoding="utf-8")
        if "Option 3" not in gtxt:
            ERRORS.append("public engineerability gate must select Option 3")

    for rel in [
        "device_designs/student_14_5/docs/com_carrier_icd.md",
        "device_designs/ds_xl_coder/docs/dual_edp_icd.md",
    ]:
        p = ROOT / rel
        if p.exists():
            t = p.read_text(encoding="utf-8")
            if "NARROW_NDA" not in t and "BLOCKED_NDA" not in t:
                ERRORS.append(f"{rel} must remain NDA-honest")

    if ERRORS:
        print("FAIL continuation-vi")
        for e in ERRORS:
            print(" -", e)
        return 1
    print("PASS continuation-vi static validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
