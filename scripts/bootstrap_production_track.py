#!/usr/bin/env python3
"""Bootstrap prototype-ready and production-candidate track packages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NOT_PRODUCTION = (
    "Production release status: Not met. "
    "This repository does not yet meet production-readiness gates."
)

PRODUCTION_VENDOR_SECTION = """
## Production-track question for vendors

Can your team help move this EVT-1 prototype package toward a production-candidate package?

Please identify which of these services you provide:

- electrical schematic review
- PCB layout
- Gerber/drill/CPL generation
- DFM review
- DFT review
- prototype PCBA
- enclosure prototyping
- battery/charger engineering review
- compliance pre-scan support
- production test fixture design
- pilot manufacturing
- packaging/labeling support
"""


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.rstrip() + "\n")
    print(f"Wrote {path}")


def main() -> None:
    write("versions/README.md", """# Version Tracks

| Track | Purpose |
|-------|---------|
| [prototype_evt1/](prototype_evt1/) | EVT-1 prototype-ready package for vendor/engineering review |
| [production_candidate/](production_candidate/) | Production-readiness requirements — **not production released** |
""")

    write("versions/prototype_evt1/README.md", """# EVT-1 Prototype-Ready Package

This is the EVT-1 prototype-ready package. It is intended for prototype vendor and engineering review. It is not a production release.

Start here:
- [PROTOTYPE_READY_PACKAGE.md](PROTOTYPE_READY_PACKAGE.md)
- [PROTOTYPE_FILE_MANIFEST.md](PROTOTYPE_FILE_MANIFEST.md)
- [PROTOTYPE_VENDOR_HANDOFF.md](PROTOTYPE_VENDOR_HANDOFF.md)
""")

    write("versions/prototype_evt1/PROTOTYPE_READY_PACKAGE.md", """# Prototype-Ready Package

**Status:** EVT-1 prototype RFQ package — suitable for prototype vendor review.

**Not claimed:** production release, certification, final PCB layout, DVT/PVT completion.

See [PROTOTYPE_FILE_MANIFEST.md](PROTOTYPE_FILE_MANIFEST.md) for artifact links.
""")

    manifest_links = """
| Artifact | Link |
|----------|------|
| PRD | [product/PRD_GUNNCHOS_MODULAR_CONSOLE_ECOSYSTEM.md](../../product/PRD_GUNNCHOS_MODULAR_CONSOLE_ECOSYSTEM.md) |
| Architecture | [architecture/SYSTEM_BLOCK_DIAGRAM.md](../../architecture/SYSTEM_BLOCK_DIAGRAM.md) |
| CAD/OpenSCAD | [cad/openscad/](../../cad/openscad/) |
| STL exports | [exports/stl/](../../exports/stl/) or [exports/OPENSCAD_EXPORT_STATUS.md](../../exports/OPENSCAD_EXPORT_STATUS.md) |
| Renders | [exports/renders/](../../exports/renders/) |
| Schematics | [schematics/](../../schematics/) |
| BOM | [bom/MASTER_BOM.md](../../bom/MASTER_BOM.md) |
| Power budget | [power/POWER_BUDGET_MASTER.md](../../power/POWER_BUDGET_MASTER.md) |
| Battery safety | [battery/BATTERY_REQUIREMENTS.md](../../battery/BATTERY_REQUIREMENTS.md) |
| Thermal | [thermal/THERMAL_REQUIREMENTS.md](../../thermal/THERMAL_REQUIREMENTS.md) |
| Compliance matrix | [compliance/REGULATORY_MATRIX.md](../../compliance/REGULATORY_MATRIX.md) |
| Prototype RFQ | [prototype_rfq/](../../prototype_rfq/) |
| Manufacturing plan | [manufacturing/EVT_DVT_PVT_PLAN.md](../../manufacturing/EVT_DVT_PVT_PLAN.md) |
| Issue closure matrix | [docs/ISSUE_CLOSURE_MATRIX.md](../../docs/ISSUE_CLOSURE_MATRIX.md) |
"""
    write("versions/prototype_evt1/PROTOTYPE_FILE_MANIFEST.md", f"# Prototype File Manifest\n\n{manifest_links}")

    write("versions/prototype_evt1/PROTOTYPE_VENDOR_HANDOFF.md", """# Prototype Vendor Handoff

Use with [prototype_rfq/FILES_TO_SEND_CHECKLIST.md](../../prototype_rfq/FILES_TO_SEND_CHECKLIST.md).

This package is for prototype quoting and engineering review only — not production release.
""")

    write("versions/prototype_evt1/PROTOTYPE_BUILD_SCOPE.md", """# Prototype Build Scope

EVT-1 functional prototype units — quantity TBD. Enclosure print, PCBA bring-up, and fit check.

Requires engineering, compliance, CM, and lab validation before production-candidate status.
""")

    write("versions/prototype_evt1/PROTOTYPE_ACCEPTANCE_TEST_PLAN.md", """# Prototype Acceptance Test Plan

- [ ] Enclosure printability check
- [ ] Mechanical fit check
- [ ] Port cutout inspection
- [ ] Device family visual review
- [ ] Schematic skeleton review
- [ ] BOM review
- [ ] Battery safety review
- [ ] Thermal assumption review
- [ ] Vendor RFQ review

**No production claims** — prototype acceptance only.
""")

    write("versions/prototype_evt1/PROTOTYPE_KNOWN_GAPS.md", """# Prototype Known Gaps

- Final routed PCB layout
- Gerbers, drill files, pick-and-place
- Compliance certification evidence
- Battery certification evidence
- DVT/PVT test reports
- Production test fixture
""")

    # Production candidate
    write("versions/production_candidate/README.md", """# Production-Candidate Track

This is the production-candidate track. It defines what must exist before the hardware can be called production-ready. The current repository does not yet meet these gates.

Start here:
- [PRODUCTION_READINESS_REQUIREMENTS.md](PRODUCTION_READINESS_REQUIREMENTS.md)
- [PRODUCTION_RELEASE_CHECKLIST.md](PRODUCTION_RELEASE_CHECKLIST.md)
- [PRODUCTION_GAP_ANALYSIS.md](PRODUCTION_GAP_ANALYSIS.md)
""")

    write("versions/production_candidate/PRODUCTION_READINESS_REQUIREMENTS.md", f"""# Production Readiness Requirements

Defines evidence required before production release can be claimed.

{NOT_PRODUCTION}

See [PRODUCTION_FILE_MANIFEST_REQUIRED.md](PRODUCTION_FILE_MANIFEST_REQUIRED.md).
""")

    write("versions/production_candidate/PRODUCTION_RELEASE_CHECKLIST.md", """# Production Release Checklist

Gates: Concept → EVT-0 → EVT-1 prototype RFQ → EVT-2 engineering prototype → DVT → PVT → Pilot production → Production release

**Current status:** EVT-1 prototype RFQ package merged.
**Production release status:** Not met.
""")

    write("versions/production_candidate/PRODUCTION_FILE_MANIFEST_REQUIRED.md", """# Production File Manifest Required

## Already present
- PRD
- architecture docs
- EVT-1 CAD/OpenSCAD
- schematic skeletons
- draft BOM
- power budget templates
- thermal/battery/compliance planning
- prototype RFQ package

## Required before production release
- final electrical schematics reviewed by hardware engineer
- routed PCB layout
- Gerber files
- drill files
- pick-and-place / centroid files
- assembly drawing
- board stackup approved by fabricator
- DFM review
- DFT review
- SI/PI review where needed
- thermal simulation or measured thermal test data
- battery pack certification evidence
- charger safety review
- FCC/CE/UKCA compliance evidence as applicable
- Wi-Fi/Bluetooth module integration evidence
- SBOM and open-source compliance evidence
- prototype build logs
- bring-up logs
- EVT test report
- DVT test report
- PVT test report
- CM signoff
- quality plan
- production test fixture plan
- warranty/repair process
""")

    write("versions/production_candidate/PRODUCTION_GAP_ANALYSIS.md", f"""# Production Gap Analysis

| Area | Present | Required for production | Gap |
|------|---------|-------------------------|-----|
| Schematics | Skeleton | EE-reviewed final | Major |
| PCB layout | Not started | Routed layout | Major |
| Gerbers | None | Verified outputs | Major |
| Compliance | Planning | Certification evidence | Major |
| Battery | Planning | Certification evidence | Major |
| DVT/PVT | Plans only | Test reports | Major |

{NOT_PRODUCTION}
""")

    write("versions/production_candidate/PRODUCTION_ACCEPTANCE_TEST_PLAN.md", """# Production Acceptance Test Plan

Production release requires DVT/PVT evidence — not yet performed.

See manufacturing/DVT_PLAN.md and manufacturing/PVT_PLAN.md.
""")

    for name in [
        "PRODUCTION_BOM_LOCK_POLICY.md",
        "PRODUCTION_PCB_OUTPUT_REQUIREMENTS.md",
        "PRODUCTION_COMPLIANCE_EVIDENCE_REQUIRED.md",
        "PRODUCTION_BATTERY_CERTIFICATION_REQUIRED.md",
        "PRODUCTION_DVT_PVT_REQUIREMENTS.md",
        "PRODUCTION_VENDOR_SIGNOFF_REQUIRED.md",
    ]:
        write(f"versions/production_candidate/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\n{NOT_PRODUCTION}\n")

    # Production backlog
    write("production_backlog/README.md", "# Production Backlog\n\nDraft GitHub issues for production-readiness work.\n")
    issues = """# Production Issues to Create

Draft only — do not auto-create without review.

## P0
1. Select electrical engineering reviewer for schematic package
2. Convert schematic skeletons into reviewed electrical schematics
3. Create routed PCB layout for Student 14.5"
4. Create routed PCB layout for Handheld Hybrid
5. Create routed PCB layout for DS-XL Coder
6. Create routed PCB layout for Wearables/Arena Set
7. Generate Gerbers, drill files, and pick-and-place outputs
8. Complete DFM review
9. Complete DFT review
10. Obtain BOM quotes from at least three vendors
11. Battery and charger engineering review
12. Thermal simulation and/or measured prototype thermal testing
13. FCC/CE/UKCA compliance pre-scan planning
14. Prototype build #1 and bring-up report

## P1
15. Production test fixture plan
16. Repairability and service manual
17. Packaging and labeling requirements
18. Warranty/SLA plan
19. Supplier quality agreement checklist
20. Pilot manufacturing run plan
"""
    write("production_backlog/PRODUCTION_ISSUES_TO_CREATE.md", issues)
    for name in ["VENDOR_WORK_PACKAGES.md", "ENGINEERING_WORK_PACKAGES.md", "COMPLIANCE_WORK_PACKAGES.md"]:
        write(f"production_backlog/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\nSee PRODUCTION_ISSUES_TO_CREATE.md.\n")

    # Manufacturing
    mfg_files = {
        "PRODUCTION_RELEASE_PLAN.md": "Production release plan — gates and evidence. Not production released.",
        "PRODUCTION_GATE_REVIEW.md": """# Production Gate Review

| Gate | Required evidence | Current status | Owner | Pass/fail |
|------|-------------------|----------------|-------|-----------|
| EVT-1 prototype RFQ | PRD, CAD, BOM, RFQ package | Met (merged) | HW | Pass |
| EVT-2 engineering prototype | Reviewed schematics, prototype build | Not met | EE | Fail |
| DVT | DVT test report | Not met | QA | Fail |
| PVT | PVT test report | Not met | CM | Fail |
| Production release | All production manifest items | Not met | Program | Fail |

Production release status: Not met.
""",
        "DVT_PLAN.md": "DVT plan — prototype-ready now; production-candidate pending.",
        "PVT_PLAN.md": "PVT plan — production-candidate pending; production release not claimed.",
        "PILOT_PRODUCTION_PLAN.md": "Pilot production plan — not yet active.",
        "PRODUCTION_TEST_FIXTURE_PLAN.md": "Production test fixture — required before production release.",
        "SUPPLIER_QUALITY_PLAN.md": "Supplier quality — production-candidate pending.",
        "REPAIR_AND_SERVICE_PLAN.md": "Repair/service — prototype docs exist; production manual pending.",
        "PACKAGING_AND_LABELING_PLAN.md": "Packaging/labeling — production-candidate requirements.",
    }
    for fname, body in mfg_files.items():
        write(f"manufacturing/{fname}", f"# {fname.replace('_', ' ').replace('.md', '')}\n\n{body}\n")

    # Compliance
    compliance_status = """
FCC/CE/UKCA status: Not certified.
Battery certification status: Not certified.
RF exposure review status: Not performed.
Compliance lab review: Not performed.
"""
    for fname in [
        "PRODUCTION_COMPLIANCE_PLAN.md",
        "FCC_EQUIPMENT_AUTHORIZATION_TRACKER.md",
        "MODULE_INTEGRATION_CHECKLIST.md",
        "LABELING_AND_USER_MANUAL_REQUIREMENTS.md",
        "RF_EXPOSURE_REVIEW_PLAN.md",
        "COMPLIANCE_LAB_RFQ_TEMPLATE.md",
    ]:
        write(f"compliance/{fname}", f"# {fname.replace('_', ' ').replace('.md', '')}\n\n{compliance_status}\nDo not fake certification.\n")

    # PCB
    pcb_status = """
No final routed PCB layout exists yet.
No Gerbers exist yet.
No drill files exist yet.
No pick-and-place files exist yet.
These are production-candidate requirements, not current artifacts.
"""
    for fname in [
        "PRODUCTION_PCB_PACKAGE_REQUIREMENTS.md",
        "GERBER_OUTPUT_STATUS.md",
        "DRILL_FILE_STATUS.md",
        "PICK_AND_PLACE_STATUS.md",
        "PCB_LAYOUT_STATUS.md",
        "PCB_VENDOR_HANDOFF_CHECKLIST.md",
        "ASSEMBLY_VENDOR_HANDOFF_CHECKLIST.md",
    ]:
        write(f"pcb/{fname}", f"# {fname.replace('_', ' ').replace('.md', '')}\n\n{pcb_status}\n")

    # Update prototype RFQ files - append section
    for rfq in [
        "prototype_rfq/FILES_TO_SEND_CHECKLIST.md",
        "prototype_rfq/VENDOR_QUESTIONNAIRE.md",
        "prototype_rfq/QUOTE_COMPARISON_MATRIX.md",
        "prototype_rfq/PROTOTYPE_BUILD_REQUEST.md",
        "prototype_rfq/ENGINEERING_REVIEW_REQUEST.md",
    ]:
        p = ROOT / rfq
        if p.exists():
            text = p.read_text()
            if "Production-track question" not in text:
                p.write_text(text.rstrip() + "\n" + PRODUCTION_VENDOR_SECTION + "\n")

    print("Bootstrap complete.")


if __name__ == "__main__":
    main()
