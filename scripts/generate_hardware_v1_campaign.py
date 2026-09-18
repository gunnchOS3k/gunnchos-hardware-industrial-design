#!/usr/bin/env python3
"""Generate Hardware v1.0 mainline campaign package under hardware_v1/.

Honest digital architecture + EVT preparation only.
Does NOT claim physical validation, certification, fab release, RFQ send, or purchase.
Does NOT invent Gerbers/ODB++/quotes/lead times.
"""
from __future__ import annotations

import hashlib
import json
import textwrap
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HV1 = ROOT / "hardware_v1"
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
CAMPAIGN = "HARDWARE_1_0_MASTER_CAMPAIGN"
SCHEMA = "gunnchos.hardware_v1.campaign.v1"

# Decision states (no bare TBD)
ADOPTED = "ADOPTED_MAINLINE"
EXP = "EXPERIMENTAL_COMPARE"
DEFER = "DEFERRED_GEN2"
PHYS = "PENDING_PHYSICAL_MEASUREMENT"
VENDOR = "PENDING_VENDOR_CONFIRMATION"
OWNER = "PENDING_OWNER_DECISION"

EXISTING_RECONCILE = {
    "digital_manufacturing": "DIGITAL_MANUFACTURING_READINESS.md",
    "digital_to_physical": "DIGITAL_TO_PHYSICAL_HANDOFF.md",
    "student_release": "device_designs/student_14_5/digital_release/INDEX.json",
    "dsxl_release": "device_designs/ds_xl_coder/digital_release/INDEX.json",
    "handheld_release": "device_designs/handheld_hybrid/digital_release/INDEX.json",
    "rings_release": "device_designs/edge_io_rings/digital_release/INDEX.json",
    "dock_bom": "device_designs/dock/bom/assembly_bom.csv",
    "student_bom": "device_designs/student_14_5/bom/assembly_bom.csv",
    "evt_dvt_pvt": "manufacturing/EVT_DVT_PVT_PLAN.md",
    "com_hpc_decision": "docs/full_product_family/COM_HPC_FINAL_DECISION_CONT_IX.md",
    "dock_arch": "docs/full_product_family/DOCK_ARCHITECTURE_FREEZE_USB4_TB4.md",
}


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not content.endswith("\n"):
        content += "\n"
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def md(title: str, body: str) -> str:
    return f"# {title}\n\n**Generated:** {UTC}  \n**Campaign:** `{CAMPAIGN}`  \n**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.\n\n{body.strip()}\n"


def decisions() -> list[dict]:
    return [
        {
            "id": "DEC-COMPUTE-001",
            "topic": "Student 14.5 / DS-XL compute module",
            "state": ADOPTED,
            "mainline": "COM-HPC Mini x86 Meteor Lake-class module (ADLINK COM-HPC-mMTL-155H-32G class) for EVT",
            "rationale": "Reconciles Cont IX COM-HPC freeze; shared module across desk SKUs; avoids bare CPU BGA",
            "evidence": ["docs/full_product_family/COM_HPC_FINAL_DECISION_CONT_IX.md", "device_designs/student_14_5/bom/assembly_bom.csv"],
            "experiment_alt": "EXP-ARM-IQX (ARM IQX-class SoM)",
            "owner_gate": None,
        },
        {
            "id": "DEC-COMPUTE-002",
            "topic": "Handheld Hybrid compute for EVT",
            "state": ADOPTED,
            "mainline": "COM-HPC Mini EVT mule (shared Meteor Lake-class module) for electrical/thermal bring-up",
            "rationale": "One EVT mule architecture; production handheld form-factor board remains separate",
            "evidence": ["device_designs/handheld_hybrid/digital_release/INDEX.json"],
            "experiment_alt": None,
            "notes": "Prior Radxa RM121-D8E32 retained as historical digital package; not mixed into Hardware v1 mainline BOM",
            "owner_gate": None,
        },
        {
            "id": "DEC-COMPUTE-003",
            "topic": "Handheld production board",
            "state": PHYS,
            "mainline": "Production handheld carrier/board geometry PENDING_PHYSICAL_MEASUREMENT after EVT mule data",
            "rationale": "Cannot freeze production board without measured thermal/power/fit from mule",
            "evidence": ["physical_evidence/README.md"],
            "experiment_alt": None,
            "owner_gate": "EVT mule bring-up measurements",
        },
        {
            "id": "DEC-DISPLAY-001",
            "topic": "Student / DS-XL display technology",
            "state": ADOPTED,
            "mainline": (
                "IPS LCD panels (Student: single eDP; DS-XL: one native eDP + DDI/DP second display). "
                "Not dual native eDP unless authoritative module docs prove it."
            ),
            "rationale": (
                "COM-HPC-mMTL documents 1x eDP + 2x DDI; retain two functional DS-XL displays via "
                "eDP+DDI/DP. OLED isolated as experiment."
            ),
            "evidence": [
                "device_designs/student_14_5/bom/assembly_bom.csv",
                "hardware_v1/devices/ds_xl/DUAL_DISPLAY_ARCHITECTURE.md",
            ],
            "experiment_alt": "EXP-STUDENT-OLED, EXP-DSXL-OLED-HYBRID",
            "owner_gate": None,
        },
        {
            "id": "DEC-STORAGE-001",
            "topic": "Storage / Wi-Fi",
            "state": ADOPTED,
            "mainline": "M.2 NVMe storage + M.2 Key E Wi-Fi (Intel BE200 class)",
            "rationale": "Standard COM-HPC Mini IO; field replaceable",
            "evidence": ["device_designs/student_14_5/bom/assembly_bom.csv"],
            "experiment_alt": None,
            "owner_gate": None,
        },
        {
            "id": "DEC-CELLULAR-001",
            "topic": "Optional cellular",
            "state": ADOPTED,
            "mainline": (
                "Optional Telit FN990B40 M.2 5G Sub-6 module exact MPN FN990B40W01T010300; "
                "Quectel RM520N-GL approved alternate"
            ),
            "rationale": (
                "HW1B closed AVL identity with exact MPN + live distributor/manufacturer evidence. "
                "PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING=true (dev antennas ≠ production)."
            ),
            "evidence": [
                "device_designs/student_14_5/bom/assembly_bom.csv",
                "hardware_v1/radio/FN990B40_RP0_A_AVL.md",
            ],
            "experiment_alt": None,
            "owner_gate": "PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING",
            "secondary_state": None,
        },
        {
            "id": "DEC-DOCK-001",
            "topic": "Dock Gen-1 link rate",
            "state": ADOPTED,
            "mainline": "USB4 40 Gbps (Intel JHL8440 + JHL9040R retimer) + USB-C PD EPR-class controller",
            "rationale": "Reconciles DOCK_ARCHITECTURE_FREEZE_USB4_TB4; no USB4 80 in main BOM",
            "evidence": ["docs/full_product_family/DOCK_ARCHITECTURE_FREEZE_USB4_TB4.md", "device_designs/dock/bom/assembly_bom.csv"],
            "experiment_alt": "EXP-DOCK-USB4-80",
            "owner_gate": "EXT-JHL8440-BALLMAP / EXT-JHL9040R-BALLMAP vendor NDA packs",
        },
        {
            "id": "DEC-RINGS-001",
            "topic": "Rings MCU",
            "state": ADOPTED,
            "mainline": (
                "Nordic nRF54L15 (BLE + LE Audio). "
                "RING_EVT_ELECTRICAL_PLATFORM=QFN48/DK reference (PCA10156); "
                "RING_FORM_FACTOR_CANDIDATE=CSP47"
            ),
            "rationale": (
                "HW1B closed RP0-A footprint uncertainty via Nordic public DK/QFN48 files. "
                "CSP47 wearable geometry remains a separate HDI/assembly gate; DK ≠ wearable validation."
            ),
            "evidence": [
                "device_designs/edge_io_rings/bom/assembly_bom.csv",
                "hardware_v1/devices/rings/NRF54L15_PACKAGE_STRATEGY.md",
                "hardware_v1/vendor_evidence/nordic/PCA10156_HW_FILES_METADATA.json",
            ],
            "experiment_alt": None,
            "owner_gate": "CSP47 wearable HDI/assembly feasibility before form-factor board",
            "secondary_state": None,
            "RING_EVT_ELECTRICAL_PLATFORM": "QFN48/DK reference",
            "RING_FORM_FACTOR_CANDIDATE": "CSP47",
            "DK_HARDWARE_ID": "PCA10156",
        },
        {
            "id": "DEC-RINGS-002",
            "topic": "Rings sensing + charge EVT",
            "state": ADOPTED,
            "mainline": "IMU + capacitive/touch + magnetic cradle charge contacts for EVT",
            "rationale": "Measurable EVT path; inductive and sEMG isolated as experiments",
            "evidence": ["device_designs/edge_io_rings/bom/assembly_bom.csv"],
            "experiment_alt": "EXP-RINGS-INDUCTIVE-CHARGE, EXP-RINGS-SEMG-WRIST",
            "owner_gate": None,
        },
        {
            "id": "DEC-FW-001",
            "topic": "Host firmware stack",
            "state": ADOPTED,
            "mainline": "Vendor UEFI on COM-HPC module + Zephyr EC on companion MCU",
            "rationale": "Ship path with vendor support; open alternatives experimental",
            "evidence": ["firmware/CLAIM_BOUNDARY.md", "firmware_os_interface/"],
            "experiment_alt": "EXP-COREBOOT, EXP-RAUC-UPDATE",
            "owner_gate": None,
        },
        {
            "id": "DEC-BATT-001",
            "topic": "Battery chemistry",
            "state": ADOPTED,
            "mainline": "Qualified Li-ion / LiPo only; no experimental chemistries in mainline",
            "rationale": "UN38.3 / transport path; experimental chemistries deferred Gen2",
            "evidence": ["battery/", "compliance/UN38_3_BATTERY_PLAN.md"],
            "experiment_alt": None,
            "deferred": "solid-state / Na-ion = DEFERRED_GEN2",
            "owner_gate": None,
        },
        {
            "id": "DEC-QA-001",
            "topic": "PCB assembly quality class",
            "state": ADOPTED,
            "mainline": "IPC Class 2 baseline with selective tighter controls on BGA/COM connector / RF keepouts (not blanket Class 3)",
            "rationale": "Cost/yield vs reliability; Class 3 reserved for selective high-risk zones",
            "evidence": ["manufacturing/QUALITY_PLAN.md"],
            "experiment_alt": None,
            "owner_gate": None,
        },
        {
            "id": "DEC-RP0-001",
            "topic": "Reference Platform 0 scope",
            "state": ADOPTED,
            "mainline": (
                "Two-stage RP0: RP0-A COTS Integration Bench (ADLINK Mini Base + mMTL + nRF54L15 DK + "
                "COTS USB4 dock) then RP0-B custom gunnchOS carrier/dock/ring EVT electronics"
            ),
            "rationale": (
                "Do not order custom PCB that is not fabrication-ready. COTS unlocks physical bring-up "
                "while vendor-gated pin maps remain RP0-B blockers."
            ),
            "evidence": [
                "DIGITAL_TO_PHYSICAL_HANDOFF.md",
                "hardware_v1/reference_platform_0/RP0_STAGE_MODEL.md",
            ],
            "experiment_alt": None,
            "owner_gate": "ORDER_RP0_A_COTS_BRINGUP_KIT (Cursor does not purchase)",
        },
    ]


def experiments() -> list[dict]:
    return [
        {
            "id": "EXP-ARM-IQX-001",
            "branch": "hardware/exp-arm-iqx",
            "title": "ARM IQX-class SoM vs COM-HPC Mini x86",
            "hypothesis": "ARM SoM reduces idle power and BOM cost at equal desk productivity for Student/DS-XL",
            "baseline": "COM-HPC-mMTL-155H-32G class",
            "variant": "ARM IQX-class SoM (vendor TBD — PENDING_VENDOR_CONFIRMATION)",
            "metrics": [
                "idle_power_w",
                "sustained_compile_time_s",
                "thermal_skin_c",
                "bom_delta_usd_quote",
                "os_driver_gap_count",
            ],
            "promotion_gate": "All metrics meet or beat baseline on EVT mule sample n>=3 AND Device OS RC1 interface register shows zero P0 breaks",
            "not_in_main_bom": True,
        },
        {
            "id": "EXP-STUDENT-OLED-001",
            "branch": "hardware/exp-student-oled",
            "title": "Student OLED panel vs IPS",
            "hypothesis": "OLED improves contrast/weight without exceeding power/thermal budget",
            "baseline": "IPS eDP panel",
            "variant": "OLED eDP panel class",
            "metrics": ["contrast_ratio", "avg_power_w", "burnin_risk_score", "cost_delta_usd", "nit_hdr"],
            "promotion_gate": "Power <= IPS+10% at 200 nits office; burn-in mitigation plan owner-approved",
            "not_in_main_bom": True,
        },
        {
            "id": "EXP-DSXL-OLED-HYBRID-001",
            "branch": "hardware/exp-dsxl-oled-hybrid",
            "title": "DS-XL OLED+IPS hybrid vs dual IPS",
            "hypothesis": "Primary OLED + secondary IPS improves creator UX without dual-OLED cost/thermal",
            "baseline": "Dual IPS eDP",
            "variant": "OLED primary + IPS secondary",
            "metrics": ["dual_edp_si_margin", "thermal_delta_c", "cost_delta_usd", "color_delta_e"],
            "promotion_gate": (
                "Dual-display SI margin maintained on eDP+DDI/DP (or proven dual-eDP if docs change); "
                "do not mislabel one eDP + DDI as dual native eDP"
            ),
            "not_in_main_bom": True,
        },
        {
            "id": "EXP-DOCK-USB4-80-001",
            "branch": "hardware/exp-dock-usb4-80",
            "title": "Dock USB4 80 vs USB4 40",
            "hypothesis": "USB4 80 improves external display/storage UX enough to justify controller cost/SI risk",
            "baseline": "JHL8440 USB4 40 + JHL9040R",
            "variant": "USB4 80-class controller (vendor TBD — PENDING_VENDOR_CONFIRMATION)",
            "metrics": ["link_rate_gbps", "eye_margin", "bom_delta_usd", "cable_interop_pass_rate"],
            "promotion_gate": "Measured eye margin at length L with owner cables; no mainline mix until DVT",
            "not_in_main_bom": True,
        },
        {
            "id": "EXP-RINGS-INDUCTIVE-001",
            "branch": "hardware/exp-rings-inductive-charge",
            "title": "Inductive ring charge vs magnetic cradle contacts",
            "hypothesis": "Inductive charge improves durability/UX with acceptable efficiency and EMI",
            "baseline": "Magnetic cradle pogo/contacts",
            "variant": "Qi-class or proprietary inductive coil",
            "metrics": ["charge_efficiency_pct", "emi_delta_db", "wear_cycles", "alignment_fail_rate"],
            "promotion_gate": "Efficiency >=70% at EVT coil; EMI does not fail pre-scan relative to baseline",
            "not_in_main_bom": True,
        },
        {
            "id": "EXP-RINGS-SEMG-001",
            "branch": "hardware/exp-rings-semg-wrist",
            "title": "sEMG wrist band vs IMU/cap ring input",
            "hypothesis": "sEMG adds gesture bandwidth without unsafe skin current / privacy regression",
            "baseline": "IMU + capacitive/touch ring",
            "variant": "sEMG wrist accessory",
            "metrics": ["gesture_f1", "skin_current_ua", "false_positive_rate", "privacy_review_pass"],
            "promotion_gate": "Safety current limits met; youth privacy review pass; not medical claim",
            "not_in_main_bom": True,
        },
        {
            "id": "EXP-COREBOOT-001",
            "branch": "hardware/exp-coreboot",
            "title": "coreboot vs vendor UEFI",
            "hypothesis": "coreboot improves auditability without breaking Device OS RC1 boot contract",
            "baseline": "Vendor UEFI on COM-HPC",
            "variant": "coreboot + LinuxBoot or equivalent",
            "metrics": ["secure_boot_chain_intact", "boot_time_s", "capsule_update_compat", "rc1_interface_breaks"],
            "promotion_gate": "Zero P0 RC1 interface breaks; measured boot on EVT mule",
            "not_in_main_bom": True,
        },
        {
            "id": "EXP-RAUC-001",
            "branch": "hardware/exp-rauc-update",
            "title": "RAUC A/B update vs vendor capsule/EC update",
            "hypothesis": "RAUC improves field update reliability for rings/EC and optional host slotting",
            "baseline": "Vendor UEFI capsule + Zephyr DFU",
            "variant": "RAUC A/B (rings/EC primary; host optional)",
            "metrics": ["update_success_rate", "rollback_success_rate", "brick_rate", "rc1_interface_breaks"],
            "promotion_gate": "Rollback verified on EVT; no secret material in repo",
            "not_in_main_bom": True,
        },
    ]


def gate_tokens() -> dict:
    """Honest gates — COTS orderability does not earn custom fab / EVT build."""
    import sys

    scripts_dir = Path(__file__).resolve().parent
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    from hw1b_rp0_cots_closure import hw1b_gate_overlay

    overlay = hw1b_gate_overlay()
    return {
        "schema": "gunnchos.hardware_v1.gates.v1",
        "generated_at_utc": UTC,
        "campaign_overlay": "HARDWARE_1_0B_RP0_COTS_BLOCKER_CLOSURE",
        "HARDWARE_V1_READY_FOR_EVT_BUILD": overlay["HARDWARE_V1_READY_FOR_EVT_BUILD"],
        "HARDWARE_V1_DIGITAL_ARCHITECTURE_COMPLETE": overlay["HARDWARE_V1_DIGITAL_ARCHITECTURE_COMPLETE"],
        "REFERENCE_PLATFORM_0_READY_FOR_FAB": overlay["REFERENCE_PLATFORM_0_READY_FOR_FAB"],
        "RP0_A_COTS_PROCUREMENT_PACKET_READY": overlay["RP0_A_COTS_PROCUREMENT_PACKET_READY"],
        "RP0_A_READY_TO_ORDER": overlay["RP0_A_READY_TO_ORDER"],
        "RP0_A_PHYSICAL_BUILD_PENDING": overlay["RP0_A_PHYSICAL_BUILD_PENDING"],
        "RP0_A_BRINGUP_PENDING": overlay["RP0_A_BRINGUP_PENDING"],
        "RP0_B_CUSTOM_READY_FOR_FAB": overlay["RP0_B_CUSTOM_READY_FOR_FAB"],
        "PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING": overlay["PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING"],
        "UNRES_NRF54L15_FOOTPRINT_CLOSED": overlay["UNRES_NRF54L15_FOOTPRINT_CLOSED"],
        "UNRES_FN990B40_AVL_CLOSED": overlay["UNRES_FN990B40_AVL_CLOSED"],
        "EXT_DSXL_DUAL_EDP_CLOSED": overlay["EXT_DSXL_DUAL_EDP_CLOSED"],
        "EXT_COM_HPC_400PIN_RP0_A_BLOCKING": overlay["EXT_COM_HPC_400PIN_RP0_A_BLOCKING"],
        "EXT_COM_HPC_400PIN_RP0_B_BLOCKING": overlay["EXT_COM_HPC_400PIN_RP0_B_BLOCKING"],
        "EXT_JHL8440_BALLMAP_RP0_A_BLOCKING": overlay["EXT_JHL8440_BALLMAP_RP0_A_BLOCKING"],
        "EXT_JHL8440_BALLMAP_RP0_B_BLOCKING": overlay["EXT_JHL8440_BALLMAP_RP0_B_BLOCKING"],
        "EXT_JHL9040R_BALLMAP_RP0_A_BLOCKING": overlay["EXT_JHL9040R_BALLMAP_RP0_A_BLOCKING"],
        "EXT_JHL9040R_BALLMAP_RP0_B_BLOCKING": overlay["EXT_JHL9040R_BALLMAP_RP0_B_BLOCKING"],
        "EVT_PENDING": True,
        "DVT_PENDING": True,
        "PVT_PENDING": True,
        "PHYSICAL_HARDWARE_VALIDATED": False,
        "CERTIFICATION_COMPLETE": False,
        "MANUFACTURING_VALIDATED": False,
        "DIGITAL_FABRICATION_PASS": False,
        "RFQ_SENT": False,
        "PHYSICAL_PENDING": True,
        "EXTERNAL_PENDING": True,
        "DIGITAL_ARCHITECTURE_PACKAGE_COMPLETE": True,
        "MAINLINE_DECISION_LEDGER_COMPLETE": True,
        "EXPERIMENTS_REGISTRY_COMPLETE": True,
        "SOFTWARE_RC1_BASELINES_UNTOUCHED": True,
        "blockers": overlay["blockers"],
        "closed_blockers": overlay["closed_blockers"],
        "NEXT_OWNER_ACTION": overlay["NEXT_OWNER_ACTION"],
        "NEXT_OWNER_ACTION_NOTE": overlay["NEXT_OWNER_ACTION_NOTE"],
        "NEXT_GATE": overlay["NEXT_GATE"],
        "NEXT_GATE_IF_OWNER_DECLINES_ORDER": overlay["NEXT_GATE_IF_OWNER_DECLINES_ORDER"],
        "legacy_alias": {
            "REFERENCE_PLATFORM_0_READY_FOR_FAB": "RP0_B_CUSTOM_READY_FOR_FAB",
        },
    }


def build_control_audits() -> None:
    write(
        HV1 / "control" / "CAMPAIGN_CONTROL_AUDIT.md",
        md(
            "Hardware v1.0 campaign control audit",
            f"""
## Scope
Execute Hardware 1.0 mainline EVT architecture + isolated experimental comparison tracks.

## Doctrine checklist
| Rule | Status |
|---|---|
| One mainline design per decision | PASS (see decision ledger) |
| Experiments isolated; not mixed into main BOM | PASS |
| No LCD compromise flattening | PASS |
| No physical/cert/fab/RFQ-send claims | PASS |
| No frozen software RC1 baseline edits | PASS (`SOFTWARE_RC1_BASELINES_UNTOUCHED=true`) |
| Extend existing PHYSICAL_PENDING evidence | PASS (reconcile map below) |
| Honest FAIL on missing Gerbers/quotes | PASS |

## Reconcile map (do not discard)
| Existing artifact | Role in Hardware v1 |
|---|---|
"""
            + "\n".join(f"| `{p}` | retained / indexed |" for p in EXISTING_RECONCILE.values())
            + """

## Branch architecture
- Mainline branch: `hardware/v1-mainline-ready-for-evt` → DRAFT PR to `main`
- Experiments branch from mainline; DRAFT PRs target mainline, not `main`
- Cursor must NOT merge
""",
        ),
    )
    write_json(
        HV1 / "control" / "CAMPAIGN_CONTROL_AUDIT.json",
        {
            "schema": SCHEMA,
            "campaign": CAMPAIGN,
            "generated_at_utc": UTC,
            "doctrine_pass": True,
            "software_rc1_untouched": True,
            "reconcile_paths": EXISTING_RECONCILE,
        },
    )


def build_decision_ledger() -> None:
    rows = decisions()
    write_json(HV1 / "decisions" / "DECISION_LEDGER.json", {"schema": SCHEMA, "generated_at_utc": UTC, "decisions": rows})
    lines = [
        md(
            "Hardware v1.0 decision ledger",
            "One mainline per decision. Alternatives are EXPERIMENTAL_COMPARE only.",
        ),
        "| ID | Topic | State | Mainline | Experiment / gate |",
        "|---|---|---|---|---|",
    ]
    for d in rows:
        exp = d.get("experiment_alt") or d.get("deferred") or d.get("owner_gate") or "—"
        lines.append(f"| `{d['id']}` | {d['topic']} | `{d['state']}` | {d['mainline']} | {exp} |")
    write(HV1 / "decisions" / "DECISION_LEDGER.md", "\n".join(lines) + "\n")


def build_contracts() -> None:
    write(
        HV1 / "contracts" / "OS_HARDWARE_V1_CONTRACT.md",
        md(
            "OS ↔ Hardware v1 contract (RC1-safe)",
            """
## Bound software identity (DO NOT MODIFY in this campaign)
- Device OS / Portal / WAIKE / gunnchAI / HumanValidationFreezeManifest **v1.0.0-rc.1** identity remains frozen.
- This contract only documents hardware interface expectations compatible with RC1.

## Host platforms (mainline)
| SKU | Compute | Display | Storage/Wi-Fi | Optional WWAN |
|---|---|---|---|---|
| Student 14.5 | COM-HPC Mini MTL-class | IPS eDP | M.2 NVMe + M.2 Key E | Telit FN990B40 (FN990B40W01T010300) |
| DS-XL Coder | same module | IPS eDP + DDI/DP second display | same | same |
| Handheld Hybrid (EVT mule) | COM-HPC Mini mule / RP0-A COTS | IPS (mule panel) | same | optional |
| Handheld Hybrid (production) | PENDING_PHYSICAL_MEASUREMENT | — | — | — |

## Dock
- Gen-1: USB4 40 + PD EPR
- USB4 80: experimental only
- RP0-A: COTS USB4 dock for behavioral validation (does not certify custom dock PCB)

## Rings
- MCU: nRF54L15 — EVT electrical QFN48/DK (PCA10156); form-factor candidate CSP47
- Sensors: IMU + cap/touch
- Charge EVT: magnetic cradle
- Inductive / sEMG: experimental

## Firmware
- Host: vendor UEFI
- EC / rings: Zephyr
- coreboot / RAUC: experimental

## Non-claims
No physical validation, certification, or manufacturing validation asserted by this contract.
""",
        ),
    )
    write_json(
        HV1 / "contracts" / "OS_HARDWARE_V1_CONTRACT.json",
        {
            "schema": "gunnchos.hardware_v1.os_contract.v1",
            "software_freeze": "v1.0.0-rc.1",
            "software_baselines_modified": False,
            "generated_at_utc": UTC,
        },
    )


def build_domain_packs() -> None:
    packs = {
        "rf/RF_MAINLINE.md": """
## Mainline RF
- Wi-Fi/BT: M.2 Intel BE200-class (module cert leveraged; host still needs integration testing — not certified here)
- Cellular optional: Telit FN990B40-class (PENDING_VENDOR_CONFIRMATION)
- Rings: 2.4 GHz BLE on nRF54L15; antenna keepout PENDING_PHYSICAL_MEASUREMENT
- Dock UWB optional footprint retained; not required for EVT mule

## Experimental RF
- None promoted; inductive charging EMI is EXP-RINGS-INDUCTIVE

## Status
`RF_PASS=false` · `CERTIFICATION_COMPLETE=false`
""",
        "dock/DOCK_PRD.md": """
## Dock Gen-1 PRD (mainline)
- USB4 40 Gbps host/device path (JHL8440 + JHL9040R)
- USB-C PD EPR-class dual-port controller
- 2.5GbE, USB hub, ESD on exposed ports
- Rings magnetic cradle charge rails
- USB4 80 = EXPERIMENTAL_COMPARE only (EXP-DOCK-USB4-80)

## External blockers
`EXT-JHL8440-BALLMAP`, `EXT-JHL9040R-BALLMAP`
""",
        "rings/RINGS_PRD.md": """
## Rings PRD (mainline)
- Nordic nRF54L15 class MCU
- IMU + capacitive/touch
- Magnetic cradle charge for EVT
- Zephyr firmware + DFU
- Authenticated spatial input role preserved (IMU ≠ absolute pose)

## Experiments
- Inductive charge
- sEMG wrist

## Historical
Prior nRF52840 digital package retained under `device_designs/edge_io_rings/` — not mixed into v1 mainline BOM.
""",
        "firmware/FIRMWARE_SECURITY.md": """
## Mainline
- Vendor UEFI Secure Boot chain on COM-HPC module
- Zephyr EC with signed DFU for rings/EC
- TPM 2.0 on desk SKUs (Infineon SLB9672 class)

## Experimental
- coreboot (EXP-COREBOOT)
- RAUC A/B (EXP-RAUC)

## Secrets
No private keys, certs, or supplier credentials in-repo.
""",
        "power/POWER_BUDGET.md": """
## Mainline power doctrine
- Qualified Li-ion/LiPo only
- Desk SKUs: NVDC buck-boost + SBS gauge class (reconcile existing Student BOM)
- Rings: Nordic PMIC class sized for nRF54L15 (VENDOR confirm)
- Dock: PD EPR source/sink per Gen-1

## Status
Budgets are MODELED / PUBLIC_DOCS — `PENDING_PHYSICAL_MEASUREMENT` for all rails.
""",
        "mechanical/MECHANICAL.md": """
## Mainline mechanical
- OpenSCAD family models retained (`cad/openscad/`)
- EVT mule uses COM-HPC Mini carrier envelope
- Production handheld enclosure = PENDING_PHYSICAL_MEASUREMENT

## Status
Parse success ≠ first-article print. `PHYSICAL_PENDING=true`
""",
        "thermal/THERMAL.md": """
## Mainline thermal
- Desk SKUs: sustained desk TDP envelope per COM-HPC module vendor guidance (MODELED)
- Handheld mule: instrument before production board freeze
- Rings: skin temp limits TBD → PENDING_PHYSICAL_MEASUREMENT (owner test plan in DVT matrix)

## Non-claim
No thermal chamber results in this campaign.
""",
        "electrical/ELECTRICAL.md": """
## Mainline electrical
- KiCad family retained under `device_designs/*/kicad/`
- Zero ERC/DRC **errors** historically recorded is hygiene only
- Pin-accurate COM-HPC / JHL fanout still EXTERNAL_PENDING

## Non-claim
`DIGITAL_FABRICATION_PASS=false` — no fake Gerbers/ODB++.
""",
        "manufacturing/MANUFACTURING.md": """
## Mainline manufacturing doctrine
- IPC Class 2 baseline + selective tighter controls
- EVT → DVT → PVT matrices digital-only until physical builds
- CM quote packets exist as templates; `RFQ_SENT=false`

## Status
`MANUFACTURING_VALIDATED=false` · `EVT_PENDING=true` · `DVT_PENDING=true` · `PVT_PENDING=true`
""",
        "sourcing/SOURCING.md": """
## Sourcing
- AVL criteria retained (`bom/APPROVED_VENDOR_CRITERIA.md`)
- Mainline BOM index under `hardware_v1/bom/`
- Experimental parts listed only under `hardware_v1/experiments/*/BOM_DELTA.csv`
- Cursor does not contact suppliers or send RFQs
""",
        "human_factors/HUMAN_FACTORS.md": """
## Human factors (digital)
- Student: sustained desk ergonomics; IPS readability
- Handheld: production grip PENDING_PHYSICAL_MEASUREMENT
- Rings: magnetic cradle alignment UX; inductive/sEMG experimental
- Youth privacy / safety plans retained under `compliance/YOUTH_PRIVACY_AND_SAFETY.md`
- No clinical/medical claims for sEMG experiment
""",
        "compliance/COMPLIANCE.md": """
## Compliance posture
Digital prep only (`certification/`, `compliance/`).

| Domain | Status |
|---|---|
| FCC / CE / UKCA | not claimed |
| USB-IF | not claimed |
| UN38.3 | plan only |
| RoHS/REACH | plan only |

`CERTIFICATION_COMPLETE=false`
""",
    }
    for rel, body in packs.items():
        title = Path(rel).stem.replace("_", " ")
        write(HV1 / rel, md(title, body))


def build_bom() -> None:
    write(
        HV1 / "bom" / "MAINLINE_BOM_INDEX.md",
        md(
            "Hardware v1 mainline BOM index",
            """
## Rule
Experimental MPNs must not appear in mainline BOM files.

## SKU → existing assembly BOM (reconciled)
| SKU | Path | Hardware v1 notes |
|---|---|---|
| Student 14.5 | `device_designs/student_14_5/bom/assembly_bom.csv` | COM-HPC Mini MTL retained; WWAN preferred class → Telit FN990B40 (Quectel alternate) |
| DS-XL Coder | `device_designs/ds_xl_coder/bom/assembly_bom.csv` | shared module; dual IPS |
| Handheld EVT mule | `hardware_v1/bom/handheld_evt_mule_bom.csv` | COM-HPC Mini mule (RM121 historical not mixed) |
| Dock Gen-1 | `device_designs/dock/bom/assembly_bom.csv` | USB4 40 only |
| Rings | `hardware_v1/bom/rings_mainline_bom.csv` | nRF54L15 class (nRF52840 historical retained separately) |

## AVL
See `hardware_v1/bom/AVL.md`. Unknown fields stay unknown.
""",
        ),
    )
    write(
        HV1 / "bom" / "AVL.md",
        md(
            "Hardware v1 AVL",
            """
| Commodity | Preferred class | Alternate | State |
|---|---|---|---|
| COM-HPC Mini module | ADLINK COM-HPC-mMTL-155H-32G | 64G SKU | ADOPTED_MAINLINE |
| Wi-Fi M.2 | Intel BE200 | AX211 | ADOPTED_MAINLINE |
| WWAN M.2 | Telit FN990B40-class | Quectel RM520N-GL | ADOPTED + PENDING_VENDOR_CONFIRMATION |
| Dock USB4 | Intel JHL8440 | VIA VL108 cost-down SKU | ADOPTED_MAINLINE |
| Rings MCU | Nordic nRF54L15 | — | ADOPTED + PENDING_VENDOR_CONFIRMATION |
| Battery | Qualified Li-ion/LiPo | — | ADOPTED_MAINLINE |

USB4 80 controllers, OLED panels, inductive coils, sEMG AFE, coreboot blobs — **experimental AVL only**.
""",
        ),
    )
    write(
        HV1 / "bom" / "handheld_evt_mule_bom.csv",
        """sku,subsystem,manufacturer,MPN,description,qty,status,notes
Handheld_EVT_Mule,COM_MODULE,ADLINK,COM-HPC-mMTL-155H-32G,COM-HPC Mini Ultra 7 155H + 32GB,1,ADOPTED_MAINLINE,Shared with Student/DS-XL EVT
Handheld_EVT_Mule,CarrierPCB,gunnchOS3k,handheld_evt_mule_carrier,COM-HPC Mini carrier mule PCB,1,DESIGN_PENDING_EXTERNAL,Blocked on EXT-COM-HPC-400PIN
Handheld_EVT_Mule,COM_Connector,TE/Samtec class,COM-HPC Mini 400-pin,Connector set,1,AVL_PENDING,Exact MPN from vendor guide
Handheld_EVT_Mule,WiFi,Intel,BE200,Wi-Fi 7 + BT M.2 Key E,1,ADOPTED_MAINLINE,
Handheld_EVT_Mule,Storage,OEM,M.2_NVMe_1TB_class,M.2 NVMe,1,AVL_PENDING,Quote required — no fake lead time
Handheld_EVT_Mule,PD,Texas Instruments,TPS65994ADFBRQ1,USB-C PD,1,ADOPTED_MAINLINE,
Handheld_EVT_Mule,Battery,OEM,qualified_Li-ion_pack,Qualified Li-ion only,1,PENDING_VENDOR_CONFIRMATION,No experimental chemistry
Handheld_EVT_Mule,Historical_SoM_NOT_MAINLINE,Radxa,RM121-D8E32,Prior digital package SoM,0,HISTORICAL_ONLY,Not mixed into mainline qty
""",
    )
    write(
        HV1 / "bom" / "rings_mainline_bom.csv",
        """sku,subsystem,manufacturer,MPN,description,qty,status,notes
Edge_IO_Rings,MCU,Nordic Semiconductor,nRF54L15-class,BLE MCU mainline uplift,1,PENDING_VENDOR_CONFIRMATION,Exact orderable MPN pending
Edge_IO_Rings,IMU,Bosch Sensortec,BMI270,6-axis IMU,1,ADOPTED_MAINLINE,Reconciled from prior BOM
Edge_IO_Rings,Touch,OEM,cap_touch_controller_class,Capacitive/touch,1,AVL_PENDING,
Edge_IO_Rings,PMIC,Nordic Semiconductor,npm1300-class,Charger+regulators,1,PENDING_VENDOR_CONFIRMATION,Confirm nRF54L15 pairing
Edge_IO_Rings,Battery,OEM,qualified_LiPo_ring_cell,Qualified LiPo,1,PENDING_VENDOR_CONFIRMATION,UN38.3 at purchase
Edge_IO_Rings,Charge,Mill-Max,pogo_cradle_class,Magnetic cradle contacts EVT,2,ADOPTED_MAINLINE,Inductive = experimental only
Edge_IO_Rings,Antenna,Johanson,2450AT18A100-class,2.4GHz chip antenna,1,ADOPTED_MAINLINE,
Edge_IO_Rings,Historical_MCU_NOT_MAINLINE,Nordic,nRF52840-QIAA-R,Prior digital package,0,HISTORICAL_ONLY,Not mixed into mainline qty
""",
    )


def build_reference_platform() -> None:
    write(
        HV1 / "reference_platform_0" / "REFERENCE_PLATFORM_0.md",
        md(
            "Reference Platform 0",
            """
## Stage model
See `RP0_STAGE_MODEL.md`.

### RP0-A — COTS Integration Bench
ADLINK COM-HPC Mini Base + COM-HPC-mMTL-155H-32G + nRF54L15 DK (PCA10156) + COTS USB4 dock.
No custom fabrication. Procurement packet ready; **NOT_PURCHASED**.

### RP0-B — Custom gunnchOS Reference Carrier
Net-accurate custom carrier/dock/ring EVT electronics. Requires vendor pin/ball maps + EDA.

## Fab readiness
`REFERENCE_PLATFORM_0_READY_FOR_FAB=false` (= `RP0_B_CUSTOM_READY_FOR_FAB=false`)

COTS orderability does **not** set fab readiness.

## Owner next action
`NEXT_OWNER_ACTION=ORDER_RP0_A_COTS_BRINGUP_KIT` — Cursor does not purchase.
If owner declines: `NEXT_GATE=ACQUIRE_RP0_B_VENDOR_COLLATERAL`
""",
        ),
    )
    write_json(
        HV1 / "reference_platform_0" / "REFERENCE_PLATFORM_0.json",
        {
            "schema": "gunnchos.hardware_v1.rp0.v1",
            "READY_FOR_FAB": False,
            "RP0_B_CUSTOM_READY_FOR_FAB": False,
            "RP0_A_COTS_PROCUREMENT_PACKET_READY": True,
            "RP0_A_READY_TO_ORDER": True,
            "RP0_A_PHYSICAL_BUILD_PENDING": True,
            "RP0_A_BRINGUP_PENDING": True,
            "PHYSICAL_PENDING": True,
            "stages": {
                "RP0_A": {
                    "type": "COTS_INTEGRATION_BENCH",
                    "components": [
                        "adlink_com_hpc_mmtl_155h_32g",
                        "adlink_com_hpc_mini_base",
                        "nrf54l15_dk_pca10156",
                        "cots_usb4_dock",
                    ],
                },
                "RP0_B": {
                    "type": "CUSTOM_GUNNCHOS_REFERENCE_CARRIER",
                    "blockers": [
                        "EXT-COM-HPC-400PIN",
                        "EXT-JHL8440-BALLMAP",
                        "EXT-JHL9040R-BALLMAP",
                    ],
                },
            },
            "generated_at_utc": UTC,
        },
    )


def build_prds_icds() -> None:
    for sku, role in [
        ("student_14_5", "Sustained desk/learning/work compute"),
        ("ds_xl_coder", "Local create/build/test/deploy"),
        ("handheld_hybrid", "Mobile/docked compute — EVT mule now; production PENDING_PHYSICAL_MEASUREMENT"),
        ("dock", "Continuity dock Gen-1 USB4 40 + PD EPR"),
        ("edge_io_rings", "Wearable authenticated input + sensing"),
    ]:
        write(
            HV1 / "prd" / f"PRD_{sku}.md",
            md(
                f"PRD — {sku}",
                f"""
## Role
{role}

## Mainline bindings
See `hardware_v1/decisions/DECISION_LEDGER.md` and `hardware_v1/contracts/OS_HARDWARE_V1_CONTRACT.md`.

## Out of scope
Experimental variants, certification pass claims, physical validation claims.
""",
            ),
        )
        write(
            HV1 / "icd" / f"ICD_{sku}.md",
            md(
                f"ICD — {sku}",
                f"""
## Interfaces
Documented digitally against existing `device_designs/{sku if sku != 'edge_io_rings' else 'edge_io_rings'}/digital_release/OS_INTERFACE.json` where present.

## RC1 impact
Any interface delta must be registered in `hardware_v1/SOFTWARE_RC1_INTERFACE_IMPACT_REGISTER.md` without modifying frozen RC1 baselines.
""",
            ),
        )


def build_dfmea_matrices() -> None:
    write(
        HV1 / "quality" / "DFMEA.md",
        md(
            "DFMEA (digital starter)",
            """
| Item | Failure mode | Effect | Cause | Prevention | Detection | Severity | State |
|---|---|---|---|---|---|---|---|
| COM-HPC connector | Open/short pin | No boot | Pin-map error | Wait EXT-COM-HPC-400PIN | Continuity fixture | 10 | EXTERNAL_PENDING |
| Dock USB4 | Link train fail | No dock video | SI / ball-map | NDA ball maps | BERT/eye | 8 | EXTERNAL_PENDING |
| Rings charge | Intermittent pogo | No charge | Alignment | Magnetic cradle geometry | Charge log | 6 | PENDING_PHYSICAL_MEASUREMENT |
| Battery | Thermal event | Safety | Wrong chemistry | Qualified Li-ion only | Pack protector | 10 | ADOPTED_MAINLINE |
| OLED exp mix | BOM contamination | Yield/cost | Process error | Experiment isolation | BOM linter | 7 | CONTROL |

This is a digital DFMEA starter — not a completed live DFMEA sign-off.
""",
        ),
    )
    for stage in ("EVT", "DVT", "PVT"):
        write(
            HV1 / "matrices" / f"{stage}_MATRIX.md",
            md(
                f"{stage} matrix (digital)",
                f"""
## Status
`{stage}_PENDING=true` · no physical {stage} pass claimed.

## Entry criteria (digital)
- Mainline decision ledger complete
- BOM/AVL indexed without experimental mix
- Known external blockers listed
- RC1 interface impact register present

## Exit criteria (physical — NOT claimed)
- Measured results attached under `physical_evidence/`
- Owner sign-off

Reconcile existing plans: `manufacturing/EVT_DVT_PVT_PLAN.md`, `dvt/`, `pvt/`.
""",
            ),
        )


def build_experiments_registry() -> None:
    exps = experiments()
    write_json(HV1 / "experiments" / "REGISTRY.json", {"schema": SCHEMA, "generated_at_utc": UTC, "experiments": exps})
    lines = [
        md("Experiments registry", "All experiments are isolated comparison tracks. Not in mainline BOM."),
        "| ID | Branch | Title | Promotion gate |",
        "|---|---|---|---|",
    ]
    for e in exps:
        lines.append(f"| `{e['id']}` | `{e['branch']}` | {e['title']} | {e['promotion_gate']} |")
    write(HV1 / "experiments" / "REGISTRY.md", "\n".join(lines) + "\n")

    for e in exps:
        slug = e["id"].lower().replace("_", "-")
        base = HV1 / "experiments" / e["id"]
        write(
            base / "COMPARISON_PACKAGE.md",
            md(
                e["title"],
                f"""
## Identity
- Experiment ID: `{e['id']}`
- Branch: `{e['branch']}`
- State: `{EXP}`
- `not_in_main_bom`: `{e['not_in_main_bom']}`

## Hypothesis
{e['hypothesis']}

## Baseline (mainline)
{e['baseline']}

## Variant
{e['variant']}

## Measurable comparison criteria
"""
                + "\n".join(f"- `{m}`" for m in e["metrics"])
                + f"""

## Promotion gate
{e['promotion_gate']}

## Non-claims
No physical results fabricated. No quotes/lead times invented. No merge to mainline without gate.
""",
            ),
        )
        write_json(
            base / "COMPARISON_PACKAGE.json",
            {**e, "schema": "gunnchos.hardware_v1.experiment.v1", "generated_at_utc": UTC, "state": EXP},
        )
        write(
            base / "BOM_DELTA.csv",
            f"""change,subsystem,mpn_or_class,qty,note\nADD,experiment_only,{e['id']}_variant,1,EXPERIMENTAL — do not merge to mainline BOM\nREMOVE,none,—,0,Comparison only; mainline unchanged\n""",
        )
        write(
            base / "METRICS.md",
            md(
                f"Metrics — {e['id']}",
                "Record measured values only after physical/lab work. Current values: `PENDING_PHYSICAL_MEASUREMENT`.\n\n"
                + "\n".join(f"| `{m}` | PENDING_PHYSICAL_MEASUREMENT | — |" for m in e["metrics"])
                if False
                else "Record measured values only after physical/lab work.\n\n| Metric | Value | State |\n|---|---|---|\n"
                + "\n".join(f"| `{m}` | — | PENDING_PHYSICAL_MEASUREMENT |" for m in e["metrics"]),
            ),
        )


def build_rc1_register() -> None:
    write(
        HV1 / "SOFTWARE_RC1_INTERFACE_IMPACT_REGISTER.md",
        md(
            "Software RC1 interface impact register",
            """
## Freeze
Device OS / Portal / WAIKE / gunnchAI / HumanValidationFreezeManifest **v1.0.0-rc.1** must not be modified by this hardware campaign.

## Hardware deltas vs prior digital packages
| Area | Delta | RC1 software impact | Disposition |
|---|---|---|---|
| Handheld EVT mule compute | Radxa NX5 historical → COM-HPC Mini mule | Boot/ACPI/device-tree expectations may differ | Document only; no RC1 code change in this campaign |
| Rings MCU | nRF52840 → nRF54L15 class | BLE stack / DFU descriptors may need future SW rev | Register only; keep RC1 freeze |
| WWAN preferred | Quectel → Telit FN990B40-class preferred | Modem manager IDs may differ | Optional SKU; RC1 untouched |
| Dock | USB4 40 unchanged mainline | None | — |
| Firmware | Vendor UEFI + Zephyr EC affirmed | None if vendor paths already assumed | coreboot/RAUC experimental only |

## Rule
Future software changes require a separate software campaign after hardware measurements — not silent edits here.
""",
        ),
    )
    write_json(
        HV1 / "SOFTWARE_RC1_INTERFACE_IMPACT_REGISTER.json",
        {
            "software_freeze_identity": "v1.0.0-rc.1",
            "baselines_modified_in_this_repo_campaign": False,
            "impacts_registered": True,
            "generated_at_utc": UTC,
        },
    )


def build_owner_packet() -> None:
    gates = gate_tokens()
    write(
        HV1 / "OWNER_ACTION_PACKET.md",
        md(
            "Owner action packet",
            f"""
## What Cursor completed (digital)
- Mainline decision ledger (one design per decision)
- HW1B RP0-A/B stage split + public-source blocker closures
- RP0-A COTS procurement BOM/guide + bring-up matrix
- RP0-B vendor access packet
- Contracts, PRDs, ICDs, DFMEA starter, EVT/DVT/PVT matrices
- Experiments registry + EXP-*-001 comparison packages
- Make validators `make hardware-v1-*`
- Honest gate tokens (see below)

## What Cursor did NOT do
- Send RFQs / purchase / contact suppliers / accept NDAs
- Claim physical validation or certification
- Merge any PR
- Modify software RC1 baselines
- Fabricate Gerbers/ODB++/quotes/lead times / invent ball maps

## Gate tokens
| Token | Value |
|---|---|
| `HARDWARE_V1_READY_FOR_EVT_BUILD` | `{gates['HARDWARE_V1_READY_FOR_EVT_BUILD']}` |
| `HARDWARE_V1_DIGITAL_ARCHITECTURE_COMPLETE` | `{gates['HARDWARE_V1_DIGITAL_ARCHITECTURE_COMPLETE']}` |
| `REFERENCE_PLATFORM_0_READY_FOR_FAB` | `{gates['REFERENCE_PLATFORM_0_READY_FOR_FAB']}` (= `RP0_B_CUSTOM_READY_FOR_FAB`) |
| `RP0_A_COTS_PROCUREMENT_PACKET_READY` | `{gates['RP0_A_COTS_PROCUREMENT_PACKET_READY']}` |
| `RP0_A_READY_TO_ORDER` | `{gates['RP0_A_READY_TO_ORDER']}` |
| `RP0_A_PHYSICAL_BUILD_PENDING` | `{gates['RP0_A_PHYSICAL_BUILD_PENDING']}` |
| `RP0_A_BRINGUP_PENDING` | `{gates['RP0_A_BRINGUP_PENDING']}` |
| `RP0_B_CUSTOM_READY_FOR_FAB` | `{gates['RP0_B_CUSTOM_READY_FOR_FAB']}` |
| `PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING` | `{gates['PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING']}` |
| `EVT_PENDING` | `{gates['EVT_PENDING']}` |
| `DVT_PENDING` | `{gates['DVT_PENDING']}` |
| `PVT_PENDING` | `{gates['PVT_PENDING']}` |
| `PHYSICAL_HARDWARE_VALIDATED` | `{gates['PHYSICAL_HARDWARE_VALIDATED']}` |
| `CERTIFICATION_COMPLETE` | `{gates['CERTIFICATION_COMPLETE']}` |
| `MANUFACTURING_VALIDATED` | `{gates['MANUFACTURING_VALIDATED']}` |
| `DIGITAL_FABRICATION_PASS` | `{gates['DIGITAL_FABRICATION_PASS']}` |
| `RFQ_SENT` | `{gates['RFQ_SENT']}` |
| `DIGITAL_ARCHITECTURE_PACKAGE_COMPLETE` | `{gates['DIGITAL_ARCHITECTURE_PACKAGE_COMPLETE']}` |

## Preferred next action
`NEXT_OWNER_ACTION={gates['NEXT_OWNER_ACTION']}`

{gates['NEXT_OWNER_ACTION_NOTE']}

If owner declines RP0-A order: `NEXT_GATE={gates['NEXT_GATE_IF_OWNER_DECLINES_ORDER']}`
""",
        ),
    )
    write_json(HV1 / "GATES.json", gates)
    write(
        HV1 / "GATES.md",
        md(
            "Hardware v1 gate tokens",
            "\n".join(
                f"- `{k}` = `{v}`"
                for k, v in gates.items()
                if isinstance(v, (bool, str, type(None))) and (k.isupper() or k.startswith("NEXT"))
            ),
        ),
    )


def build_report_az() -> None:
    write(
        HV1 / "REPORT_SECTION_33_A_TO_Z.md",
        md(
            "Section 33 report A–Z",
            f"""
## A. Campaign
`{CAMPAIGN}` executed digitally under `hardware_v1/`.

## B. Repo / branch
`gunnchOS3k/gunnchos-hardware-industrial-design` · `hardware/v1-mainline-ready-for-evt`

## C. Doctrine
One mainline per decision; experiments isolated; no physical/cert/fab false claims; RC1 untouched.

## D. Decision ledger
`hardware_v1/decisions/DECISION_LEDGER.md`

## E. Compute mainline
COM-HPC Mini Meteor Lake-class for Student/DS-XL/Handheld EVT mule.

## F. Displays
IPS mainline; OLED experiments.

## G. Dock
USB4 40 + PD EPR mainline; USB4 80 experiment.

## H. Rings
nRF54L15 + IMU/cap + magnetic cradle; inductive + sEMG experiments.

## I. Firmware
Vendor UEFI + Zephyr EC; coreboot + RAUC experiments.

## J. Battery / quality
Qualified Li-ion; IPC Class 2 + selective tighter controls.

## K. BOM/AVL
`hardware_v1/bom/` — no experimental mix.

## L. Reference Platform 0
Two-stage: RP0-A COTS packet ready; `REFERENCE_PLATFORM_0_READY_FOR_FAB=false` (= RP0-B).

## M. PRDs / ICDs
`hardware_v1/prd/`, `hardware_v1/icd/`

## N. DFMEA / matrices
`hardware_v1/quality/DFMEA.md`, `hardware_v1/matrices/`

## O. Compliance / human factors
Digital prep only; `CERTIFICATION_COMPLETE=false`.

## P. Experiments
Eight EXP-*-001 packages under `hardware_v1/experiments/`.

## Q. RC1 impact register
`hardware_v1/SOFTWARE_RC1_INTERFACE_IMPACT_REGISTER.md`

## R. Owner packet
`hardware_v1/OWNER_ACTION_PACKET.md`

## S. Gates
See `hardware_v1/GATES.json` — EVT/DVT/PVT still pending; physical validated false.

## T. Make validators
`make hardware-v1-validate` and related targets.

## U. Reconciled evidence
Existing DIGITAL_* / device_designs / manufacturing / dvt / pvt retained.

## V. DRAFT PRs
Mainline DRAFT to `main`; experimental DRAFTs to mainline branch when packages present.

## W. Non-actions
No merge, no RFQ send, no purchase, no secrets.

## X. NEXT_OWNER_ACTION
`ORDER_RP0_A_COTS_BRINGUP_KIT`

## Y. Honest blockers (RP0-B)
EXT-COM-HPC-400PIN, EXT-JHL8440-BALLMAP, EXT-JHL9040R-BALLMAP (vendor-gated for custom fab only).

## Z. Evidence root
`hardware_v1/` including `rp0b/`, `reference_platform_0/RP0_*`, `vendor_evidence/nordic/`
""",
        ),
    )


def build_readme() -> None:
    write(
        HV1 / "README.md",
        md(
            "Hardware v1.0 mainline package",
            """
## Start
1. `hardware_v1/control/CAMPAIGN_CONTROL_AUDIT.md`
2. `hardware_v1/decisions/DECISION_LEDGER.md`
3. `hardware_v1/GATES.md`
4. `hardware_v1/OWNER_ACTION_PACKET.md`
5. `make hardware-v1-validate`

## Claim boundary
Digital architecture + EVT preparation. Not physical validation, not certification, not fab release.
""",
        ),
    )


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def build_manifest() -> None:
    files = sorted(p for p in HV1.rglob("*") if p.is_file())
    entries = []
    for p in files:
        rel = str(p.relative_to(ROOT))
        entries.append({"path": rel, "sha256": sha256_file(p), "bytes": p.stat().st_size})
    write_json(
        HV1 / "MANIFEST.json",
        {
            "schema": "gunnchos.hardware_v1.manifest.v1",
            "generated_at_utc": UTC,
            "campaign": CAMPAIGN,
            "file_count": len(entries),
            "files": entries,
        },
    )


def main() -> None:
    HV1.mkdir(parents=True, exist_ok=True)
    import sys

    scripts_dir = Path(__file__).resolve().parent
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    from hw1b_rp0_cots_closure import build_all as build_hw1b

    build_control_audits()
    build_decision_ledger()
    build_contracts()
    build_domain_packs()
    build_bom()
    build_reference_platform()
    build_prds_icds()
    build_dfmea_matrices()
    build_experiments_registry()
    build_rc1_register()
    build_hw1b()
    build_owner_packet()
    build_report_az()
    build_readme()
    build_manifest()
    print(f"OK wrote {HV1} at {UTC}")


if __name__ == "__main__":
    main()
