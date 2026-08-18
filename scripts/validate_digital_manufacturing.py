#!/usr/bin/env python3
"""Validate supervisor-ready DIGITAL manufacturing packet.

Checks presence, UML lanes, packets, and forbidden fabrication/cert claims.
Does not claim DIGITAL_FABRICATION_PASS or RFQ_SENT.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "DIGITAL_MANUFACTURING_READINESS.md",
    "DIGITAL_TO_PHYSICAL_HANDOFF.md",
    "docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md",
    "docs/packets/MANUFACTURER_RFQ_SEND_PACKET.md",
    "os_compatibility/OS_HARDWARE_INTERFACE_TRACEABILITY.md",
    "docs/uml/README.md",
    "docs/uml/traceability_matrix.md",
    "docs/uml/current/index.md",
    "docs/uml/current/component.md",
    "docs/uml/current/composite_structure.md",
    "docs/uml/current/deployment.md",
    "docs/uml/current/state_power_boot.md",
    "docs/uml/current/timing.md",
    "docs/uml/current/sequence_bringup.md",
    "docs/uml/future/index.md",
    "docs/uml/future/physical_evt_and_cm.md",
    "docs/uml/legacy/index.md",
    "docs/uml/legacy/evt0_concept.md",
    "docs/uml/rendered/README.md",
    "scripts/run_supervisor_eda_checks.sh",
]

REQUIRED_PHRASES = {
    "DIGITAL_MANUFACTURING_READINESS.md": [
        "PHYSICAL_PENDING",
        "DIGITAL_FABRICATION_PASS",
        "UNRES-COM-HPC-400PIN",
    ],
    "DIGITAL_TO_PHYSICAL_HANDOFF.md": [
        "PHYSICAL_PENDING",
        "Student 14.5",
        "Handheld Hybrid",
        "DS-XL Coder",
        "Edge I/O Rings",
        "Do not invent",
    ],
    "docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md": [
        "PHYSICAL_PENDING",
        "Do **not** copy YAML",
    ],
    "docs/packets/MANUFACTURER_RFQ_SEND_PACKET.md": [
        "EXTERNAL_PENDING",
        "Owner sends the RFQ",
    ],
}

FORBIDDEN_CLAIM_PATTERNS = [
    r"(?<!not )FCC certified",
    r"(?<!not )CE certified",
    r"(?<!not )USB-IF certified",
    r"RFQ_SENT[`\s|*]*\|[^\n]*TRUE",
    r"DIGITAL_FABRICATION_PASS[`\s|*]*\|[^\n]*TRUE",
    r"manufacturing release complete",
    r"PHYSICAL_PENDING converted",
]

CLAIM_DOCS = [
    "DIGITAL_MANUFACTURING_READINESS.md",
    "DIGITAL_TO_PHYSICAL_HANDOFF.md",
    "docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md",
    "docs/packets/MANUFACTURER_RFQ_SEND_PACKET.md",
    "os_compatibility/OS_HARDWARE_INTERFACE_TRACEABILITY.md",
    "README.md",
]


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing {rel}")
        elif path.stat().st_size < 80:
            errors.append(f"too_short {rel}")

    for rel, needles in REQUIRED_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                errors.append(f"missing_phrase {rel}: {needle}")

    dmr = (ROOT / "DIGITAL_MANUFACTURING_READINESS.md").read_text(encoding="utf-8") if (
        ROOT / "DIGITAL_MANUFACTURING_READINESS.md"
    ).exists() else ""
    if dmr:
        if "DIGITAL_FABRICATION_PASS" in dmr and re.search(
            r"DIGITAL_FABRICATION_PASS[`\s|*]*\|[^\n]*TRUE", dmr
        ):
            errors.append("DIGITAL_FABRICATION_PASS must remain FALSE")
        if "**FALSE**" not in dmr.split("DIGITAL_FABRICATION_PASS", 1)[-1][:400]:
            errors.append("DIGITAL_FABRICATION_PASS row must be FALSE")

    for rel in CLAIM_DOCS:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pat in FORBIDDEN_CLAIM_PATTERNS:
            if re.search(pat, text, re.I):
                errors.append(f"forbidden_claim {rel}: {pat}")

    bringup = ROOT / "docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md"
    if bringup.exists():
        t = bringup.read_text(encoding="utf-8")
        if "invent" in t.lower() and "not invent" not in t.lower() and "Do **not**" not in t:
            errors.append("bring-up packet must forbid inventing measured voltages")

    summary = ROOT / "artifacts/supervisor_ready_eda/SUMMARY.json"
    if summary.exists():
        try:
            data = json.loads(summary.read_text())
        except json.JSONDecodeError as exc:
            errors.append(f"bad SUMMARY.json: {exc}")
        else:
            if data.get("DIGITAL_FABRICATION_PASS") is True:
                errors.append("SUMMARY.json must not set DIGITAL_FABRICATION_PASS true")
            if data.get("rfq_sent") is True:
                errors.append("SUMMARY.json must not set rfq_sent true")
            if data.get("fcc_ce_usbif") is True:
                errors.append("SUMMARY.json must not set fcc_ce_usbif true")

    if errors:
        print("FAIL digital manufacturing validation:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("PASS digital manufacturing validation (packet only; fabrication still PHYSICAL_PENDING)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
