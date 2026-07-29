#!/usr/bin/env python3
"""Gate 6 dry-run for gunnchos-hardware-industrial-design.

Synthetic/emulated harness only. Physical claims stay DESIGN_ONLY /
HARDWARE_PROTOTYPE_PENDING.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHYS = ROOT / "physical_evidence"
REPORT = PHYS / "GATE6_DRY_RUN_REPORT.json"
SCHEMA = PHYS / "prototype_evidence.schema.json"
PTB_SCHEMA = PHYS / "power_thermal_battery_log.schema.json"
FIXTURE = PHYS / "fixtures" / "synthetic_prototype_dry_run.json"
PTB_FIXTURE = PHYS / "fixtures" / "synthetic_power_thermal_dry_run.json"

REQUIRED_FILES = [
    "prototype_evidence.schema.json",
    "BOARD_BRINGUP_CHECKLIST.md",
    "power_thermal_battery_log.schema.json",
    "MECHANICAL_FIT_RECORD_TEMPLATE.json",
    "DEFECT_REGISTRY_TEMPLATE.json",
    "fixtures/synthetic_prototype_dry_run.json",
    "fixtures/synthetic_power_thermal_dry_run.json",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must be a JSON object")
    return data


def check_files() -> dict:
    missing = [name for name in REQUIRED_FILES if not (PHYS / name).is_file()]
    return {"ok": not missing, "missing": missing, "required": REQUIRED_FILES}


def validate_against_required(data: dict, required: list[str], label: str) -> list[str]:
    return [f"{label}: missing {k}" for k in required if k not in data]


def check_fixtures() -> dict:
    errors: list[str] = []
    proto = load_json(FIXTURE)
    errors.extend(
        validate_against_required(
            proto,
            [
                "evidence_id",
                "evidence_label",
                "domain",
                "status",
                "claim_boundary",
                "artifacts",
            ],
            "prototype",
        )
    )
    if proto.get("evidence_label") != "SYNTHETIC_EXPERIMENT":
        errors.append("prototype: evidence_label must be SYNTHETIC_EXPERIMENT")
    if proto.get("claim_boundary") not in ("DESIGN_ONLY", "HARDWARE_PROTOTYPE_PENDING"):
        errors.append("prototype: claim_boundary must remain DESIGN_ONLY or HARDWARE_PROTOTYPE_PENDING")
    if proto.get("status") != "DRY_RUN_SYNTHETIC":
        errors.append("prototype: status must be DRY_RUN_SYNTHETIC")

    ptb = load_json(PTB_FIXTURE)
    errors.extend(
        validate_against_required(
            ptb,
            ["log_id", "mode", "claim_boundary", "samples", "status"],
            "power_thermal",
        )
    )
    if ptb.get("mode") not in ("DRY_RUN", "EMULATED"):
        errors.append("power_thermal: mode must be DRY_RUN or EMULATED")
    if ptb.get("claim_boundary") not in ("DESIGN_ONLY", "HARDWARE_PROTOTYPE_PENDING"):
        errors.append("power_thermal: claim_boundary must not claim PHYSICAL_MEASURED")

    # Schemas must parse as JSON objects with $id
    for path in (SCHEMA, PTB_SCHEMA):
        schema = load_json(path)
        if "$id" not in schema:
            errors.append(f"schema missing $id: {path.name}")

    return {"ok": not errors, "errors": errors}


def main() -> int:
    PHYS.mkdir(parents=True, exist_ok=True)
    files = check_files()
    fixtures = check_fixtures() if files["ok"] else {"ok": False, "errors": ["required files missing"]}
    harness_ok = files["ok"] and fixtures["ok"]

    report = {
        "gate": "6",
        "repository": "gunnchos-hardware-industrial-design",
        "mode": "dry_run",
        "started": utc_now(),
        "files": files,
        "fixtures": fixtures,
        "statuses": {
            "GATE6_HARNESS": "GATE6_HARNESS_PASS" if harness_ok else "GATE6_HARNESS_FAIL",
            "HARDWARE_PROTOTYPE": "HARDWARE_PROTOTYPE_PENDING",
            "CLAIM_BOUNDARY": "DESIGN_ONLY",
            "PHYSICAL_EVIDENCE": "PHYSICAL_EVIDENCE_PENDING",
        },
        "claim": "GATE6_HARNESS_PASS only — DESIGN_ONLY / HARDWARE_PROTOTYPE_PENDING for physical claims",
        "finished": utc_now(),
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": harness_ok, "report": str(REPORT), "statuses": report["statuses"]}, indent=2))
    return 0 if harness_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
