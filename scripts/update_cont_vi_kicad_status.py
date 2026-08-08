#!/usr/bin/env python3
"""Refresh per-product ERC_DRC_STATUS.json from Cont VI family KiCad CLI meta."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "docs/full_product_family/evidence/kicad_cli/family_kicad_cli_meta.json"


def main() -> int:
    meta = json.loads(META.read_text(encoding="utf-8"))
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    products = meta.get("products") or {}
    if isinstance(products, list):
        print("CLI absent meta — nothing to refresh")
        return 0
    for prod, info in products.items():
        path = ROOT / "device_designs" / prod / "manufacturing" / "ERC_DRC_STATUS.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        pos = ROOT / "docs/full_product_family/evidence/kicad_cli" / prod / "pos" / "pick_place.csv"
        obj = {
            "product": prod,
            "updated_at_utc": ts,
            "kicad_cli": meta.get("kicad_cli"),
            "kicad_version": meta.get("version"),
            "erc": {
                "status": "RAN_WITH_VIOLATIONS" if info.get("erc.json") else "NOT_RUN",
                "report": f"docs/full_product_family/evidence/kicad_cli/{prod}/erc.json",
            },
            "drc": {
                "status": (
                    "RAN"
                    if info.get("drc.json")
                    else ("NO_PCB" if not (ROOT / "device_designs" / prod / "kicad" / f"{prod}.kicad_pcb").exists() else "NOT_RUN")
                ),
                "report": (
                    f"docs/full_product_family/evidence/kicad_cli/{prod}/drc.json"
                    if info.get("drc.json")
                    else None
                ),
            },
            "gerber": {
                "status": "EXPORTED" if info.get("gerber_count", 0) > 0 else "NOT_EXPORTED",
                "count": info.get("gerber_count", 0),
            },
            "pick_place": {"status": "EXPORTED" if pos.exists() else "PLAN_ONLY"},
            "step": {"status": "EXPORTED" if info.get("board.step") else "NOT_EXPORTED"},
            "full_hardware_design_release_complete": False,
            "design_release_complete": False,
            "kicad_cli_erc_pass": False,
            "kicad_cli_drc_pass": False,
            "note": "Device:R skeleton expected ERC violations; no PASS / COMPLETE claim",
        }
        path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")
        print("wrote", path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
