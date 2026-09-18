#!/usr/bin/env python3
"""Generate KiCad symbol for i.MX95 19x19 FCBGA from authoritative ballmap CSV.

Inputs: hardware_v1/open_custom_nxp/collateral_extract/IMX95IEC_19mm_ballmap_SPN_r1.0.csv
Outputs:
  - eda/cpb0_open/lib/gunnchos_imx95.kicad_sym
  - eda/cpb0_open/lib/IMX95_SYMBOL_REPORT.json
  - eda/cpb0_open/lib/IMX95_UNRESOLVED_PINS.csv
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NXP = ROOT / "hardware_v1" / "open_custom_nxp"
BALLMAP = NXP / "collateral_extract" / "IMX95IEC_19mm_ballmap_SPN_r1.0.csv"
LIB_DIR = NXP / "eda" / "cpb0_open" / "lib"
SYM_PATH = LIB_DIR / "gunnchos_imx95.kicad_sym"
REPORT_PATH = LIB_DIR / "IMX95_SYMBOL_REPORT.json"
UNRES_PATH = LIB_DIR / "IMX95_UNRESOLVED_PINS.csv"
EXPECTED_BALLS = 758
SYMBOL_NAME = "MIMX9596_VZ_19x19"


def classify(net: str) -> tuple[str, int]:
    """Return (electrical_type, unit_index). KiCad etypes: power_in, power_out, input, output, bidirectional, passive, no_connect."""
    u = net.upper()
    if u == "DEPOP":
        return "no_connect", 8
    if u in {"VSS", "GND"} or u.startswith("VSS"):
        return "power_in", 1
    if (
        u.startswith("VDD")
        or u.startswith("NVCC")
        or u.startswith("VDDQ")
        or u.startswith("VDD2")
        or u.startswith("VREF")
    ):
        return "power_in", 1
    if u in {"NC", "DNU"} or "RESERVED" in u or u.startswith("NC"):
        return "no_connect", 8
    if u.startswith("DRAM_"):
        return "bidirectional", 2
    if u.startswith("PCIE"):
        return "bidirectional", 3
    if u.startswith("USB"):
        return "bidirectional", 3
    if "ENET" in u or u.startswith("ETH"):
        return "bidirectional", 4
    if "MIPI" in u or "LVDS" in u:
        return "bidirectional", 5
    if u in {"TMS", "TCK", "TDI", "TDO", "TRST_B"} or "JTAG" in u or "DAP" in u:
        return "bidirectional", 6
    if u in {"POR_B", "ONOFF", "PMIC_ON_REQ", "PMIC_STBY_REQ", "WDOG_ANY"}:
        return "bidirectional", 6
    return "bidirectional", 7


def pin_name(net: str, ball: str) -> str:
    # KiCad pin names must be unique; power nets often share names across balls — suffix ball.
    safe = re.sub(r"[^A-Za-z0-9_/~]", "_", net)
    if not safe:
        safe = f"BALL_{ball}"
    return f"{safe}/{ball}"


def load_balls() -> list[dict]:
    rows = []
    with BALLMAP.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            ball = (r.get("PIN_NUMBER") or "").strip()
            net = (r.get("NET_NAME") or "").strip()
            if not ball:
                continue
            etype, unit = classify(net)
            rows.append(
                {
                    "ball": ball,
                    "primary_signal": net,
                    "etype": etype,
                    "unit": unit,
                    "pin_name": pin_name(net, ball),
                    "x": r.get("PIN_X"),
                    "y": r.get("PIN_Y"),
                }
            )
    return rows


def emit_symbol(balls: list[dict]) -> str:
    # Group by unit for readability
    by_unit: dict[int, list[dict]] = defaultdict(list)
    for b in balls:
        by_unit[b["unit"]].append(b)

    unit_names = {
        1: "Power_Ground",
        2: "DRAM",
        3: "PCIe_USB",
        4: "Ethernet",
        5: "MIPI_LVDS",
        6: "Boot_Debug_PMIC",
        7: "GPIO_Misc",
        8: "NC_DEPOP",
    }

    parts = [
        "(kicad_symbol_lib",
        '  (version 20231120)',
        '  (generator "generate_imx95_kicad_symbol")',
        f'  (symbol "{SYMBOL_NAME}"',
        "    (exclude_from_sim no)",
        "    (in_bom yes)",
        "    (on_board yes)",
        f'    (property "Reference" "U" (at 0 5.08 0) (effects (font (size 1.27 1.27))))',
        f'    (property "Value" "{SYMBOL_NAME}" (at 0 2.54 0) (effects (font (size 1.27 1.27))))',
        f'    (property "Footprint" "gunnchos_imx95:IMX95_FCBGA_19x19_0P7" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))',
        f'    (property "Datasheet" "IMX95IEC Rev 8" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))',
        f'    (property "Description" "i.MX95 19x19 FCBGA ball symbol from IMX95IEC attached ballmap" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))',
        "    (property \"ki_keywords\" \"NXP i.MX95 MIMX9596 FCBGA\" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))",
    ]

    # unit 0 rectangle shared
    parts.append(f'    (symbol "{SYMBOL_NAME}_0_1"')
    parts.append("      (rectangle (start -50.8 50.8) (end 50.8 -50.8)")
    parts.append("        (stroke (width 0.254) (type default)) (fill (type background)))")
    parts.append("    )")

    pin_number = 1  # KiCad requires unique pin numbers; use sequential, store ball in name/number field
    # Prefer ball as pin number string when alphanumeric-safe
    for unit in sorted(by_unit):
        pins = sorted(by_unit[unit], key=lambda x: x["ball"])
        parts.append(f'    (symbol "{SYMBOL_NAME}_{unit}_1"')
        # Layout pins in two columns
        n = len(pins)
        left = pins[: (n + 1) // 2]
        right = pins[(n + 1) // 2 :]
        y0 = 45.72
        for i, p in enumerate(left):
            y = y0 - i * 2.54
            parts.append(
                f'      (pin {p["etype"]} line (at -55.88 {y:.2f} 0) (length 5.08)'
                f' (name "{p["pin_name"]}" (effects (font (size 1.016 1.016))))'
                f' (number "{p["ball"]}" (effects (font (size 1.016 1.016)))))'
            )
        for i, p in enumerate(right):
            y = y0 - i * 2.54
            parts.append(
                f'      (pin {p["etype"]} line (at 55.88 {y:.2f} 180) (length 5.08)'
                f' (name "{p["pin_name"]}" (effects (font (size 1.016 1.016))))'
                f' (number "{p["ball"]}" (effects (font (size 1.016 1.016)))))'
            )
        # unit label
        uname = unit_names.get(unit, f"Unit{unit}")
        parts.append(
            f'      (text "{uname}" (at 0 48.26 0) (effects (font (size 1.27 1.27))))'
        )
        parts.append("    )")

    parts.append("  )")
    parts.append(")")
    return "\n".join(parts) + "\n"


def main() -> int:
    if not BALLMAP.exists():
        print(f"FAIL: missing ballmap {BALLMAP}", file=sys.stderr)
        return 1
    balls = load_balls()
    unresolved = [b for b in balls if not b["primary_signal"]]
    errors = []
    if len(balls) != EXPECTED_BALLS:
        errors.append(f"ball count {len(balls)} != expected {EXPECTED_BALLS}")
    balls_set = [b["ball"] for b in balls]
    if len(balls_set) != len(set(balls_set)):
        errors.append("duplicate balls in map")
    if unresolved:
        errors.append(f"{len(unresolved)} balls missing primary signal")

    LIB_DIR.mkdir(parents=True, exist_ok=True)
    body = emit_symbol(balls)
    SYM_PATH.write_text(body, encoding="utf-8")
    digest = hashlib.sha256(body.encode()).hexdigest()

    with UNRES_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["ball", "primary_signal", "reason"])
        w.writeheader()
        for b in unresolved:
            w.writerow({"ball": b["ball"], "primary_signal": b["primary_signal"], "reason": "empty_net"})

    report = {
        "schema": "gunnchos.hardware_v1.nxp1.imx95_symbol_report.v1",
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "symbol_name": SYMBOL_NAME,
        "symbol_path": str(SYM_PATH.relative_to(ROOT)),
        "source_ballmap": str(BALLMAP.relative_to(ROOT)),
        "pin_count": len(balls),
        "expected_pin_count": EXPECTED_BALLS,
        "unresolved_count": len(unresolved),
        "sha256": digest,
        "units": sorted({b["unit"] for b in balls}),
        "validation_errors": errors,
        "CPB0_OPEN_SOC_SYMBOL_VALIDATED": len(errors) == 0 and len(unresolved) == 0,
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"pin_count": len(balls), "sha256": digest, "ok": not errors}, indent=2))
    if errors:
        for e in errors:
            print("ERROR:", e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
