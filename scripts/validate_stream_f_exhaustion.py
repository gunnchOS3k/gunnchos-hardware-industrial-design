#!/usr/bin/env python3
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

    tokens = json.loads((ROOT / "evt_dvt_pvt" / "TOKENS.json").read_text())
    for k in ("PHYSICALLY_VALIDATED", "EVT_PHYSICAL_PASS", "DVT_PHYSICAL_PASS", "PVT_PHYSICAL_PASS"):
        if tokens.get(k) is not False:
            return fail(f"token {k} must be false")

    rfq = json.loads((ROOT / "manufacturing" / "stream_f" / "RFQ_SENT.json").read_text())
    if rfq.get("RFQ_SENT") is not False:
        return fail("RFQ_SENT must be false")

    for status_path in (ROOT / "hardware_v1" / "mechanical" / "skus").glob("*/STATUS.json"):
        st = json.loads(status_path.read_text())
        if st.get("ERGONOMIC_PASS") is not False:
            return fail(f"{status_path} ERGONOMIC_PASS must be false")
        if st.get("PHYSICAL_FIT_PASS") is not False:
            return fail(f"{status_path} PHYSICAL_FIT_PASS must be false")

    matrix = json.loads((ROOT / "certification" / "stream_f" / "SKU_MARKET_CERT_MATRIX.json").read_text())
    if matrix.get("certified_any") is not False:
        return fail("certified_any must be false")
    for row in matrix.get("rows", []):
        if row.get("certified") is True:
            return fail(f"row certified true: {row}")

    # Affirmative false-green patterns
    bad = [
        re.compile(r'(?i)"ERGONOMIC_PASS"\s*:\s*true'),
        re.compile(r'(?i)"RFQ_SENT"\s*:\s*true'),
        re.compile(r'(?i)"certified_any"\s*:\s*true'),
        re.compile(r'(?i)"CERTIFICATION_COMPLETE"\s*:\s*true'),
        re.compile(r'(?i)"PHYSICALLY_VALIDATED"\s*:\s*true'),
        re.compile(r'(?i)"EVT_PHYSICAL_PASS"\s*:\s*true'),
        re.compile(r'(?i)"DVT_PHYSICAL_PASS"\s*:\s*true'),
        re.compile(r'(?i)"PVT_PHYSICAL_PASS"\s*:\s*true'),
    ]
    scan_roots = [
        ROOT / "hardware_v1" / "mechanical",
        ROOT / "evt_dvt_pvt",
        ROOT / "certification" / "stream_f",
        ROOT / "manufacturing" / "stream_f",
        ART,
    ]
    for scan_root in scan_roots:
        for path in scan_root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in {".md", ".json", ".txt"}:
                continue
            text = path.read_text(errors="replace")
            for pat in bad:
                if pat.search(text):
                    return fail(f"forbidden true token in {path}: {pat.pattern}")

    if not index.get("coordinates_with"):
        return fail("index missing coordinates_with")

    # Required path presence
    required_paths = [
        ROOT / "hardware_v1" / "mechanical" / "GATE_SECTION_15.json",
        ROOT / "evt_dvt_pvt" / "GATE_SECTION_16.json",
        ROOT / "certification" / "stream_f" / "GATE_SECTION_17.json",
        ROOT / "manufacturing" / "stream_f" / "GATE_SECTION_18.json",
        ROOT / "evt_dvt_pvt" / "evt" / "EVT_TEST_PACK.json",
        ROOT / "evt_dvt_pvt" / "dvt" / "DVT_TEST_PACK.json",
        ROOT / "evt_dvt_pvt" / "pvt" / "PVT_TEST_PACK.json",
        ROOT / "manufacturing" / "stream_f" / "MES_SCHEMAS" / "work_order.schema.json",
    ]
    for rp in required_paths:
        if not rp.exists():
            return fail(f"missing {rp}")

    sku_dirs = list((ROOT / "hardware_v1" / "mechanical" / "skus").iterdir())
    if len(sku_dirs) < 5:
        return fail("expected >=5 mechanical SKU packs")

    print("PASS Stream F digital engineering exhaustion validation")
    print(json.dumps({k: True for k in REQUIRED_GATES.values()}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
