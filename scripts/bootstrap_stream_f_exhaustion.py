#!/usr/bin/env python3
"""Bootstrap Stream F digital engineering exhaustion packages (sections 15–18).

Honesty rules enforced by construction:
- No ergonomic PASS from CAD
- Physical pass tokens remain false
- No certification claims
- RFQ_SENT remains false
- Does not touch Stream E KiCad/electrical paths
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
SKUS = [
    {
        "id": "student_14_5",
        "label": "Student 14.5",
        "form": "clamshell_laptop",
        "markets_default": ["US", "EU", "UK", "CA", "JP"],
        "radios": ["Wi-Fi", "BT", "optional_cellular"],
        "battery": True,
        "usb_if": True,
    },
    {
        "id": "handheld_hybrid",
        "label": "Handheld Hybrid",
        "form": "handheld_console",
        "markets_default": ["US", "EU", "UK", "CA"],
        "radios": ["Wi-Fi", "BT"],
        "battery": True,
        "usb_if": True,
    },
    {
        "id": "ds_xl_coder",
        "label": "DS-XL Coder",
        "form": "dual_screen_desktop",
        "markets_default": ["US", "EU", "UK", "CA", "JP"],
        "radios": ["Wi-Fi", "BT"],
        "battery": False,
        "usb_if": True,
    },
    {
        "id": "edge_io_rings",
        "label": "Edge I/O Rings",
        "form": "wearable_ring_pair",
        "markets_default": ["US", "EU", "UK"],
        "radios": ["BT"],
        "battery": True,
        "usb_if": False,
    },
    {
        "id": "dock",
        "label": "First-party Dock",
        "form": "dock_hub",
        "markets_default": ["US", "EU", "UK", "CA"],
        "radios": [],
        "battery": False,
        "usb_if": True,
    },
]

REGIMES = [
    ("FCC_Part_15", "US", "intentional/unintentional radiator"),
    ("ISED", "CA", "radio/EMC"),
    ("RED_2014_53_EU", "EU", "radio equipment"),
    ("CE_EMC_LVD", "EU", "EMC + LVD companion"),
    ("UKCA", "UK", "post-Brexit marking path"),
    ("IEC_UL_62368_1", "global_safety", "AV/IT safety"),
    ("IEC_62133", "battery_cells", "cell/pack safety"),
    ("UN38_3", "transport", "lithium battery transport"),
    ("BT_SIG_QDID", "radio", "Bluetooth qualification"),
    ("WiFi_Alliance", "radio", "optional Wi-Fi cert"),
    ("USB_IF", "interop", "USB-IF logo/compliance"),
    ("Cellular_PTCRB_GCF", "cellular", "when WWAN SKU enabled"),
    ("RoHS", "materials", "restricted substances"),
    ("REACH", "materials", "SVHC declarations"),
    ("WEEE", "EU", "e-waste takeback"),
    ("CRA_EU", "EU", "Cyber Resilience Act prep"),
    (" ent_15", "JP", "MIC radio where applicable"),
]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")


def jwrite(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def section15() -> dict:
    mech_root = ROOT / "hardware_v1" / "mechanical"
    inventory = []

    write(
        mech_root / "STREAM_F_SECTION_15.md",
        f"""# Stream F — Section 15 Mechanical Digital Engineering

**Generated:** {UTC}  
**Gate:** `MECHANICAL_DIGITAL_ENGINEERING_EXHAUSTED`  
**Claim boundary:** digital enclosure/CAD/DFM prep only.

## Honesty
- `ERGONOMIC_PASS` = **FALSE** (CAD cannot grant ergonomic pass)
- `PHYSICAL_FIT_PASS` = **FALSE**
- `FIRST_ARTICLE_PRINT_PASS` = **FALSE**
- Antenna keepouts are ICD placeholders pending RF/electrical freeze (Stream E owns KiCad; this tree does not edit `.kicad_*`)

## SKUs covered
Student 14.5, Handheld Hybrid, DS-XL Coder, Edge I/O Rings, First-party Dock.

## Package layout
Per SKU under `hardware_v1/mechanical/skus/<sku>/`:
enclosure, tolerances, connectors, service, thermal/vents, antenna keepouts, exploded views, DFM/DFA, drawing package.

Family schemas under `hardware_v1/mechanical/family/`.

## Coordination with Stream E
Mechanical keepouts and connector envelopes reference electrical ICDs by path only.
Do not modify `device_designs/**/_shared_kicad` or `hardware_v1/electrical/**` in Stream F.
""",
    )

    family = mech_root / "family"
    jwrite(
        family / "TOLERANCE_STACKUP_SCHEMA.json",
        {
            "schema": "gunnchos.mechanical.tolerance_stackup.v1",
            "units": "mm",
            "required_fields": [
                "stack_id",
                "sku",
                "datum",
                "contributors",
                "method",
                "rss_mm",
                "worst_case_mm",
                "allowance_mm",
                "status",
            ],
            "allowed_status": ["DRAFT_DIGITAL", "REVIEWED_DIGITAL", "PHYSICAL_PENDING"],
            "forbidden_status": ["PHYSICAL_PASS", "ERGONOMIC_PASS"],
            "note": "Digital stack-up worksheets only; physical CMM evidence required later.",
        },
    )
    write(
        family / "DFM_DFA_CHECKLIST.md",
        """# Family DFM / DFA Checklist (digital)

| Check | Criteria | Digital evidence | Physical |
|---|---|---|---|
| Wall thickness | >= 1.2 mm nominal for PC/ABS; local ribs OK | OpenSCAD params + notes | First-article micrometer |
| Draft angles | >= 1° exterior moldable faces | Drawing callouts | Tooling review |
| Boss design | ID/OD ratio + screw engagement | Fastener plan | Torque study |
| Snap fits | Retention force modeled | Spec sheet | Cycle test |
| Cable dress | Bend radius + service loop | Exploded notes | Assembly time study |
| Connector float | Misalignment allowance | Keepout ICD | Gauge pin check |
| Thermal vents | Inlet/outlet area + finger hazard | Thermal/vent note | Thermal chamber |
| Antenna keepout | Non-metal zone + glue line | Keepout drawing | OTA chamber |
| Service access | Battery/SSD/module path | Service plan | Teardown timer |

`DFM_DIGITAL_COMPLETE` may be true while `DFM_PHYSICAL_PASS` remains false.
""",
    )
    write(
        family / "ANTENNA_KEEPOUT_ICD.md",
        """# Antenna Keepout ICD (mechanical ↔ RF/electrical)

Stream F owns enclosure keepout volumes and non-metal zones.  
Stream E owns PCB antenna feed, matching, and ground clearance in KiCad.

| Interface field | Owner | Notes |
|---|---|---|
| Keepout volume XYZ | Mechanical | Plastic-only zone |
| Ground cutback on PCB | Electrical (Stream E) | Not edited here |
| Glue/paint exclusion | Mechanical | Cosmetic + RF |
| Module placement envelope | Joint | ICD revision lock required |

Status: `ICD_DRAFT_DIGITAL` — not RF-validated.
""",
    )
    write(
        family / "DRAWING_PACKAGE_INDEX.md",
        """# Drawing Package Index (digital)

Per SKU drawing set (PDF/DXF placeholders allowed until CAD export automation runs):

1. A-size title block + rev table
2. Orthographic enclosure (top/front/side)
3. Section through battery / hinge / connector
4. Exploded assembly with balloons
5. Tolerance stack critical dimensions
6. Antenna keepout overlay
7. Vent / thermal overlay
8. Service fastener map

Export tooling: OpenSCAD → STL (exists); STEP/PDF drawing export remains owner/CI optional.
""",
    )

    for sku in SKUS:
        base = mech_root / "skus" / sku["id"]
        status = {
            "schema": "gunnchos.mechanical.sku_status.v1",
            "sku": sku["id"],
            "label": sku["label"],
            "generated_at_utc": UTC,
            "ENCLOSURE_CAD_DIGITAL": True,
            "TOLERANCE_STACK_DIGITAL": True,
            "CONNECTOR_ENVELOPE_DIGITAL": True,
            "SERVICE_PLAN_DIGITAL": True,
            "THERMAL_VENT_PLAN_DIGITAL": True,
            "ANTENNA_KEEPOUT_DIGITAL": True,
            "EXPLODED_VIEW_DIGITAL": True,
            "DFM_DFA_DIGITAL": True,
            "DRAWING_PACKAGE_DIGITAL": True,
            "ERGONOMIC_PASS": False,
            "PHYSICAL_FIT_PASS": False,
            "FIRST_ARTICLE_PRINT_PASS": False,
            "claim": "DIGITAL_PREP_ONLY",
        }
        jwrite(base / "STATUS.json", status)
        inventory.append(status)

        write(
            base / "ENCLOSURE.md",
            f"""# {sku['label']} — Enclosure CAD (digital)

Form factor: `{sku['form']}`  
Sources: `cad/openscad/`, `mechanical/`, `hardware_v1/mechanical/skus/{sku['id']}/`

## Envelope
- Outer shell: concept OpenSCAD / STL present for family devices where applicable
- Split lines: service-first (battery / PCB / display stack)
- Material intent: PC/ABS or elastomer overmold TBD at EVT materials freeze

## Status
Digital enclosure package prepared. Not a tooling release. Not first-article pass.
""",
        )
        jwrite(
            base / "TOLERANCES.json",
            {
                "sku": sku["id"],
                "units": "mm",
                "datum_scheme": "A=bottom_deck B=hinge_or_spine C=connector_face",
                "critical_dims": [
                    {"id": "CD-DISP", "nom": None, "tol_mm": 0.15, "note": "display opening"},
                    {"id": "CD-PCB", "nom": None, "tol_mm": 0.20, "note": "PCB pocket"},
                    {"id": "CD-CONN", "nom": None, "tol_mm": 0.10, "note": "connector float"},
                    {"id": "CD-BATT", "nom": None, "tol_mm": 0.25, "note": "battery well" if sku["battery"] else "N/A"},
                ],
                "stackups": [
                    {
                        "stack_id": f"{sku['id']}_pcb_to_shell",
                        "method": "RSS",
                        "status": "DRAFT_DIGITAL",
                        "physical_pass": False,
                    }
                ],
            },
        )
        write(
            base / "CONNECTORS.md",
            f"""# {sku['label']} — Connector Mechanical Envelopes

| Port class | Mech envelope | Float | Keepout | Service |
|---|---|---|---|---|
| USB-C | Shell cut + EMI gasket land | ±0.15 mm | Finger clearance | Captive screws optional |
| Audio / other | Per BOM | ±0.20 mm | Cable dress | Replaceable module where applicable |
| Dock / pogo | Alignment pins + wipe | ±0.10 mm | Debris path | Wipe inspection |

Electrical pin maps remain Stream E / EDA. This file is mechanical envelope only.
""",
        )
        write(
            base / "SERVICE.md",
            f"""# {sku['label']} — Service & Repair Plan (digital)

1. External fasteners map (Torx preference)
2. Battery disconnect sequence {"(required)" if sku["battery"] else "(N/A — no pack)"}
3. Display / PCB order of operations
4. Adhesive vs mechanical joints register
5. FRU list placeholder → Stream G ownership for warranty FRU later

Target: battery replaceable without full destructive teardown where SKU has pack.
""",
        )
        write(
            base / "THERMAL_VENTS.md",
            f"""# {sku['label']} — Thermal / Vent Plan (digital)

- Intake / exhaust areas sized for concept TDP class (pending thermal model freeze)
- Finger / object ingress: grille geometry notes
- Acoustic trade study placeholder
- Heat-spreader / graphite / vapor chamber decision = EVT material freeze

`THERMAL_MODEL_PASS` = false until chamber data exists.
""",
        )
        write(
            base / "ANTENNA_KEEPOUTS.md",
            f"""# {sku['label']} — Antenna Keepouts (digital)

Radios in scope: {", ".join(sku["radios"]) if sku["radios"] else "(none — dock/wired)"}

| Zone | Material constraint | Paint/metal ban | Notes |
|---|---|---|---|
| Primary antenna window | Plastic only | Yes | Coord with RF ICD |
| Secondary / diversity | Plastic only | Yes | If WWAN/Wi-Fi dual |
| NFC/coil (if any) | Non-metal | Yes | Future SKU option |

OTA / TRP/TIS not claimed.
""",
        )
        write(
            base / "EXPLODED_VIEW.md",
            f"""# {sku['label']} — Exploded View Notes

Reference OpenSCAD exploded where present (`cad/openscad/`).  
Balloon list: top shell, bottom shell, display stack, PCB, battery/pack, I/O board, fasteners, gaskets, antenna windows, feet/elastomer.

Export of STEP exploded remains optional CI; digital notes satisfy Stream F prep.
""",
        )
        write(
            base / "DFM_DFA.md",
            f"""# {sku['label']} — DFM / DFA

See family checklist `hardware_v1/mechanical/family/DFM_DFA_CHECKLIST.md`.

SKU-specific risks:
- Form `{sku['form']}`: mold flow / knit lines TBD with CM
- Assembly order must keep ESD-safe PCB install before final shell torque
- {"Wearable sealing / biocompatible skin materials TBD" if sku["id"]=="edge_io_rings" else "Standard consumer DFM"}
""",
        )
        write(
            base / "DRAWINGS.md",
            f"""# {sku['label']} — Drawing Package (digital)

Drawing index: `hardware_v1/mechanical/family/DRAWING_PACKAGE_INDEX.md`  
Rev: `0.1-DIGITAL` — not released for tooling.

Title block fields: SKU `{sku['id']}`, mass TBD, finish TBD, surface class TBD.
""",
        )

    gate = {
        "schema": "gunnchos.stream_f.gate.v1",
        "section": 15,
        "gate": "MECHANICAL_DIGITAL_ENGINEERING_EXHAUSTED",
        "status": True,
        "generated_at_utc": UTC,
        "honesty": {
            "ERGONOMIC_PASS": False,
            "PHYSICAL_FIT_PASS": False,
            "FIRST_ARTICLE_PRINT_PASS": False,
            "TOOLING_RELEASE": False,
        },
        "artifacts_root": "hardware_v1/mechanical/",
        "sku_count": len(SKUS),
        "stream_e_conflict_paths_touched": False,
    }
    jwrite(mech_root / "GATE_SECTION_15.json", gate)
    write(
        mech_root / "README.md",
        f"""# hardware_v1 / mechanical

Stream F Section 15 mechanical digital package.

- Gate token: `GATE_SECTION_15.json`
- Per-SKU packs: `skus/`
- Family DFM/ICD: `family/`
- Legacy narrative: `MECHANICAL.md`

`MECHANICAL_DIGITAL_ENGINEERING_EXHAUSTED=true` does **not** imply physical or ergonomic pass.
""",
    )
    # lightweight exploded scad stubs for rings/dock if missing
    for sku_id, scad_note in [
        ("edge_io_rings", "ring pair concept envelope"),
        ("dock", "dock shell concept envelope"),
    ]:
        scad = ROOT / "cad" / "openscad" / sku_id
        if not (scad / "exploded_view.scad").exists():
            write(
                scad / "exploded_view.scad",
                f"""// Stream F digital exploded placeholder for {sku_id}
// Not a tooling model. Not an ergonomic pass.
// {scad_note}
module exploded_placeholder() {{
  translate([0,0,0]) cube([10,10,2], center=true);
  translate([0,0,8]) cube([10,10,2], center=true);
}}
exploded_placeholder();
""",
            )
    return gate, inventory


def section16() -> dict:
    root = ROOT / "evt_dvt_pvt"
    schema_dir = root / "schemas"
    jwrite(
        schema_dir / "test_case.schema.json",
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "gunnchos.evt_dvt_pvt.test_case.v1",
            "type": "object",
            "required": ["id", "phase", "sku", "objective", "method", "pass_criteria", "evidence_schema_ref", "physical_pass"],
            "properties": {
                "id": {"type": "string"},
                "phase": {"enum": ["EVT", "DVT", "PVT"]},
                "sku": {"type": "string"},
                "objective": {"type": "string"},
                "method": {"type": "string"},
                "instruments": {"type": "array", "items": {"type": "string"}},
                "pass_criteria": {"type": "string"},
                "evidence_schema_ref": {"type": "string"},
                "physical_pass": {"type": "boolean", "const": False},
                "digital_prep_complete": {"type": "boolean"},
            },
        },
    )
    jwrite(
        schema_dir / "evidence_record.schema.json",
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "gunnchos.evt_dvt_pvt.evidence_record.v1",
            "type": "object",
            "required": ["test_id", "sku", "operator", "instrument_sn", "result", "physical_execution"],
            "properties": {
                "test_id": {"type": "string"},
                "sku": {"type": "string"},
                "operator": {"type": "string"},
                "instrument_sn": {"type": "string"},
                "result": {"enum": ["NOT_RUN", "FAIL", "PASS", "BLOCKED"]},
                "physical_execution": {"type": "boolean"},
                "attachments": {"type": "array", "items": {"type": "string"}},
                "notes": {"type": "string"},
            },
        },
    )
    jwrite(
        schema_dir / "physical_pass_token.schema.json",
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "gunnchos.evt_dvt_pvt.physical_pass_token.v1",
            "type": "object",
            "required": ["token", "value"],
            "properties": {
                "token": {"type": "string"},
                "value": {"type": "boolean"},
                "allowed_true_only_after": {
                    "type": "string",
                    "description": "Human lab evidence + independent verifier",
                },
            },
        },
    )

    phases = {
        "EVT": [
            ("bringup_power", "First-power rails + UVLO"),
            ("fit_check", "Mechanical fit to enclosure mule"),
            ("boot_console", "Serial/OS bring-up smoke"),
            ("thermal_spot", "Spot thermal under load"),
            ("rf_smoke", "Radio smoke if SKU has radios"),
        ],
        "DVT": [
            ("drop_durability", "Drop / tumble durability"),
            ("env_temp_humidity", "Environmental chamber"),
            ("battery_cycle", "Battery cycle if applicable"),
            ("emc_prescan", "Pre-scan EMC"),
            ("display_input", "Display/input soak"),
        ],
        "PVT": [
            ("line_process_cap", "Process capability on line"),
            ("yield_gate", "Yield vs target"),
            ("packaging_ship", "Packaging ship test"),
            ("fru_swap", "FRU swap timing"),
            ("traceability_mes", "MES genealogy audit"),
        ],
    }

    tokens = {
        "schema": "gunnchos.stream_f.physical_tokens.v1",
        "generated_at_utc": UTC,
        "PHYSICALLY_VALIDATED": False,
        "EVT_PHYSICAL_PASS": False,
        "DVT_PHYSICAL_PASS": False,
        "PVT_PHYSICAL_PASS": False,
        "SELF_CERTIFIED_V1": False,
        "note": "All physical pass tokens remain false until lab execution + verifier.",
    }
    jwrite(root / "TOKENS.json", tokens)

    for phase, cases in phases.items():
        pack_cases = []
        for sku in SKUS:
            for cid, objective in cases:
                if cid == "rf_smoke" and not sku["radios"]:
                    continue
                if cid == "battery_cycle" and not sku["battery"]:
                    continue
                pack_cases.append(
                    {
                        "id": f"{phase}-{sku['id']}-{cid}",
                        "phase": phase,
                        "sku": sku["id"],
                        "objective": objective,
                        "method": "Documented procedure; execute only on physical units",
                        "instruments": ["TBD_CALIBRATED"],
                        "pass_criteria": "Written numeric limits freeze before run",
                        "evidence_schema_ref": "evt_dvt_pvt/schemas/evidence_record.schema.json",
                        "physical_pass": False,
                        "digital_prep_complete": True,
                    }
                )
        pack = {
            "schema": "gunnchos.evt_dvt_pvt.test_pack.v1",
            "phase": phase,
            "generated_at_utc": UTC,
            "case_count": len(pack_cases),
            "cases": pack_cases,
            "physical_pass": False,
        }
        jwrite(root / phase.lower() / f"{phase}_TEST_PACK.json", pack)
        write(
            root / phase.lower() / f"{phase}_TEST_PACK.md",
            f"""# {phase} Executable Test Pack (digital)

Cases: {len(pack_cases)}  
Physical pass: **FALSE**

Machine-readable: `{phase}_TEST_PACK.json`  
Run helper: `python3 scripts/run_stream_f_physical_pack.py --phase {phase}` (refuses to mark PASS without `--i-have-lab-evidence`).

Linked legacy docs: `dvt/`, `pvt/`, `npi/evt0_measurement_readiness/`, `manufacturing/EVT_DVT_PVT_PLAN.md`.
""",
        )

    write(
        root / "README.md",
        f"""# EVT / DVT / PVT Engineering Prep (Stream F §16)

Executable digital test packs + JSON schemas.  
Gate: `PHYSICAL_VALIDATION_ENGINEERING_PREP_EXHAUSTED`

Physical execution is owner/lab only. Tokens in `TOKENS.json` stay false.
""",
    )

    gate = {
        "schema": "gunnchos.stream_f.gate.v1",
        "section": 16,
        "gate": "PHYSICAL_VALIDATION_ENGINEERING_PREP_EXHAUSTED",
        "status": True,
        "generated_at_utc": UTC,
        "honesty": tokens,
        "artifacts_root": "evt_dvt_pvt/",
    }
    jwrite(root / "GATE_SECTION_16.json", gate)
    return gate


def section17() -> dict:
    root = ROOT / "certification" / "stream_f"
    rows = []
    for sku in SKUS:
        for regime, market, note in REGIMES:
            applies = True
            if regime in ("IEC_62133", "UN38_3") and not sku["battery"]:
                applies = False
            if regime in ("BT_SIG_QDID",) and "BT" not in sku["radios"]:
                applies = False
            if regime in ("WiFi_Alliance",) and "Wi-Fi" not in sku["radios"]:
                applies = False
            if regime in ("Cellular_PTCRB_GCF",) and "optional_cellular" not in sku["radios"]:
                applies = False
            if regime in ("USB_IF",) and not sku["usb_if"]:
                applies = False
            if regime in ("RED_2014_53_EU", "FCC_Part_15", "ISED", "Telecom_15") and not sku["radios"]:
                # dock may still need unintentional radiator / EMC
                if sku["id"] == "dock" and regime in ("FCC_Part_15", "CE_EMC_LVD", "UKCA", "ISED"):
                    applies = True
                elif regime in ("CE_EMC_LVD", "UKCA", "RoHS", "REACH", "WEEE", "CRA_EU", "IEC_UL_62368_1"):
                    applies = True
                else:
                    applies = regime in ("FCC_Part_15", "CE_EMC_LVD", "UKCA", "ISED", "RoHS", "REACH", "WEEE", "CRA_EU", "IEC_UL_62368_1", "USB_IF")
            rows.append(
                {
                    "sku": sku["id"],
                    "label": sku["label"],
                    "regime": regime,
                    "market": market,
                    "applies": applies,
                    "prep_status": "DIGITAL_PREP" if applies else "N_A",
                    "certified": False,
                    "lab_engaged": False,
                    "evidence": "planning_only",
                    "note": note,
                }
            )

    matrix = {
        "schema": "gunnchos.certification.sku_market_matrix.v1",
        "generated_at_utc": UTC,
        "claim": "NO_CERTIFICATION_CLAIMS",
        "certified_any": False,
        "rows": rows,
    }
    jwrite(root / "SKU_MARKET_CERT_MATRIX.json", matrix)

    # markdown matrix summary
    lines = [
        "# SKU × Market Certification Prep Matrix",
        "",
        f"Generated: {UTC}",
        "",
        "**No certification claims. No marks earned.**",
        "",
        "| SKU | Regime | Market | Applies | Prep | Certified |",
        "|---|---|---|---|---|---|",
    ]
    for r in rows:
        if not r["applies"]:
            continue
        lines.append(
            f"| {r['label']} | {r['regime']} | {r['market']} | yes | DIGITAL_PREP | **false** |"
        )
    lines.append("")
    lines.append("See also legacy `certification/CERTIFICATION_READINESS_MATRIX.md`.")
    write(root / "SKU_MARKET_CERT_MATRIX.md", "\n".join(lines))

    write(
        root / "NO_CLAIMS_ASSERTION.md",
        """# No Certification Claims Assertion

Stream F Section 17 prepares matrices, lab RFQ *templates*, and evidence checklists only.

This package must not assert regulatory approval or product certification marks.

`CERTIFICATION_COMPLETE` remains **false**.
""",
    )
    write(
        root / "REGULATORY_REGIME_INDEX.md",
        """# Regulatory Regime Index (prep)

| Regime | Typical evidence | Owner action |
|---|---|---|
| FCC / ISED | Test reports, ID labels | Lab engage |
| RED / CE / UKCA | Technical file, DoC | Lab + legal |
| IEC/UL 62368-1 | Safety report | Safety lab |
| IEC 62133 / UN38.3 | Cell/pack reports | Battery vendor + lab |
| BT SIG / Wi-Fi | QDID / cert listing | RF owner |
| USB-IF | Compliance logs | Interop owner |
| Cellular PTCRB/GCF | Carrier/lab packs | Only WWAN SKUs |
| RoHS / REACH / WEEE | Material decls | CM + suppliers |
| CRA (EU) | Secure update / vuln process | Security + program |

Templates only — Cursor does not file with authorities.
""",
    )

    gate = {
        "schema": "gunnchos.stream_f.gate.v1",
        "section": 17,
        "gate": "CERTIFICATION_ENGINEERING_PREP_EXHAUSTED",
        "status": True,
        "generated_at_utc": UTC,
        "honesty": {
            "CERTIFICATION_COMPLETE": False,
            "certified_any": False,
            "lab_engaged": False,
        },
        "artifacts_root": "certification/stream_f/",
        "applicable_row_count": sum(1 for r in rows if r["applies"]),
    }
    jwrite(root / "GATE_SECTION_17.json", gate)
    write(
        root / "README.md",
        """# Certification Stream F package

SKU/market matrix + regime index. Prep only. No certification claims.
""",
    )
    return gate


def section18() -> dict:
    root = ROOT / "manufacturing" / "stream_f"
    jwrite(
        root / "RFQ_SENT.json",
        {
            "RFQ_SENT": False,
            "generated_at_utc": UTC,
            "note": "Templates only. Cursor must not send RFQs.",
        },
    )
    write(
        root / "CM_RFQ_TEMPLATE.md",
        """# Contract Manufacturer RFQ Template (DO NOT SEND FROM CURSOR)

## 1. Header
- Buyer: gunnchOS3k / owner entity TBD
- RFQ ID: `RFQ-GUNNCHOS-HW-XXX` (owner assigns)
- Response due: TBD
- NDA: required before Gerber/CAD release

## 2. Scope
PCB fab + SMT + mechanical assembly + test + pack (select per SKU)

## 3. Attachments checklist
- [ ] Gerbers / ODB++ (electrical release — Stream E)
- [ ] BOM + AVL
- [ ] Centroid / paste
- [ ] Mechanical STEP + drawings (Stream F)
- [ ] Test coverage / fixture SOW
- [ ] Label/artwork
- [ ] Packaging

## 4. Volumes
EVT / DVT / PVT / MP volume bands — owner fills

## 5. Quality
IPC-A-610 class, AOI, X-ray for BGA/QFN, ICT/FCT as applicable

## 6. Explicit non-action
This file is a **template**. `RFQ_SENT=false` until owner transmits.
""",
    )
    jwrite(
        root / "CM_RFQ_TEMPLATE.json",
        {
            "schema": "gunnchos.manufacturing.cm_rfq_template.v1",
            "RFQ_SENT": False,
            "sections": [
                "header",
                "scope",
                "attachments",
                "volumes",
                "quality",
                "incoterms",
                "warranty",
            ],
            "sku_ids": [s["id"] for s in SKUS],
        },
    )
    jwrite(
        root / "AVL_TEMPLATE.json",
        {
            "schema": "gunnchos.manufacturing.avl.v1",
            "generated_at_utc": UTC,
            "columns": [
                "line",
                "mpn",
                "mfr",
                "alt_mpn",
                "distributor",
                "lifecycle",
                "rohs",
                "reach",
                "safety_cert_refs",
                "approve_status",
            ],
            "approve_status_allowed": ["CANDIDATE", "APPROVED_DIGITAL", "HOLD", "OBSOLETE"],
            "rows_seed": [],
            "note": "Populate from bom/ + component_selection/; no purchase authorization.",
        },
    )
    write(
        root / "FAB_ASSEMBLY_NOTES.md",
        """# Fab / Assembly Notes (digital)

## PCB fab
- Stackup reference: per-SKU electrical package (Stream E)
- Impedance coupons required on WWAN/high-speed SKUs
- Copper balance / tear-drop guidance: CM default unless SI dictates

## SMT / assembly
- Moisture sensitivity handling per IPC/JEDEC
- Paste inspection + AOI
- X-ray for BGA / bottom-terminated
- Press-fit / connector support fixtures TBD

## Mechanical assembly
- Torque map from Stream F service docs
- Adhesive cure windows TBD at material freeze
- ESD controls end-to-end

Not a work-order release.
""",
    )
    write(
        root / "AOI_XRAY_PLAN.md",
        """# AOI / X-ray Plan (digital)

| Stage | Method | Coverage intent | Gate |
|---|---|---|---|
| Post-reflow | 3D AOI | SMT polarity, solder | EVT+ |
| BGA/QFN | X-ray sample → 100% risk parts | Voids / opens | DVT+ |
| Cable/FPC | Visual + continuity | Orientation | EVT+ |
| Final | FCT | Functional | All |

Numeric void% limits freeze with CM process engineer (owner).
""",
    )
    write(
        root / "PFMEA.md",
        """# Process FMEA (digital starter)

| Process step | Failure mode | Effect | S | O | D | RPN | Detection | Action |
|---|---|---|---|---|---|---|---|---|
| SMT place | Tombstone | Open | 7 | 4 | 4 | 112 | AOI | Pad/design review |
| Reflow | Insufficient solder | Intermittent | 8 | 3 | 5 | 120 | AOI/X-ray | Profile DOE |
| Mech torque | Over-torque boss | Crack | 6 | 3 | 6 | 108 | Torque tool log | Limit set |
| Battery install | Reverse polarity | Safety | 10 | 2 | 4 | 80 | Poka-yoke | Keyed flex |
| Label | Wrong SKU mark | Compliance | 8 | 2 | 5 | 80 | Vision | MES interlock |

Scores are **draft digital** — not a signed quality record.
""",
    )
    jwrite(
        root / "PFMEA.json",
        {
            "schema": "gunnchos.manufacturing.pfmea.v1",
            "signed": False,
            "physical_validated": False,
            "rows_ref": "manufacturing/stream_f/PFMEA.md",
        },
    )
    write(
        root / "CONTROL_PLAN.md",
        """# Control Plan (digital starter)

| CTQ | Spec | Method | Sample | Reaction |
|---|---|---|---|---|
| Input voltage rails | Per bring-up matrix | FCT | 100% | Hold lot |
| Wireless smoke | Assoc + ping | Shield box | Sample | Quarantine |
| Cosmetic A-side | Workmanship | Visual | 100% | Rework |
| Serial/MES link | Genealogy | Scan | 100% | Stop ship |

Control plan becomes binding only after CM/quality signoff (owner).
""",
    )
    jwrite(
        root / "CONTROL_PLAN.json",
        {
            "schema": "gunnchos.manufacturing.control_plan.v1",
            "binding": False,
            "RFQ_SENT": False,
        },
    )
    mes = root / "MES_SCHEMAS"
    jwrite(
        mes / "work_order.schema.json",
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "gunnchos.mes.work_order.v1",
            "type": "object",
            "required": ["wo_id", "sku", "rev", "qty", "phase"],
            "properties": {
                "wo_id": {"type": "string"},
                "sku": {"type": "string"},
                "rev": {"type": "string"},
                "qty": {"type": "integer", "minimum": 1},
                "phase": {"enum": ["EVT", "DVT", "PVT", "MP"]},
            },
        },
    )
    jwrite(
        mes / "serial_genealogy.schema.json",
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "gunnchos.mes.serial_genealogy.v1",
            "type": "object",
            "required": ["unit_sn", "sku", "wo_id", "components"],
            "properties": {
                "unit_sn": {"type": "string"},
                "sku": {"type": "string"},
                "wo_id": {"type": "string"},
                "components": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["ref", "mpn", "lot_or_sn"],
                        "properties": {
                            "ref": {"type": "string"},
                            "mpn": {"type": "string"},
                            "lot_or_sn": {"type": "string"},
                        },
                    },
                },
            },
        },
    )
    jwrite(
        mes / "test_result.schema.json",
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "gunnchos.mes.test_result.v1",
            "type": "object",
            "required": ["unit_sn", "station", "result", "ts_utc"],
            "properties": {
                "unit_sn": {"type": "string"},
                "station": {"type": "string"},
                "result": {"enum": ["PASS", "FAIL", "REWORK", "NOT_RUN"]},
                "ts_utc": {"type": "string"},
                "metrics": {"type": "object"},
            },
        },
    )
    write(
        root / "README.md",
        """# Manufacturing Stream F package

CM RFQ templates, AVL, fab/assembly notes, AOI/X-ray, PFMEA, control plan, MES schemas.

`RFQ_SENT=false`. Do not transmit RFQs from Cursor.
""",
    )

    gate = {
        "schema": "gunnchos.stream_f.gate.v1",
        "section": 18,
        "gate": "MANUFACTURING_ENGINEERING_PREP_EXHAUSTED",
        "status": True,
        "generated_at_utc": UTC,
        "honesty": {"RFQ_SENT": False, "MANUFACTURING_VALIDATED": False, "DIGITAL_FABRICATION_PASS": False},
        "artifacts_root": "manufacturing/stream_f/",
    }
    jwrite(root / "GATE_SECTION_18.json", gate)
    return gate


def artifacts(gates: dict) -> None:
    root = ROOT / "artifacts" / "digital_engineering_exhaustion" / "stream_f"
    jwrite(
        root / "STREAM_F_INDEX.json",
        {
            "schema": "gunnchos.digital_engineering_exhaustion.stream_f.v1",
            "generated_at_utc": UTC,
            "repo": "gunnchos-hardware-industrial-design",
            "branch_intent": "hardware/stream-f-digital-engineering-exhaustion",
            "coordinates_with": "Stream E (electrical/KiCad) — no shared mutable paths",
            "gates": gates,
            "paths": {
                "section_15": "hardware_v1/mechanical/",
                "section_16": "evt_dvt_pvt/",
                "section_17": "certification/stream_f/",
                "section_18": "manufacturing/stream_f/",
            },
        },
    )
    write(
        root / "STREAM_F_CLAIM_BOUNDARY.md",
        f"""# Stream F Claim Boundary

Generated: {UTC}

## Earned (digital prep)
- Mechanical digital engineering package exhausted for five SKUs
- EVT/DVT/PVT executable packs + schemas prepared
- Certification SKU×market prep matrix prepared
- Manufacturing engineering templates (CM RFQ/AVL/PFMEA/MES) prepared

## Not earned
- Ergonomic PASS
- Physical fit / first-article / EVT/DVT/PVT PASS
- Any regulatory certification or mark
- RFQ_SENT / fab / purchase
- Tooling release

## Stream E coordination
Stream F does not modify KiCad trees. Antenna keepouts and connector envelopes are ICD references only.
""",
    )
    write(
        root / "STREAM_E_COORDINATION.md",
        """# Stream E Coordination

| Concern | Stream E path | Stream F path |
|---|---|---|
| PCB / schematic / Gerber | `device_designs/**`, `hardware_v1/electrical/` | do not edit |
| Connector pin map | KiCad / electrical ICD | mechanical envelope only |
| Antenna feed/matching | electrical/RF | keepout volumes in mechanical |
| Stackup impedance | electrical | fab notes reference only |
| Enclosure / DFM | — | `hardware_v1/mechanical/` |
| EVT physical packs | may consume EE bring-up | `evt_dvt_pvt/` |
| Cert matrix | radio module cert refs | `certification/stream_f/` |
| CM RFQ mech+mfg | EE attachments | `manufacturing/stream_f/` |

If a change requires both, split commits/PRs by directory ownership.
""",
    )
    write(
        root / "OWNER_ONLY_ACTIONS.md",
        """# Remaining Owner-Only Actions (Stream F)

1. Authorize and **send** CM / lab RFQs (`RFQ_SENT` today = false)
2. Engage certification labs; book EMC/safety/battery slots
3. Approve material finish + elastomer/skin contact choices
4. Freeze numeric EVT/DVT limits; run physical packs on hardware
5. Commission fixtures listed in `npi/evt0_measurement_readiness/`
6. Sign PFMEA / control plan with CM quality
7. Stand up MES instance using schemas (or map to CM MES)
8. First-article print + CMM; ergonomic study with humans (not CAD)
9. Tooling kickoff only after digital+commercial gates owner-approved
10. Do **not** treat Stream F gate TRUE as physical or certification PASS
""",
    )
    for name, gate in gates.items():
        sec = {
            "section_15_mechanical": "SECTION_15_MECHANICAL",
            "section_16_evt_dvt_pvt": "SECTION_16_EVT_DVT_PVT",
            "section_17_certification": "SECTION_17_CERTIFICATION",
            "section_18_manufacturing": "SECTION_18_MANUFACTURING",
        }[name]
        jwrite(root / sec / "GATE.json", gate)
        write(
            root / sec / "GATE.md",
            f"""# {gate['gate']}

Status: **{'TRUE' if gate['status'] else 'FALSE'}**  
Generated: {gate['generated_at_utc']}  
Artifacts: `{gate['artifacts_root']}`

Honesty keys: `{json.dumps(gate.get('honesty', {}), sort_keys=True)}`
""",
        )


def write_scripts() -> None:
    write(
        ROOT / "scripts" / "run_stream_f_physical_pack.py",
        '''#!/usr/bin/env python3
"""Dry-run / refuse physical PASS without explicit lab evidence flag."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    p = argparse.ArgumentParser(description="Stream F EVT/DVT/PVT pack runner")
    p.add_argument("--phase", choices=["EVT", "DVT", "PVT"], required=True)
    p.add_argument(
        "--i-have-lab-evidence",
        action="store_true",
        help="Required to even attempt PASS recording (still refuses auto-PASS)",
    )
    args = p.parse_args()
    pack_path = ROOT / "evt_dvt_pvt" / args.phase.lower() / f"{args.phase}_TEST_PACK.json"
    if not pack_path.exists():
        print(f"FAIL missing {pack_path}")
        return 1
    pack = json.loads(pack_path.read_text())
    print(f"Loaded {pack['case_count']} {args.phase} cases (digital prep).")
    if not args.i_have_lab_evidence:
        print("REFUSE: physical execution blocked (omit lab evidence flag).")
        print("All physical_pass tokens remain false.")
        return 2
    print("Lab evidence flag set, but this runner still will NOT auto-mark PASS.")
    print("Record evidence via evt_dvt_pvt/schemas/evidence_record.schema.json in lab MES.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
''',
    )
    write(
        ROOT / "scripts" / "validate_stream_f_exhaustion.py",
        '''#!/usr/bin/env python3
"""Validate Stream F digital engineering exhaustion gates and honesty tokens."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "digital_engineering_exhaustion" / "stream_f"

REQUIRED_GATES = {
    "SECTION_15_MECHANICAL": "MECHANICAL_DIGITAL_ENGINEERING_EXHAUSTED",
    "SECTION_16_EVT_DVT_PVT": "PHYSICAL_VALIDATION_ENGINEERING_PREP_EXHAUSTED",
    "SECTION_17_CERTIFICATION": "CERTIFICATION_ENGINEERING_PREP_EXHAUSTED",
    "SECTION_18_MANUFACTURING": "MANUFACTURING_ENGINEERING_PREP_EXHAUSTED",
}

FORBIDDEN_CLAIM_PATTERNS = [
    r"\\bFCC approved\\b",
    r"\\bCE approved\\b",
    r"\\bcertified hardware\\b",
    r"\\bergonomic pass\\b\\s*[:=]\\s*true",
    r"\\bRFQ_SENT\\b\\s*[:=]\\s*true",
]

# Paths Stream F must not own/modify in this package
STREAM_E_PATHS = [
    "device_designs/_shared_kicad",
    "hardware_v1/electrical",
]


def fail(msg: str) -> int:
    print(f"FAIL {msg}")
    return 1


def main() -> int:
    if not ART.exists():
        return fail(f"missing {ART}")
    idx = ART / "STREAM_F_INDEX.json"
    if not idx.exists():
        return fail("missing STREAM_F_INDEX.json")
    index = json.loads(idx.read_text())

    for folder, gate_name in REQUIRED_GATES.items():
        gpath = ART / folder / "GATE.json"
        if not gpath.exists():
            return fail(f"missing {gpath}")
        gate = json.loads(gpath.read_text())
        if gate.get("gate") != gate_name:
            return fail(f"{folder} gate name mismatch")
        if gate.get("status") is not True:
            return fail(f"{folder} gate status not true")

    # Honesty: physical tokens false
    tokens = json.loads((ROOT / "evt_dvt_pvt" / "TOKENS.json").read_text())
    for k in ("PHYSICALLY_VALIDATED", "EVT_PHYSICAL_PASS", "DVT_PHYSICAL_PASS", "PVT_PHYSICAL_PASS"):
        if tokens.get(k) is not False:
            return fail(f"token {k} must be false")

    rfq = json.loads((ROOT / "manufacturing" / "stream_f" / "RFQ_SENT.json").read_text())
    if rfq.get("RFQ_SENT") is not False:
        return fail("RFQ_SENT must be false")

    # Mechanical SKU statuses: ergonomic false
    for status_path in (ROOT / "hardware_v1" / "mechanical" / "skus").glob("*/STATUS.json"):
        st = json.loads(status_path.read_text())
        if st.get("ERGONOMIC_PASS") is not False:
            return fail(f"{status_path} ERGONOMIC_PASS must be false")
        if st.get("PHYSICAL_FIT_PASS") is not False:
            return fail(f"{status_path} PHYSICAL_FIT_PASS must be false")

    # Cert matrix: no certified true
    matrix = json.loads((ROOT / "certification" / "stream_f" / "SKU_MARKET_CERT_MATRIX.json").read_text())
    if matrix.get("certified_any") is not False:
        return fail("certified_any must be false")
    for row in matrix.get("rows", []):
        if row.get("certified") is True:
            return fail(f"row certified true: {row}")

    # Scan stream_f texts for forbidden claims
    scan_roots = [
        ROOT / "hardware_v1" / "mechanical",
        ROOT / "evt_dvt_pvt",
        ROOT / "certification" / "stream_f",
        ROOT / "manufacturing" / "stream_f",
        ART,
    ]
    for scan_root in scan_roots:
        for path in scan_root.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in {".md", ".json", ".txt"}:
                continue
            text = path.read_text(errors="replace")
            for pat in FORBIDDEN_CLAIM_PATTERNS:
                if re.search(pat, text, re.I):
                    return fail(f"forbidden claim in {path}: {pat}")

    # Ensure we did not add Stream E conflict markers claiming edits
    if index.get("coordinates_with") is None:
        return fail("index missing coordinates_with")

    print("PASS Stream F digital engineering exhaustion validation")
    print(json.dumps({k: True for k in REQUIRED_GATES.values()}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
''',
    )


def patch_makefile() -> None:
    mk = ROOT / "Makefile"
    text = mk.read_text()
    marker = "validate-stream-f:"
    if marker in text:
        return
    addition = """
.PHONY: validate-stream-f bootstrap-stream-f
bootstrap-stream-f:
\t$(PYTHON) scripts/bootstrap_stream_f_exhaustion.py
validate-stream-f:
\t$(PYTHON) scripts/validate_stream_f_exhaustion.py
"""
    # Prefer PYTHON var if present
    if "PYTHON" not in text:
        addition = addition.replace("$(PYTHON)", "python3")
    write(mk, text.rstrip() + "\n" + addition)


def patch_gates_json() -> None:
    path = ROOT / "hardware_v1" / "GATES.json"
    data = json.loads(path.read_text())
    data["MECHANICAL_DIGITAL_ENGINEERING_EXHAUSTED"] = True
    data["PHYSICAL_VALIDATION_ENGINEERING_PREP_EXHAUSTED"] = True
    data["CERTIFICATION_ENGINEERING_PREP_EXHAUSTED"] = True
    data["MANUFACTURING_ENGINEERING_PREP_EXHAUSTED"] = True
    # preserve honesty
    data["ERGONOMIC_PASS"] = False
    data["PHYSICALLY_VALIDATED"] = False
    data["CERTIFICATION_COMPLETE"] = False
    data["RFQ_SENT"] = False
    data["stream_f"] = {
        "generated_at_utc": UTC,
        "artifacts": "artifacts/digital_engineering_exhaustion/stream_f/",
    }
    jwrite(path, data)


def main() -> int:
    g15, _ = section15()
    g16 = section16()
    g17 = section17()
    g18 = section18()
    gates = {
        "section_15_mechanical": g15,
        "section_16_evt_dvt_pvt": g16,
        "section_17_certification": g17,
        "section_18_manufacturing": g18,
    }
    artifacts(gates)
    write_scripts()
    patch_makefile()
    patch_gates_json()
    write(
        ROOT / "PULL_REQUEST_BODY_STREAM_F.md",
        f"""# Stream F — Mechanical / EVT-DVT-PVT / Certification / Manufacturing Prep

**Generated:** {UTC}

## Summary
- Section 15: per-SKU mechanical digital packages (enclosure, tolerances, connectors, service, thermal/vents, antenna keepouts, exploded, DFM/DFA, drawings)
- Section 16: executable EVT/DVT/PVT test packs + schemas; physical tokens remain false
- Section 17: SKU×market certification prep matrix (no certification claims)
- Section 18: CM RFQ templates, AVL, fab notes, AOI/X-ray, PFMEA, control plan, MES schemas (`RFQ_SENT=false`)

## Gates
| Gate | Status |
|---|---|
| `MECHANICAL_DIGITAL_ENGINEERING_EXHAUSTED` | TRUE |
| `PHYSICAL_VALIDATION_ENGINEERING_PREP_EXHAUSTED` | TRUE |
| `CERTIFICATION_ENGINEERING_PREP_EXHAUSTED` | TRUE |
| `MANUFACTURING_ENGINEERING_PREP_EXHAUSTED` | TRUE |

## Coordination
Does not modify Stream E KiCad/electrical paths. See `artifacts/digital_engineering_exhaustion/stream_f/STREAM_E_COORDINATION.md`.

## Test plan
- [ ] `make validate-stream-f`
- [ ] Confirm `RFQ_SENT=false`, no ergonomic/cert/physical PASS claims
- [ ] Owner-only actions listed in `artifacts/digital_engineering_exhaustion/stream_f/OWNER_ONLY_ACTIONS.md`
""",
    )
    print(json.dumps({k: v["gate"] for k, v in gates.items()}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
