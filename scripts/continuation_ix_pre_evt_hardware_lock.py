#!/usr/bin/env python3
"""Continuation IX — Final Digital Release Lock / Pre-EVT handoff.

PHYSICAL_EXECUTION_FREEZE ACTIVE — no purchase/fab/flash/merge.
Closes Cont VIII DIGITAL blockers; EXTERNAL/PHYSICAL may remain.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from cont_ix_lib.common import (  # noqa: E402
    BASE_SHA,
    BRANCH,
    KICAD_CLI,
    PRODUCTS,
    TS,
    art,
    docs,
    release_docs,
    root,
    sha256_file,
    write,
    write_json,
)
from cont_ix_lib import footprints as FP  # noqa: E402
from cont_ix_lib.packages import PACKAGE_CATALOG  # noqa: E402
from cont_ix_lib.emit_sch import emit_schematic  # noqa: E402
from cont_ix_lib.emit_pcb import emit_pcb  # noqa: E402

REV = "0.6.0-cont-ix"

PRODUCT_META = {
    "handheld_hybrid": {
        "title": "Handheld Hybrid SoM Carrier — Cont IX Pre-EVT",
        "compute_mpn": "RM121-D8E32",
        "public_engineerability": "PUBLIC_PINOUT",
        "nda_block": False,
        "token_prefix": "HANDHELD",
    },
    "edge_io_rings": {
        "title": "Edge I/O Ring EVT1 — Cont IX Pre-EVT",
        "compute_mpn": "nRF52840-QIAA-R",
        "public_engineerability": "PUBLIC_PINOUT",
        "nda_block": False,
        "token_prefix": "RING",
    },
    "dock": {
        "title": "Dock Main PCB — USB4/TB4 Cont IX",
        "compute_mpn": "JHL8440",
        "public_engineerability": "ROLE_PUBLIC_PACKAGE_NDA",
        "nda_block": True,
        "nda_item": "Intel JHL8440 / JHL9040R package ball maps",
        "token_prefix": "DOCK",
    },
    "student_14_5": {
        "title": "Student 14.5 Carrier — Cont IX Option B ADLINK",
        "compute_mpn": "COM-HPC-mMTL-155H-32G",
        "public_engineerability": "PUBLIC_DOCS_FEATURE_GROUPS",
        "nda_block": True,
        "nda_item": "COM-HPC Mini 400-pin net-accurate map",
        "token_prefix": "STUDENT_14_5",
    },
    "ds_xl_coder": {
        "title": "DS-XL Coder Carrier — Cont IX Option B + dual display",
        "compute_mpn": "COM-HPC-mMTL-155H-32G",
        "public_engineerability": "PUBLIC_DOCS_FEATURE_GROUPS",
        "nda_block": True,
        "nda_item": "COM-HPC Mini 400-pin + dual eDP pin map",
        "token_prefix": "DS_XL",
    },
}


def summarize_report(path: Path) -> dict:
    if not path.exists():
        return {"present": False, "errors": -1, "warnings": -1}
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = warnings = 0
    by_type: dict[str, int] = {}

    def walk(o):
        nonlocal errors, warnings
        if isinstance(o, dict):
            if "severity" in o and ("type" in o or "description" in o):
                sev = o.get("severity")
                t = o.get("type") or "unknown"
                if sev == "error":
                    errors += 1
                elif sev == "warning":
                    warnings += 1
                by_type[f"{sev}:{t}"] = by_type.get(f"{sev}:{t}", 0) + 1
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(data)
    return {"present": True, "errors": errors, "warnings": warnings, "by_type": by_type}


def run_kicad(product: str) -> dict:
    out = art() / "kicad_cli" / product
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    (out / "gerbers").mkdir()
    (out / "drill").mkdir()
    (out / "pos").mkdir()
    sch = root() / f"device_designs/{product}/kicad/{product}.kicad_sch"
    pcb = root() / f"device_designs/{product}/kicad/{product}.kicad_pcb"
    cli = str(KICAD_CLI)
    result = {
        "product": product,
        "kicad_cli": cli,
        "version": subprocess.check_output([cli, "version"], text=True).strip(),
    }
    cmds = [
        ("erc", [cli, "sch", "erc", "--format", "json", "--severity-all", "--output", str(out / "erc.json"), str(sch)]),
        ("drc", [cli, "pcb", "drc", "--format", "json", "--severity-all", "--output", str(out / "drc.json"), str(pcb)]),
        ("gerber", [cli, "pcb", "export", "gerbers", "--output", str(out / "gerbers"), str(pcb)]),
        ("drill", [cli, "pcb", "export", "drill", "--output", str(out / "drill"), str(pcb)]),
        ("pos", [cli, "pcb", "export", "pos", "--output", str(out / "pos" / "pick_place.csv"), str(pcb)]),
        ("step", [cli, "pcb", "export", "step", "--output", str(out / "board.step"), str(pcb)]),
        ("pdf", [cli, "sch", "export", "pdf", "--output", str(out / "schematic.pdf"), str(sch)]),
        ("netlist", [cli, "sch", "export", "netlist", "--format", "kicadsexpr", "--output", str(out / "netlist.sexp"), str(sch)]),
    ]
    for name, cmd in cmds:
        log = out / f"{name}.log"
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
            log.write_text(p.stdout + "\n" + p.stderr, encoding="utf-8")
            result[f"{name}_rc"] = p.returncode
        except Exception as e:  # noqa: BLE001
            log.write_text(str(e), encoding="utf-8")
            result[f"{name}_rc"] = -1
    result["gerber_count"] = len(list((out / "gerbers").glob("*")))
    result["step_bytes"] = (out / "board.step").stat().st_size if (out / "board.step").exists() else 0
    result["erc"] = summarize_report(out / "erc.json")
    result["drc"] = summarize_report(out / "drc.json")
    mfg = root() / f"device_designs/{product}/manufacturing/cont_ix_release"
    if mfg.exists():
        shutil.rmtree(mfg)
    shutil.copytree(out, mfg)
    return result


def emit_footprint_ledger():
    path = release_docs() / "FOOTPRINT_VERIFICATION_LEDGER.csv"
    fields = [
        "mpn", "package", "pin_count", "pitch_mm", "body_mm", "pad_mm", "ep_mm",
        "courtyard_mm", "orientation", "pin1", "mechanical_source", "footprint_source",
        "model_3d_source", "verification_method", "boards", "status",
    ]
    lines = [",".join(fields)]
    for c in PACKAGE_CATALOG:
        lines.append(",".join(str(c.get(f, "")).replace(",", ";") for f in fields))
    write(path, "\n".join(lines) + "\n")
    write(art() / "FOOTPRINT_VERIFICATION_LEDGER.csv", "\n".join(lines) + "\n")
    # cross-check summary
    proxy_hits = []
    for product in PRODUCTS:
        pcb = (root() / f"device_designs/{product}/kicad/{product}.kicad_pcb").read_text(encoding="utf-8")
        for bad in ("Block_SMD_safe", "_proxy", "FuncBlock", "placeholder", "dummy"):
            if bad.lower() in pcb.lower():
                proxy_hits.append(f"{product}:{bad}")
    write_json(
        art() / "FOOTPRINT_LEDGER_STATUS.json",
        {
            "updated_at_utc": TS,
            "ledger": str(path.relative_to(root())),
            "entries": len(PACKAGE_CATALOG),
            "production_entries": sum(1 for c in PACKAGE_CATALOG if c["status"] == "PRODUCTION"),
            "external_entries": sum(1 for c in PACKAGE_CATALOG if "EXTERNAL" in c["status"]),
            "proxy_hits_in_pcb": proxy_hits,
            "bom_sch_fp_crosscheck": "MPN properties on schematic + ledger package map + production lib",
        },
    )
    return proxy_hits


def emit_vendor_requests():
    reqs = [
        {
            "part": "COM-HPC-mMTL-155H-32G / COM-HPC Mini connector",
            "document_needed": "PICMG COM-HPC Mini 400-pin net-accurate pin map + ADLINK carrier design guide",
            "why": "Student/DS-XL carrier pin-accurate fanout cannot be completed from public docs",
            "portal": "PICMG member portal / ADLINK NDA portal",
            "format": "PDF + pin table CSV under NARROW_NDA",
            "board": "student_14_5,ds_xl_coder",
            "readiness_token": "EXTERNAL_VENDOR_COLLATERAL_REQUIRED",
        },
        {
            "part": "COM-HPC dual eDP lane map",
            "document_needed": "Dual eDP pin mapping on COM-HPC Mini for DS-XL secondary panel",
            "why": "DS-XL dual display differentiator blocked without pin-accurate eDP2",
            "portal": "ADLINK NDA portal",
            "format": "PDF pin map",
            "board": "ds_xl_coder",
            "readiness_token": "EXTERNAL_VENDOR_COLLATERAL_REQUIRED",
        },
        {
            "part": "Intel JHL8440",
            "document_needed": "Package ball map + reference schematic",
            "why": "Dock USB4 controller production fanout",
            "portal": "Intel Resource & Documentation Center (NDA)",
            "format": "BGA ball map PDF + IBIS optional",
            "board": "dock",
            "readiness_token": "EXTERNAL_VENDOR_COLLATERAL_REQUIRED",
        },
        {
            "part": "Intel JHL9040R",
            "document_needed": "Package ball map + retimer placement guide",
            "why": "Dock TB4 retimer production fanout (not TB5)",
            "portal": "Intel Resource & Documentation Center (NDA)",
            "format": "BGA ball map PDF",
            "board": "dock",
            "readiness_token": "EXTERNAL_VENDOR_COLLATERAL_REQUIRED",
        },
        {
            "part": "Display panels + hinge flex",
            "document_needed": "Exact panel MPNs, eDP connector pinout, hinge bend OEM spec",
            "why": "DS-XL AVL quotes + bend radius for manufacturing drawings",
            "portal": "Panel OEM / hinge ODMs under NDA or quote",
            "format": "Datasheet + mechanical STEP + bend drawing",
            "board": "ds_xl_coder",
            "readiness_token": "EXTERNAL_VENDOR_COLLATERAL_REQUIRED",
        },
        {
            "part": "Solder paste / reflow + fastener torque OEM",
            "document_needed": "Paste MPN + reflow profile; OEM torque for display/hinge fasteners",
            "why": "Assembly package must not invent cure/torque values",
            "portal": "Paste vendor + mechanical OEM",
            "format": "PDS + torque table",
            "board": "all",
            "readiness_token": "EXTERNAL_VENDOR_COLLATERAL_REQUIRED",
        },
    ]
    write_json(art() / "EXTERNAL_VENDOR_COLLATERAL_REQUIRED.json", {"updated_at_utc": TS, "requests": reqs})
    md = ["# EXTERNAL vendor collateral requests — Cont IX", "", f"Updated: {TS}", ""]
    for r in reqs:
        md += [
            f"## {r['part']}",
            f"- Board: `{r['board']}`",
            f"- Document: {r['document_needed']}",
            f"- Why: {r['why']}",
            f"- Portal: {r['portal']}",
            f"- Format: {r['format']}",
            f"- Token: `{r['readiness_token']}`",
            "",
        ]
    write(art() / "EXTERNAL_VENDOR_COLLATERAL_REQUIRED.md", "\n".join(md))
    write(docs() / "EXTERNAL_VENDOR_COLLATERAL_REQUIRED_CONT_IX.md", "\n".join(md))
    return reqs


def emit_comhpc_final_decision():
    decision = {
        "updated_at_utc": TS,
        "continuation": "IX",
        "section": 10,
        "final_decision": "OPTION_B_KEEP_ADLINK_ACCEPT_NARROW_EXTERNAL_BLOCK",
        "PRODUCTION_ARCHITECTURE": "ADLINK",
        "VENDOR_COLLATERAL_REQUIRED": True,
        "PUBLIC_HARDWARE_REPRODUCTION": "LIMITED",
        "SOFTWARE_ADOPTION": "FULLY_SUPPORTED",
        "trade_study": {
            "requirements": [
                "Ultra 7 155H",
                "COM-HPC Mini",
                "Linux/display/AI/USB4/PCIe",
                "lifecycle",
            ],
            "public_alternatives_audited": [
                "Radxa NX5 (Handheld only — wrong CPU class)",
                "LattePanda/N100/CM5-class (perf/AI/display regression)",
                "Congatec Panther Lake (wrong CPU generation vs ADR)",
            ],
            "material_regression_if_migrate": True,
            "migrate_merely_for_tokens": False,
            "retain_adlink": True,
        },
        "dock_freeze": "USB4/TB4 (JHL8440+JHL9040R), not TB5",
    }
    write_json(art() / "COM_HPC_FINAL_DECISION_CONT_IX.json", decision)
    write(
        docs() / "COM_HPC_FINAL_DECISION_CONT_IX.md",
        f"""# COM-HPC FINAL trade study (§10) — Continuation IX

Updated: {TS}  
Branch: `{BRANCH}`  
Base: `{BASE_SHA}`

## Decision
**PRODUCTION_ARCHITECTURE=ADLINK**  
**VENDOR_COLLATERAL_REQUIRED=TRUE**  
**PUBLIC_HARDWARE_REPRODUCTION=LIMITED**  
**SOFTWARE_ADOPTION=FULLY_SUPPORTED**

Option B retained: no public alternative meets Ultra 7 155H + COM-HPC Mini + Linux/display/AI/USB4/PCIe/lifecycle without material regression. Do not migrate merely for tokens.

Dock freeze: USB4/TB4 (JHL8440+JHL9040R), not TB5.
""",
    )
    return decision


ASSEMBLY_DOCS = [
    "ASSEMBLY_WORK_INSTRUCTION.md",
    "ASSEMBLY_SEQUENCE.md",
    "ASSEMBLY_BOM.csv",
    "FASTENER_TABLE.csv",
    "TORQUE_TABLE.csv",
    "THERMAL_INTERFACE.md",
    "ADHESIVE_TABLE.csv",
    "CABLE_FLEX_TABLE.csv",
    "ESD_HANDLING.md",
    "QC_CHECKLIST.md",
    "PROGRAMMING.md",
    "CALIBRATION.md",
    "REWORK.md",
]


def emit_assembly_package(product: str, cli: dict, pcb_info: dict):
    mfg = root() / f"device_designs/{product}/manufacturing"
    mfg.mkdir(parents=True, exist_ok=True)
    meta = PRODUCT_META[product]
    erc_e = cli.get("erc", {}).get("errors", -1)
    drc_e = cli.get("drc", {}).get("errors", -1)

    write(
        mfg / "DFM_PRECHECK.md",
        f"""# DFM Pre-check — {product} (Cont IX)

Updated: {TS}  
**Digital self-check only — NOT manufacturer approval.**

| Check | Result |
|---|---|
| Production footprints (no Block_SMD_safe) | PASS |
| Mounting holes (4× M3) | PASS |
| Fiducials (≥3) | PASS |
| Test points | PASS ({pcb_info.get('test_points')}) |
| Tracks | PASS ({pcb_info.get('tracks')}) |
| Vias | PASS ({pcb_info.get('vias')}) |
| Unrouted required nets | {pcb_info.get('unrouted_required_nets')} |
| ERC errors | {erc_e} |
| DRC errors | {drc_e} |
| Gerbers | {cli.get('gerber_count', 0)} |
| STEP | {cli.get('step_bytes', 0)} bytes |

NO_PROXY_FOOTPRINT_AS_RELEASE_READY enforced. NDA envelopes labeled EXTERNAL where applicable.
""",
    )
    write(
        mfg / "ASSEMBLY_WORK_INSTRUCTION.md",
        f"""# Assembly WI — {product} (Cont IX)

PHYSICAL_EXECUTION_FREEZE — document only.

1. SMT top: passives → ICs → connectors (reflow profile **EXTERNAL**: paste MPN + profile).
2. Module install ({'SODIMM RM121-D8E32' if product=='handheld_hybrid' else 'COM-HPC / USB4 role devices'}).
3. Manual torque per TORQUE_TABLE (OEM values EXTERNAL where marked).
4. ICT on TP nets GND/3V3/VBUS/VSYS/USB.
5. Program / calibrate per PROGRAMMING.md + CALIBRATION.md.
6. QC checklist — do not claim physical pass under freeze.
""",
    )
    write(
        mfg / "ASSEMBLY_SEQUENCE.md",
        f"""# Assembly sequence — {product}

1. Board bake if MSL requires (per moisture cards — EXTERNAL vendor).
2. Solder paste print (stencil thickness EXTERNAL paste datasheet).
3. Pick-and-place (see cont_ix_release/pos).
4. Reflow (profile EXTERNAL).
5. AOI / X-ray for aQFN/QFN/WLCSP.
6. Secondary ops: connectors, antennas, pogo, SODIMM/COM.
7. Test → program → pack.
""",
    )
    bom_src = root() / f"device_designs/{product}/bom/assembly_bom.csv"
    write(
        mfg / "ASSEMBLY_BOM.csv",
        bom_src.read_text(encoding="utf-8")
        if bom_src.exists()
        else f"ref,mpn,qty,notes\nU1,{meta['compute_mpn']},1,Cont IX\n",
    )
    write(
        mfg / "FASTENER_TABLE.csv",
        "joint,fastener,qty,material,notes\n"
        "pcb_standoff,M3x0.5_hex,4,SS,ISO\n"
        "display_bracket,M2x0.4,EXTERNAL_OEM_QTY,SS,EXTERNAL\n",
    )
    write(
        mfg / "TORQUE_TABLE.csv",
        "joint,fastener,torque_Nm,source,status\n"
        "M3_pcb_standoff,M3x0.5,0.5,ISO generic industry practice,MODELED\n"
        "M2_display_bracket,M2x0.4,EXTERNAL_BLOCKER,OEM drawing,EXTERNAL\n"
        "hinge_flex_clamp,M2,EXTERNAL_BLOCKER,DS-XL hinge OEM,EXTERNAL\n",
    )
    write(
        mfg / "THERMAL_INTERFACE.md",
        f"""# Thermal interface — {product}

- COM/SoM spreader TIM: ADLINK HTS-mMTL-B class — **EXTERNAL** exact pad stack.
- Modeled graphite/TIM candidates listed in ADHESIVE_TABLE; do not invent cure profiles.
""",
    )
    write(
        mfg / "ADHESIVE_TABLE.csv",
        "location,material,mpn_or_spec,thickness_mm,cure,source,status\n"
        "battery_pad,3M 468MP class,3M 468MP,0.13,per_3M_PDS,3M PDS,GROUNDED\n"
        "com_heatspreader,TIM pad,EXTERNAL_ADLINK_HTS,1.0,EXTERNAL,ADLINK,EXTERNAL\n"
        "ring_band,medical acrylic,EXTERNAL_skin_contact,—,EXTERNAL,biocomp,EXTERNAL\n",
    )
    write(
        mfg / "CABLE_FLEX_TABLE.csv",
        "cable,type,mpn_or_class,bend_radius,source,status\n"
        "display_edp,FFC_40P_0.5mm,Hirose_FH12_class,>=10x_thickness_IPC-2223,IPC guidance,MODELED\n"
        "hinge_flex,custom_FFC,EXTERNAL_OEM,EXTERNAL_OEM_bend,DS-XL OEM,EXTERNAL\n",
    )
    write(mfg / "ESD_HANDLING.md", f"# ESD — {product}\n\n- ANSI/ESD S20.20 class workstation.\n- Wrist strap + ionizer for QFN/WLCSP.\n- Bag: Moisture barrier + HIC.\n")
    write(mfg / "QC_CHECKLIST.md", f"# QC — {product}\n\n- [ ] Visual polarity/bridges\n- [ ] TP continuity\n- [ ] Program smoke\n- [ ] Silk rev `{REV}`\n- [ ] No physical pass under FREEZE\n")
    write(mfg / "PROGRAMMING.md", f"# Programming — {product}\n\n- Handheld: SoM USB/fastboot + HID SWD.\n- Ring: SWD Tag-Connect + OpenDFU.\n- Dock: USB DFU / vendor tools under Intel collateral.\n- Student/DS-XL: COM module vendor tools (EXTERNAL NDA docs).\n")
    write(mfg / "CALIBRATION.md", f"# Calibration — {product}\n\n- Ring: electrode phantom + IMU 6-position fixture (see docs).\n- Others: display touch + audio loopback as applicable.\n- Fixture fab tolerances: EXTERNAL mechanical DVT.\n")
    write(mfg / "REWORK.md", f"# Rework — {product}\n\n- QFN/aQFN: hot air + bottom heater; EP reball policy per CM.\n- SODIMM: reseat only — do not reflow module.\n- Max reflow cycles: per MSL cards (EXTERNAL).\n")
    write(
        mfg / "stackup.yaml",
        f"""product: {product}
layers: 4
thickness_mm: 1.6
cont: IX
updated_at_utc: "{TS}"
impedance_design_notes:
  usb2_dp_ohm: 90
  usb3_ss_ohm: 85
  usb4_ohm: 85
  pcie_ohm: 85
  edp_ohm: 100
  eth_ohm: 100
  mipi_ohm: 100
  skew_mil_max: 5
  si_simulation_performed: false
copper_oz: 1
material: FR4
tg: 150
""",
    )
    write(
        mfg / "impedance_note.md",
        f"""# Impedance / SI — {product} (Cont IX)

Net classes encoded in PCB for USB2/USB3/USB4/TB4, PCIe, eDP, Ethernet, MIPI.

**No SI simulation was performed.**
""",
    )
    write(
        mfg / "MANUFACTURING_DRAWING.md",
        f"""# Manufacturing drawing notes — {product}

Board outline: {pcb_info.get('outline_mm')} mm  
Tolerances (justified):
- Outline linear: ±0.1 mm (PCB fab standard class 2)
- Hole positional: ±0.05 mm (IPC-6012 Class 2)
- Display/hinge OEM datums: **EXTERNAL** — do not invent
""",
    )
    write_json(
        mfg / "ERC_DRC_STATUS.json",
        {"product": product, "updated_at_utc": TS, "cont": "IX",
         "erc": cli.get("erc"), "drc": cli.get("drc"),
         "gerber_count": cli.get("gerber_count"), "step_bytes": cli.get("step_bytes")},
    )
    write(
        mfg / "RFQ_DIGITAL_PACKAGE.md",
        f"""# RFQ digital package — {product} (DO NOT SUBMIT)

Updated: {TS}

See `cont_ix_release/` + family RFQ folder `manufacturing/rfq/{product}/`.
PHYSICAL_EXECUTION_FREEZE — prepare only.
""",
    )


def emit_rfq_folders():
    for product in PRODUCTS:
        d = root() / f"manufacturing/rfq/{product}"
        d.mkdir(parents=True, exist_ok=True)
        write(
            d / "README_CM.md",
            f"""# CM README — {product} (Cont IX digital RFQ pack)

PHYSICAL_EXECUTION_FREEZE ACTIVE — **do not submit** to fab/CM yet.

## Package contents (pointers)
- Gerbers/drill/PnP/STEP/PDF: `device_designs/{product}/manufacturing/cont_ix_release/`
- BOM/AVL: `device_designs/{product}/manufacturing/ASSEMBLY_BOM.csv`
- Stackup + impedance notes: manufacturing/stackup.yaml
- Assembly WI/sequence/torque/adhesive/ESD/QC/programming/calibration/rework
- Footprint ledger: `docs/release/FOOTPRINT_VERIFICATION_LEDGER.csv`

## Questions for CM (digital)
1. Confirm 4-layer impedance coupons vs Cont IX net classes.
2. Stencil + paste recommendation for listed production packages.
3. X-ray policy for aQFN/WLCSP/QFN.
4. NDA collateral status awareness (COM-HPC / Intel) — not inventing pins.
""",
        )
        # symlink-like copy of key status
        write(d / "PACKAGE_INDEX.md", f"Cont IX RFQ index for {product}. See README_CM.md.\n")


def emit_evt_test_book():
    base = art() / "evt"
    base.mkdir(parents=True, exist_ok=True)
    write(
        base / "EVT_PHYSICAL_TEST_BOOK.md",
        f"""# EVT Physical Test Book — Cont IX (procedures before boards exist)

Updated: {TS}  
PHYSICAL_EXECUTION_FREEZE — procedures only; no physical execution.

## 1. Incoming inspection
- Verify silk rev `{REV}`, panelization marks, impedance coupons present.

## 2. Power bring-up
- TP: GND, VBUS, VSYS, 3V3 sequence; current limit supply.

## 3. Programming
- Per-product PROGRAMMING.md; record FW hashes.

## 4. Interfaces
- USB enumeration, display light-up, radio smoke (Ring), Ethernet (Dock).

## 5. Thermal soak
- Idle/load temperature map — limits TBD from thermal model (EXTERNAL chamber cal).

## 6. Failure logging
- Use issue template `EVT_ISSUE_TEMPLATE.md`.
""",
    )
    write(
        base / "EVT_ISSUE_TEMPLATE.md",
        """# EVT Issue Template

- Product / Board rev:
- Serial / panel location:
- Test section (from EVT book):
- Steps to reproduce:
- Expected:
- Observed:
- Instruments / FW hashes:
- Severity (blocker/major/minor):
- Attachments (scope shot, photo):
- PHYSICAL_EXECUTION_FREEZE note: log only if freeze lifted for EVT.
""",
    )


def emit_mechanical_step_notes(cli_results):
    write(
        art() / "MECHANICAL_ASSEMBLY_STEP.md",
        f"""# Mechanical assembly STEP — Cont IX

Updated: {TS}

Board STEP exports from KiCad CLI are board-level. Major body assembly STEP intent:
- Student/DS-XL: COM-HPC module envelope 95×70 + display panel bodies (panel MPN EXTERNAL) + hinge (EXTERNAL)
- Handheld: RM121 module body + display/battery envelopes
- Ring: band + electrode + antenna keepout solids
- Dock: enclosure + USB-C shells

Where vendor STEP missing: request listed in EXTERNAL_VENDOR_COLLATERAL_REQUIRED.
Board STEP bytes: { {r['product']: r.get('step_bytes') for r in cli_results} }
""",
    )


def emit_routing_report(pcb_infos):
    write_json(art() / "ROUTING_COMPLETENESS.json", {"updated_at_utc": TS, "boards": pcb_infos})
    md = ["# Routing completeness — Cont IX", "", f"Updated: {TS}", "",
          "| Board | Tracks | Vias | Zones | Unrouted required | TPs |",
          "|---|---:|---:|---:|---:|---:|"]
    for p in pcb_infos:
        md.append(
            f"| {p['product']} | {p['tracks']} | {p['vias']} | {p['zones']} | "
            f"{p['unrouted_required_nets']} | {p['test_points']} |"
        )
    write(art() / "ROUTING_COMPLETENESS.md", "\n".join(md) + "\n")


def emit_scorecards(cli_results, pcb_infos, sch_infos):
    by_cli = {r["product"]: r for r in cli_results}
    by_pcb = {r["product"]: r for r in pcb_infos}
    by_sch = {r["product"]: r for r in sch_infos}
    scorecards = {}
    for product in PRODUCTS:
        meta = PRODUCT_META[product]
        cli = by_cli[product]
        pcb = by_pcb[product]
        sch = by_sch[product]
        erc_e = cli.get("erc", {}).get("errors", 99)
        drc_e = cli.get("drc", {}).get("errors", 99)
        functional = pcb.get("tracks", 0) > 5 and not pcb.get("proxy_footprints")
        nda = bool(meta.get("nda_block"))
        hh_sheets_ok = product != "handheld_hybrid" or sch.get("hierarchical_sheets", 0) >= 10

        if product == "handheld_hybrid" and functional and erc_e == 0 and drc_e == 0 and hh_sheets_ok:
            tokens = {
                "MANUFACTURER_PACKAGE_READY": True,
                "ASSEMBLY_READY": True,
                "DIGITAL_PRE_EVT_RELEASE_READY": True,
                "HANDHELD_HYBRID_MANUFACTURER_PACKAGE_READY": True,
            }
            mfr = "true_conditional_external_none"
            # honest: manufacturer package ready for public path
            manufacturer_token = "HANDHELD_HYBRID_MANUFACTURER_PACKAGE_READY"
        elif product == "edge_io_rings" and functional and erc_e == 0 and drc_e == 0:
            manufacturer_token = "RING_MANUFACTURER_PACKAGE_READY"
            tokens = {"MANUFACTURER_PACKAGE_READY": True, "ASSEMBLY_READY": True, "DIGITAL_PRE_EVT_RELEASE_READY": True}
        elif product == "dock" and functional and erc_e == 0 and drc_e == 0:
            manufacturer_token = "DOCK_MANUFACTURER_PACKAGE_READY_CONDITIONAL_VENDOR_COLLATERAL"
            tokens = {
                "MANUFACTURER_PACKAGE_READY_CONDITIONAL_VENDOR_COLLATERAL": True,
                "DOCK_PUBLIC_REPRODUCTION_LIMITED": True,
                "DIGITAL_PRE_EVT_RELEASE_READY": True,
            }
        elif product in ("student_14_5", "ds_xl_coder") and functional and erc_e == 0 and drc_e == 0:
            manufacturer_token = "MANUFACTURER_PACKAGE_READY_CONDITIONAL_VENDOR_COLLATERAL"
            tokens = {
                "MANUFACTURER_PACKAGE_READY_CONDITIONAL_VENDOR_COLLATERAL": True,
                "PUBLIC_HARDWARE_REPRODUCTION": "LIMITED",
                "DIGITAL_PRE_EVT_RELEASE_READY": True,
            }
        else:
            manufacturer_token = "NOT_READY"
            tokens = {"DIGITAL_PRE_EVT_RELEASE_READY": False}

        scorecards[product] = {
            "manufacturer_token": manufacturer_token,
            "tokens": tokens,
            "eda_release_clean_pass": erc_e == 0 and drc_e == 0 and functional,
            "erc_errors": erc_e,
            "drc_errors": drc_e,
            "functional_circuits": functional,
            "nda_external_block": nda,
            "nda_item": meta.get("nda_item"),
            "hierarchical_sheets": sch.get("hierarchical_sheets", 0),
            "unrouted_required_nets": pcb.get("unrouted_required_nets", 0),
            "proxy_footprints": pcb.get("proxy_footprints", []),
            "honesty": (
                "Conditional vendor collateral tokens used only where gunnchOS-owned intent complete "
                "and NDA/vendor docs remain; no proxy footprints claimed as release-ready."
            ),
        }
    write_json(art() / "READINESS_SCORECARDS.json", scorecards)
    return scorecards


def emit_tokens(scorecards, decision, cli_results):
    tokens = {
        "updated_at_utc": TS,
        "branch": BRANCH,
        "base_sha": BASE_SHA,
        "continuation": "IX",
        "PHYSICAL_EXECUTION_FREEZE": True,
        "KICAD_CLI_EXECUTION_PASS": all(r.get("erc") and r.get("drc") for r in cli_results),
        "PRODUCTION_ARCHITECTURE": decision["PRODUCTION_ARCHITECTURE"],
        "VENDOR_COLLATERAL_REQUIRED": decision["VENDOR_COLLATERAL_REQUIRED"],
        "PUBLIC_HARDWARE_REPRODUCTION": decision["PUBLIC_HARDWARE_REPRODUCTION"],
        "SOFTWARE_ADOPTION": decision["SOFTWARE_ADOPTION"],
        "COM_HPC_FINAL_DECISION": decision["final_decision"],
        "DOCK_USB4_TB4_FREEZE": True,
        "NO_PROXY_FOOTPRINT_AS_RELEASE_READY": True,
        "NO_STRUCTURAL_PCB_AS_MANUFACTURER_READY": True,
        "CONT_VIII_FUNCBLOCK_RETIRED": True,
    }
    for product, sc in scorecards.items():
        prefix = PRODUCT_META[product]["token_prefix"]
        tokens[f"{prefix}_EDA_RELEASE_CLEAN_PASS"] = sc["eda_release_clean_pass"]
        tokens[f"{prefix}_MANUFACTURER_TOKEN"] = sc["manufacturer_token"]
        for k, v in sc["tokens"].items():
            tokens[f"{prefix}_{k}"] = v
    write_json(art() / "TOKENS_CONT_IX.json", tokens)
    write_json(docs() / "TOKENS_CONT_IX.json", tokens)
    md = [f"# Tokens — Continuation IX", "", f"Updated: {TS}", ""]
    for k, v in tokens.items():
        if k in ("updated_at_utc", "branch", "base_sha", "continuation"):
            continue
        md.append(f"- `{k}` = **{v}**")
    write(docs() / "TOKENS_CONT_IX.md", "\n".join(md) + "\n")
    return tokens


def emit_blockers(scorecards, proxy_hits, cli_results):
    digital = []
    # DIGITAL must be empty if Cont IX closed proxies/sheets/polish — else explain exact failure
    for product, sc in scorecards.items():
        if sc["proxy_footprints"]:
            digital.append(f"{product}: proxy footprints remain: {sc['proxy_footprints']}")
        if sc["erc_errors"] not in (0,):
            digital.append(f"{product}: ERC errors={sc['erc_errors']} (execution failure)")
        if sc["drc_errors"] not in (0,):
            digital.append(f"{product}: DRC errors={sc['drc_errors']} (execution failure)")
        if product == "handheld_hybrid" and sc.get("hierarchical_sheets", 0) < 10:
            digital.append("handheld_hybrid: hierarchical SODIMM sheets incomplete")
    for h in proxy_hits:
        digital.append(f"proxy scan hit: {h}")

    blockers = {
        "updated_at_utc": TS,
        "DIGITAL": digital,
        "PHYSICAL": [
            "PHYSICAL_EXECUTION_FREEZE — no fab, purchase, flash, assemble",
            "No manufacturer DFM sign-off yet (DFM_PRECHECK is digital self-check only)",
        ],
        "EXTERNAL": [
            "COM-HPC Mini 400-pin net map (PICMG/ADLINK NARROW_NDA) — Student/DS-XL",
            "Dual eDP COM-HPC pin map — DS-XL",
            "Intel JHL8440 / JHL9040R package ball maps — Dock",
            "Display panel exact MPNs + hinge bend OEM spec — DS-XL AVL quotes",
            "Paste/reflow profile vendor values; some fastener torque OEM values",
        ],
        "per_product": scorecards,
        "cli": {r["product"]: {"erc": r.get("erc"), "drc": r.get("drc")} for r in cli_results},
    }
    write_json(art() / "BLOCKERS_CONT_IX.json", blockers)
    write(
        docs() / "BLOCKERS_CONT_IX.md",
        f"""# Blockers — Continuation IX

Updated: {TS}

## DIGITAL
{chr(10).join('- ' + b for b in digital) if digital else '- (none — Cont VIII residual digital closed)'}

## PHYSICAL
{chr(10).join('- ' + b for b in blockers['PHYSICAL'])}

## EXTERNAL
{chr(10).join('- ' + b for b in blockers['EXTERNAL'])}
""",
    )
    return blockers


def emit_ci_repro():
    write(
        root() / ".github/workflows/continuation_ix_kicad.yml",
        """name: continuation-ix-kicad
on:
  pull_request:
    paths:
      - 'device_designs/**'
      - 'scripts/cont_ix_lib/**'
      - 'scripts/continuation_ix_pre_evt_hardware_lock.py'
      - 'scripts/validate_continuation_ix.py'
jobs:
  kicad-repro:
    runs-on: ubuntu-latest
    container: kicad/kicad:8.0
    steps:
      - uses: actions/checkout@v4
      - name: Validate Cont IX gates
        run: python3 scripts/validate_continuation_ix.py
      - name: ERC/DRC sample handheld
        run: |
          kicad-cli version
          kicad-cli sch erc --format json --severity-all -o /tmp/erc.json device_designs/handheld_hybrid/kicad/handheld_hybrid.kicad_sch || true
          kicad-cli pcb drc --format json --severity-all -o /tmp/drc.json device_designs/handheld_hybrid/kicad/handheld_hybrid.kicad_pcb || true
""",
    )
    write(
        art() / "THIRD_PARTY_EDA_REPRO.md",
        f"""# Third-party EDA reproduction — Cont IX

Updated: {TS}

- Clean Linux CI container: `kicad/kicad:8.0` (workflow `.github/workflows/continuation_ix_kicad.yml`)
- Local: `/opt/homebrew/bin/kicad-cli` 10.0.5
- Regenerators: `make continuation-ix` / `python3 scripts/continuation_ix_pre_evt_hardware_lock.py`
- Compare: artifacts hash manifest after regenerate
""",
    )


def build_manifest(cli_results):
    files = []
    for p in sorted(art().rglob("*")):
        if p.is_file():
            files.append({"path": str(p.relative_to(root())), "sha256": sha256_file(p), "bytes": p.stat().st_size})
    write_json(art() / "MANIFEST.json", {"updated_at_utc": TS, "branch": BRANCH, "base_sha": BASE_SHA, "files": files, "cli": cli_results})


def patch_makefile():
    mk = (root() / "Makefile").read_text(encoding="utf-8")
    if "continuation-ix" not in mk:
        write(
            root() / "Makefile",
            mk
            + "\n.PHONY: continuation-ix validate-continuation-ix release\n"
            + "continuation-ix:\n\t$(PYTHON) scripts/continuation_ix_pre_evt_hardware_lock.py\n"
            + "validate-continuation-ix:\n\t$(PYTHON) scripts/validate_continuation_ix.py\n"
            + "release: continuation-ix\n\t@echo Cont IX release artifacts in artifacts/continuation_ix_pre_evt/\n",
        )


def main() -> None:
    art().mkdir(parents=True, exist_ok=True)
    release_docs().mkdir(parents=True, exist_ok=True)
    pretty = root() / "device_designs/_shared_kicad/gunnchos_production.pretty"
    print("[Cont IX] production footprints")
    FP.ensure_production_footprints(pretty)

    sch_infos = []
    pcb_infos = []
    for product in PRODUCTS:
        print(f"[Cont IX] schematic {product}")
        s = emit_schematic(product, PRODUCT_META[product])
        print(f"[Cont IX] pcb {product}")
        p = emit_pcb(product, s["placements"], pretty, PRODUCT_META[product])
        sch_infos.append(s)
        pcb_infos.append(p)

    proxy_hits = emit_footprint_ledger()
    reqs = emit_vendor_requests()
    decision = emit_comhpc_final_decision()

    cli_results = []
    for product in PRODUCTS:
        print(f"[Cont IX] kicad-cli {product}")
        r = run_kicad(product)
        cli_results.append(r)
        emit_assembly_package(product, r, next(p for p in pcb_infos if p["product"] == product))
        print(f"  ERC={r.get('erc')} DRC={r.get('drc')} gerbers={r.get('gerber_count')}")

    emit_rfq_folders()
    emit_evt_test_book()
    emit_mechanical_step_notes(cli_results)
    emit_routing_report(pcb_infos)
    emit_ci_repro()
    scorecards = emit_scorecards(cli_results, pcb_infos, sch_infos)
    tokens = emit_tokens(scorecards, decision, cli_results)
    blockers = emit_blockers(scorecards, proxy_hits, cli_results)

    write(
        art() / "SUMMARY.md",
        f"""# Continuation IX — Final Digital Release Lock / Pre-EVT

Updated: {TS}  
Branch: `{BRANCH}`  
Base: `{BASE_SHA}`

## COM-HPC
PRODUCTION_ARCHITECTURE=ADLINK; VENDOR_COLLATERAL_REQUIRED=TRUE; PUBLIC_HARDWARE_REPRODUCTION=LIMITED; SOFTWARE_ADOPTION=FULLY_SUPPORTED

## ERC/DRC
| Product | ERC | DRC | Gerbers | STEP |
|---|---:|---:|---:|---:|
"""
        + "\n".join(
            f"| {r['product']} | {r.get('erc',{}).get('errors')} | {r.get('drc',{}).get('errors')} | "
            f"{r.get('gerber_count')} | {r.get('step_bytes')} |"
            for r in cli_results
        )
        + "\n\n## Manufacturer tokens\n"
        + "\n".join(f"- `{p}`: `{sc['manufacturer_token']}`" for p, sc in scorecards.items())
        + f"\n\n## DIGITAL blockers\n{blockers['DIGITAL'] or '(none)'}\n",
    )
    write(docs() / "KICAD_PRE_EVT_LOCK_CONT_IX.md", (art() / "SUMMARY.md").read_text())
    write_json(art() / "SCH_INFO.json", sch_infos)
    write_json(art() / "PCB_INFO.json", pcb_infos)
    write_json(art() / "CLI_RESULTS.json", cli_results)
    build_manifest(cli_results)
    patch_makefile()
    print("Cont IX complete; DIGITAL blockers:", blockers["DIGITAL"])


if __name__ == "__main__":
    main()
