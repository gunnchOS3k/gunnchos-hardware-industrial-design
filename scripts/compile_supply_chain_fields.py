#!/usr/bin/env python3
"""Compile ASSEMBLY_BOM.csv rows into supply-chain field JSON.

Does not invent stock, price, lead time, or MOQ. Empty/unknown stays UNKNOWN.
Does not place RFQ, purchase, or fab.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "manufacturing" / "supply_chain"
UNKNOWN = "UNKNOWN"
CLAIM = (
    "Machine-readable supply-chain fields compiled from existing BOM CSVs. "
    "Stock, unit price, lead time, and MOQ stay UNKNOWN unless a cited supplier "
    "quote exists (none in this STREAM). RFQ/purchase/fab NOT_THIS_STREAM. "
    "PRODUCTION_RELEASE_CLAIMED=false."
)

BOM_PATHS = {
    "handheld_hybrid": ROOT / "device_designs/handheld_hybrid/manufacturing/ASSEMBLY_BOM.csv",
    "student_14_5": ROOT / "device_designs/student_14_5/manufacturing/ASSEMBLY_BOM.csv",
    "ds_xl_coder": ROOT / "device_designs/ds_xl_coder/manufacturing/ASSEMBLY_BOM.csv",
    "dock": ROOT / "device_designs/dock/manufacturing/ASSEMBLY_BOM.csv",
    "edge_io_rings": ROOT / "device_designs/edge_io_rings/manufacturing/ASSEMBLY_BOM.csv",
}


def _cell(row: dict[str, str], *names: str) -> str:
    for name in names:
        if name in row and str(row[name]).strip():
            return str(row[name]).strip()
    return ""


def _lifecycle(notes: str) -> str:
    upper = notes.upper()
    if "NRND" in upper:
        return "NRND"
    if "EOL" in upper and "SOLE" not in upper:
        return "EOL"
    return UNKNOWN


def _sole_source(alternate: str) -> bool | str:
    return False if alternate else UNKNOWN


def _avl(manufacturer: str, status: str) -> list[dict[str, str]]:
    qual = "AVL_PENDING" if "AVL_PENDING" in status.upper() else "CANDIDATE"
    vendor = manufacturer or UNKNOWN
    return [{"vendor": vendor, "qualification": qual if vendor != UNKNOWN else UNKNOWN}]


def compile_sku(sku: str, path: Path) -> dict:
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    parts = []
    for row in rows:
        mpn = _cell(row, "MPN", "mpn")
        if not mpn:
            continue
        alternate = _cell(row, "approved_alternative")
        manufacturer = _cell(row, "manufacturer")
        status = _cell(row, "status", "reason")
        notes = _cell(row, "notes", "reason")
        qty_raw = _cell(row, "qty", "quantity") or UNKNOWN
        try:
            qty: int | str = int(qty_raw)
        except ValueError:
            qty = qty_raw
        parts.append(
            {
                "subsystem": _cell(row, "subsystem", "device"),
                "manufacturer": manufacturer or UNKNOWN,
                "mpn": mpn,
                "description": _cell(row, "description"),
                "qty": qty,
                "preferred_or_alternate": _cell(row, "preferred_or_alternate") or UNKNOWN,
                "alternate_mpn": alternate or UNKNOWN,
                "bom_status": status or UNKNOWN,
                "avl": _avl(manufacturer, status),
                "sole_source": _sole_source(alternate),
                "lifecycle_status": _lifecycle(notes),
                "lead_time_weeks": UNKNOWN,
                "moq": UNKNOWN,
                "unit_price": UNKNOWN,
                "stock_qty": UNKNOWN,
                "notes": notes,
            }
        )
    return {
        "schema": "gunnchos.supply_chain.fields.v1",
        "sku": sku,
        "source_bom": str(path.relative_to(ROOT)),
        "PRODUCTION_RELEASE_CLAIMED": False,
        "rfq_purchase_fab": "NOT_THIS_STREAM",
        "claim_boundary": CLAIM,
        "parts": parts,
    }


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    index = []
    for sku, path in BOM_PATHS.items():
        if not path.exists():
            print("MISSING", path)
            return 1
        payload = compile_sku(sku, path)
        dest = OUT_DIR / f"{sku}.json"
        dest.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        index.append({"sku": sku, "path": str(dest.relative_to(ROOT)), "parts": len(payload["parts"])})
        print(f"WROTE {dest.relative_to(ROOT)} parts={len(payload['parts'])}")
    (OUT_DIR / "INDEX.json").write_text(
        json.dumps(
            {
                "schema": "gunnchos.supply_chain.index.v1",
                "PRODUCTION_RELEASE_CLAIMED": False,
                "rfq_purchase_fab": "NOT_THIS_STREAM",
                "skus": index,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
