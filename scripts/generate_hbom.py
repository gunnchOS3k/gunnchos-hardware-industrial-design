#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEVICES = ["student_14_5", "handheld_hybrid", "ds_xl_coder", "wearables_arena_set"]


def main() -> None:
    out = ROOT / "results/hbom"
    out.mkdir(parents=True, exist_ok=True)
    items = []
    for d in DEVICES:
        bom = ROOT / "bom" / d / "bom.csv"
        if bom.exists():
            items.append({"device_id": d, "bom_path": str(bom.relative_to(ROOT))})
    (out / "gunnchos_hardware_bom.json").write_text(
        json.dumps({"devices": items, "readiness": "H2"}, indent=2) + "\n",
        encoding="utf-8",
    )
    (out / "hardware_bom_report.md").write_text(
        "# Hardware BOM report\n\nAggregated BOM paths — unit costs are TODO_quote until supplier quotes.\n",
        encoding="utf-8",
    )
    print("Generated HBOM")


if __name__ == "__main__":
    main()
