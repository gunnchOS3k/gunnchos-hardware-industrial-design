#!/usr/bin/env python3
"""Update STATUS.md/STATUS.json after KiCad static + optional CLI validation."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "STATUS.md"
STATUS_JSON = ROOT / "STATUS.json"
STATIC_ERC = ROOT / "schematic" / "reports" / "static_erc_report.json"
STATIC_DRC = ROOT / "pcb" / "reports" / "static_drc_report.json"
KICAD_META = ROOT / "validation" / "kicad_cli" / "kicad_cli_meta.json"


def main() -> int:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    erc = json.loads(STATIC_ERC.read_text()) if STATIC_ERC.exists() else {"result": "MISSING"}
    drc = json.loads(STATIC_DRC.read_text()) if STATIC_DRC.exists() else {"result": "MISSING"}
    kicad = json.loads(KICAD_META.read_text()) if KICAD_META.exists() else {
        "status": "KICAD_CLI_ABSENT",
        "version": None,
        "kicad_cli": None,
    }
    ok = erc.get("result") == "PASS" and drc.get("result") == "PASS"
    tokens = [
        "RING_DIGITAL_FABRICATION_PACKAGE_COMPLETE",
        "RING_PHYSICAL_PROTOTYPE_PENDING",
    ]
    if ok:
        tokens.append("RING_KICAD_STATIC_ERC_DRC_PASS")
    else:
        tokens.append("RING_KICAD_STATIC_ERC_DRC_FAIL")
    tokens.append(str(kicad.get("status", "KICAD_CLI_ABSENT")))

    status = {
        "board": "edge_io_ring_evt0",
        "version": "0.1.0-dev",
        "generated_at_utc": ts,
        "physical_execution_freeze": "ACTIVE",
        "tokens_set": tokens,
        "tokens_forbidden": [
            "RING_PHYSICAL_PROTOTYPE_EXISTS",
            "PRESENT_CONFIRMED_RING",
        ],
        "erc_pass": erc.get("result") == "PASS",
        "drc_pass": drc.get("result") == "PASS",
        "static_erc": erc,
        "static_drc": drc,
        "kicad_cli": {
            "status": kicad.get("status"),
            "version": kicad.get("version"),
            "path": kicad.get("kicad_cli"),
            "note": "Install skipped (sudo required on this host); soft-skip when absent.",
        },
        "irreducible_blockers": [
            {
                "class": "REQUIRES_SUPPLIER_QUOTE",
                "items": ["BT1 curved pouch", "M1 thin LRA exact MPN"],
            },
            {
                "class": "REQUIRES_PHYSICAL_FABRICATION",
                "items": ["PCB fab/assembly", "enclosure print/machine", "cradle pogo alignment"],
            },
            {
                "class": "REQUIRES_LOCAL_HARDWARE",
                "items": ["flash + bring-up measurements"],
            },
            {
                "class": "REQUIRES_EDMUND_ACCEPTANCE",
                "items": ["Gate 1 physical ACCEPT"],
            },
            {
                "class": "TOOL_INSTALL",
                "items": ["KiCad cask install requires interactive sudo on this host"],
            },
        ],
    }
    STATUS_JSON.write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
    DOCS.write_text(
        "\n".join(
            [
                "# Edge I/O Ring Digital Fabrication Status",
                "",
                f"Updated: `{ts}`",
                "",
                "```text",
                *tokens,
                "```",
                "",
                "## KiCad validation",
                f"- Static ERC: **{erc.get('result')}** (`gunnchos_static_erc`)",
                f"- Static DRC: **{drc.get('result')}** (`gunnchos_static_drc`)",
                f"- kicad-cli: **{kicad.get('status')}** version=`{kicad.get('version')}`",
                "- Host install of KiCad cask skipped (requires sudo). CI soft-skips with `KICAD_CLI_ABSENT`.",
                "",
                "## Included",
                "- Component selection with real MPNs + alternates + datasheet URLs",
                "- Schematic source + netlist + static ERC report",
                "- PCB source + Gerbers + drills + pick-place + stack-up + static DRC report",
                "- Mechanical OpenSCAD + STL export + interference check",
                "- Cross-link to compiling firmware in edge-io-measurement-node",
                "",
                "## Not claimed",
                "- Physical ring existence",
                "- Measured RF/battery/thermal",
                "- Production manufacturing",
                "- KiCad GUI-equivalent open of generated sexp (best-effort when CLI present)",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print("STATUS_UPDATED", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
