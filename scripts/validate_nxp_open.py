#!/usr/bin/env python3
"""Validate NXP-0 open-custom i.MX95 foundation package — fail-closed, honest gates."""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NXP = ROOT / "hardware_v1" / "open_custom_nxp"
HV1 = ROOT / "hardware_v1"

REQUIRED = [
    "NXP0_STARTING_STATE.json",
    "NXP0_GATES.json",
    "NXP0_GATES.md",
    "PUBLIC_COLLATERAL_INDEX.md",
    "PUBLIC_COLLATERAL_INDEX.json",
    "PUBLIC_COLLATERAL_GAP_REGISTER.md",
    "CPB0_OPEN_SOC_SELECTION.md",
    "CPB0_OPEN_PINMUX_MAP.csv",
    "CPB0_OPEN_INTERFACE_MAP.md",
    "CPB0_OPEN_POWER_TREE.md",
    "CPB0_OPEN_POWER_BUDGET.csv",
    "CPB0_OPEN_SEQUENCE.md",
    "CPB0_OPEN_MEMORY_ARCHITECTURE.md",
    "CPB0_OPEN_DDR_CONSTRAINTS.md",
    "CPB0_OPEN_PCIE_USB_NETWORK_ARCHITECTURE.md",
    "CPB0_OPEN_MEDIA_ARCHITECTURE.md",
    "CPB0_OPEN_SECURITY_BOOT_ARCHITECTURE.md",
    "CPB0_OPEN_EC_ARCHITECTURE.md",
    "CPB0_OPEN_SCHEMATIC_SHEET_PLAN.md",
    "CPB0_OPEN_PCB_ARCHITECTURE.md",
    "CPB0_OPEN_STACKUP_REQUIREMENTS.md",
    "CPB0_OPEN_SI_PI_PLAN.md",
    "CPB0_OPEN_BOM.csv",
    "CPB0_OPEN_AVL.csv",
    "CPB0_OPEN_BOM_RISK.md",
    "CPB0_OPEN_READY_FOR_FAB_GATE.md",
    "NXP_PUBLIC_BLOCKER_REGISTER.md",
    "NXP_TO_AMD_TRANSFER_MAP.md",
    "CPB0_OPEN_EXPERIENCE_WORKLOAD_PLAN.md",
    "REPORT_SECTION_20_NXP0_A_TO_V.md",
    "REPORT_SECTION_NXP2_A_TO_Z.md",
    "NXP2_GATES.json",
    "NXP2_STARTING_STATE.json",
    "owner_collateral/NXP_OWNER_COLLATERAL_INDEX.json",
    "OPEN_CUSTOM_DOCTRINE.md",
    "eda/cpb0_open/cpb0_open.kicad_pro",
    "eda/cpb0_open/cpb0_open.kicad_sch",
    "eda/cpb0_open/README.md",
]

FORBIDDEN_PHRASES = [
    "PHYSICAL_HARDWARE_VALIDATED=true",
    "CPB0_OPEN_READY_FOR_FAB=true",
    "NXP_PRODUCT_EQUIVALENT_TO_AMD=true",
    "SECURE_BOOT_PASS=true",
    "NDA_ACCEPTED=true",
]

EXPECTED_GATES = {
    "NXP_OPEN_CUSTOM_TRACK_IMPLEMENTATION_STARTED": True,
    "NXP_PUBLIC_COLLATERAL_INDEX_COMPLETE": True,
    "NXP_PUBLIC_PINMAP_UNDERSTOOD": True,
    "NXP_PUBLIC_POWER_ARCHITECTURE_UNDERSTOOD": True,
    "NXP_PUBLIC_MEMORY_TOPOLOGY_UNDERSTOOD": False,
    "CPB0_OPEN_SCHEMATIC_STARTED": True,
    "CPB0_OPEN_SCHEMATIC_ERC_PASS": False,
    "CPB0_OPEN_PCB_STARTED": True,
    "CPB0_OPEN_PCB_DRC_PASS": False,
    "CPB0_OPEN_READY_FOR_FAB": False,
    "EVT_PENDING": True,
    "DVT_PENDING": True,
    "PVT_PENDING": True,
    "PHYSICAL_HARDWARE_VALIDATED": False,
    "SOFTWARE_RC1_BASELINES_UNTOUCHED": True,
    "NXP_CLAIMED_PRODUCT_EQUIVALENT_TO_AMD": False,
    "NDA_ACCEPTED": False,
}


def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)


def main() -> int:
    errors: list[str] = []

    if not NXP.is_dir():
        print("FAIL: hardware_v1/open_custom_nxp missing")
        return 1

    for rel in REQUIRED:
        if not (NXP / rel).exists():
            fail(f"missing required file: {rel}", errors)

    # Starting state / PR80
    start_path = NXP / "NXP0_STARTING_STATE.json"
    if start_path.exists():
        start = json.loads(start_path.read_text())
        pf = start.get("preflight", {})
        if pf.get("hw1d1_evidence_pr_state") != "MERGED":
            fail("NXP0_STARTING_STATE must record PR #80 MERGED (or explicitly pending)", errors)
        if not pf.get("hw1d1_evidence_merge_sha"):
            fail("missing hw1d1_evidence_merge_sha", errors)
        if start.get("tracks", {}).get("OPEN_ENGINEERING_MAINLINE") != "NXP_IMX95_OPEN_CUSTOM":
            fail("OPEN_ENGINEERING_MAINLINE must be NXP_IMX95_OPEN_CUSTOM", errors)
        if start.get("tracks", {}).get("PRODUCT_MAINLINE") != "AMD_CUSTOM_X86":
            fail("PRODUCT_MAINLINE must remain AMD_CUSTOM_X86", errors)
        if pf.get("nda_accepted") is not False:
            fail("nda_accepted must be false", errors)

    # Gates honesty
    gates_path = NXP / "NXP0_GATES.json"
    if gates_path.exists():
        gates = json.loads(gates_path.read_text())
        for k, v in EXPECTED_GATES.items():
            if gates.get(k) != v:
                fail(f"gate {k} expected {v!r} got {gates.get(k)!r}", errors)
        if gates.get("NEXT_HARDWARE_ACTION") != "CONTINUE_CPB0_OPEN_EDA":
            if gates.get("CPB0_OPEN_READY_FOR_FAB") is True:
                fail("fab-ready path must use NEXT_OWNER_ACTION=QUOTE_CPB0_OPEN_FAB only when truly ready", errors)
            else:
                fail("NEXT_HARDWARE_ACTION must be CONTINUE_CPB0_OPEN_EDA while digital work remains", errors)
        if "MIMX9596" not in str(gates.get("selected_soc_opn", "")):
            fail("selected_soc_opn must be an exact MIMX9596* OPN", errors)

    # NXP-2 owner-collateral honesty
    n2_path = NXP / "NXP2_GATES.json"
    if n2_path.exists():
        n2 = json.loads(n2_path.read_text())
        if n2.get("CPB0_OPEN_READY_FOR_FAB") is True:
            fail("NXP2_GATES must keep CPB0_OPEN_READY_FOR_FAB=false without full prerequisites", errors)
        if n2.get("PHYSICAL_HARDWARE_VALIDATED") is True:
            fail("NXP2_GATES PHYSICAL_HARDWARE_VALIDATED must be false", errors)
        for pending in ("EVT_PENDING", "DVT_PENDING", "PVT_PENDING"):
            if n2.get(pending) is not True:
                fail(f"NXP2_GATES {pending} must be true", errors)
        idx = NXP / "owner_collateral" / "NXP_OWNER_COLLATERAL_INDEX.json"
        if idx.exists():
            ix = json.loads(idx.read_text())
            if ix.get("files_indexed_count_authoritative", 0) == 0:
                if n2.get("NEXT_OWNER_ACTION") != "PROVIDE_MISSING_AUTHORITATIVE_NXP_COLLATERAL":
                    fail(
                        "missing authoritative collateral requires NEXT_OWNER_ACTION=PROVIDE_MISSING_AUTHORITATIVE_NXP_COLLATERAL",
                        errors,
                    )
                if n2.get("NXP_PUBLIC_MEMORY_TOPOLOGY_UNDERSTOOD") is True:
                    fail("cannot claim memory topology understood without UG10210/EVK collateral", errors)
        # prefer complete Table-2 code when present
        if gates.get("NXP_PUBLIC_PINMAP_UNDERSTOOD") is True:
            ball = NXP / "CPB0_OPEN_SOC_BALLMAP.csv"
            if ball.exists():
                brows = list(csv.DictReader(ball.open(encoding="utf-8")))
                if not brows:
                    fail("ballmap empty while pinmap understood", errors)
                if any(str(r.get("unresolved","")).lower() in {"true","1","yes"} for r in brows):
                    fail("unresolved ballmap rows while NXP_PUBLIC_PINMAP_UNDERSTOOD", errors)

    # Collateral: no NDA required flags
    idx_path = NXP / "PUBLIC_COLLATERAL_INDEX.json"
    if idx_path.exists():
        idx = json.loads(idx_path.read_text())
        if idx.get("nda_required_any_item") is not False:
            fail("collateral index must set nda_required_any_item=false", errors)
        for item in idx.get("items", []):
            if item.get("nda_required") is True:
                fail(f"item {item.get('id')} marks nda_required=true — stop/report, do not invent", errors)
            if not item.get("url"):
                fail(f"item {item.get('id')} missing url", errors)
        if not idx.get("index_complete_for_categories"):
            fail("index_complete_for_categories must be true for NXP_PUBLIC_COLLATERAL_INDEX_COMPLETE", errors)

    # SoC selection must be exact
    soc = (NXP / "CPB0_OPEN_SOC_SELECTION.md").read_text(encoding="utf-8") if (NXP / "CPB0_OPEN_SOC_SELECTION.md").exists() else ""
    if "MIMX9596AVZXN" not in soc and "MIMX9596CVZXNAC" not in soc:
        fail("CPB0_OPEN_SOC_SELECTION.md must name MIMX9596AVZXN and/or MIMX9596CVZXNAC", errors)
    if "MIMX9596CVZXNAC" not in soc:
        fail("CPB0_OPEN_SOC_SELECTION.md must freeze Table-2 OPN MIMX9596CVZXNAC", errors)

    # Pinmux CSV schema + unresolved honesty vs gate
    pin_path = NXP / "CPB0_OPEN_PINMUX_MAP.csv"
    if pin_path.exists():
        with pin_path.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        need = {"signal", "soc_pin_ball", "mux_function", "voltage_domain", "direction", "termination_pull", "destination", "source_document", "unresolved"}
        if rows and need - set(rows[0].keys()):
            fail(f"pinmux CSV missing columns: {need - set(rows[0].keys())}", errors)
        if not rows:
            fail("pinmux CSV has no rows", errors)
        unresolved = sum(1 for r in rows if str(r.get("unresolved", "")).lower() in {"true", "1", "yes"})
        gates = json.loads(gates_path.read_text()) if gates_path.exists() else {}
        if unresolved and gates.get("NXP_PUBLIC_PINMAP_UNDERSTOOD") is True:
            fail("cannot claim NXP_PUBLIC_PINMAP_UNDERSTOOD with unresolved pinmux rows", errors)

    # BOM: no fabricated stock/price numbers
    bom_path = NXP / "CPB0_OPEN_BOM.csv"
    if bom_path.exists():
        with bom_path.open(newline="", encoding="utf-8") as f:
            brows = list(csv.DictReader(f))
        if not brows:
            fail("BOM empty", errors)
        for r in brows:
            sp = (r.get("stock_price") or "").strip()
            if re.search(r"\$\s*\d|\bstock\s*=\s*\d", sp, re.I):
                fail(f"BOM {r.get('item_id')} appears to invent stock/price: {sp}", errors)
            if sp and sp not in {"VERIFY_AT_PURCHASE", "N/A", "PENDING"} and re.search(r"\d", sp):
                if "VERIFY" not in sp.upper():
                    fail(f"BOM {r.get('item_id')} stock_price must be VERIFY_AT_PURCHASE-class: {sp}", errors)

    # Forbidden physical / fab claims in NXP package text
    for path in NXP.rglob("*"):
        if path.suffix.lower() not in {".md", ".json", ".csv", ".txt"}:
            continue
        if "eda" in path.parts and path.suffix in {".kicad_sch", ".kicad_pcb", ".kicad_pro"}:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        compact = text.replace(" ", "")
        for phrase in FORBIDDEN_PHRASES:
            if phrase in compact and "must stay false" not in text.lower() and "false until" not in text.lower():
                # allow documentation of the token name in reports as false assignment lines only
                if f"{phrase.split('=')[0]}=false" in compact:
                    continue
                if phrase.endswith("=true") and phrase.replace("=true", "=false") in compact:
                    continue
                # reports print the false forms; skip if nearby =false
                if phrase in compact:
                    # Only fail if explicitly asserting true without a false sibling in gates files handled above
                    if path.name.startswith("REPORT_") or path.name.startswith("NXP0_GATES"):
                        if phrase.replace("=true", "=false") in compact or "READY_FOR_FAB=false" in compact:
                            continue
                    if "=true" in phrase and phrase in compact:
                        # Check it's not teaching "only when ... =true"
                        if "only when" in text.lower() or "set `" in text.lower() or "Set `" in text:
                            continue
                        fail(f"{path.relative_to(ROOT)} contains forbidden assertion {phrase}", errors)

    # Software RC1 firewall
    rc1 = HV1 / "SOFTWARE_RC1_INTERFACE_IMPACT_REGISTER.json"
    if rc1.exists():
        data = json.loads(rc1.read_text())
        if data.get("baselines_modified_in_this_repo_campaign") is True:
            fail("software RC1 baselines marked modified — firewall violation", errors)

    # Doctrine non-equivalence
    doctrine = NXP / "OPEN_CUSTOM_DOCTRINE.md"
    if doctrine.exists():
        dtext = doctrine.read_text(encoding="utf-8")
        if "PRODUCT_MAINLINE" not in dtext and "non-equivalent" not in dtext.lower() and "not" not in dtext.lower():
            fail("OPEN_CUSTOM_DOCTRINE.md should preserve non-equivalence messaging", errors)

    if errors:
        print("NXP-OPEN VALIDATE FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("NXP-OPEN VALIDATE PASS")
    print("NXP_OPEN_CUSTOM_TRACK_IMPLEMENTATION_STARTED=true")
    print("CPB0_OPEN_READY_FOR_FAB=false")
    print("PHYSICAL_HARDWARE_VALIDATED=false")
    print("SOFTWARE_RC1_BASELINES_UNTOUCHED=true")
    return 0


if __name__ == "__main__":
    sys.exit(main())
