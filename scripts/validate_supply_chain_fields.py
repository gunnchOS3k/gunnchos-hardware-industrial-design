#!/usr/bin/env python3
"""Honesty gate: required supply-chain fields present; unknown stays unknown."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "manufacturing" / "supply_chain"
UNKNOWN = "UNKNOWN"
NUMERIC_FORBIDDEN = ("unit_price", "stock_qty", "lead_time_weeks", "moq")


def _is_invented_number(value) -> bool:
    if value == UNKNOWN:
        return False
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, str):
        stripped = value.strip().replace("$", "")
        try:
            float(stripped)
            return True
        except ValueError:
            return False
    return False


def validate_doc(path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("PRODUCTION_RELEASE_CLAIMED") is not False:
        errors.append(f"{path.name}: PRODUCTION_RELEASE_CLAIMED must be false")
    if data.get("rfq_purchase_fab") != "NOT_THIS_STREAM":
        errors.append(f"{path.name}: rfq_purchase_fab must be NOT_THIS_STREAM")
    parts = data.get("parts") or []
    if not parts:
        errors.append(f"{path.name}: no parts")
    required = (
        "mpn",
        "manufacturer",
        "qty",
        "preferred_or_alternate",
        "alternate_mpn",
        "avl",
        "sole_source",
        "lifecycle_status",
        "lead_time_weeks",
        "moq",
        "unit_price",
        "stock_qty",
    )
    for i, part in enumerate(parts):
        for field in required:
            if field not in part:
                errors.append(f"{path.name} part[{i}] missing {field}")
        for field in NUMERIC_FORBIDDEN:
            if _is_invented_number(part.get(field)):
                errors.append(
                    f"{path.name} part[{i}] {field}={part.get(field)!r} invented; must be UNKNOWN without a cited quote"
                )
        sole = part.get("sole_source")
        if sole is True:
            errors.append(
                f"{path.name} part[{i}] sole_source=true inferred; use UNKNOWN unless a human declared sole-source"
            )
        if part.get("lifecycle_status") not in ("ACTIVE", "NRND", "EOL", UNKNOWN):
            errors.append(f"{path.name} part[{i}] bad lifecycle_status")
        avl = part.get("avl")
        if not isinstance(avl, list) or not avl:
            errors.append(f"{path.name} part[{i}] avl must be a non-empty list")
    return errors


def main() -> int:
    files = sorted(p for p in DIR.glob("*.json") if p.name not in ("SCHEMA.json", "INDEX.json"))
    if not files:
        print("FAIL no supply-chain JSON")
        return 1
    errors: list[str] = []
    for path in files:
        errors.extend(validate_doc(path))
    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print(f"PASS {len(files)} supply-chain field files (unknown stays unknown)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
