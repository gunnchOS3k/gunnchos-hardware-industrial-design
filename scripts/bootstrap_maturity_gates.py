#!/usr/bin/env python3
"""Bootstrap mechanical/printability/DVT/PVT/certification/production packages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOUNDARY = (
    "This package defines readiness gates only. It does not claim production release, "
    "certification, or DVT/PVT completion without external evidence."
)

RFQ_SECTION = """
## Project summary
EVT-1 gunnchOS hardware — moving toward production-candidate status.

## Files available
See `versions/prototype_evt1/PROTOTYPE_FILE_MANIFEST.md`.

## What is not ready yet
Final routed PCB, Gerbers, certification reports, DVT/PVT test data, production release.

## NDA/IP
See `prototype_rfq/NDA_AND_IP_NOTES.md`.
"""


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.rstrip() + "\n")
    print(f"Wrote {path}")


def main() -> None:
    # Mechanical correctness
    write("mechanical_correctness/README.md", f"""# Mechanical Correctness Validation Track

Requires external engineering review and physical prototype test evidence.

See [MECHANICAL_CORRECTNESS_STATUS.md](MECHANICAL_CORRECTNESS_STATUS.md).

{BOUNDARY}
""")

    mech_files = {
        "MECHANICAL_CORRECTNESS_REQUIREMENTS.md": "Dimensional control, interference, tolerance, and assembly requirements.",
        "DIMENSION_CONTROL_PLAN.md": "Critical dimensions and inspection points — EVT-1 placeholders.",
        "TOLERANCE_STACKUP_PLAN.md": "Stack-up analysis plan per device family.",
        "WALL_THICKNESS_REQUIREMENTS.md": "Minimum wall thickness targets for print/enclosure.",
        "PORT_CLEARANCE_REQUIREMENTS.md": "USB-C, audio, vent, and dock clearances.",
        "FASTENER_BOSS_REQUIREMENTS.md": "Screw boss and fastener plan placeholders.",
        "BUTTON_CONTROL_CLEARANCE_REQUIREMENTS.md": "Button, stick, and control clearance.",
        "DISPLAY_FIT_CHECK_PLAN.md": "Display opening and bezel fit checks.",
        "BATTERY_COMPARTMENT_FIT_CHECK.md": "Battery compartment volume and service access.",
        "CONNECTOR_KEEP_OUT_ZONES.md": "RF and structural keep-out zones.",
        "ENCLOSURE_INTERFERENCE_CHECK_PLAN.md": "PCB/enclosure interference check plan.",
        "ASSEMBLY_CLEARANCE_CHECKLIST.md": "Pre-assembly clearance checklist.",
        "MECHANICAL_REVIEW_GATE.md": "Gate before DVT — engineer signoff required.",
    }
    for name, body in mech_files.items():
        write(f"mechanical_correctness/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\n{body}\n\n{BOUNDARY}\n")

    write("mechanical_correctness/MECHANICAL_CORRECTNESS_STATUS.md", """# Mechanical Correctness Status

Current status: CAD/STL artifacts exist and basic STL validation passes.
Mechanical correctness status: Not yet proven.
Required next evidence: dimensional review, interference checks, tolerance review, print test, physical assembly review, and engineer signoff.

| Device | STL exists | Dimensions defined | Wall thickness checked | Port clearance checked | Assembly checked | Status |
|--------|------------|--------------------|------------------------|------------------------|------------------|--------|
| Student 14.5" | Yes | Partial (OpenSCAD) | No | No | No | not proven |
| Handheld Hybrid | Yes | Partial | No | No | No | not proven |
| DS-XL Coder | Yes | Partial | No | No | No | not proven |
| Wearables/Arena Set | Yes | Partial | No | No | No | not proven |
""")

    # Printability
    write("printability/README.md", f"# Printability Validation Track\n\n{BOUNDARY}\n")
    for name in [
        "PRINTABILITY_REQUIREMENTS.md",
        "PRINT_ORIENTATION_PLAN.md",
        "SUPPORT_MATERIAL_PLAN.md",
        "WALL_THICKNESS_AND_CLEARANCE_PLAN.md",
        "MATERIAL_SELECTION_FOR_PROTOTYPES.md",
        "PRINT_VENDOR_RFQ.md",
        "FIRST_ARTICLE_PRINT_CHECKLIST.md",
        "FIT_AND_FINISH_REVIEW.md",
    ]:
        write(f"printability/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\n{BOUNDARY}\n")

    write("printability/PRINTABILITY_STATUS.md", """# Printability Status

Current status: STL files exist and are validated as plausible STL artifacts.
Printability status: Not fully proven.
Required next evidence: mesh/manifold validation, wall-thickness validation, slicer review, first-article print, fit check, and vendor/engineer review.

## First-article print checklist
- [ ] print orientation selected
- [ ] material selected
- [ ] scale verified
- [ ] wall thickness reviewed
- [ ] port cutouts inspected
- [ ] button/control holes inspected
- [ ] screw bosses inspected
- [ ] service panel inspected
- [ ] display opening inspected
- [ ] assembly interference checked
- [ ] revision notes captured
- [ ] photo evidence added
""")

    # DVT
    write("dvt/README.md", f"# DVT Readiness Package\n\nDVT complete status: **Not complete.**\n\n{BOUNDARY}\n")
    dvt_tests = """## DVT test areas
- mechanical fit
- enclosure durability
- hinge durability (DS-XL)
- button/stick wear
- port insertion cycle plan
- thermal load testing
- battery charge/discharge testing
- display tests
- audio tests
- wireless module integration tests
- safety inspection
- firmware/OS integration
- drop/handling plan
- school-use durability assumptions
"""
    for name in [
        "DVT_READINESS_REQUIREMENTS.md",
        "DVT_TEST_PLAN.md",
        "DVT_MECHANICAL_TEST_PLAN.md",
        "DVT_ELECTRICAL_TEST_PLAN.md",
        "DVT_THERMAL_TEST_PLAN.md",
        "DVT_BATTERY_TEST_PLAN.md",
        "DVT_DISPLAY_INPUT_TEST_PLAN.md",
        "DVT_DROP_AND_DURABILITY_TEST_PLAN.md",
        "DVT_ENVIRONMENTAL_TEST_PLAN.md",
        "DVT_SOFTWARE_HARDWARE_INTEGRATION_PLAN.md",
        "DVT_SAMPLE_SIZE_PLAN.md",
        "DVT_PASS_FAIL_CRITERIA.md",
        "DVT_REPORT_TEMPLATE.md",
    ]:
        extra = dvt_tests if name == "DVT_TEST_PLAN.md" else ""
        write(f"dvt/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\n{extra}\n{BOUNDARY}\n")

    write("dvt/DVT_STATUS.md", """# DVT Status

Current status: DVT readiness documentation exists after this pass.
DVT complete status: Not complete.
Required evidence: physical EVT prototypes, test execution logs, failure reports, fixes, retest evidence, and engineering signoff.
""")

    # PVT
    write("pvt/README.md", f"# PVT Readiness Package\n\nPVT complete status: **Not complete.**\n\n{BOUNDARY}\n")
    pvt_body = """## PVT scope
- assembly line readiness
- test fixture readiness
- packaging and labeling
- supplier readiness
- work instructions
- production test plan
- yield tracking
- failure analysis loop
- quality metrics
- service/repair readiness
"""
    for name in [
        "PVT_READINESS_REQUIREMENTS.md",
        "PVT_TEST_PLAN.md",
        "PVT_BUILD_PLAN.md",
        "PVT_FACTORY_PROCESS_PLAN.md",
        "PVT_YIELD_TARGETS.md",
        "PVT_PRODUCTION_TEST_PLAN.md",
        "PVT_QUALITY_METRICS.md",
        "PVT_SUPPLIER_READINESS_CHECKLIST.md",
        "PVT_PACKAGING_AND_LABELING_CHECKLIST.md",
        "PVT_REPAIR_AND_SERVICE_CHECKLIST.md",
        "PVT_REPORT_TEMPLATE.md",
    ]:
        extra = pvt_body if name == "PVT_TEST_PLAN.md" else ""
        write(f"pvt/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\n{extra}\n{BOUNDARY}\n")

    write("pvt/PVT_STATUS.md", """# PVT Status

Current status: PVT readiness documentation exists after this pass.
PVT complete status: Not complete.
Required evidence: pilot production build, factory process data, yield data, production test logs, supplier signoff, packaging/labeling review, and quality signoff.
""")

    # Certification
    write("certification/README.md", f"# Certification Readiness Package\n\nCertification status: **Not certified.**\n\n{BOUNDARY}\n")
    write("certification/CERTIFICATION_READINESS_MATRIX.md", """# Certification Readiness Matrix

| Certification / compliance area | Applies? | Required evidence | Current evidence | Status | Owner | Next action |
|---|---|---|---|---|---|---|
| FCC Part 15 / equipment authorization | Yes | Lab test report, ID label | Planning docs only | planned | Compliance | Lab RFQ |
| CE | Yes | Technical file, DoC | Planning docs only | planned | Compliance | Lab RFQ |
| UKCA | Yes | Technical file | Planning docs only | planned | Compliance | Lab RFQ |
| RoHS | Yes | Material declarations | Planning docs only | planned | CM | Supplier docs |
| REACH | Yes | SVHC declarations | Planning docs only | planned | CM | Supplier docs |
| UN 38.3 battery transport | Yes | Test summary | Planning docs only | planned | Battery EE | Lab quote |
| IEC/UL safety review | Yes | Safety test report | Planning docs only | planned | Safety | Lab quote |
| Wi-Fi/Bluetooth module integration | Yes | Module cert + integration evidence | Planning docs only | planned | RF EE | Module selection |
| RF exposure review | Yes | SAR/exposure assessment | None | not_started | Compliance | Lab plan |
| Labeling and manual requirements | Yes | Label art, manual | Draft requirements | planned | Program | Content draft |
| Open-source SBOM | Yes | SBOM artifact | Plan only | planned | Legal/Eng | SBOM generation |
| Youth/privacy/safety documentation | Yes | Policy docs | Draft in compliance/ | planned | Program | Review |
""")

    write("certification/CERTIFICATION_STATUS.md", """# Certification Status

Current status: certification readiness planning exists after this pass.
Certification status: Not certified.
Required evidence: lab engagement, test plans, test reports, responsible party documentation, technical file, product labels, user manual, declarations, and applicable regulatory approvals.

FCC/CE/UKCA status: Not certified.
Battery certification status: Not certified.
RF exposure review status: Not performed.
Compliance lab review: Not performed.
""")

    for name in [
        "FCC_CERTIFICATION_READINESS.md",
        "CE_UKCA_READINESS.md",
        "ROHS_REACH_READINESS.md",
        "UN38_3_BATTERY_READINESS.md",
        "IEC_UL_SAFETY_READINESS.md",
        "WIFI_BLUETOOTH_MODULE_CERT_READINESS.md",
        "RF_EXPOSURE_READINESS.md",
        "LABELING_AND_USER_MANUAL_READINESS.md",
        "CERTIFICATION_LAB_RFQ.md",
        "CERTIFICATION_EVIDENCE_REQUIRED.md",
    ]:
        write(f"certification/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\nCertification status: Not certified.\n\n{BOUNDARY}\n")

    # Production release
    write("production_release/README.md", f"# Production Release Gate Package\n\nProduction release status: **Not released.**\n\n{BOUNDARY}\n")
    write("production_release/PRODUCTION_RELEASE_EVIDENCE_MATRIX.md", """# Production Release Evidence Matrix

| Gate | Required evidence | Current evidence | Status | Signoff role | Blocking? |
|------|-------------------|------------------|--------|--------------|-----------|
| mechanical correctness | Engineer review + fit check | STL + validation report | planned | ME | Yes |
| printability | First-article print + mesh check | STL only | planned | ME/Vendor | Yes |
| electrical schematic review | EE-reviewed schematics | Skeleton only | not_started | EE | Yes |
| routed PCB | Layout files | Not started | not_started | EE | Yes |
| Gerbers/drill/CPL | Fabrication outputs | None | not_started | EE/CM | Yes |
| DFM review | Vendor report | Not performed | not_started | CM | Yes |
| DFT review | Test coverage report | Not performed | not_started | EE | Yes |
| BOM lock | Locked BOM + AVL | Draft BOM | planned | Program | Yes |
| supplier quotes | ≥3 quotes | Tracker only | planned | Program | Yes |
| battery safety | EE review + cert path | Planning docs | planned | Battery EE | Yes |
| thermal validation | Sim or measured data | Assumptions only | not_started | Thermal EE | Yes |
| firmware/OS integration | Integration test report | OS alpha external | planned | SW/HW | Yes |
| DVT pass | DVT report | Not complete | not_started | QA | Yes |
| PVT pass | PVT report | Not complete | not_started | CM/QA | Yes |
| compliance/certification | Lab reports | Not certified | not_started | Compliance | Yes |
| packaging/labeling | Approved art/manual | Plan only | planned | Program | Yes |
| repair/service | Service manual | Plan only | planned | Service | Yes |
| production test fixture | Fixture design + validation | Plan only | planned | EE/CM | Yes |
| CM signoff | CM release letter | None | not_started | CM | Yes |
""")

    write("production_release/PRODUCTION_RELEASE_STATUS.md", """# Production Release Status

Current status: production release requirements defined.
Production release status: Not released.
Required evidence: DVT pass, PVT pass, certification evidence, final BOM lock, routed PCB outputs, CM signoff, quality plan, service plan, packaging plan, and release signoff.
""")

    for name in [
        "PRODUCTION_RELEASE_REQUIREMENTS.md",
        "PRODUCTION_RELEASE_GATE.md",
        "PRODUCTION_RELEASE_CHECKLIST.md",
        "PRODUCTION_RELEASE_RISK_REGISTER.md",
        "PRODUCTION_RELEASE_SIGNOFF_TEMPLATE.md",
    ]:
        write(f"production_release/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\nProduction release status: Not released.\n\n{BOUNDARY}\n")

    # Vendor labs
    write("vendor_labs/README.md", "# Vendor and Lab RFQ Package\n")
    rfqs = [
        "MECHANICAL_ENGINEERING_REVIEW_RFQ.md",
        "PRINT_VENDOR_RFQ.md",
        "PCB_PCBA_VENDOR_RFQ.md",
        "COMPLIANCE_LAB_RFQ.md",
        "BATTERY_ENGINEERING_REVIEW_RFQ.md",
        "THERMAL_ENGINEERING_REVIEW_RFQ.md",
        "CONTRACT_MANUFACTURER_RFQ.md",
    ]
    for name in rfqs:
        write(f"vendor_labs/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n{RFQ_SECTION}\n")

    write("vendor_labs/VENDOR_RESPONSE_SCORECARD.md", """# Vendor Response Scorecard

| Vendor | Technical capability | Similar product experience | DFM/DFT | Compliance | Battery safety | Enclosure/prototype | Production scaling | Lead time | Cost transparency | Mission fit | Total |
|--------|---------------------|---------------------------|---------|------------|----------------|---------------------|-------------------|-----------|-------------------|-------------|-------|
""")

    # Production backlog issues
    write("production_backlog/MECHANICAL_PRINT_DVT_PVT_CERTIFICATION_ISSUES.md", """# Mechanical / Print / DVT / PVT / Certification Issue Drafts

Draft only — do not auto-create without review.

## P0
1. **Mechanical engineer review of STL/CAD package** — Review OpenSCAD/STL, tolerance plan, interference.
2. **Printability/manifold/wall-thickness validation** — Run admesh/slicer review on all STLs.
3. **First article 3D print — Student 14.5"**
4. **First article 3D print — Handheld Hybrid**
5. **First article 3D print — DS-XL Coder**
6. **First article 3D print — Wearables/Arena Set**
7. **Convert schematic skeletons into reviewed electrical schematics**
8. **Create routed PCB layout package**
9. **Generate Gerbers, drill files, and pick-and-place outputs**
10. **DFM/DFT review with PCB/PCBA vendor**
11. **Battery engineering review**
12. **Thermal engineering review**
13. **FCC pre-scan/compliance lab quote**
14. **CE/UKCA/RoHS/REACH compliance plan quote**
15. **UN 38.3 battery transport documentation quote**
16. **DVT test execution package**
17. **PVT build plan and factory readiness package**
18. **Production release gate review**

## P1
19. **Packaging and labeling review**
20. **Repair/service manual and warranty readiness**
""")

    print("Bootstrap complete.")


if __name__ == "__main__":
    main()
