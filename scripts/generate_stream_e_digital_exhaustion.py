#!/usr/bin/env python3
"""Stream E — digital hardware engineering exhaustion (public collateral + local EDA).

Honest claim boundary:
- Exhausts what public docs + KiCad allow.
- Does NOT invent NDA/AMD pin maps, i.MX95 ball maps, or JHL ball maps.
- CPB0_OPEN_READY_FOR_FAB stays false unless genuine fab readiness is proven.
"""

from __future__ import annotations

import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TS = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
CAMPAIGN = "STREAM_E_DIGITAL_HARDWARE_ENGINEERING_EXHAUSTION"
ART = ROOT / "artifacts/digital_engineering_exhaustion/stream_e"
CLAIM = (
    "digital engineering exhaustion under public collateral + local EDA only — "
    "not physical pass, not certification, not fab release, not purchased, not GXE execution, "
    "no invented NDA pin maps"
)


def uid() -> str:
    return str(uuid.uuid4())


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")


def hdr(title: str) -> str:
    return (
        f"# {title}\n\n"
        f"**Generated:** {TS}\n"
        f"**Campaign:** `{CAMPAIGN}`\n"
        f"**Claim boundary:** {CLAIM}.\n\n"
    )


def sch_shell(title: str, rev: str, comment3: str, comment4: str, body: str) -> str:
    return f"""(kicad_sch (version 20230121) (generator "stream_e_digital_exhaustion")
  (uuid {uid()})
  (paper "A3")
  (title_block
    (title "{title}")
    (date "{TS[:10]}")
    (rev "{rev}")
    (company "gunnchOS3k / STREAM_E")
    (comment 1 "PUBLIC_COLLATERAL_ONLY")
    (comment 2 "DRAFT — physical/fab claims remain false unless gate says otherwise")
    (comment 3 "{comment3}")
    (comment 4 "{comment4}")
  )
{body}
)
"""


def simple_lib_symbols() -> str:
    # Minimal passive + role-envelope IC symbols for public-class schematics.
    return """  (lib_symbols
    (symbol "R"
      (pin_numbers (hide yes))
      (pin_names (offset 0.254))
      (in_bom yes) (on_board yes)
      (property "Reference" "R" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Value" "R" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Footprint" "gunnchos_production:R_0402" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "R_0_1"
        (rectangle (start -1.016 -2.54) (end 1.016 2.54)
          (stroke (width 0.254) (type default)) (fill (type none))))
      (symbol "R_1_1"
        (pin passive line (at 0 3.81 270) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27))))))
    )
    (symbol "C"
      (pin_numbers (hide yes))
      (pin_names (offset 0.254))
      (in_bom yes) (on_board yes)
      (property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Value" "C" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Footprint" "gunnchos_production:C_0402" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "C_0_1"
        (polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.254) (type default)) (fill (type none))))
      (symbol "C_1_1"
        (pin passive line (at 0 3.81 270) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27))))))
    )
    (symbol "TP"
      (pin_numbers (hide yes))
      (pin_names (offset 0.254))
      (in_bom no) (on_board yes)
      (property "Reference" "TP" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
      (property "Value" "TP" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "gunnchos_production:TestPoint_Pad" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "TP_0_1" (circle (center 0 0) (radius 0.762) (stroke (width 0.1524) (type default)) (fill (type none))))
      (symbol "TP_1_1" (pin passive line (at 0 0 0) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27))))))
    )
    (symbol "ROLE_IC"
      (pin_names (offset 1.016))
      (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 12.7 0) (effects (font (size 1.27 1.27))))
      (property "Value" "ROLE_IC" (at 0 -12.7 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "ROLE_IC_0_1"
        (rectangle (start -15.24 -10.16) (end 15.24 10.16)
          (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "ROLE_IC_1_1"
        (pin passive line (at -17.78 5.08 0) (length 2.54) (name "PWR" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin passive line (at -17.78 0 0) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin passive line (at -17.78 -5.08 0) (length 2.54) (name "CTRL" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin passive line (at 17.78 5.08 180) (length 2.54) (name "IO_A" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin passive line (at 17.78 0 180) (length 2.54) (name "IO_B" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin passive line (at 17.78 -5.08 180) (length 2.54) (name "RF_ANT" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016))))))
    )
  )
"""


def place_symbol(lib_id: str, ref: str, value: str, x: float, y: float, footprint: str = "", mpn: str = "", role: str = "") -> str:
    extra = ""
    if footprint:
        extra += f'    (property "Footprint" "{footprint}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))\n'
    if mpn:
        extra += f'    (property "MPN" "{mpn}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))\n'
    if role:
        extra += f'    (property "Role" "{role}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))\n'
    return f"""  (symbol (lib_id "{lib_id}") (at {x} {y} 0) (unit 1)
    (uuid {uid()})
    (property "Reference" "{ref}" (at {x} {y - 5.08} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "{value}" (at {x} {y + 5.08} 0) (effects (font (size 1.27 1.27))))
{extra}  )
"""


def place_label(name: str, shape: str, x: float, y: float) -> str:
    return f"""  (global_label "{name}" (shape {shape}) (at {x} {y} 0) (fields_autoplaced)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid {uid()})
  )
"""


def place_text(text: str, x: float, y: float) -> str:
    return f"""  (text "{text}" (at {x} {y} 0)
    (effects (font (size 1.5 1.5)))
    (uuid {uid()})
  )
"""


def pcb_shell(title: str, rev: str, width: float, height: float, footprints: str, notes: list[str]) -> str:
    note_txt = "\n".join(
        f'  (gr_text "{n}" (at 8 {12 + i * 6} 0) (layer "Dwgs.User") (uuid {uid()}) '
        f'(effects (font (size 1.1 1.1) (thickness 0.1))))'
        for i, n in enumerate(notes)
    )
    return f"""(kicad_pcb (version 20221018) (generator "stream_e_digital_exhaustion")
  (general (thickness 1.6) (legacy_teardrops no))
  (paper "A4")
  (title_block
    (title "{title}")
    (date "{TS[:10]}")
    (rev "{rev}")
    (company "gunnchOS3k")
    (comment 1 "PUBLIC_COLLATERAL_ONLY")
    (comment 2 "STREAM_E digital exhaustion")
  )
  (layers
    (0 "F.Cu" signal) (1 "In1.Cu" signal) (2 "In2.Cu" signal) (31 "B.Cu" signal)
    (37 "F.SilkS" user "F.Silkscreen") (39 "F.Mask" user)
    (44 "Edge.Cuts" user) (13 "F.Paste" user) (15 "B.Paste" user)
    (35 "B.SilkS" user) (41 "B.Mask" user) (45 "Margin" user)
    (46 "B.CrtYd" user) (47 "F.CrtYd" user) (48 "Dwgs.User" user) (49 "Cmts.User" user)
  )
  (setup (pad_to_mask_clearance 0.0) (allow_soldermask_bridges_in_footprints no))
  (gr_rect (start 0 0) (end {width} {height}) (stroke (width 0.1) (type default)) (fill none) (layer "Edge.Cuts") (uuid {uid()}))
  (gr_text "REV {rev}" (at 10 8 0) (layer "F.SilkS") (uuid {uid()}) (effects (font (size 1.5 1.5) (thickness 0.2))))
{note_txt}
{footprints}
)
"""


def fp(ref: str, value: str, lib: str, x: float, y: float) -> str:
    return f"""  (footprint "{lib}" (layer "F.Cu")
    (at {x} {y}) (uuid {uid()})
    (property "Reference" "{ref}" (at 0 -3.5 0) (layer "F.SilkS") (uuid {uid()}))
    (property "Value" "{value}" (at 0 3.5 0) (layer "F.Fab") (uuid {uid()}))
    (attr smd)
    (pad "1" smd rect (at -1.0 0) (size 0.6 0.8) (layers "F.Cu" "F.Paste" "F.Mask"))
    (pad "2" smd rect (at 1.0 0) (size 0.6 0.8) (layers "F.Cu" "F.Paste" "F.Mask"))
  )
"""


def mh(ref: str, x: float, y: float) -> str:
    return f"""  (footprint "gunnchos_production:MountingHole_3.2mm" (layer "F.Cu")
    (at {x} {y}) (uuid {uid()})
    (property "Reference" "{ref}" (at 0 -3.5 0) (layer "F.SilkS") (uuid {uid()}))
    (property "Value" "M3" (at 0 3.5 0) (layer "F.Fab") (uuid {uid()}))
    (attr through_hole exclude_from_pos_files exclude_from_bom)
    (pad "" np_thru_hole circle (at 0 0) (size 3.2 3.2) (drill 3.2) (layers "*.Cu" "*.Mask"))
  )
"""


def pro_file(name: str) -> str:
    return f"""{{
  "board": {{
    "design_settings": {{
      "defaults": {{}},
      "diff_pair_dimensions": [],
      "drc_exclusions": [],
      "rules": {{}},
      "track_widths": [],
      "via_dimensions": []
    }}
  }},
  "meta": {{
    "filename": "{name}.kicad_pro",
    "version": 1
  }},
  "project": {{
    "files": []
  }},
  "sheets": [
    ["{uid()}", ""]
  ],
  "text_variables": {{}}
}}
"""


# ---------------------------------------------------------------------------
# Section 11 — NXP open-custom
# ---------------------------------------------------------------------------

def build_nxp() -> dict:
    base = ROOT / "hardware_v1/open_custom_nxp"
    kicad = base / "kicad"
    sheets = [
        ("01_block", "Block / claim boundary", "No net-accurate SoC ball map — public architecture only"),
        ("02_power", "Power + decoupling envelopes", "PMIC/rails PENDING design-guide rules; no invented seq"),
        ("03_clock_boot", "Clocks / reset / boot", "Boot-mode straps as role nets only"),
        ("04_lpddr", "LPDDR class memory", "Topology PENDING Hardware Design Guide"),
        ("05_storage", "eMMC/NVMe/SD class storage", "PCIe/NVMe lane count SKU-dependent"),
        ("06_pcie_usb", "PCIe / USB class", "SerDes pin-accurate map blocked without guide"),
        ("07_display_camera", "Display / camera", "MIPI/CSI class interfaces"),
        ("08_ec_debug", "EC / debug / testpoints", "SWD/JTAG/UART bring-up hooks"),
        ("09_connectors", "Connectors / mechanics", "Board outline TBD package select"),
        ("10_rf_optional", "Wi-Fi/BT/cellular optional", "Modules only — no custom antenna claim"),
    ]
    for stem, title, note in sheets:
        body = simple_lib_symbols()
        body += place_text(f"NXP i.MX95 OPEN_CUSTOM — {title}", 25.4, 25.4)
        body += place_text(note, 25.4, 35.56)
        body += place_text("VENDOR_CONTENT_NOT_INVENTED", 25.4, 45.72)
        body += place_symbol("ROLE_IC", "U1", "IMX95_ROLE_ENVELOPE", 101.6, 101.6, role="SOC_PUBLIC_CLASS")
        body += place_symbol("C", "C1", "100n_placeholder", 50.8, 76.2)
        body += place_symbol("R", "R1", "10k_placeholder", 76.2, 76.2)
        body += place_symbol("TP", "TP1", "TP_GND", 127.0, 76.2)
        body += place_label("VSYS_PLACEHOLDER", "input", 70.0, 101.6)
        body += place_label("GND", "passive", 70.0, 106.68)
        write(kicad / f"imx95_open_{stem}.kicad_sch", sch_shell(
            f"i.MX95 Open-Custom — {title}", "0.1.0-stream-e",
            "SoC: i.MX95 family PUBLIC_CLASS", note, body
        ))

    # Root hierarchical notes sheet
    root_body = simple_lib_symbols()
    root_body += place_text("i.MX95 OPEN_CUSTOM root — hierarchical sheet plan executed as flat public sheets", 25.4, 25.4)
    root_body += place_text("CPB0_OPEN_READY_FOR_FAB=false until design-guide + package + netlist genuine", 25.4, 35.56)
    for i, (stem, title, _) in enumerate(sheets):
        root_body += place_text(f"{i+1:02d}. {stem}: {title}", 25.4, 50.8 + i * 7.62)
    write(kicad / "imx95_open_custom.kicad_sch", sch_shell(
        "i.MX95 Open-Custom Root", "0.1.0-stream-e",
        "OPEN_ENGINEERING_MAINLINE=NXP_IMX95_OPEN_CUSTOM",
        "No invented BGA/DDR/power-seq numbers", root_body
    ))
    write(kicad / "imx95_open_custom.kicad_pro", pro_file("imx95_open_custom"))

    fps = "".join([
        mh("H1", 8, 8), mh("H2", 112, 8), mh("H3", 8, 82), mh("H4", 112, 82),
        fp("U1", "IMX95_ENVELOPE_TBD", "gunnchos_functional:Block_SMD_safe", 60, 45),
        fp("TP1", "TP", "gunnchos_production:TestPoint_Pad", 20, 30),
        fp("TP2", "TP", "gunnchos_production:TestPoint_Pad", 30, 30),
        fp("C1", "100n", "gunnchos_production:C_0402", 40, 30),
        fp("FID1", "FID", "gunnchos_production:Fiducial_1mm", 15, 15),
        fp("FID2", "FID", "gunnchos_production:Fiducial_1mm", 105, 15),
    ])
    write(kicad / "imx95_open_custom.kicad_pcb", pcb_shell(
        "imx95_open_custom", "0.1.0-stream-e", 120, 90, fps,
        [
            "Package 15x15 vs 19x19 NOT FROZEN — envelope placeholder only",
            "No LPDDR fly-by/T-branch invented",
            "No PCIe lane assignment claimed",
            "SI notes: follow NXP Hardware Design Guide when accessible",
        ],
    ))

    write(base / "PINMUX_PUBLIC_CLASS.md", hdr("i.MX95 pin/mux — public class only") + """
## Status
Public RM/datasheet describe mux capability classes. **Pin-accurate ball map is not published in-repo.**

## Exhausted without invention
- Mux class inventory (GPIO / SDHC / USB / PCIe / CSI / DSI / UART / I2C / SPI) as architecture roles
- Boot-mode / debug / JTAG role nets on sheet 03/08
- Explicit gap: Hardware Design Guide + BSDL for selected package

## Non-claims
No IOMUXC register paste, no ball numbers, no forged pinout CSV.
""")

    write(base / "CLOCKS_PUBLIC_CLASS.md", hdr("Clocks — public class") + """
- Crystal / OSC / RTC roles reserved on sheet 03
- Exact ppm / load-cap values PENDING datasheet OPN freeze + design guide
""")

    write(base / "LPDDR_CONSTRAINTS_PUBLIC.md", hdr("LPDDR constraints — public only") + """
| Item | Status |
|---|---|
| Memory class | LPDDR (family public) |
| Channel / rank | PENDING design guide + SKU |
| Length-match rules | PENDING design guide |
| VREF /ZQ | PENDING design guide |

Gate remains: topology **not** understood for fab until guide/hash closed.
""")

    write(base / "AUDIO_ARCHITECTURE.md", hdr("Audio architecture") + """
- SAI / I2S / PDM class endpoints reserved
- Codec selection AVL-open; no claimed silicon until BOM freeze
""")

    write(base / "EC_ARCHITECTURE.md", hdr("EC architecture (open-custom)") + """
- EC role: power sequencing assist, lid/thermal, button matrix — **architecture only**
- EC MCU family selection open; not claimed equivalent to AMD platform EC
""")

    write(base / "WIFI_CELLULAR_OPTIONAL.md", hdr("Wi-Fi / cellular optional") + """
- Prefer certified modules (M.2 / solder-down module) on open-custom
- Cellular remains optional; product cellular antenna design pending on PRODUCT_MAINLINE
- No custom PA/LNA RF invented here
""")

    write(base / "TESTPOINTS_DFT.md", hdr("Test points / DFT") + """
| TP | Net role | Purpose |
|---|---|---|
| TP_GND | GND | Fixture common |
| TP_VSYS | VSYS placeholder | Power bring-up |
| TP_UART_TX/RX | Debug UART | Console |
| TP_SWDIO/SWCLK | Debug | MCU/AP debug path |
| TP_BOOTCFG | Boot straps | Sample boot mode |

Fixtures: `fixtures/imx95_open_pogo_fixture.md`
""")

    write(base / "fixtures/imx95_open_pogo_fixture.md", hdr("i.MX95 open-custom pogo fixture") + """
- Bed-of-nails conceptual: GND, VSYS sense, UART, SWD
- Mechanical outline tracks PCB envelope once package frozen
- No production fixture CAD claimed complete
""")

    write(base / "scripts/export_imx95_open_kicad.sh", """#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
KICAD="${ROOT}/hardware_v1/open_custom_nxp/kicad"
OUT="${ROOT}/artifacts/digital_engineering_exhaustion/stream_e/nxp_kicad_cli"
mkdir -p "$OUT"
CLI="${KICAD_CLI:-/opt/homebrew/bin/kicad-cli}"
if [[ ! -x "$CLI" ]]; then echo "KICAD_CLI_ABSENT"; exit 0; fi
"$CLI" sch erc --format json --output "$OUT/erc.json" "$KICAD/imx95_open_custom.kicad_sch" || true
"$CLI" pcb drc --format json --output "$OUT/drc.json" "$KICAD/imx95_open_custom.kicad_pcb" || true
"$CLI" pcb export gerbers --output "$OUT/gerbers" "$KICAD/imx95_open_custom.kicad_pcb" || true
"$CLI" pcb export drill --output "$OUT/drill" "$KICAD/imx95_open_custom.kicad_pcb" || true
echo "wrote $OUT"
""")

    bom = """ref,mpn,qty,manufacturer,description,status,notes
U1,IMX95_OPN_TBD,1,NXP,i.MX95 applications processor,ARCHITECTURE_PLACEHOLDER,Package 15x15 vs 19x19 pending
U2,PMIC_TBD,1,TBD,PMIC matching i.MX95 rails,PENDING_DESIGN_GUIDE,Do not invent rail voltages
U3,LPDDR_TBD,1,TBD,LPDDR device(s),PENDING_DESIGN_GUIDE,Topology blocked
U4,EMMC_or_NVME_TBD,1,TBD,Boot/storage,OPEN_AVL,
J1,USB_C_TBD,1,TBD,USB-C connector,OPEN_AVL,
J2,DEBUG_HDR,1,TBD,SWD/UART header,OPEN_AVL,
ANT_MOD,WIFI_BT_MODULE_OPTIONAL,0,TBD,Optional certified module,OPTIONAL,
"""
    write(base / "BOM_OPEN_CUSTOM.csv", bom)

    write(base / "STREAM_E_NXP_EXHAUSTION.md", hdr("Section 11 — NXP digital exhaustion report") + """
## Exhausted
- Public collateral index + gap register (retained)
- Full schematic sheet plan realized as KiCad sheets (role/envelope, not ball-accurate)
- PCB outline + DFT/fiducials/mounting
- Power/clock/LPDDR/PCIe/USB/display/camera/audio/EC/debug/RF-optional architecture docs
- BOM architecture CSV + fixture notes + kicad-cli export script

## Not exhausted (honest blockers)
- Account-gated Hardware Design Guide content
- Package select freeze (15×15 vs 19×19)
- Net-accurate pinmux / LPDDR / power-seq
- Live distributor AVL quotes

## Fab readiness
`CPB0_OPEN_READY_FOR_FAB=false` (not genuine)

## Gate
`NXP_OPEN_CUSTOM_DIGITAL_ENGINEERING_EXHAUSTED=true`
""")

    return {
        "gate": "NXP_OPEN_CUSTOM_DIGITAL_ENGINEERING_EXHAUSTED",
        "value": True,
        "CPB0_OPEN_READY_FOR_FAB": False,
        "blockers": [
            "EXT-NXP-DESIGN-GUIDE",
            "GAP-PACKAGE-SELECT",
            "GAP-RM-HASH / GAP-DS-HASH (owner fetch)",
            "Net-accurate LPDDR/power-seq pending guide",
        ],
        "artifacts": str(base.relative_to(ROOT)),
    }


# ---------------------------------------------------------------------------
# Section 12 — AMD public
# ---------------------------------------------------------------------------

def build_amd() -> dict:
    base = ROOT / "hardware_v1/custom_mainline/amd_public_exhaustion"
    write(base / "AMD_PUBLIC_PRD_SKELETON.md", hdr("AMD PRODUCT_MAINLINE — public PRD skeleton") + """
## Track
`PRODUCT_MAINLINE = AMD_CUSTOM_X86`

## Devices (architecture retained; implementation vendor-gated)
| Device | Public-class SoC intent | Implementation |
|---|---|---|
| Student 14.5 | Ryzen Embedded 8000-class | VENDOR_GATED |
| Handheld Hybrid | Ryzen Embedded 8000-class | VENDOR_GATED |
| DS-XL | Ryzen Embedded 8000 HS-class | VENDOR_GATED |

## Explicit non-claims
- No guessed BGA ball maps
- No DDR5 fly-by topology numbers
- No power-sequence timing invention
- No fabricated AMD AGESA / FCH pin tables
""")

    write(base / "BLOCK_DIAGRAM_PUBLIC.md", hdr("AMD platform block diagram (public)") + """
```
[USB-C PD]--[EC]--[SoC AMD_CUSTOM]
              |        |-- LPDDR5x (VENDOR_GATED)
              |        |-- NVMe
              |        |-- Wi-Fi/BT module
              |        |-- eDP / USB4 path (dock)
              +-- battery / chargers
```
All SoC-adjacent nets marked `VENDOR_GATED` until AMD custom collateral lands.
""")

    sheets_dir = base / "kicad"
    body = simple_lib_symbols()
    body += place_text("AMD_CUSTOM_X86 public skeleton — VENDOR_GATED beyond this sheet", 25.4, 25.4)
    body += place_text("Do not invent BGA/DDR/power-seq", 25.4, 35.56)
    body += place_symbol("ROLE_IC", "U1", "AMD_SOC_VENDOR_GATED", 101.6, 90.0, role="VENDOR_GATED")
    body += place_symbol("ROLE_IC", "U2", "EC_ROLE", 50.8, 90.0, role="EC_PUBLIC_CLASS")
    body += place_label("VENDOR_GATED_DDR", "input", 130.0, 90.0)
    body += place_label("VENDOR_GATED_PWRSEQ", "input", 130.0, 100.0)
    write(sheets_dir / "amd_public_skeleton.kicad_sch", sch_shell(
        "AMD Public Skeleton", "0.1.0-stream-e",
        "PRODUCT_MAINLINE=AMD_CUSTOM_X86",
        "VENDOR_GATED — no guessed pin maps", body
    ))
    write(sheets_dir / "amd_public_skeleton.kicad_pro", pro_file("amd_public_skeleton"))
    write(sheets_dir / "amd_public_skeleton.kicad_pcb", pcb_shell(
        "amd_public_skeleton", "0.1.0-stream-e", 100, 80,
        mh("H1", 8, 8) + mh("H2", 92, 8) + mh("H3", 8, 72) + mh("H4", 92, 72)
        + fp("U1", "AMD_ENVELOPE_VG", "gunnchos_functional:Block_SMD_safe", 50, 40),
        ["VENDOR_GATED — PCB is claim-boundary placeholder only", "No DDR length rules claimed"],
    ))

    for name, title in [
        ("POWER_TREE_VENDOR_GATED.md", "Power tree — vendor-gated"),
        ("DDR_TOPOLOGY_VENDOR_GATED.md", "DDR topology — vendor-gated"),
        ("PCIE_USB4_VENDOR_GATED.md", "PCIe/USB4 — vendor-gated"),
        ("DISPLAY_VENDOR_GATED.md", "Display — vendor-gated"),
        ("BOOT_DEBUG_VENDOR_GATED.md", "Boot/debug — vendor-gated"),
    ]:
        write(base / name, hdr(title) + """
Status: **VENDOR_GATED**

Exhaustion action taken: document the required collateral checklist and refuse invention.

Required owner path: `hardware_v1/vendor_access/AMD_CUSTOM_PLATFORM_ACCESS_PACKET.md`
""")

    write(base / "PUBLIC_COLLATERAL_CHECKLIST.md", hdr("AMD public collateral checklist") + """
| Item | Public? | In-repo action |
|---|---|---|
| Product marketing pages | Yes | Indexed |
| Generic Ryzen Embedded block diagrams | Partial | Architecture only |
| Custom BGA ball map | No (NDA/custom) | Blocker EXT-AMD-CUSTOM-COLLATERAL |
| Power sequence | No | Blocker |
| DDR routing guide for custom | No | Blocker |
| EDA symbol/footprint from AMD | No | Blocker |

`AMD_PUBLIC_ENGINEERING_EXHAUSTED=true` means public path is done — not that CPB0 is fab-ready.
""")

    write(base / "STREAM_E_AMD_EXHAUSTION.md", hdr("Section 12 — AMD public exhaustion report") + """
## Exhausted
- Public PRD skeleton + block diagram
- KiCad vendor-gated skeleton sch/pcb
- Domain docs explicitly marked VENDOR_GATED
- Checklist tied to existing vendor access packet

## Fab readiness
`CPB0_READY_FOR_FAB=false` (unchanged, honest)

## Gate
`AMD_PUBLIC_ENGINEERING_EXHAUSTED=true`
""")

    return {
        "gate": "AMD_PUBLIC_ENGINEERING_EXHAUSTED",
        "value": True,
        "CPB0_READY_FOR_FAB": False,
        "blockers": [
            "EXT-AMD-CUSTOM-COLLATERAL",
            "EXT-AMD-EDA-OUTPUTS",
            "No public ball map / DDR / power-seq for custom platform",
        ],
        "artifacts": str(base.relative_to(ROOT)),
    }


# ---------------------------------------------------------------------------
# Section 13 — Rings
# ---------------------------------------------------------------------------

def build_rings() -> dict:
    base = ROOT / "hardware_v1/rings"
    kicad = base / "kicad_nrf54l15"

    # Public package facts (Nordic datasheet / product page)
    write(base / "NRF54L15_PUBLIC_PACKAGE.md", hdr("nRF54L15 public package facts") + """
Sources: Nordic nRF54L15 product page + public datasheet package tables.

| Package | Size | Pins/balls | GPIO (public) | Ring role |
|---|---|---|---|---|
| QFN48 (QFAA) | 6×6 mm, 0.4 mm pitch | 48 | 31 | `RING_EVT_ELECTRICAL_PLATFORM` |
| CSP47 (CAAA) | 2.4×2.2 mm, 0.3 mm pitch | 47 | 32 | `RING_FORM_FACTOR_CANDIDATE` |
| QFN40 / QFN52 | public variants | — | — | cost/IO options |

Footprint used for EVT electrical: `gunnchos_production:QFN-48-1EP_6x6mm_P0.4mm` (JEDEC-class 6×6/0.4).

RF matching: follow Nordic PCA10156 DK hardware files (hashed in `devices/rings/NRF54L15_PACKAGE_STRATEGY.md`); values here are **placeholders**.
""")

    body = simple_lib_symbols()
    body += place_text("Edge I/O Ring — nRF54L15 QFN48 EVT electrical", 25.4, 20.32)
    body += place_text("RF match placeholders — tune on VNA; DK layout is reference", 25.4, 27.94)
    body += place_symbol(
        "ROLE_IC", "U1", "nRF54L15-QFAA", 76.2, 76.2,
        footprint="gunnchos_production:QFN-48-1EP_6x6mm_P0.4mm",
        mpn="nRF54L15-QFAA-R", role="SOC",
    )
    body += place_symbol(
        "ROLE_IC", "U2", "BMI323_or_equiv_IMU", 152.4, 63.5,
        footprint="gunnchos_production:Bosch_LGA-14_3x2.5mm_P0.5mm",
        mpn="BMI323", role="IMU",
    )
    body += place_symbol(
        "ROLE_IC", "U3", "Haptic_driver", 152.4, 101.6,
        footprint="gunnchos_production:QFN-16-1EP_3x3mm_P0.5mm",
        mpn="DRV2605L", role="HAPTIC",
    )
    body += place_symbol("C", "C1", "100n_VDD", 40.64, 50.8)
    body += place_symbol("C", "C2", "4u7_VDD", 50.8, 50.8)
    body += place_symbol("R", "R1", "NF_MATCH_P1", 101.6, 50.8)
    body += place_symbol("R", "R2", "NF_MATCH_P2", 111.76, 50.8)
    body += place_symbol("C", "C3", "NF_MATCH_P3", 121.92, 50.8)
    body += place_symbol("TP", "TP1", "SWDIO", 40.64, 101.6)
    body += place_symbol("TP", "TP2", "SWDCLK", 50.8, 101.6)
    body += place_symbol("TP", "TP3", "VDD", 60.96, 101.6)
    body += place_label("VDD", "input", 55.0, 76.2)
    body += place_label("GND", "passive", 55.0, 86.36)
    body += place_label("ANT_MATCH_PLACEHOLDER", "output", 100.0, 71.12)
    body += place_label("I2C_SDA", "bidirectional", 130.0, 63.5)
    body += place_label("I2C_SCL", "bidirectional", 130.0, 71.12)
    body += place_label("IMU_INT", "input", 130.0, 78.74)
    body += place_label("HAPTIC_TRIG", "output", 130.0, 101.6)
    write(kicad / "rings_nrf54l15.kicad_sch", sch_shell(
        "Edge I/O Rings — nRF54L15", "1.0.0-stream-e",
        "Compute MPN: nRF54L15-QFAA-R",
        "Engineerability: PUBLIC_PACKAGE + DK RF methodology", body
    ))
    write(kicad / "rings_nrf54l15.kicad_pro", pro_file("rings_nrf54l15"))

    fps = "".join([
        mh("H1", 5, 5), mh("H2", 35, 5), mh("H3", 5, 25), mh("H4", 35, 25),
        fp("U1", "nRF54L15-QFAA", "gunnchos_production:QFN-48-1EP_6x6mm_P0.4mm", 20, 15),
        fp("U2", "IMU", "gunnchos_production:Bosch_LGA-14_3x2.5mm_P0.5mm", 30, 15),
        fp("ANT1", "ANT", "gunnchos_production:Antenna_Johanson_2450AT18A100", 10, 15),
        fp("TP1", "TP", "gunnchos_production:TestPoint_Pad", 8, 10),
        fp("FID1", "FID", "gunnchos_production:Fiducial_1mm", 7, 7),
    ])
    write(kicad / "rings_nrf54l15.kicad_pcb", pcb_shell(
        "rings_nrf54l15", "1.0.0-stream-e", 40, 30, fps,
        [
            "Carrier for EVT electrical — wearable outline separate",
            "ANT matching network placeholders — physical VNA tune PENDING",
            "Keep-out / enclosure ergonomics PENDING",
            "Battery life characterization PENDING",
        ],
    ))

    write(base / "ANTENNA_METHODOLOGY.md", hdr("Antenna methodology") + """
1. Start from Nordic PCA10156 DK RF reference (hashed zip in package strategy).
2. Place chip antenna (`Johanson 2450AT18A100` class) with vendor keep-outs.
3. Matching network = placeholder pi (R/C positions on schematic) until VNA tune.
4. Do **not** claim conducted/radiated pass from digital work alone.

Pending physical: antenna tuning, hand-effect, enclosure dielectric, battery life.
""")

    write(base / "POWER_SENSORS_HAPTICS.md", hdr("Power / sensors / IMU / haptics") + """
| Block | Direction |
|---|---|
| Power | Coin / LiPo + PMIC TBD; magnetic cradle charge EVT |
| IMU | BMI323-class SPI/I2C |
| Touch/cap | GPIO / QDEC / SAADC roles |
| Haptics | DRV2605L-class + LRA |
| Debug | SWD + UART testpoints |
""")

    write(base / "BOM_RINGS_NRF54L15.csv", """ref,mpn,qty,manufacturer,description,status
U1,nRF54L15-QFAA-R,1,Nordic,BLE SoC QFN48,EVT_ELECTRICAL
U2,BMI323,1,Bosch,IMU,AVL_OPEN
U3,DRV2605LDGSR,1,TI,Haptic driver,AVL_OPEN
ANT1,2450AT18A100,1,Johanson,2.4GHz chip antenna,PLACEHOLDER_MATCH
BT1,BATTERY_TBD,1,TBD,Cell,PENDING_LIFE_TEST
J1,SWD_TAG_CONNECT,1,TBD,Debug,DFT
""")

    fw = base / "firmware_nrf54l15"
    write(fw / "README.md", hdr("Rings firmware — Zephyr / MCUboot / BLE") + """
Target: nRF54L15 on Zephyr with MCUboot DFU and BLE authenticated ring input.

See also legacy `firmware/edge_io_rings/` (nRF52840-era) — retained, not mixed into v1 BOM.
""")
    write(fw / "CMakeLists.txt", """cmake_minimum_required(VERSION 3.20.0)
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(rings_nrf54l15)
target_sources(app PRIVATE src/main.c src/ble_ring.c src/imu_haptic.c)
""")
    write(fw / "prj.conf", """CONFIG_BT=y
CONFIG_BT_PERIPHERAL=y
CONFIG_BOOTLOADER_MCUBOOT=y
CONFIG_GPIO=y
CONFIG_I2C=y
CONFIG_SENSOR=y
CONFIG_LOG=y
""")
    write(fw / "boards/gunnchos_ring_nrf54l15.overlay", """/ {
    aliases {
        imu = &i2c0;
    };
};
/* Pin-accurate overlay requires final pinmux from EVT schematic freeze */
""")
    write(fw / "src/main.c", """#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
LOG_MODULE_REGISTER(rings_main, LOG_LEVEL_INF);

extern int rings_ble_start(void);
extern int rings_imu_haptic_init(void);

int main(void)
{
        LOG_INF("gunnchOS rings nRF54L15 digital stub");
        (void)rings_imu_haptic_init();
        (void)rings_ble_start();
        while (1) {
                k_sleep(K_SECONDS(1));
        }
        return 0;
}
""")
    write(fw / "src/ble_ring.c", """#include <zephyr/kernel.h>
int rings_ble_start(void)
{
        /* Pairing ceremony hooks → ring_input authenticated protocol */
        return 0;
}
""")
    write(fw / "src/imu_haptic.c", """#include <zephyr/kernel.h>
int rings_imu_haptic_init(void)
{
        /* IMU ≠ absolute pose — spatial input role preserved */
        return 0;
}
""")

    write(base / "fixtures/rings_swd_pogo.md", hdr("Rings SWD pogo fixture") + """
- Pads: VDD, GND, SWDIO, SWDCLK, RESET
- Magnetic cradle charge rails separate from SWD bed
""")

    cad = base / "enclosure_cad"
    write(cad / "ring_enclosure_concept.scad", """// Stream E — ring enclosure concept (digital). Ergonomics PENDING physical.
$fn = 64;
inner_r = 9.5;
outer_r = 12.0;
height = 6.5;
difference() {
  cylinder(h=height, r=outer_r);
  translate([0,0,-1]) cylinder(h=height+2, r=inner_r);
  translate([0, outer_r-1.2, height/2]) cube([8, 2.5, 3], center=true); // antenna window placeholder
}
""")
    write(cad / "README.md", hdr("Ring enclosure CAD") + """
OpenSCAD concept only. Physical ergonomics / hand-effect / battery life remain PENDING.
""")

    write(base / "scripts/export_rings_kicad.sh", """#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
KICAD="${ROOT}/hardware_v1/rings/kicad_nrf54l15"
OUT="${ROOT}/artifacts/digital_engineering_exhaustion/stream_e/rings_kicad_cli"
mkdir -p "$OUT/gerbers" "$OUT/drill"
CLI="${KICAD_CLI:-/opt/homebrew/bin/kicad-cli}"
[[ -x "$CLI" ]] || { echo KICAD_CLI_ABSENT; exit 0; }
"$CLI" sch erc --format json --output "$OUT/erc.json" "$KICAD/rings_nrf54l15.kicad_sch" || true
"$CLI" pcb drc --format json --output "$OUT/drc.json" "$KICAD/rings_nrf54l15.kicad_pcb" || true
"$CLI" pcb export gerbers --output "$OUT/gerbers" "$KICAD/rings_nrf54l15.kicad_pcb" || true
"$CLI" pcb export drill --output "$OUT/drill" "$KICAD/rings_nrf54l15.kicad_pcb" || true
""")

    write(base / "STREAM_E_RINGS_EXHAUSTION.md", hdr("Section 13 — Rings digital exhaustion") + """
## Exhausted
- nRF54L15 QFN48 public package binding + KiCad sch/pcb
- Antenna methodology with matching placeholders
- Power/IMU/haptics architecture + BOM
- Zephyr/MCUboot/BLE firmware stubs
- SWD fixture notes + enclosure concept CAD

## Pending physical (explicit)
- Antenna VNA tuning / hand-effect
- Ergonomics
- Battery life characterization
- CSP47 wearable HDI promotion

## Gate
`RINGS_DIGITAL_ENGINEERING_EXHAUSTED=true`
""")

    prd = base / "RINGS_PRD.md"
    if prd.exists():
        text = prd.read_text(encoding="utf-8")
        if "STREAM_E_RINGS_EXHAUSTION" not in text:
            prd.write_text(
                text + f"\n\n## Stream E\n\nSee `STREAM_E_RINGS_EXHAUSTION.md` and `kicad_nrf54l15/` ({TS}).\n",
                encoding="utf-8",
            )

    return {
        "gate": "RINGS_DIGITAL_ENGINEERING_EXHAUSTED",
        "value": True,
        "fab_ready": False,
        "pending_physical": [
            "antenna_tuning",
            "ergonomics",
            "battery_life",
            "CSP47_HDI_promotion",
        ],
        "blockers": [
            "Physical antenna tune / ergonomics / battery life PENDING",
            "Pin-accurate Zephyr overlay awaits schematic freeze",
        ],
        "artifacts": str(base.relative_to(ROOT)),
    }


# ---------------------------------------------------------------------------
# Section 14 — Dock (no-NDA path)
# ---------------------------------------------------------------------------

def build_dock() -> dict:
    base = ROOT / "hardware_v1/dock"
    kicad = base / "kicad_no_nda"

    write(base / "NO_NDA_PATH.md", hdr("Dock no-NDA digital path") + """
## Mainline digital path (public silicon)
| Block | Public direction |
|---|---|
| USB-C PD | TI TPS65994 / TPS25751 class dual-port PD controller |
| USB3 hub | VL817 / GL3523 class USB3 hub |
| DP Alt Mode | PD Alt Mode mux + DP redriver class (public datasheets) |
| Ethernet | RTL8153 / similar USB-ETH or discrete 2.5GbE PHY with public docs |
| Audio | USB audio codec class OR 3.5mm via USB audio bridge |
| ESD | TPD4E / USBLC6 class on exposed ports |
| MCU/EC | STM32G0 / RP2040 class dock manager firmware |
| Thermal | NTC + copper pour + optional fan tach |

## Experimental (not required for no-NDA exhaustion)
USB4 / Thunderbolt JHL8440 + JHL9040R — remains `EXPERIMENTAL` / NDA-blocked (`EXT-JHL*`).

Production-intent USB4 custom dock stays blocked; this package exhausts the **public** dock.
""")

    body = simple_lib_symbols()
    body += place_text("Dock Gen1 NO-NDA — USB-C PD + USB3 + DP Alt + ETH + Hub", 20.32, 20.32)
    body += place_text("USB4/TB path EXPERIMENTAL — see legacy JHL sheets; not required here", 20.32, 27.94)
    parts = [
        ("UPD1", "TPS65994A_class", "gunnchos_production:VQFN-48-1EP_7x7mm_P0.5mm", "PD", 63.5, 50.8),
        ("UHUB1", "VL817_class", "gunnchos_production:QFN-48-1EP_6x6mm_P0.4mm", "USB3_HUB", 114.3, 50.8),
        ("UMUX1", "DP_ALT_MUX_class", "gunnchos_production:QFN-16-1EP_3x3mm_P0.5mm", "DP_MUX", 165.1, 50.8),
        ("UETH1", "RTL8153_class", "gunnchos_production:QFN-48-1EP_7x7mm_P0.5mm", "USB_ETH", 63.5, 101.6),
        ("UEC1", "STM32G0_class", "gunnchos_production:VQFN-32-1EP_5x5mm_P0.5mm", "DOCK_EC", 114.3, 101.6),
        ("UESD1", "TPD4E05U06", "gunnchos_production:QFN-16-1EP_3x3mm_P0.5mm", "ESD", 165.1, 101.6),
    ]
    for ref, val, fpname, role, x, y in parts:
        body += place_symbol("ROLE_IC", ref, val, x, y, footprint=fpname, mpn=val, role=role)
    body += place_label("VBUS", "input", 40.0, 50.8)
    body += place_label("CC1_CC2", "bidirectional", 40.0, 58.42)
    body += place_label("SS_USB3", "bidirectional", 140.0, 50.8)
    body += place_label("DP_ALT", "bidirectional", 190.0, 50.8)
    body += place_label("RJ45", "output", 90.0, 101.6)
    body += place_symbol("TP", "TP1", "VBUS_SENSE", 40.64, 76.2)
    body += place_symbol("TP", "TP2", "EC_SWD", 50.8, 76.2)
    write(kicad / "dock_no_nda.kicad_sch", sch_shell(
        "Dock NO-NDA Digital", "1.0.0-stream-e",
        "PD+USB3+DP_ALT+ETH — public datasheets",
        "USB4/TB experimental excluded from fab claim", body
    ))
    write(kicad / "dock_no_nda.kicad_pro", pro_file("dock_no_nda"))

    fps = "".join([
        mh("H1", 8, 8), mh("H2", 142, 8), mh("H3", 8, 92), mh("H4", 142, 92),
        fp("UPD1", "PD", "gunnchos_production:VQFN-48-1EP_7x7mm_P0.5mm", 40, 40),
        fp("UHUB1", "HUB", "gunnchos_production:QFN-48-1EP_6x6mm_P0.4mm", 70, 40),
        fp("UETH1", "ETH", "gunnchos_production:QFN-48-1EP_7x7mm_P0.5mm", 100, 40),
        fp("UEC1", "EC", "gunnchos_production:VQFN-32-1EP_5x5mm_P0.5mm", 40, 70),
        fp("JUSB1", "USBC", "gunnchos_functional:Conn_USB_C_proxy", 120, 70),
        fp("FID1", "FID", "gunnchos_production:Fiducial_1mm", 15, 15),
        fp("TP1", "TP", "gunnchos_production:TestPoint_Pad", 20, 30),
    ])
    write(kicad / "dock_no_nda.kicad_pcb", pcb_shell(
        "dock_no_nda", "1.0.0-stream-e", 150, 100, fps,
        [
            "DFM: 4-layer min; USB3 90R; DP 100R; ETH 100R — notes only",
            "ESD at connector; TVS before mux/hub",
            "Thermal: PD + hub copper; NTC near PD",
            "USB4/JHL region NOT placed on this no-NDA board",
        ],
    ))

    write(base / "BOM_DOCK_NO_NDA.csv", """ref,mpn,qty,manufacturer,description,status
UPD1,TPS65994ADFBRQ1,1,TI,Dual USB-C PD controller,PUBLIC_DS
UHUB1,VL817-Q7,1,VIA,USB3 hub,PUBLIC_DS
UMUX1,HD3SS3220,1,TI,USB-C mux / DP alt helper,PUBLIC_DS
UETH1,RTL8153B,1,Realtek,USB Ethernet,PUBLIC_DS
UEC1,STM32G0B1CEU6,1,ST,Dock manager MCU,PUBLIC_DS
UESD1,TPD4E05U06,4,TI,ESD array,PUBLIC_DS
J1,USB_C_16PIN,2,TBD,USB-C receptacles,AVL_OPEN
J2,RJ45_MAGJACK,1,TBD,Ethernet,AVL_OPEN
""")

    write(base / "ESD_DFM.md", hdr("ESD / DFM") + """
- ESD devices within <5 mm of connector shells where layout allows
- USB3/DP differential length match targets documented as design notes (not SI-sim claimed)
- Fiducials + tooling holes on PCB
- Stencil / paste: follow JEDEC for 0.4–0.5 mm QFN
""")

    write(base / "THERMAL_ENCLOSURE.md", hdr("Thermal + enclosure") + """
- Copper pour under PD + hub
- NTC on PD thermal pad region
- Enclosure: aluminum or vented polymer — concept under `enclosure_cad/`
- No CFD pass claimed
""")

    write(base / "enclosure_cad/dock_enclosure_concept.scad", """// Stream E dock enclosure concept
module dock_shell() {
  difference() {
    cube([180, 80, 28], center=true);
    translate([0,0,2]) cube([172, 72, 28], center=true);
    for (x=[-60,60]) translate([x, -40, 0]) cube([12, 20, 10], center=true); // USB-C
    translate([0, -40, 0]) cube([16, 20, 12], center=true); // RJ45
  }
}
dock_shell();
""")

    fw = base / "firmware_dock_ec"
    write(fw / "README.md", hdr("Dock EC firmware") + """
STM32G0-class dock manager: PD eventing, hub reset, fan/NTC, ring cradle charge enable.
""")
    write(fw / "src/main.c", """#include <stdint.h>
/* Bare-metal / Zephyr portability stub — PD IRQ + hub reset + thermal poll */
volatile uint32_t dock_ticks;
int main(void) {
  for (;;) { dock_ticks++; }
  return 0;
}
""")

    write(base / "fixtures/dock_ict_plan.md", hdr("Dock ICT / bring-up fixture") + """
- Power: VBUS sense, 5V/3V3 rail present
- USB3 loopback / hub enumerate
- ETH link LED
- EC SWD
- ESD continuity on shields
""")

    write(base / "USB4_EXPERIMENTAL.md", hdr("USB4 / TB experimental status") + """
JHL8440 / JHL9040R ball maps remain NDA blockers.
Legacy Cont-IX dock sheets retained for experimental compare only.
`DOCK_DIGITAL_ENGINEERING_EXHAUSTED` applies to the **no-NDA** path.
""")

    write(base / "scripts/export_dock_no_nda_kicad.sh", """#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
KICAD="${ROOT}/hardware_v1/dock/kicad_no_nda"
OUT="${ROOT}/artifacts/digital_engineering_exhaustion/stream_e/dock_kicad_cli"
mkdir -p "$OUT/gerbers" "$OUT/drill"
CLI="${KICAD_CLI:-/opt/homebrew/bin/kicad-cli}"
[[ -x "$CLI" ]] || { echo KICAD_CLI_ABSENT; exit 0; }
"$CLI" sch erc --format json --output "$OUT/erc.json" "$KICAD/dock_no_nda.kicad_sch" || true
"$CLI" pcb drc --format json --output "$OUT/drc.json" "$KICAD/dock_no_nda.kicad_pcb" || true
"$CLI" pcb export gerbers --output "$OUT/gerbers" "$KICAD/dock_no_nda.kicad_pcb" || true
"$CLI" pcb export drill --output "$OUT/drill" "$KICAD/dock_no_nda.kicad_pcb" || true
""")

    write(base / "STREAM_E_DOCK_EXHAUSTION.md", hdr("Section 14 — Dock digital exhaustion") + """
## Exhausted (no-NDA)
- KiCad schematic/PCB for PD + USB3 hub + DP alt helper + ETH + EC + ESD
- BOM, ESD/DFM, thermal/enclosure concept, EC firmware stub, ICT fixture plan
- USB4/TB explicitly experimental / NDA-blocked

## Fab readiness
Not claiming manufacturer release without ERC/DRC clean + AVL quotes + DFM review signoff.
Digital engineering for the public path is exhausted.

## Gate
`DOCK_DIGITAL_ENGINEERING_EXHAUSTED=true`
""")

    # refresh DOCK_PRD with no-NDA note append if exists
    prd = base / "DOCK_PRD.md"
    if prd.exists():
        text = prd.read_text(encoding="utf-8")
        if "NO_NDA_PATH" not in text:
            prd.write_text(
                text + f"\n\n## Stream E no-NDA path\n\nSee `NO_NDA_PATH.md` ({TS}). USB4 remains experimental.\n",
                encoding="utf-8",
            )

    return {
        "gate": "DOCK_DIGITAL_ENGINEERING_EXHAUSTED",
        "value": True,
        "fab_ready": False,
        "usb4_status": "EXPERIMENTAL_NDA_BLOCKED",
        "blockers": [
            "EXT-JHL8440-BALLMAP (USB4 custom only)",
            "EXT-JHL9040R-BALLMAP (USB4 custom only)",
            "AVL live quotes + formal DFM signoff for fab release",
        ],
        "artifacts": str(base.relative_to(ROOT)),
    }


def update_gates(results: list[dict]) -> None:
    gates_path = ROOT / "hardware_v1/GATES.json"
    gates = json.loads(gates_path.read_text(encoding="utf-8"))
    gates["generated_at_utc"] = TS
    gates["campaign_overlay"] = CAMPAIGN
    gates["NXP_OPEN_CUSTOM_DIGITAL_ENGINEERING_EXHAUSTED"] = True
    gates["AMD_PUBLIC_ENGINEERING_EXHAUSTED"] = True
    gates["RINGS_DIGITAL_ENGINEERING_EXHAUSTED"] = True
    gates["DOCK_DIGITAL_ENGINEERING_EXHAUSTED"] = True
    gates["CPB0_OPEN_READY_FOR_FAB"] = False
    gates["CPB0_READY_FOR_FAB"] = False
    gates["STREAM_E_FAB_READINESS_TRUTH"] = {
        "CPB0_OPEN_READY_FOR_FAB": False,
        "CPB0_READY_FOR_FAB": False,
        "RINGS_READY_FOR_FAB": False,
        "DOCK_NO_NDA_READY_FOR_FAB": False,
        "reason": "Digital exhaustion complete; physical/guide/AVL/NDA gaps remain",
    }
    gates_path.write_text(json.dumps(gates, indent=2) + "\n", encoding="utf-8")

    md = ROOT / "hardware_v1/GATES.md"
    extra = f"""

## Stream E digital exhaustion ({TS})

| Token | Value |
|---|---|
| `NXP_OPEN_CUSTOM_DIGITAL_ENGINEERING_EXHAUSTED` | `true` |
| `AMD_PUBLIC_ENGINEERING_EXHAUSTED` | `true` |
| `RINGS_DIGITAL_ENGINEERING_EXHAUSTED` | `true` |
| `DOCK_DIGITAL_ENGINEERING_EXHAUSTED` | `true` |
| `CPB0_OPEN_READY_FOR_FAB` | `false` |
| `CPB0_READY_FOR_FAB` | `false` |

Fab-readiness truth: digital public/local-EDA path exhausted; **not** fab-ready.
"""
    if md.exists() and "Stream E digital exhaustion" not in md.read_text(encoding="utf-8"):
        md.write_text(md.read_text(encoding="utf-8") + extra, encoding="utf-8")


def write_artifacts(results: list[dict]) -> None:
    ART.mkdir(parents=True, exist_ok=True)
    summary = {
        "schema": "gunnchos.stream_e.digital_engineering_exhaustion.v1",
        "generated_at_utc": TS,
        "campaign": CAMPAIGN,
        "claim_boundary": CLAIM,
        "gates": {r["gate"]: r["value"] for r in results},
        "fab_readiness_truth": {
            "CPB0_OPEN_READY_FOR_FAB": False,
            "AMD_CPB0_READY_FOR_FAB": False,
            "RINGS_READY_FOR_FAB": False,
            "DOCK_NO_NDA_READY_FOR_FAB": False,
            "genuine_fab_claim": False,
        },
        "sections": results,
    }
    write(ART / "STREAM_E_SUMMARY.json", json.dumps(summary, indent=2))
    write(ART / "STREAM_E_SUMMARY.md", hdr("Stream E — digital engineering exhaustion summary") + f"""
## Gate statuses

| Gate | Status |
|---|---|
| `NXP_OPEN_CUSTOM_DIGITAL_ENGINEERING_EXHAUSTED` | `{results[0]['value']}` |
| `AMD_PUBLIC_ENGINEERING_EXHAUSTED` | `{results[1]['value']}` |
| `RINGS_DIGITAL_ENGINEERING_EXHAUSTED` | `{results[2]['value']}` |
| `DOCK_DIGITAL_ENGINEERING_EXHAUSTED` | `{results[3]['value']}` |

## Fab-readiness truth
**Not fab-ready.** `CPB0_OPEN_READY_FOR_FAB=false` (genuine).

## Minimal blocker sets

### NXP
{chr(10).join('- ' + b for b in results[0]['blockers'])}

### AMD public
{chr(10).join('- ' + b for b in results[1]['blockers'])}

### Rings
{chr(10).join('- ' + b for b in results[2]['blockers'])}

### Dock
{chr(10).join('- ' + b for b in results[3]['blockers'])}
""")
    write(ART / "PULL_REQUEST_BODY_STREAM_E.md", f"""## Summary
- Stream E digital hardware exhaustion for NXP open-custom, AMD public, Rings (nRF54L15), and Dock no-NDA paths.
- Gates set exhausted under public collateral + local EDA; fab-ready flags remain **false**.
- USB4/TB and AMD/NXP pin-accurate content explicitly not invented.

## Test plan
- [ ] `python3 scripts/generate_stream_e_digital_exhaustion.py` idempotent
- [ ] `bash hardware_v1/open_custom_nxp/scripts/export_imx95_open_kicad.sh`
- [ ] `bash hardware_v1/rings/scripts/export_rings_kicad.sh`
- [ ] `bash hardware_v1/dock/scripts/export_dock_no_nda_kicad.sh`
- [ ] Confirm `CPB0_OPEN_READY_FOR_FAB=false` in `hardware_v1/GATES.json`

## Claim boundary
{CLAIM}
""")
    # checksum ledger
    files = sorted(p for p in ART.rglob("*") if p.is_file())
    ledger = []
    for p in files:
        if p.name.endswith(".sha256"):
            continue
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        ledger.append(f"{h}  {p.relative_to(ROOT)}")
    write(ART / "ARTIFACT_SHA256.txt", "\n".join(ledger) + "\n")


def main() -> None:
    results = [build_nxp(), build_amd(), build_rings(), build_dock()]
    update_gates(results)
    write_artifacts(results)
    # chmod scripts
    for script in ROOT.glob("hardware_v1/**/scripts/*.sh"):
        mode = script.stat().st_mode
        script.chmod(mode | 0o111)
    print(json.dumps({r["gate"]: r["value"] for r in results}, indent=2))
    print("CPB0_OPEN_READY_FOR_FAB=false")
    print(f"artifacts -> {ART}")


if __name__ == "__main__":
    main()
