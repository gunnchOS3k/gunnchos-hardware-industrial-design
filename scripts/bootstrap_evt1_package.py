#!/usr/bin/env python3
"""One-time bootstrap for EVT-1 RFQ package missing artifacts."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]

BOUNDARY = (
    "This repository is moving from EVT-0 concept toward EVT-1 prototype RFQ package. "
    "It is not a final schematic package, not certified hardware, not FCC/CE approved, "
    "not DVT/PVT complete, and not a manufacturing release."
)

SCHEMATIC_BOUNDARY = (
    "EVT-1 schematic skeleton only. Requires electrical engineering review. "
    "Requires PCB layout, DFM, DFT, EMC, thermal, battery, and compliance review. "
    "Not final manufacturing schematic."
)

POWER_HEADER = "device,subsystem,mode,min_w_typ,max_w_typ,duty_cycle_estimate,notes\n"

POWER_ROWS = {
    "student_14": [
        "student_14,usb_c_input,charging,15,45,0.15,USB-C PD placeholder",
        "student_14,battery,school,3,8,0.35,APU light load",
        "student_14,main_system_rail,developer,12,25,0.20,compile/build",
        "student_14,display_rail,media,4,10,0.15,streaming",
        "student_14,radio_rail,standby,0.5,2,0.10,Wi-Fi idle",
        "student_14,display_rail,play,8,18,0.10,Steam gaming",
        "student_14,charger,docked,20,60,0.05,dock charge",
    ],
    "handheld_hybrid": [
        "handheld_hybrid,battery,play,8,15,0.40,gaming",
        "handheld_hybrid,main_system_rail,school,4,8,0.20,learning",
        "handheld_hybrid,controller/input_rail,play,1,3,0.40,controls",
        "handheld_hybrid,display_rail,media,3,7,0.15,streaming",
        "handheld_hybrid,radio_rail,standby,0.3,1.5,0.10,BLE/Wi-Fi",
        "handheld_hybrid,usb_c_input,charging,10,30,0.10,PD charge",
    ],
    "ds_xl_coder": [
        "ds_xl_coder,battery,developer,5,10,0.35,dual-screen dev",
        "ds_xl_coder,display_rail,school,4,8,0.30,lesson mode",
        "ds_xl_coder,main_system_rail,research,6,12,0.15,local build",
        "ds_xl_coder,audio_rail,media,0.5,2,0.10,speakers",
        "ds_xl_coder,standby,standby,0.2,1,0.10,sleep",
    ],
    "wearables_arena": [
        "wearables_arena,battery,school,0.3,1.5,0.50,beacon idle",
        "wearables_arena,radio_rail,research,0.5,2,0.30,BLE mesh",
        "wearables_arena,main_system_rail,play,1,4,0.15,arena game",
        "wearables_arena,always-on_rail,standby,0.05,0.3,0.40,sensor wake",
        "wearables_arena,usb_c_input,charging,2,5,0.05,case charge",
    ],
}

DEVICES = ["student_14", "handheld_hybrid", "ds_xl_coder", "wearables_arena"]

PORT_TEMPLATE = """# {title} — Port and I/O Map (EVT-1)

> **Not final pinout.** Placeholder for vendor RFQ review.

## USB-C charging/data/video
- USB-C PD target: TBD watt class
- Alt-mode display: TBD (HDMI/DP over USB-C)

## Display
- Internal display connector: TBD eDP/LVDS/MIPI class

## Audio
- Headphone jack: 3.5 mm TRRS placeholder
- Speakers: stereo placeholder

## Wireless
- Wi-Fi/BT module: pre-certified module preferred (FCC/CE module integration)

## Debug and service
- Service connector: pogo or header placeholder — see `io/DEBUG_AND_SERVICE_PORTS.md`

## Dock assumptions
- Dock power + I/O: TBD

## Warning
{BOUNDARY}
"""

THERMAL_TEMPLATE = """# {title} — Thermal Profile (EVT-1)

> No simulated thermal results. Assumptions only.

## Expected heat sources
- SoC/APU, display, PMIC, wireless module, battery charge path

## Touch temperature
- Handheld/skin contact limits per IEC 62368 planning — TBD validation

## Cooling
- Passive vents + optional fan TBD per mechanical review

## Docked mode
- Higher sustained power allowed when docked; throttling policy defers to gunnchOS

## Test equipment needed
- IR camera, thermocouples, ambient chamber (planned EVT-2)

{BOUNDARY}
"""


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists() or p.stat().st_size < 50:
        p.write_text(content.rstrip() + "\n")
        print(f"Wrote {path}")


def main() -> None:
    # Product docs
    write("product/PRODUCT_LINE_REQUIREMENTS.md", f"""# Product Line Requirements (EVT-1)

Derived from [PRD_GUNNCHOS_MODULAR_CONSOLE_ECOSYSTEM.md](PRD_GUNNCHOS_MODULAR_CONSOLE_ECOSYSTEM.md).

| Device | Form factor | Primary workloads |
|--------|-------------|-------------------|
| Student 14.5" | Laptop-adjacent | School, university, Steam, WAIKE |
| Handheld Hybrid | Portable console | Gaming, docked play, deploy target |
| DS-XL Coder | Dual-screen handheld | Coding, game jam, offline lessons |
| Wearables/Arena Set | BLE wearables + puck | Field labs, arena games, Edge-IO |

{BOUNDARY}
""")

    write("product/EVT1_ACCEPTANCE_CRITERIA.md", f"""# EVT-1 Acceptance Criteria

Target: **EVT-1 prototype RFQ package** — vendor-reviewable documentation, not manufacturing release.

## Must have for EVT-1 RFQ pass
- [x] PRD §1–17 coverage in product docs
- [x] Architecture block diagrams for all four device families
- [x] OpenSCAD CAD source for all four families
- [x] Schematic skeleton KiCad blocks per device
- [x] BOM CSV templates with validation
- [x] Power budget CSV templates with validation
- [x] Battery, thermal, compliance planning docs
- [x] Prototype RFQ vendor handoff package
- [ ] EE-reviewed schematics (requires external review)
- [ ] Routed PCB layout (not claimed)
- [ ] Physical prototype test data (not claimed)

{BOUNDARY}
""")

    write("product/CLAIM_BOUNDARY.md", f"""# Claim Boundary

{BOUNDARY}

**Safe claim:** gunnchOS3k has an EVT-1 prototype RFQ documentation package suitable for engineering and vendor scope review.

**Not claimed:** FCC/CE certification, final schematics, Gerbers, DVT/PVT sign-off, manufacturing release.
""")

    # Issue matrix
    issues = [
        (1, "Create product system overview", "docs/PRODUCT_SYSTEM_OVERVIEW.md, architecture/*", "docs/ISSUE_CLOSURE_MATRIX.md", "Closes #1", "Closes #1"),
        (2, "EVT-0 concept CAD Student 14.5\"", "cad/openscad/student_14.scad", "ls cad/openscad/student_14.scad", "Closes #2", "Closes #2"),
        (3, "EVT-0 concept CAD Handheld Hybrid", "cad/openscad/handheld_hybrid.scad", "ls cad/openscad/handheld_hybrid.scad", "Closes #3", "Closes #3"),
        (4, "EVT-0 concept CAD DS-XL Coder", "cad/openscad/ds_xl_coder.scad", "ls cad/openscad/ds_xl_coder.scad", "Closes #4", "Closes #4"),
        (5, "EVT-0 concept CAD Wearables/Arena", "cad/openscad/wearables_arena_set.scad", "ls cad/openscad/wearables_arena_set.scad", "Closes #5", "Closes #5"),
        (6, "Port and I/O docs", "io/*.md", "ls io/", "Closes #6", "Closes #6"),
        (7, "Power budget templates", "power/*_power_budget.csv", "python scripts/validate_power_budget.py", "Closes #7", "Closes #7"),
        (8, "Battery safety notes", "battery/*.md", "ls battery/", "Closes #8", "Closes #8"),
        (9, "Thermal assumptions", "thermal/*.md", "ls thermal/", "Closes #9", "Closes #9"),
        (10, "BOM templates", "bom/*_bom.csv", "python scripts/validate_bom.py", "Closes #10", "Closes #10"),
        (11, "Compliance tracker", "compliance/REGULATORY_MATRIX.md", "ls compliance/", "Closes #11", "Closes #11"),
        (12, "STL exports", "exports/stl/ or exports/OPENSCAD_EXPORT_STATUS.md", "scripts/export_stl_batch.sh", "Refs #12", "Refs #12"),
        (13, "Placeholder renders", "exports/renders/*_placeholder.svg", "ls exports/renders/", "Closes #13", "Closes #13"),
        (14, "Professor/student demo checklist", "demo/PROFESSOR_STUDENT_DEMO_CHECKLIST.md", "ls demo/", "Closes #14", "Closes #14"),
        (15, "Investor diligence checklist", "diligence/INVESTOR_TECHNICAL_DILIGENCE_CHECKLIST.md", "ls diligence/", "Closes #15", "Closes #15"),
        (17, "WAIKE integration", "docs/WAIKE_INTEGRATION.md, docs/TUTOR_CARDS.md", "ls docs/WAIKE*", "Closes #17", "Closes #17"),
    ]
    matrix = """# Issue Closure Matrix

| Issue | Title | Concrete artifact(s) | Validation command/file | Close status | PR keyword |
|---|---|---|---|---|---|
"""
    for row in issues:
        matrix += f"| #{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} |\n"
    write("docs/ISSUE_CLOSURE_MATRIX.md", matrix)

    # Architecture
    if (ROOT / "docs/OS_HARDWARE_CONTRACT.md").exists():
        shutil.copy(ROOT / "docs/OS_HARDWARE_CONTRACT.md", ROOT / "architecture/OS_HARDWARE_CONTRACT.md")

    write("architecture/ECOSYSTEM_DATA_FLOW.md", f"""# Ecosystem Data Flow

```mermaid
flowchart LR
  WAIKE[WAIKE / gunnchAI3k] --> OS[gunnchOS device OS]
  EdgeIO[Edge-IO nodes] --> OS
  OS --> S[Student 14.5]
  OS --> H[Handheld Hybrid]
  OS --> D[DS-XL Coder]
  OS --> W[Wearables Arena]
  H --> Steam[Steam / gaming path]
  S --> Media[Streaming / media path]
  D --> Local[Offline learning path]
```

See also [DATA_FLOW_AND_CONNECTOR_MAP.md](DATA_FLOW_AND_CONNECTOR_MAP.md).

{BOUNDARY}
""")

    # Product system overview
    src = ROOT / "docs/00_product_system_overview.md"
    if src.exists():
        content = src.read_text()
    else:
        content = "# Product System Overview\n"
    write("docs/PRODUCT_SYSTEM_OVERVIEW.md", content + f"\n\nSee [HARDWARE_PACKAGE_INDEX.md](HARDWARE_PACKAGE_INDEX.md).\n\n{BOUNDARY}\n")

    # CAD files
    write("cad/openscad/common_modules.scad", """// EVT-1 common modules — dimensions/tolerances are placeholders, not final mechanical drawings
include <common/dimensions.scad>
include <common/ports.scad>
include <common/branding.scad>
include <common/labels.scad>

module screw_boss(r=2.5, h=6) { cylinder(r=r, h=h, $fn=24); }
module service_panel(w=40, h=20, t=2) { cube([w, h, t]); }
module cooling_vent(w=60, slots=5) {
  for (i=[0:slots-1]) translate([i*12-w/2, 0, 0]) cube([8, 2, 4], center=true);
}
module battery_compartment(w=80, d=60, h=8) { cube([w, d, h], center=true); }
module label_zone(w=30, h=10) { translate([0,0,0.1]) cube([w, h, 0.2]); }
""")

    cad_map = {
        "student_14.scad": "student_14_5/student_14_5_concept.scad",
        "handheld_hybrid.scad": "handheld_hybrid/handheld_hybrid_concept.scad",
        "ds_xl_coder.scad": "ds_xl_coder/ds_xl_coder_concept.scad",
    }
    for dest, src_rel in cad_map.items():
        src_path = ROOT / "cad/openscad" / src_rel
        content = f"""// EVT-1 placeholder — dimensions/tolerances not final mechanical drawings
// Canonical wrapper for vendor RFQ — source: {src_rel}
include <common_modules.scad>
use <{src_rel.replace('.scad', '')}>
"""
        if src_path.exists():
            content = f"""// EVT-1 placeholder — dimensions/tolerances not final mechanical drawings
// Re-exports concept model from {src_rel}
include <common_modules.scad>
include <{src_rel}>
"""
        write(f"cad/openscad/{dest}", content)

    write("cad/openscad/wearables_arena_set.scad", """// EVT-1 wearables arena set — placeholder assembly
// Dimensions/tolerances are EVT-1 placeholders, not final mechanical drawings
include <common_modules.scad>
include <wearables/beacon_puck_concept.scad>
include <wearables/charger_case_concept.scad>
""")

    write("cad/openscad/EXPORT_NOTES.md", f"""# OpenSCAD Export Notes

Export STLs with `scripts/export_stl_batch.sh` when OpenSCAD CLI is installed.

{BOUNDARY}
""")

    # Mechanical
    for name, body in [
        ("MECHANICAL_REQUIREMENTS.md", "Parametric EVT-1 enclosure requirements per device family."),
        ("ENCLOSURE_REQUIREMENTS.md", "Material, IP, drop, and service access placeholders for RFQ."),
        ("REPAIRABILITY_REQUIREMENTS.md", "User-serviceable battery/storage targets; screw-access panels."),
        ("ASSEMBLY_EXPLODED_VIEW_NOTES.md", "Exploded views in cad/openscad/student_14_5/exploded_view.scad — EVT-1 only."),
        ("FASTENER_AND_SERVICE_PLAN.md", "Standard screw bosses; service panel placeholders in OpenSCAD."),
    ]:
        write(f"mechanical/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\n{body}\n\n{BOUNDARY}\n")

    # IO
    titles = {
        "student_14_ports.md": "Student 14.5\"",
        "handheld_hybrid_ports.md": "Handheld Hybrid",
        "ds_xl_coder_ports.md": "DS-XL Coder",
        "wearables_arena_ports.md": "Wearables/Arena Set",
    }
    for fname, title in titles.items():
        write(f"io/{fname}", PORT_TEMPLATE.format(title=title, BOUNDARY=BOUNDARY))

    write("io/PORT_IO_MASTER_MATRIX.md", """# Port I/O Master Matrix

| Device | USB-C | Display | Audio | Wireless | Debug | Dock |
|--------|-------|---------|-------|----------|-------|------|
| Student 14.5" | 2× PD/data | Internal + ext | 3.5 mm + speakers | Wi-Fi/BT module | Service header | USB-C dock |
| Handheld Hybrid | 1× PD/video | Internal | 3.5 mm + stereo | Wi-Fi/BT | UART placeholder | TV dock |
| DS-XL Coder | 1× PD/data | Dual internal | Speakers | Wi-Fi/BT | SWD placeholder | Deploy dock |
| Wearables/Arena | Case USB-C | N/A / AR lite | BLE audio TBD | BLE | Puck debug | Arena charger case |

> Not final pinout — see per-device docs.
""")

    write("io/CONNECTOR_PINOUT_PLACEHOLDERS.md", f"""# Connector Pinout Placeholders

All pinouts are **TBD** pending EE review. Do not use for PCB routing without sign-off.

{BOUNDARY}
""")

    write("io/DEBUG_AND_SERVICE_PORTS.md", f"""# Debug and Service Ports

| Device | Debug | Service |
|--------|-------|---------|
| Student 14.5" | UART/USB service header placeholder | Battery/service panel |
| Handheld Hybrid | Pogo or USB-C debug mode | Thumb-screw back |
| DS-XL Coder | SWD header placeholder | Hinge service access |
| Wearables | Puck UART placeholder | Case contact pins |

{BOUNDARY}
""")

    # Power
    write("power/POWER_BUDGET_MASTER.md", f"""# Power Budget Master

Per-device CSVs under `power/`. Rails: USB-C input, battery, charger, main system, display, storage, radio, controller, audio, always-on, debug.

Validate: `python scripts/validate_power_budget.py`

{BOUNDARY}
""")

    if (ROOT / "architecture/POWER_TREE.md").exists():
        shutil.copy(ROOT / "architecture/POWER_TREE.md", ROOT / "power/POWER_TREE.md")
    else:
        write("power/POWER_TREE.md", "# Power Tree\n\nSee architecture/POWER_TREE.md\n")

    for dev in POWER_ROWS:
        fname = f"power/{dev}_power_budget.csv" if dev != "wearables_arena" else "power/wearables_arena_power_budget.csv"
        write(fname, POWER_HEADER + "\n".join(POWER_ROWS[dev]) + "\n")

    write("power/BATTERY_LIFE_ESTIMATION_METHOD.md", f"""# Battery Life Estimation Method

Wh = sum(mode_power × duty_cycle × hours). Values in CSV are watts (typ range).

No field-validated battery life claims in EVT-1.

{BOUNDARY}
""")

    # Battery expansion
    for name, body in [
        ("BMS_REQUIREMENTS.md", "BMS required on all battery packs; OCP/OVP/UVP/OTP mandatory."),
        ("BATTERY_TEST_PLAN.md", "Charge/discharge cycling, storage, shipping prep — EVT-2 lab."),
        ("BATTERY_RISK_REGISTER.md", "Thermal runaway, shipping, youth deployment — mitigations TBD."),
        ("CHARGER_SELECTION_CRITERIA.md", "Use certified vendor packs; no custom pack without battery engineer."),
    ]:
        write(f"battery/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\n{body}\n\nUse certified vendor battery packs where possible. No DIY unsafe assembly instructions.\n\n{BOUNDARY}\n")

    # Expand thin battery requirements
    write("battery/BATTERY_REQUIREMENTS.md", f"""# Battery Requirements

- Use certified vendor battery packs where possible
- No custom pack without battery engineer review
- BMS required (see BMS_REQUIREMENTS.md)
- Youth/school deployment safety notes in compliance/YOUTH_PRIVACY_AND_SAFETY.md

{BOUNDARY}
""")

    # Thermal
    write("thermal/THERMAL_ASSUMPTIONS.md", f"""# Thermal Assumptions

Passive cooling default; fan optional on Student 14.5\". No fake simulation results.

{BOUNDARY}
""")
    write("thermal/THERMAL_RISK_REGISTER.md", "# Thermal Risk Register\n\nSkin contact, docked sustained load, battery heat — review at EVT-2.\n")

    thermal_titles = {
        "student_14_thermal_profile.md": "Student 14.5\"",
        "handheld_hybrid_thermal_profile.md": "Handheld Hybrid",
        "ds_xl_coder_thermal_profile.md": "DS-XL Coder",
        "wearables_arena_thermal_profile.md": "Wearables/Arena Set",
    }
    for fname, title in thermal_titles.items():
        write(f"thermal/{fname}", THERMAL_TEMPLATE.format(title=title, BOUNDARY=BOUNDARY))

    # BOM extras
    for name in ["BOM_ASSUMPTIONS.md", "APPROVED_VENDOR_CRITERIA.md", "MAKE_BUY_DECISIONS.md"]:
        write(f"bom/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\nTBD module classes; no final part numbers unless quoted.\n\n{BOUNDARY}\n")

    # Schematics
    write("schematics/SCHEMATIC_CLAIM_BOUNDARY.md", f"# Schematic Claim Boundary\n\n{SCHEMATIC_BOUNDARY}\n")
    if (ROOT / "docs/SCHEMATIC_REVIEW_CHECKLIST.md").exists():
        shutil.copy(ROOT / "docs/SCHEMATIC_REVIEW_CHECKLIST.md", ROOT / "schematics/SCHEMATIC_REVIEW_CHECKLIST.md")
    else:
        write("schematics/SCHEMATIC_REVIEW_CHECKLIST.md", f"# Schematic Review Checklist\n\n{SCHEMATIC_BOUNDARY}\n")

    # PCB extras
    for name in [
        "FABRICATION_OUTPUTS_CHECKLIST.md",
        "ASSEMBLY_OUTPUTS_CHECKLIST.md",
        "GERBER_EXPORT_PLAN.md",
        "PICK_AND_PLACE_PLAN.md",
        "PCB_REVIEW_GATE.md",
    ]:
        write(f"pcb/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\nNo Gerbers claimed until layout complete.\n\n{BOUNDARY}\n")

    # Compliance extras
    for name, body in [
        ("UN38_3_BATTERY_PLAN.md", "UN 38.3 transport testing plan — links battery/UN38_3_TRACKER.md"),
        ("WIFI_BLUETOOTH_MODULE_CERT_PLAN.md", "Pre-certified module integration; no DIY RF certification claims"),
        ("COMPLIANCE_EVIDENCE_TRACKER.md", "All certifications planned — none claimed complete"),
    ]:
        write(f"compliance/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\n{body}\n\n{BOUNDARY}\n")

    # Prototype RFQ
    rfq_files = {
        "README.md": "# Prototype RFQ Package\n\nVendor handoff for EVT-1 prototype quoting.\n",
        "RFQ_COVER_LETTER_TEMPLATE.md": "# RFQ Cover Letter Template\n\nDear vendor,\n\nPlease review the attached EVT-1 prototype RFQ package...\n",
        "VENDOR_QUESTIONNAIRE.md": "# Vendor Questionnaire\n\n- Capabilities\n- Lead time\n- MOQ\n- Compliance support\n",
        "FILES_TO_SEND_CHECKLIST.md": """# Files to Send Checklist

## Ready now
- PRD
- block diagrams
- draft BOM
- CAD/OpenSCAD source
- STL exports or export status
- schematic skeletons
- compliance matrix
- power/thermal assumptions
- RFQ cover letter
- vendor questionnaire

## Not ready yet
- final routed PCB
- Gerbers
- drill files
- pick-and-place
- real DFM/DFT review
- compliance pre-scan
- battery certification
- prototype test data
- CM quotes
""",
        "NDA_AND_IP_NOTES.md": "# NDA and IP Notes\n\nExecute NDA before sharing detailed EE artifacts.\n",
        "QUOTE_COMPARISON_MATRIX.md": "# Quote Comparison Matrix\n\n| Vendor | Scope | Lead time | Cost | Notes |\n",
        "PROTOTYPE_BUILD_REQUEST.md": "# Prototype Build Request\n\nEVT-1 functional prototype units — quantity TBD.\n",
        "ENGINEERING_REVIEW_REQUEST.md": "# Engineering Review Request\n\nRequest EE review of schematic skeletons and power tree.\n",
        "CM_SHORTLIST_TRACKER.md": "# CM Shortlist Tracker\n\n| CM | Region | Status |\n",
    }
    for fname, body in rfq_files.items():
        write(f"prototype_rfq/{fname}", body + f"\n{BOUNDARY}\n")

    # Manufacturing extras
    write("manufacturing/SPC_METRICS_PLAN.md", f"# SPC Metrics Plan\n\nPilot build metrics — not active until DVT.\n\n{BOUNDARY}\n")
    write("manufacturing/REV_A_TO_REV_B_PLAN.md", f"# Rev A to Rev B Plan\n\nPost-prototype design iteration gate.\n\n{BOUNDARY}\n")

    # Demo & diligence
    write("demo/PROFESSOR_STUDENT_DEMO_CHECKLIST.md", """# Professor/Student Demo Checklist

- [ ] Product vision (PRD)
- [ ] Each device family walkthrough
- [ ] CAD/renders (placeholder labeled)
- [ ] Port maps
- [ ] Power/battery/thermal docs
- [ ] WAIKE integration
- [ ] Repairability
- [ ] Accessibility
- [ ] What is real vs not claimed
""")
    write("demo/DEVICE_WALKTHROUGH_SCRIPT.md", "# Device Walkthrough Script\n\n30-min demo script per device family.\n")
    write("demo/SCREENSHOT_RENDER_CAPTURE_PLAN.md", "# Screenshot/Render Capture Plan\n\nCapture OpenSCAD preview or placeholder SVGs.\n")

    write("diligence/INVESTOR_TECHNICAL_DILIGENCE_CHECKLIST.md", """# Investor Technical Diligence Checklist

- [ ] PRD
- [ ] CAD
- [ ] Schematics (skeleton)
- [ ] BOM
- [ ] Compliance matrix
- [ ] Manufacturing plan
- [ ] Unit economics reference (bom cost models)
- [ ] Risk register
- [ ] IP/FTO notes (NDA)
- [ ] Vendor RFQ package
- [ ] Prototype milestones
""")
    write("diligence/ENGINEERING_DILIGENCE_RESPONSE.md", "# Engineering Diligence Response\n\nTemplate responses for technical reviewers.\n")
    write("diligence/OPEN_GAPS_FOR_PROTOTYPE_VENDOR.md", "# Open Gaps for Prototype Vendor\n\nPCB layout, certification, physical test data.\n")

    # WAIKE docs
    write("docs/TUTOR_CARDS.md", """# Tutor Cards (gunnchAI3k)

| Card | Device | Task |
|------|--------|------|
| HW-01 | Student 14.5" | Explain port map |
| HW-02 | Handheld | Dock vs handheld power |
| HW-03 | DS-XL | Dual-screen dev workflow |
| HW-04 | Wearables | BLE arena setup |
""")
    write("docs/STUDENT_TASKS.md", """# Student Tasks by Device

See docs/DEVICE_LEARNING_PATHWAYS.md and docs/WAIKE_INTEGRATION.md.
""")
    write("docs/DEVICE_LEARNING_PATHWAYS.md", """# Device Learning Pathways

Local/offline learning, coding/game jam, field measurement, teardown/repair tasks per device.
""")
    write("docs/EDUCATOR_DEMO_SCRIPT.md", """# Educator Demo Script

Safety rules for minors; accessibility and low-cost access notes.
""")

    # Exports
    write("exports/README.md", "# Exports\n\nSTL and placeholder renders for vendor review.\n")
    write("exports/OPENSCAD_EXPORT_STATUS.md", """# OpenSCAD Export Status

OpenSCAD CLI was **not available** in the CI/local environment used for this pass.

## To generate STLs

```bash
./scripts/export_stl_batch.sh
```

Requires OpenSCAD installed. Do not commit fake STL geometry.

## Expected outputs
- exports/stl/student_14_placeholder.stl
- exports/stl/handheld_hybrid_placeholder.stl
- exports/stl/ds_xl_coder_placeholder.stl
- exports/stl/wearables_arena_set_placeholder.stl
""")

    # Placeholder SVG renders
    svg_template = """<svg xmlns="http://www.w3.org/2000/svg" width="400" height="240" viewBox="0 0 400 240">
  <rect width="400" height="240" fill="#f4f4f5"/>
  <text x="200" y="110" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#52525b">{label}</text>
  <text x="200" y="140" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#71717a">EVT-1 PLACEHOLDER RENDER</text>
  <text x="200" y="165" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#a1a1aa">Not a manufacturing drawing</text>
</svg>"""
    render_names = {
        "student_14_placeholder.svg": "Student 14.5\"",
        "handheld_hybrid_placeholder.svg": "Handheld Hybrid",
        "ds_xl_coder_placeholder.svg": "DS-XL Coder",
        "wearables_arena_set_placeholder.svg": "Wearables/Arena Set",
    }
    for fname, label in render_names.items():
        write(f"exports/renders/{fname}", svg_template.format(label=label))

    # Audit doc
    write("docs/EVT1_FINALIZATION_AUDIT.md", """# EVT-1 Finalization Audit

See validation scripts for current status. Bootstrap completed missing RFQ paths.

| Area | Status |
|------|--------|
| product/ | exists_complete after bootstrap |
| prototype_rfq/ | created |
| io/ power/ exports/ | created |
| cad/openscad canonical names | created |
| validation scripts | updated |
""")

    print("Bootstrap complete.")


if __name__ == "__main__":
    main()
