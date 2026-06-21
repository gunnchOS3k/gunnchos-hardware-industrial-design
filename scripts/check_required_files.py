#!/usr/bin/env python3
"""Verify EVT-1 prototype RFQ package required files exist."""
from pathlib import Path
import sys

REQUIRED = [
    "README.md",
    "product/PRD_GUNNCHOS_MODULAR_CONSOLE_ECOSYSTEM.md",
    "product/PRODUCT_LINE_REQUIREMENTS.md",
    "product/EVT1_ACCEPTANCE_CRITERIA.md",
    "product/CLAIM_BOUNDARY.md",
    "docs/ISSUE_CLOSURE_MATRIX.md",
    "docs/PRODUCT_SYSTEM_OVERVIEW.md",
    "docs/HARDWARE_PACKAGE_INDEX.md",
    "docs/WAIKE_INTEGRATION.md",
    "docs/TUTOR_CARDS.md",
    "docs/STUDENT_TASKS.md",
    "architecture/SYSTEM_BLOCK_DIAGRAM.md",
    "architecture/PRODUCT_LINE_ARCHITECTURE.md",
    "architecture/DEVICE_COMPARISON_MATRIX.md",
    "architecture/ECOSYSTEM_DATA_FLOW.md",
    "architecture/OS_HARDWARE_CONTRACT.md",
    "cad/README.md",
    "cad/openscad/common_modules.scad",
    "cad/openscad/student_14.scad",
    "cad/openscad/handheld_hybrid.scad",
    "cad/openscad/ds_xl_coder.scad",
    "cad/openscad/wearables_arena_set.scad",
    "cad/openscad/EXPORT_NOTES.md",
    "mechanical/MECHANICAL_REQUIREMENTS.md",
    "mechanical/ENCLOSURE_REQUIREMENTS.md",
    "mechanical/REPAIRABILITY_REQUIREMENTS.md",
    "mechanical/ASSEMBLY_EXPLODED_VIEW_NOTES.md",
    "mechanical/FASTENER_AND_SERVICE_PLAN.md",
    "exports/README.md",
    "io/PORT_IO_MASTER_MATRIX.md",
    "io/student_14_ports.md",
    "io/handheld_hybrid_ports.md",
    "io/ds_xl_coder_ports.md",
    "io/wearables_arena_ports.md",
    "io/CONNECTOR_PINOUT_PLACEHOLDERS.md",
    "io/DEBUG_AND_SERVICE_PORTS.md",
    "power/POWER_BUDGET_MASTER.md",
    "power/POWER_TREE.md",
    "power/student_14_power_budget.csv",
    "power/handheld_hybrid_power_budget.csv",
    "power/ds_xl_coder_power_budget.csv",
    "power/wearables_arena_power_budget.csv",
    "power/BATTERY_LIFE_ESTIMATION_METHOD.md",
    "battery/BATTERY_REQUIREMENTS.md",
    "battery/CHARGING_AND_POWER_SAFETY.md",
    "battery/BMS_REQUIREMENTS.md",
    "battery/UN38_3_TRACKER.md",
    "battery/BATTERY_TEST_PLAN.md",
    "battery/BATTERY_RISK_REGISTER.md",
    "battery/CHARGER_SELECTION_CRITERIA.md",
    "thermal/THERMAL_REQUIREMENTS.md",
    "thermal/THERMAL_ASSUMPTIONS.md",
    "thermal/THERMAL_TEST_PLAN.md",
    "thermal/THERMAL_RISK_REGISTER.md",
    "thermal/student_14_thermal_profile.md",
    "thermal/handheld_hybrid_thermal_profile.md",
    "thermal/ds_xl_coder_thermal_profile.md",
    "thermal/wearables_arena_thermal_profile.md",
    "bom/MASTER_BOM.md",
    "bom/student_14_bom.csv",
    "bom/handheld_hybrid_bom.csv",
    "bom/ds_xl_coder_bom.csv",
    "bom/wearables_arena_bom.csv",
    "bom/BOM_ASSUMPTIONS.md",
    "bom/VENDOR_QUOTE_TRACKER.md",
    "bom/APPROVED_VENDOR_CRITERIA.md",
    "bom/MAKE_BUY_DECISIONS.md",
    "schematics/README.md",
    "schematics/SCHEMATIC_CLAIM_BOUNDARY.md",
    "schematics/SCHEMATIC_REVIEW_CHECKLIST.md",
    "schematics/student_14/student_14_system_block.kicad_sch",
    "schematics/handheld_hybrid/handheld_hybrid_system_block.kicad_sch",
    "schematics/ds_xl_coder/ds_xl_coder_system_block.kicad_sch",
    "schematics/wearables_arena/wearables_arena_system_block.kicad_sch",
    "pcb/README.md",
    "pcb/STACKUP_PLAN.md",
    "pcb/DFM_NOTES.md",
    "pcb/DFT_NOTES.md",
    "pcb/FABRICATION_OUTPUTS_CHECKLIST.md",
    "pcb/ASSEMBLY_OUTPUTS_CHECKLIST.md",
    "pcb/GERBER_EXPORT_PLAN.md",
    "pcb/PICK_AND_PLACE_PLAN.md",
    "pcb/PCB_REVIEW_GATE.md",
    "compliance/REGULATORY_MATRIX.md",
    "compliance/FCC_PART_15_PLAN.md",
    "compliance/CE_UKCA_PLAN.md",
    "compliance/ROHS_REACH_PLAN.md",
    "compliance/UN38_3_BATTERY_PLAN.md",
    "compliance/WIFI_BLUETOOTH_MODULE_CERT_PLAN.md",
    "compliance/OPEN_SOURCE_SBOM_PLAN.md",
    "compliance/YOUTH_PRIVACY_AND_SAFETY.md",
    "compliance/COMPLIANCE_EVIDENCE_TRACKER.md",
    "prototype_rfq/README.md",
    "prototype_rfq/RFQ_COVER_LETTER_TEMPLATE.md",
    "prototype_rfq/VENDOR_QUESTIONNAIRE.md",
    "prototype_rfq/FILES_TO_SEND_CHECKLIST.md",
    "prototype_rfq/NDA_AND_IP_NOTES.md",
    "prototype_rfq/QUOTE_COMPARISON_MATRIX.md",
    "prototype_rfq/PROTOTYPE_BUILD_REQUEST.md",
    "prototype_rfq/ENGINEERING_REVIEW_REQUEST.md",
    "prototype_rfq/CM_SHORTLIST_TRACKER.md",
    "manufacturing/EVT_DVT_PVT_PLAN.md",
    "manufacturing/MANUFACTURING_READINESS_CHECKLIST.md",
    "manufacturing/CM_QUOTE_PACKAGE_CHECKLIST.md",
    "manufacturing/PILOT_YIELD_PLAN.md",
    "manufacturing/QUALITY_PLAN.md",
    "manufacturing/SPC_METRICS_PLAN.md",
    "manufacturing/RISK_REGISTER.md",
    "manufacturing/REV_A_TO_REV_B_PLAN.md",
    "demo/PROFESSOR_STUDENT_DEMO_CHECKLIST.md",
    "demo/DEVICE_WALKTHROUGH_SCRIPT.md",
    "demo/SCREENSHOT_RENDER_CAPTURE_PLAN.md",
    "diligence/INVESTOR_TECHNICAL_DILIGENCE_CHECKLIST.md",
    "diligence/ENGINEERING_DILIGENCE_RESPONSE.md",
    "diligence/OPEN_GAPS_FOR_PROTOTYPE_VENDOR.md",
    "scripts/check_required_files.py",
    "scripts/validate_bom.py",
    "scripts/validate_power_budget.py",
    "scripts/validate_issue_closure_matrix.py",
    "scripts/generate_hardware_package_index.py",
    ".github/workflows/hardware-package-ci.yml",
]

# At least one of STL exports or export status must exist
STL_EXPORTS = [
    "exports/stl/student_14_placeholder.stl",
    "exports/stl/handheld_hybrid_placeholder.stl",
    "exports/stl/ds_xl_coder_placeholder.stl",
    "exports/stl/wearables_arena_set_placeholder.stl",
]
RENDER_EXPORTS = [
    "exports/renders/student_14_placeholder.svg",
    "exports/renders/handheld_hybrid_placeholder.svg",
    "exports/renders/ds_xl_coder_placeholder.svg",
    "exports/renders/wearables_arena_set_placeholder.svg",
]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = [f for f in REQUIRED if not (root / f).exists()]
    if missing:
        print("Missing required files:")
        for m in missing:
            print(f"  - {m}")
        return 1

    stl_ok = all((root / f).exists() for f in STL_EXPORTS)
    status_ok = (root / "exports/OPENSCAD_EXPORT_STATUS.md").exists()
    if not stl_ok and not status_ok:
        print("Missing STL exports and exports/OPENSCAD_EXPORT_STATUS.md")
        return 1

    render_missing = [f for f in RENDER_EXPORTS if not (root / f).exists()]
    if render_missing:
        print("Missing placeholder renders:")
        for m in render_missing:
            print(f"  - {m}")
        return 1

    print(f"All {len(REQUIRED)} required files present.")
    if status_ok and not stl_ok:
        print("Note: STL exports pending — OPENSCAD_EXPORT_STATUS.md documents next steps.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
