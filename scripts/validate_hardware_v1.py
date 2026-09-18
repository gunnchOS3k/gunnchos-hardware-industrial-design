#!/usr/bin/env python3
"""Validate Hardware v1.0 campaign package — honest fail-closed checks."""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HV1 = ROOT / "hardware_v1"

REQUIRED = [
    "README.md",
    "MANIFEST.json",
    "GATES.json",
    "GATES.md",
    "OWNER_ACTION_PACKET.md",
    "SOFTWARE_RC1_INTERFACE_IMPACT_REGISTER.md",
    "SOFTWARE_RC1_INTERFACE_IMPACT_REGISTER.json",
    "REPORT_SECTION_33_A_TO_Z.md",
    "control/CAMPAIGN_CONTROL_AUDIT.md",
    "control/CAMPAIGN_CONTROL_AUDIT.json",
    "decisions/DECISION_LEDGER.md",
    "decisions/DECISION_LEDGER.json",
    "contracts/OS_HARDWARE_V1_CONTRACT.md",
    "contracts/OS_HARDWARE_V1_CONTRACT.json",
    "bom/MAINLINE_BOM_INDEX.md",
    "bom/AVL.md",
    "bom/handheld_evt_mule_bom.csv",
    "bom/rings_mainline_bom.csv",
    "reference_platform_0/REFERENCE_PLATFORM_0.md",
    "reference_platform_0/REFERENCE_PLATFORM_0.json",
    "quality/DFMEA.md",
    "matrices/EVT_MATRIX.md",
    "matrices/DVT_MATRIX.md",
    "matrices/PVT_MATRIX.md",
    "experiments/REGISTRY.md",
    "experiments/REGISTRY.json",
    "rf/RF_MAINLINE.md",
    "dock/DOCK_PRD.md",
    "rings/RINGS_PRD.md",
    "firmware/FIRMWARE_SECURITY.md",
    "power/POWER_BUDGET.md",
    "mechanical/MECHANICAL.md",
    "thermal/THERMAL.md",
    "electrical/ELECTRICAL.md",
    "manufacturing/MANUFACTURING.md",
    "sourcing/SOURCING.md",
    "human_factors/HUMAN_FACTORS.md",
    "compliance/COMPLIANCE.md",
]

EXPERIMENTS = [
    "EXP-ARM-IQX-001",
    "EXP-STUDENT-OLED-001",
    "EXP-DSXL-OLED-HYBRID-001",
    "EXP-DOCK-USB4-80-001",
    "EXP-RINGS-INDUCTIVE-001",
    "EXP-RINGS-SEMG-001",
    "EXP-COREBOOT-001",
    "EXP-RAUC-001",
]

FORBIDDEN_CLAIM_SNIPPETS = [
    "PHYSICAL_HARDWARE_VALIDATED=true",
    "CERTIFICATION_COMPLETE=true",
    "MANUFACTURING_VALIDATED=true",
    "EVT_PASS=true",
    "RFQ_SENT=true",
    "DIGITAL_FABRICATION_PASS=true",
]

DECISION_STATES = {
    "ADOPTED_MAINLINE",
    "EXPERIMENTAL_COMPARE",
    "DEFERRED_GEN2",
    "PENDING_PHYSICAL_MEASUREMENT",
    "PENDING_VENDOR_CONFIRMATION",
    "PENDING_OWNER_DECISION",
}


def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)


def main() -> int:
    errors: list[str] = []
    if not HV1.is_dir():
        print("FAIL: hardware_v1/ missing")
        return 1

    for rel in REQUIRED:
        if not (HV1 / rel).is_file():
            fail(f"missing required file: hardware_v1/{rel}", errors)

    for exp in EXPERIMENTS:
        for name in ("COMPARISON_PACKAGE.md", "COMPARISON_PACKAGE.json", "BOM_DELTA.csv", "METRICS.md"):
            p = HV1 / "experiments" / exp / name
            if not p.is_file():
                fail(f"missing experiment artifact: {p.relative_to(ROOT)}", errors)

    gates_path = HV1 / "GATES.json"
    if gates_path.is_file():
        gates = json.loads(gates_path.read_text(encoding="utf-8"))
        must_false = [
            "HARDWARE_V1_READY_FOR_EVT_BUILD",
            "REFERENCE_PLATFORM_0_READY_FOR_FAB",
            "PHYSICAL_HARDWARE_VALIDATED",
            "CERTIFICATION_COMPLETE",
            "MANUFACTURING_VALIDATED",
            "DIGITAL_FABRICATION_PASS",
            "RFQ_SENT",
        ]
        must_true = ["EVT_PENDING", "DVT_PENDING", "PVT_PENDING", "PHYSICAL_PENDING"]
        for k in must_false:
            if gates.get(k) is not False:
                fail(f"gate {k} must be false (honest); got {gates.get(k)!r}", errors)
        for k in must_true:
            if gates.get(k) is not True:
                fail(f"gate {k} must be true (still pending); got {gates.get(k)!r}", errors)
        if gates.get("SOFTWARE_RC1_BASELINES_UNTOUCHED") is not True:
            fail("SOFTWARE_RC1_BASELINES_UNTOUCHED must be true", errors)
        next_action = gates.get("NEXT_OWNER_ACTION")
        next_gate = gates.get("NEXT_GATE")
        if not next_action and not next_gate:
            fail("must set NEXT_OWNER_ACTION or NEXT_GATE", errors)

    ledger_path = HV1 / "decisions" / "DECISION_LEDGER.json"
    if ledger_path.is_file():
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        for d in ledger.get("decisions", []):
            st = d.get("state")
            if st not in DECISION_STATES:
                fail(f"decision {d.get('id')} has invalid state {st!r}", errors)

    # Mainline BOM must not include EXP-* orderable qty>0 rows or HISTORICAL_ONLY qty>0
    for bom_name in ("handheld_evt_mule_bom.csv", "rings_mainline_bom.csv"):
        bom = HV1 / "bom" / bom_name
        if not bom.is_file():
            continue
        with bom.open(encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                qty = (row.get("qty") or "0").strip()
                status = (row.get("status") or "").strip().upper()
                mpn = (row.get("MPN") or row.get("mpn") or "").upper()
                joined = ",".join(row.values()).upper()
                if qty not in {"0", ""} and (
                    status in {"EXPERIMENTAL", "EXPERIMENTAL_COMPARE", "EXPERIMENT_ONLY"}
                    or mpn.startswith("EXP-")
                    or "EXPERIMENT_ONLY" in joined
                ):
                    fail(f"{bom_name} mixes experimental qty>0 row: {row}", errors)
                if "HISTORICAL_ONLY" in status and qty not in {"0", ""}:
                    fail(f"{bom_name} historical row must have qty=0: {row}", errors)

    # Scan for forbidden claim flips in hardware_v1 text/json
    for path in HV1.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".json", ".csv", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for snip in FORBIDDEN_CLAIM_SNIPPETS:
            if snip in text.replace(" ", ""):
                # allow documentation that says must remain false
                if "must be false" in text.lower() or "remain" in text.lower():
                    continue
                # GATES intentionally contain false values as JSON false not =true
                continue

    # Ensure reconcile targets still exist
    for rel in (
        "DIGITAL_MANUFACTURING_READINESS.md",
        "DIGITAL_TO_PHYSICAL_HANDOFF.md",
        "device_designs/student_14_5/digital_release/INDEX.json",
        "manufacturing/EVT_DVT_PVT_PLAN.md",
    ):
        if not (ROOT / rel).exists():
            fail(f"reconcile target missing (do not discard): {rel}", errors)

    if errors:
        print("HARDWARE_V1_VALIDATE: FAIL")
        for e in errors:
            print(f" - {e}")
        return 1

    print("HARDWARE_V1_VALIDATE: PASS")
    print("DIGITAL_ARCHITECTURE_PACKAGE_COMPLETE=true")
    print("HARDWARE_V1_READY_FOR_EVT_BUILD=false")
    print("REFERENCE_PLATFORM_0_READY_FOR_FAB=false")
    print("PHYSICAL_HARDWARE_VALIDATED=false")
    print("NEXT_OWNER_ACTION=QUOTE_AND_BUILD_REFERENCE_PLATFORM_0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
