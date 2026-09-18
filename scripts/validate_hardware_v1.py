#!/usr/bin/env python3
"""Validate Hardware v1.0 / HW1B / HW1C campaign package — honest fail-closed checks."""
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
    "REPORT_SECTION_15_HW1B_A_TO_T.md",
    "REPORT_SECTION_24_HW1C_A_TO_Z.md",
    "control/CAMPAIGN_CONTROL_AUDIT.md",
    "control/CAMPAIGN_CONTROL_AUDIT.json",
    "decisions/DECISION_LEDGER.md",
    "decisions/DECISION_LEDGER.json",
    "contracts/OS_HARDWARE_V1_CONTRACT.md",
    "contracts/OS_HARDWARE_V1_CONTRACT.json",
    "bom/MAINLINE_BOM_INDEX.md",
    "bom/MAINLINE_CUSTOM_BOM.csv",
    "bom/REFERENCE_CONTROL_BOM.csv",
    "bom/EXPERIMENTAL_BOM_INDEX.md",
    "bom/AVL.md",
    "bom/handheld_evt_mule_bom.csv",
    "bom/rings_mainline_bom.csv",
    "reference_platform_0/REFERENCE_PLATFORM_0.md",
    "reference_platform_0/REFERENCE_PLATFORM_0.json",
    "reference_platform_0/RP0_STAGE_MODEL.md",
    "reference_platform_0/RP0_A_COMPUTE_PLATFORM.md",
    "reference_platform_0/RP0_A_DOCK_VALIDATION_PATH.md",
    "reference_platform_0/RP0_A_PROCUREMENT_BOM.csv",
    "reference_platform_0/RP0_A_PROCUREMENT_GUIDE.md",
    "reference_platform_0/RP0_A_BRINGUP_MATRIX.csv",
    "rp0b/HW1B_STARTING_BLOCKER_SNAPSHOT.json",
    "rp0b/BLOCKER_CLOSURE_MATRIX.md",
    "rp0b/BLOCKER_CLOSURE_MATRIX.json",
    "devices/rings/NRF54L15_PACKAGE_STRATEGY.md",
    "devices/ds_xl/DUAL_DISPLAY_ARCHITECTURE.md",
    "devices/dock/CUSTOM_DOCK_VENDOR_COLLATERAL_REQUIREMENTS.md",
    "radio/FN990B40_RP0_A_AVL.md",
    "vendor_evidence/nordic/README.md",
    "vendor_evidence/nordic/PCA10156_HW_FILES_METADATA.json",
    "vendor_access/RP0_B_VENDOR_ACCESS_PACKET.md",
    "vendor_access/AMD_CUSTOM_PLATFORM_ACCESS_PACKET.md",
    "custom_mainline/HW1C_STARTING_STATE.json",
    "custom_mainline/CUSTOM_FIRST_ARCHITECTURE_DOCTRINE.md",
    "custom_mainline/PLATFORM_CORE_V1.md",
    "custom_mainline/DEVICE_SOC_SELECTION_MATRIX.md",
    "custom_mainline/COMMON_PLATFORM_BLOCKS.md",
    "custom_mainline/BOARD_REUSE_STRATEGY.md",
    "custom_mainline/FIRMWARE_OWNERSHIP_BOUNDARY.md",
    "custom_mainline/MEMORY_TOPOLOGY_DECISION.md",
    "custom_mainline/KNOWLEDGE_MAP.md",
    "custom_mainline/CUSTOM_MAINLINE_COMPLEXITY_REGISTER.md",
    "custom_mainline/LEARNING_GATES.md",
    "custom_mainline/cpb0/PRD.md",
    "custom_mainline/cpb0/SYSTEM_BLOCK_DIAGRAM.md",
    "custom_mainline/cpb0/POWER_TREE.md",
    "custom_mainline/cpb0/CLOCK_RESET_MAP.md",
    "custom_mainline/cpb0/INTERFACE_MATRIX.csv",
    "custom_mainline/cpb0/DEBUG_PLAN.md",
    "custom_mainline/cpb0/PRELIMINARY_BOM.csv",
    "custom_mainline/cpb0/SCHEMATIC_SHEET_PLAN.md",
    "custom_mainline/cpb0/PCB_CONSTRAINT_PLAN.md",
    "custom_mainline/cpb0/BRINGUP_PLAN.md",
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
    "EXP-COM-HPC-MODULAR-001",
    "EXP-DSXL-X100-001",
    "EXP-P100-AI-001",
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

CLOSED_CLASSIFICATIONS = {
    "CLOSED_PUBLIC_EVIDENCE",
    "CLOSED_BY_ARCHITECTURE_CHANGE",
    "NOT_NEEDED_FOR_RP0_A",
    "STILL_VENDOR_GATED_FOR_RP0_B",
    "OWNER_ACTION_REQUIRED",
}

LEARNING_GATES = [
    "CUSTOM_SOC_PINMAP_UNDERSTOOD",
    "CUSTOM_POWER_TREE_UNDERSTOOD",
    "CUSTOM_DDR_TOPOLOGY_UNDERSTOOD",
    "CUSTOM_PCIE_TOPOLOGY_UNDERSTOOD",
    "CUSTOM_USB4_TOPOLOGY_UNDERSTOOD",
    "CUSTOM_DISPLAY_TOPOLOGY_UNDERSTOOD",
    "CUSTOM_EC_ARCHITECTURE_UNDERSTOOD",
    "CUSTOM_BOOT_CHAIN_UNDERSTOOD",
    "CUSTOM_DEBUG_ARCHITECTURE_UNDERSTOOD",
    "CUSTOM_MANUFACTURING_FLOW_UNDERSTOOD",
]


def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)


def validate_hw1b_fail_closed(gates: dict, errors: list[str]) -> None:
    """HW1B fail-closed semantics (preserved)."""
    if gates.get("RP0_A_COTS_PROCUREMENT_PACKET_READY") is True and gates.get("RP0_B_CUSTOM_READY_FOR_FAB") is True:
        fail("RP0-A COTS ready must not imply RP0_B_CUSTOM_READY_FOR_FAB=true without pin-accurate package", errors)
    if gates.get("RP0_A_READY_TO_ORDER") is True and gates.get("REFERENCE_PLATFORM_0_READY_FOR_FAB") is True:
        fail("COTS ready-to-order must not set REFERENCE_PLATFORM_0_READY_FOR_FAB=true", errors)

    if gates.get("REFERENCE_PLATFORM_0_READY_FOR_FAB") != gates.get("RP0_B_CUSTOM_READY_FOR_FAB"):
        fail("REFERENCE_PLATFORM_0_READY_FOR_FAB must equal RP0_B_CUSTOM_READY_FOR_FAB", errors)

    matrix_path = HV1 / "rp0b" / "BLOCKER_CLOSURE_MATRIX.json"
    if matrix_path.is_file():
        matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
        by_id = {b["id"]: b for b in matrix.get("blockers", [])}
        for bid in ("EXT-COM-HPC-400PIN", "EXT-JHL8440-BALLMAP", "EXT-JHL9040R-BALLMAP"):
            b = by_id.get(bid)
            if not b:
                fail(f"blocker matrix missing {bid}", errors)
                continue
            if b.get("classification") not in CLOSED_CLASSIFICATIONS:
                fail(f"{bid} classification invalid: {b.get('classification')}", errors)
            if b.get("classification") in {"CLOSED_PUBLIC_EVIDENCE", "CLOSED_BY_ARCHITECTURE_CHANGE"}:
                fail(f"{bid} must remain vendor-gated for RP0-B (got {b.get('classification')})", errors)
            if b.get("rp0_b_blocking") is not True:
                fail(f"{bid} must block RP0-B", errors)
            if b.get("rp0_a_blocking") is True:
                fail(f"{bid} must not block RP0-A after COTS path", errors)
            if not b.get("evidence_path") or not (ROOT / b["evidence_path"]).is_file():
                fail(f"{bid} missing evidence path file", errors)

        for bid in ("EXT-DSXL-DUAL-EDP", "UNRES-NRF54L15-FOOTPRINT", "UNRES-FN990B40-AVL"):
            b = by_id.get(bid)
            if not b:
                fail(f"blocker matrix missing closed blocker {bid}", errors)
                continue
            if b.get("classification") not in {
                "CLOSED_PUBLIC_EVIDENCE",
                "CLOSED_BY_ARCHITECTURE_CHANGE",
            }:
                fail(f"{bid} expected closed classification, got {b.get('classification')}", errors)
            if not b.get("evidence_path") or not (ROOT / b["evidence_path"]).is_file():
                fail(f"{bid} closed without evidence file", errors)

    dock_path = HV1 / "reference_platform_0" / "RP0_A_DOCK_VALIDATION_PATH.md"
    if dock_path.is_file():
        text = dock_path.read_text(encoding="utf-8").lower()
        if "do not" not in text or "custom" not in text:
            fail("RP0-A dock path must state COTS results do not certify custom dock PCB", errors)

    rings_path = HV1 / "devices" / "rings" / "NRF54L15_PACKAGE_STRATEGY.md"
    if rings_path.is_file():
        text = rings_path.read_text(encoding="utf-8")
        if "RING_EVT_ELECTRICAL_PLATFORM" not in text or "CSP47" not in text:
            fail("rings strategy must distinguish QFN48/DK vs CSP47", errors)
        if "wearable-form-factor validation" not in text.lower() and "wearable" not in text.lower():
            fail("rings strategy must warn DK ≠ wearable validation", errors)

    if gates.get("PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING") is not True:
        fail("PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING must remain true", errors)
    radio = HV1 / "radio" / "FN990B40_RP0_A_AVL.md"
    if radio.is_file():
        t = radio.read_text(encoding="utf-8")
        if "FN990B40W01T010300" not in t:
            fail("FN990 AVL must record exact MPN FN990B40W01T010300", errors)
        if "PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING" not in t:
            fail("FN990 AVL must keep antenna design pending", errors)

    disp = HV1 / "devices" / "ds_xl" / "DUAL_DISPLAY_ARCHITECTURE.md"
    if disp.is_file():
        t = disp.read_text(encoding="utf-8").lower()
        if "dual native edp" in t and "not" not in t:
            fail("display architecture appears to claim dual native eDP without negation", errors)
        if "ddi" not in t or "edp" not in t:
            fail("display architecture must document eDP + DDI", errors)

    bringup = HV1 / "reference_platform_0" / "RP0_A_BRINGUP_MATRIX.csv"
    if bringup.is_file():
        with bringup.open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row.get("current_state") != "UNTESTED_PENDING_PHYSICAL":
                    fail(f"bring-up row not untested: {row.get('test')}", errors)

    bom = HV1 / "reference_platform_0" / "RP0_A_PROCUREMENT_BOM.csv"
    if bom.is_file():
        with bom.open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                for col in ("price", "stock", "lead_time"):
                    if row.get(col) != "VERIFY_AT_PURCHASE":
                        fail(f"procurement {row.get('item_id')} {col} must be VERIFY_AT_PURCHASE", errors)
                if row.get("physical_purchase_status") != "NOT_PURCHASED":
                    fail(f"procurement {row.get('item_id')} must be NOT_PURCHASED", errors)


def validate_hw1c_fail_closed(gates: dict, errors: list[str]) -> None:
    """HW1C custom-first fail-closed semantics."""
    # Alias consistency
    if gates.get("HARDWARE_V1_READY_FOR_EVT_BUILD") != gates.get("CUSTOM_MAINLINE_READY_FOR_EVT_BUILD"):
        fail("HARDWARE_V1_READY_FOR_EVT_BUILD must equal CUSTOM_MAINLINE_READY_FOR_EVT_BUILD", errors)

    # COTS cannot flip custom EVT ready
    if gates.get("RP0_A_READY_TO_ORDER") is True and gates.get("CUSTOM_MAINLINE_READY_FOR_EVT_BUILD") is True:
        fail("COTS RP0-A readiness must not flip CUSTOM_MAINLINE_READY_FOR_EVT_BUILD=true", errors)
    if gates.get("RP0_A_COTS_PROCUREMENT_PACKET_READY") is True and gates.get("CPB0_READY_FOR_FAB") is True:
        fail("COTS packet must not imply CPB0_READY_FOR_FAB=true", errors)

    # COM-HPC cannot be product mainline
    if gates.get("COM_HPC_IS_PRODUCT_MAINLINE") is True:
        fail("COM_HPC_IS_PRODUCT_MAINLINE must be false under custom-first doctrine", errors)
    if gates.get("COM_HPC_CLASSIFICATION") != "REFERENCE_CONTROL_MODULAR_X86":
        fail("COM_HPC_CLASSIFICATION must be REFERENCE_CONTROL_MODULAR_X86", errors)
    if gates.get("MAINLINE_COMPUTE") != "CUSTOM_AMD_PLATFORM_CORE_V1":
        fail("MAINLINE_COMPUTE must be CUSTOM_AMD_PLATFORM_CORE_V1", errors)

    # Vendor access / fab honesty
    if gates.get("CUSTOM_PLATFORM_VENDOR_ACCESS_READY") is not False:
        fail("CUSTOM_PLATFORM_VENDOR_ACCESS_READY must be false without acquired AMD collateral", errors)
    for k in ("CPB0_SCHEMATIC_READY", "CPB0_PCB_READY", "CPB0_READY_FOR_FAB", "CUSTOM_MAINLINE_READY_FOR_EVT_BUILD"):
        if gates.get(k) is not False:
            fail(f"{k} must be false without real EDA/collateral", errors)

    # Learning gates false without collateral
    for k in LEARNING_GATES:
        if gates.get(k) is not False:
            fail(f"learning gate {k} must be false where AMD collateral missing", errors)

    # Architecture frozen digitally
    if gates.get("CUSTOM_MAINLINE_ARCHITECTURE_FROZEN") is not True:
        fail("CUSTOM_MAINLINE_ARCHITECTURE_FROZEN must be true after HW1C doctrine pivot", errors)

    # Preferred next action
    if gates.get("NEXT_OWNER_ACTION") != "ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL":
        fail(
            f"NEXT_OWNER_ACTION must be ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL, got {gates.get('NEXT_OWNER_ACTION')!r}",
            errors,
        )
    if gates.get("OPTIONAL_OWNER_ACTION") != "ORDER_RP0_A_COTS_CONTROL_KIT":
        fail(
            f"OPTIONAL_OWNER_ACTION must be ORDER_RP0_A_COTS_CONTROL_KIT, got {gates.get('OPTIONAL_OWNER_ACTION')!r}",
            errors,
        )

    # Doctrine files must reject inventing pin compatibility
    soc = HV1 / "custom_mainline" / "DEVICE_SOC_SELECTION_MATRIX.md"
    if soc.is_file():
        t = soc.read_text(encoding="utf-8").lower()
        pin_ok = ("pin compatibility" in t or "pin-compatible" in t) and (
            "not assumed" in t
            or "not assume" in t
            or "not proof" in t
            or "without amd confirmation" in t
            or "do **not** treat" in t
            or "do not treat" in t.replace("*", "")
        )
        if not pin_ok:
            fail("SoC matrix must state pin compatibility is not assumed", errors)

    doctrine = HV1 / "custom_mainline" / "CUSTOM_FIRST_ARCHITECTURE_DOCTRINE.md"
    if doctrine.is_file():
        t = doctrine.read_text(encoding="utf-8")
        for needle in ("MAINLINE_CUSTOM", "REFERENCE_CONTROL", "EXPERIMENTAL_VARIANT"):
            if needle not in t:
                fail(f"doctrine missing {needle}", errors)

    # Mainline custom BOM must not classify COM-HPC as MAINLINE_CUSTOM
    mcb = HV1 / "bom" / "MAINLINE_CUSTOM_BOM.csv"
    if mcb.is_file():
        with mcb.open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                joined = ",".join(row.values()).upper()
                if "COM-HPC" in joined or "COM_HPC" in joined:
                    fail("MAINLINE_CUSTOM_BOM must not contain COM-HPC product architecture rows", errors)
                if (row.get("class") or "") != "MAINLINE_CUSTOM":
                    fail(f"MAINLINE_CUSTOM_BOM row class must be MAINLINE_CUSTOM: {row.get('item_id')}", errors)

    rcb = HV1 / "bom" / "REFERENCE_CONTROL_BOM.csv"
    if rcb.is_file():
        with rcb.open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if (row.get("class") or "") != "REFERENCE_CONTROL":
                    fail(f"REFERENCE_CONTROL_BOM mixed class: {row.get('item_id')}", errors)
                if row.get("physical_purchase_status") not in {None, "", "NOT_PURCHASED"}:
                    if row.get("physical_purchase_status") != "NOT_PURCHASED":
                        fail("reference control items must remain NOT_PURCHASED", errors)

    # Decision ledger must adopt custom Platform Core
    ledger_path = HV1 / "decisions" / "DECISION_LEDGER.json"
    if ledger_path.is_file():
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        compute = next((d for d in ledger.get("decisions", []) if d.get("id") == "DEC-COMPUTE-001"), None)
        if not compute:
            fail("DEC-COMPUTE-001 missing", errors)
        else:
            mainline = (compute.get("mainline") or "").upper()
            if "PLATFORM CORE" not in mainline and "RYZEN EMBEDDED" not in mainline:
                fail("DEC-COMPUTE-001 must adopt Platform Core / Ryzen Embedded custom mainline", errors)
            if "COM-HPC" in mainline and "REFERENCE" not in mainline:
                # allow mention only if clearly not claiming COM-HPC as mainline compute
                if "ADOPTED" in (compute.get("state") or "") and mainline.startswith("COM-HPC"):
                    fail("DEC-COMPUTE-001 must not keep COM-HPC as adopted product mainline", errors)

    # AMD access packet must not invent restricted pin maps
    amd = HV1 / "vendor_access" / "AMD_CUSTOM_PLATFORM_ACCESS_PACKET.md"
    if amd.is_file():
        t = amd.read_text(encoding="utf-8")
        if "NDA_REQUIRED" not in t:
            fail("AMD access packet must classify NDA_REQUIRED artifacts", errors)
        if "does not submit" not in t.lower() and "will not" not in t.lower():
            fail("AMD access packet must state Cursor does not submit agreements", errors)

    # CPB0 cannot claim ready for fab in docs
    for rel in (
        "custom_mainline/cpb0/PRD.md",
        "custom_mainline/cpb0/SCHEMATIC_SHEET_PLAN.md",
        "custom_mainline/cpb0/PCB_CONSTRAINT_PLAN.md",
    ):
        p = HV1 / rel
        if p.is_file():
            t = p.read_text(encoding="utf-8")
            if "CPB0_READY_FOR_FAB=true" in t.replace(" ", ""):
                fail(f"{rel} must not claim CPB0_READY_FOR_FAB=true", errors)

    # Experiment registry hierarchy
    reg = HV1 / "experiments" / "REGISTRY.json"
    if reg.is_file():
        r = json.loads(reg.read_text(encoding="utf-8"))
        ids = {e.get("id") for e in r.get("experiments", [])}
        for needed in ("EXP-COM-HPC-MODULAR-001", "EXP-DSXL-X100-001", "EXP-P100-AI-001"):
            if needed not in ids:
                fail(f"registry missing {needed}", errors)
        hier = r.get("hierarchy") or {}
        mainline = (hier.get("mainline") or "").upper()
        if "CUSTOM" not in mainline or "AMD" not in mainline:
            fail("experiment hierarchy mainline must be custom AMD motherboard", errors)


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
    gates: dict = {}
    if gates_path.is_file():
        gates = json.loads(gates_path.read_text(encoding="utf-8"))
        must_false = [
            "HARDWARE_V1_READY_FOR_EVT_BUILD",
            "CUSTOM_MAINLINE_READY_FOR_EVT_BUILD",
            "REFERENCE_PLATFORM_0_READY_FOR_FAB",
            "RP0_B_CUSTOM_READY_FOR_FAB",
            "CPB0_READY_FOR_FAB",
            "CPB0_SCHEMATIC_READY",
            "CPB0_PCB_READY",
            "CUSTOM_PLATFORM_VENDOR_ACCESS_READY",
            "PHYSICAL_HARDWARE_VALIDATED",
            "CERTIFICATION_COMPLETE",
            "MANUFACTURING_VALIDATED",
            "DIGITAL_FABRICATION_PASS",
            "RFQ_SENT",
            "COM_HPC_IS_PRODUCT_MAINLINE",
        ]
        must_true = [
            "EVT_PENDING",
            "DVT_PENDING",
            "PVT_PENDING",
            "PHYSICAL_PENDING",
            "RP0_A_COTS_PROCUREMENT_PACKET_READY",
            "RP0_A_READY_TO_ORDER",
            "RP0_A_PHYSICAL_BUILD_PENDING",
            "RP0_A_BRINGUP_PENDING",
            "PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING",
            "CUSTOM_MAINLINE_ARCHITECTURE_FROZEN",
            "SOFTWARE_RC1_BASELINES_UNTOUCHED",
        ]
        for k in must_false:
            if gates.get(k) is not False:
                fail(f"gate {k} must be false (honest); got {gates.get(k)!r}", errors)
        for k in must_true:
            if gates.get(k) is not True:
                fail(f"gate {k} must be true; got {gates.get(k)!r}", errors)
        next_action = gates.get("NEXT_OWNER_ACTION")
        next_gate = gates.get("NEXT_GATE")
        if not next_action and not next_gate:
            fail("must set NEXT_OWNER_ACTION or NEXT_GATE", errors)
        validate_hw1b_fail_closed(gates, errors)
        validate_hw1c_fail_closed(gates, errors)

    ledger_path = HV1 / "decisions" / "DECISION_LEDGER.json"
    if ledger_path.is_file():
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        for d in ledger.get("decisions", []):
            st = d.get("state")
            if st not in DECISION_STATES:
                fail(f"decision {d.get('id')} has invalid state {st!r}", errors)
        rings = next((d for d in ledger.get("decisions", []) if d.get("id") == "DEC-RINGS-001"), None)
        if rings:
            if rings.get("RING_EVT_ELECTRICAL_PLATFORM") != "QFN48/DK reference":
                fail("DEC-RINGS-001 must set RING_EVT_ELECTRICAL_PLATFORM=QFN48/DK reference", errors)
            if rings.get("RING_FORM_FACTOR_CANDIDATE") != "CSP47":
                fail("DEC-RINGS-001 must set RING_FORM_FACTOR_CANDIDATE=CSP47", errors)

    for bom_name in ("handheld_evt_mule_bom.csv", "rings_mainline_bom.csv", "MAINLINE_CUSTOM_BOM.csv"):
        bom = HV1 / "bom" / bom_name
        if not bom.is_file():
            continue
        with bom.open(encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                qty = (row.get("qty") or "0").strip()
                status = (row.get("status") or "").strip().upper()
                mpn = (row.get("MPN") or row.get("mpn") or row.get("mpn_or_class") or "").upper()
                joined = ",".join(row.values()).upper()
                if qty not in {"0", ""} and (
                    status in {"EXPERIMENTAL", "EXPERIMENTAL_COMPARE", "EXPERIMENT_ONLY"}
                    or mpn.startswith("EXP-")
                    or "EXPERIMENT_ONLY" in joined
                ):
                    fail(f"{bom_name} mixes experimental qty>0 row: {row}", errors)
                if "HISTORICAL_ONLY" in status and qty not in {"0", ""}:
                    fail(f"{bom_name} historical row must have qty=0: {row}", errors)

    for path in HV1.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".json", ".csv", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for snip in FORBIDDEN_CLAIM_SNIPPETS:
            if snip in text.replace(" ", ""):
                if "must be false" in text.lower() or "remain" in text.lower():
                    continue
                continue

    for rel in (
        "DIGITAL_MANUFACTURING_READINESS.md",
        "DIGITAL_TO_PHYSICAL_HANDOFF.md",
        "device_designs/student_14_5/digital_release/INDEX.json",
        "manufacturing/EVT_DVT_PVT_PLAN.md",
    ):
        if not (ROOT / rel).exists():
            fail(f"reconcile target missing (do not discard): {rel}", errors)

    rc1 = HV1 / "SOFTWARE_RC1_INTERFACE_IMPACT_REGISTER.json"
    if rc1.is_file():
        r = json.loads(rc1.read_text(encoding="utf-8"))
        if r.get("baselines_modified_in_this_repo_campaign") is not False:
            fail("RC1 baselines_modified_in_this_repo_campaign must be false", errors)
        if r.get("software_freeze_identity") != "v1.0.0-rc.1":
            fail("RC1 freeze identity must remain v1.0.0-rc.1", errors)

    if errors:
        print("HARDWARE_V1_VALIDATE: FAIL")
        for e in errors:
            print(f" - {e}")
        return 1

    print("HARDWARE_V1_VALIDATE: PASS")
    print("DIGITAL_ARCHITECTURE_PACKAGE_COMPLETE=true")
    print("HARDWARE_V1_DIGITAL_ARCHITECTURE_COMPLETE=true")
    print("CUSTOM_MAINLINE_ARCHITECTURE_FROZEN=true")
    print("CUSTOM_PLATFORM_VENDOR_ACCESS_READY=false")
    print("CUSTOM_MAINLINE_READY_FOR_EVT_BUILD=false")
    print("HARDWARE_V1_READY_FOR_EVT_BUILD=false")
    print("CPB0_READY_FOR_FAB=false")
    print("REFERENCE_PLATFORM_0_READY_FOR_FAB=false")
    print("RP0_A_COTS_PROCUREMENT_PACKET_READY=true")
    print("RP0_A_READY_TO_ORDER=true")
    print("PHYSICAL_HARDWARE_VALIDATED=false")
    print("NEXT_OWNER_ACTION=ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL")
    print("OPTIONAL_OWNER_ACTION=ORDER_RP0_A_COTS_CONTROL_KIT")
    return 0


if __name__ == "__main__":
    sys.exit(main())
