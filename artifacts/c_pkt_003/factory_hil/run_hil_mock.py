#!/usr/bin/env python3
"""Digital-only HIL/factory mock for C-PKT-003. Never claims physical factory PASS."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

RESULTS = Path(__file__).resolve().parent / "results"

DEVICES = {
    "student_14_5": ["power_rail_probe", "boot_console", "usb_enumerate"],
    "ds_xl_coder": ["power_rail_probe", "boot_console", "usb_enumerate", "display_hotplug"],
    "handheld_hybrid": ["power_rail_probe", "boot_console", "usb_enumerate"],
    "dock": ["power_rail_probe", "usb_enumerate", "display_hotplug"],
    "edge_io_rings": ["power_rail_probe", "boot_console", "ring_imu_sample"],
}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--product", required=True, choices=sorted(DEVICES))
    args = p.parse_args()
    checks = []
    for name in DEVICES[args.product]:
        checks.append({
            "check": name,
            "result": "MOCK_PASS",
            "physical": False,
            "note": "Synthetic digital mock — not factory line evidence",
        })
    out = {
        "schema": "gunnchos.c_pkt_003.hil_mock_result.v1",
        "product": args.product,
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "mode": "MOCK_DIGITAL_ONLY",
        "checks": checks,
        "FACTORY_PHYSICAL_PASS": False,
        "EVT_PHYSICAL_PASS": False,
        "overall": "DIGITAL_MOCK_OK",
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    path = RESULTS / f"{args.product}_hil_mock.json"
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
