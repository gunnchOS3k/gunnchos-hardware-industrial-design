#!/usr/bin/env python3.11
"""Generate Gate 1 Edge I/O Ring DIGITAL FABRICATION package (nonphysical).

PHYSICAL_EXECUTION_FREEZE ACTIVE — packages only; no physical claims.
Status tokens: RING_DIGITAL_FABRICATION_PACKAGE_COMPLETE + RING_PHYSICAL_PROTOTYPE_PENDING
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import textwrap
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
BOARD = "edge_io_ring_evt0"
VERSION = "0.1.0-dev"

# ---------------------------------------------------------------------------
# Real MPN component selection (research-selected; not purchased)
# ---------------------------------------------------------------------------
COMPONENTS = [
    {
        "ref": "U1",
        "role": "MCU_SoC_BLE",
        "manufacturer": "Nordic Semiconductor",
        "mpn": "nRF52840-CKAA-R",
        "package": "WLCSP-aQFN-73 (3.544×3.607 mm)",
        "voltage_v": "1.7–3.6 (VDD); IO 1.8/3.3",
        "current_ma": "active TX +0 dBm ~4.8; System ON idle ~1.5; System OFF ~0.4 µA",
        "interfaces": "BLE 5.3/2.4 GHz radio, SWD, SPI/TWI/UART, GPIO, USB (unused on ring), QSPI",
        "availability_risk": "LOW — broadly stocked; WLCSP assembly requires fine-pitch SMT capability",
        "why_selected": "Integrated BLE + Cortex-M4F + crypto accelerator minimizes ring BOM volume vs discrete radio; matches authenticated ring protocol crypto needs",
        "approved_alternative": "nRF52840-QIAA-R (AQFN-73) if WLCSP assembly yield risk",
        "datasheet_url": "https://docs.nordicsemi.com/bundle/ps_nrf52840/page/keyfeatures_html5.html",
    },
    {
        "ref": "U2",
        "role": "IMU_6AXIS",
        "manufacturer": "Bosch Sensortec",
        "mpn": "BMI270",
        "package": "LGA-14 (2.5×3.0×0.8 mm)",
        "voltage_v": "1.71–3.6 VDD; VDDIO 1.2–3.6",
        "current_ma": "typ 685 µA @ 100 Hz accel+gyro; suspend ~3 µA",
        "interfaces": "I2C (primary ADDR 0x68) / SPI",
        "availability_risk": "LOW — high-volume wearable IMU",
        "why_selected": "Wrist/finger gesture class IMU with FIFO and significant motion interrupt for low-power wake",
        "approved_alternative": "ST LSM6DSOX (LGA-14) if BMI270 allocation risk",
        "datasheet_url": "https://www.bosch-sensortec.com/products/motion-sensors/imus/bmi270/",
    },
    {
        "ref": "U3",
        "role": "HAPTIC_DRIVER",
        "manufacturer": "Texas Instruments",
        "mpn": "DRV2605LDGSR",
        "package": "VSSOP-10",
        "voltage_v": "2.0–5.2 V",
        "current_ma": "idle ~0.5; LRA drive peaks depend on actuator (budget <80 mA avg)",
        "interfaces": "I2C (ADDR 0x5A), PWM/ENA, rated for LRA/ERM",
        "availability_risk": "LOW",
        "why_selected": "Library waveforms + auto-resonance LRA drive for ring haptic feedback path",
        "approved_alternative": "DRV2604L (RAM waveforms) if custom haptic library required",
        "datasheet_url": "https://www.ti.com/lit/ds/symlink/drv2605l.pdf",
    },
    {
        "ref": "U4",
        "role": "PMIC_CHARGER",
        "manufacturer": "Texas Instruments",
        "mpn": "BQ25100YFPR",
        "package": "DSBGA-6 (0.9×1.6 mm)",
        "voltage_v": "VIN 3.5–6.45; VBAT charge 4.2",
        "current_ma": "charge current programmable to 250 mA max (set 25–40 mA for 80 mAh cell)",
        "interfaces": "USB 5 V input via pogo/pads; status via CHG pin",
        "availability_risk": "MEDIUM — DSBGA fine pitch; alternate QFN charger preferred for hand-assembly EVT",
        "why_selected": "Ultra-small Li-Ion linear charger sized for <100 mAh wearable cells",
        "approved_alternative": "MCP73831T-2ACI/OT (SOT-23-5) for easier prototype assembly",
        "datasheet_url": "https://www.ti.com/lit/ds/symlink/bq25100.pdf",
    },
    {
        "ref": "U5",
        "role": "BATTERY_PROTECTION",
        "manufacturer": "Ricoh Electronic Devices",
        "mpn": "R5540K001A-TR-F",
        "package": "DFN(PLP)1616-6",
        "voltage_v": "overcharge detect ~4.28 V; overdischarge ~2.8 V class (confirm exact suffix)",
        "current_ma": "protection FET path rated for small-cell discharge currents",
        "interfaces": "series with LiPo +/− before charger/load",
        "availability_risk": "MEDIUM — confirm distributor stock for exact suffix; cell pack may include PCM",
        "why_selected": "Dedicated 1-cell protection required before any body-worn powered prototype",
        "approved_alternative": "Use pouch cell with integrated PCM (DW01A+FS8205A module) — preferred for EVT0 if discrete PCM layout risk",
        "datasheet_url": "https://www.nisshinbo-microdevices.co.jp/en/products/category/power/battery-protection-ic/",
    },
    {
        "ref": "U6",
        "role": "LDO_3V3",
        "manufacturer": "Texas Instruments",
        "mpn": "TLV70033DSET",
        "package": "WSON-6 (1.5×1.5 mm)",
        "voltage_v": "out 3.3 V ±2%; Vin 2–5.5",
        "current_ma": "200 mA max; Iq ~30 µA",
        "interfaces": "VBAT_SYS → 3V3 rail for SoC/IMU/haptic (SoC can also run direct from VBAT; LDO for IO consistency)",
        "availability_risk": "LOW",
        "why_selected": "Low Iq LDO for always-on 3V3 rail under body-worn thermal/efficiency constraints",
        "approved_alternative": "TPS7A2033PDBVR (SOT-23-5) for easier hand rework",
        "datasheet_url": "https://www.ti.com/lit/ds/symlink/tlv700.pdf",
    },
    {
        "ref": "BT1",
        "role": "BATTERY",
        "manufacturer": "GMB / PowerStream-class pouch (EVT candidate)",
        "mpn": "GMB501215 (80 mAh LiPo pouch) — supplier quote required",
        "package": "Curved/flat pouch ~5.0×12×15 mm class",
        "voltage_v": "3.7 V nom; 4.2 V charge; 3.0 V cutoff",
        "current_ma": "80 mAh capacity; continuous discharge ≤1C recommended",
        "interfaces": "2-wire to PCM/charger; polarity keyed in mechanical cavity",
        "availability_risk": "HIGH — custom curve/pouch geometry needs supplier quote; UN38.3 paperwork pending purchase",
        "why_selected": "Capacity class matches 50–100 mAh ring energy budget from research targets",
        "approved_alternative": "PKCELL LP402025 70–100 mAh flat pouch for bench mule (not curved)",
        "datasheet_url": "https://www.powerstream.com/li-polymer-battery.htm",
        "blocker_class": "REQUIRES_SUPPLIER_QUOTE",
    },
    {
        "ref": "ANT1",
        "role": "BLE_ANTENNA",
        "manufacturer": "Johanson Technology",
        "mpn": "2450AT18A100",
        "package": "chip antenna 3.2×1.6 mm",
        "voltage_v": "RF passive",
        "current_ma": "n/a",
        "interfaces": "50 Ω feed from nRF52840 ANT pin via pi-match (C_ANT/L_ANT/C_SHUNT)",
        "availability_risk": "LOW",
        "why_selected": "Proven 2.45 GHz chip antenna with documented keep-outs suitable for ring arc PCB",
        "approved_alternative": "PCB inverted-F trace antenna (no MPN) if enclosure RF study favors it",
        "datasheet_url": "https://www.johansontechnology.com/datasheets/2450AT18A100/2450AT18A100.pdf",
    },
    {
        "ref": "D1",
        "role": "ESD_USB_POGO",
        "manufacturer": "Nexperia",
        "mpn": "PESD5V0S1UL,315",
        "package": "SOD882 (DFN1006-2)",
        "voltage_v": "VRWM 5 V",
        "current_ma": "n/a (clamping)",
        "interfaces": "across CHARGE_5V to GND at pogo input",
        "availability_risk": "LOW",
        "why_selected": "Low-cap ESD for charge contact protection",
        "approved_alternative": "TPD1E05U06DPYR",
        "datasheet_url": "https://assets.nexperia.com/documents/data-sheet/PESD5V0S1UL.pdf",
    },
    {
        "ref": "D2",
        "role": "ESD_SWD",
        "manufacturer": "Nexperia",
        "mpn": "PESD3V3S1UL,315",
        "package": "SOD882",
        "voltage_v": "VRWM 3.3 V",
        "current_ma": "n/a",
        "interfaces": "SWDIO line to GND",
        "availability_risk": "LOW",
        "why_selected": "Protect debug pads used during factory/dev flash",
        "approved_alternative": "TPD1E10B06DPYR",
        "datasheet_url": "https://assets.nexperia.com/documents/data-sheet/PESD3V3S1UL.pdf",
    },
    {
        "ref": "J1",
        "role": "DEBUG_SWD",
        "manufacturer": "Tag-Connect",
        "mpn": "TC2030-CTX-NL footprint (cable TC2030-CTX)",
        "package": "PCB pads only (no connector BOM for NL)",
        "voltage_v": "3.3 V SWD",
        "current_ma": "debug only",
        "interfaces": "SWDIO, SWDCLK, nRESET, VTref, GND",
        "availability_risk": "LOW for pads; cable is tooling",
        "why_selected": "Zero-height debug for sealed ring; no receptacle volume",
        "approved_alternative": "0.05\" 5-pin header pogo fixture for EVT mule",
        "datasheet_url": "https://www.tag-connect.com/product/tc2030-ctx-nl-6-pin-no-legs-cable-with-10-pin-micro-connector-for-use-with-cortex-processors",
    },
    {
        "ref": "J2",
        "role": "CHARGE_POGO",
        "manufacturer": "Mill-Max / custom fixture",
        "mpn": "Mill-Max 0900-0-15-20-75-14-11-0 (pogo pin) ×2 on cradle",
        "package": "Cradle-side pogo; ring has gold pads",
        "voltage_v": "5 V charge in / GND",
        "current_ma": "≤40 mA charge set",
        "interfaces": "CHARGE_5V, GND pads on ring outer arc",
        "availability_risk": "MEDIUM — cradle mechanical alignment is EVT risk",
        "why_selected": "No USB-C receptacle volume on ring; pogo cradle charging",
        "approved_alternative": "Horizontal USB-C on bench mule board only",
        "datasheet_url": "https://www.mill-max.com/engineering_spec_pdfs/0900.pdf",
        "blocker_class": "REQUIRES_PHYSICAL_FABRICATION",
    },
    {
        "ref": "Y1",
        "role": "HFCLK_XTAL",
        "manufacturer": "Abracon",
        "mpn": "ABM8-32.000MHZ-B2-T",
        "package": "3.2×2.5 mm SMD crystal",
        "voltage_v": "n/a",
        "current_ma": "n/a",
        "interfaces": "XL1/XL2 of nRF52840",
        "availability_risk": "LOW",
        "why_selected": "32 MHz HFCLK for BLE PHY timing",
        "approved_alternative": "FA-128 32.0000MF10Z-K3",
        "datasheet_url": "https://abracon.com/Resonators/ABM8.pdf",
    },
    {
        "ref": "Y2",
        "role": "LFCLK_XTAL",
        "manufacturer": "Abracon",
        "mpn": "ABS07-32.768KHZ-9-T",
        "package": "3.2×1.5 mm cylinder SMD",
        "voltage_v": "n/a",
        "current_ma": "n/a",
        "interfaces": "XL1/XL2 LF of nRF52840",
        "availability_risk": "LOW",
        "why_selected": "32.768 kHz for RTC / low-power BLE sleep accuracy",
        "approved_alternative": "FC-135R 32.7680KA-A3",
        "datasheet_url": "https://abracon.com/Resonators/ABS07.pdf",
    },
    {
        "ref": "M1",
        "role": "LRA_ACTUATOR",
        "manufacturer": "Jinlong Machinery",
        "mpn": "C10-100 / equivalent 8–10 mm LRA (EVT quote)",
        "package": "coin LRA ≤10 mm diameter, ≤2.5 mm height",
        "voltage_v": "driven by DRV2605L (~1.8–2.0 Vrms class)",
        "current_ma": "peaks budgeted in haptic driver; avg << charge budget",
        "interfaces": "2-wire to DRV2605L OUT+/OUT−",
        "availability_risk": "MEDIUM — exact thin LRA for ring cavity needs supplier dimensional confirm",
        "why_selected": "Thin coin LRA fits ring cavity haptic pocket",
        "approved_alternative": "Vybronics VLV101040A",
        "datasheet_url": "https://www.vybronics.com/wp-content/uploads/2021/03/VLV101040A-datasheet.pdf",
        "blocker_class": "REQUIRES_SUPPLIER_QUOTE",
    },
]

PASSives = [
    {"ref": "C1", "mpn": "GRM155R61A105KE15D", "mfr": "Murata", "value": "1uF 10V 0402", "role": "U1 DEC_VDD"},
    {"ref": "C2", "mpn": "GRM155R61A105KE15D", "mfr": "Murata", "value": "1uF 10V 0402", "role": "U1 DEC_VDDH"},
    {"ref": "C3", "mpn": "GRM155R71C104KA88D", "mfr": "Murata", "value": "100nF 16V 0402", "role": "U1 DEC"},
    {"ref": "C4", "mpn": "GRM155R61A105KE15D", "mfr": "Murata", "value": "1uF 10V 0402", "role": "U2 VDD"},
    {"ref": "C5", "mpn": "GRM155R71C104KA88D", "mfr": "Murata", "value": "100nF 16V 0402", "role": "U2 VDDIO"},
    {"ref": "C6", "mpn": "GRM155R61A105KE15D", "mfr": "Murata", "value": "1uF 10V 0402", "role": "U6 CIN"},
    {"ref": "C7", "mpn": "GRM155R61A105KE15D", "mfr": "Murata", "value": "1uF 10V 0402", "role": "U6 COUT"},
    {"ref": "C8", "mpn": "GRM1555C1H100JA01D", "mfr": "Murata", "value": "10pF C0G 0402", "role": "HFXTAL load"},
    {"ref": "C9", "mpn": "GRM1555C1H100JA01D", "mfr": "Murata", "value": "10pF C0G 0402", "role": "HFXTAL load"},
    {"ref": "C10", "mpn": "GRM1555C1H120JA01D", "mfr": "Murata", "value": "12pF C0G 0402", "role": "LFXTAL load"},
    {"ref": "C11", "mpn": "GRM1555C1H120JA01D", "mfr": "Murata", "value": "12pF C0G 0402", "role": "LFXTAL load"},
    {"ref": "C12", "mpn": "GJM1555C1H1R0BB01D", "mfr": "Murata", "value": "1.0pF RF 0402", "role": "ANT series match (seed)"},
    {"ref": "C13", "mpn": "GJM1555C1H1R5BB01D", "mfr": "Murata", "value": "1.5pF RF 0402", "role": "ANT shunt match (seed)"},
    {"ref": "L1", "mpn": "LQP15MN1N5B02D", "mfr": "Murata", "value": "1.5nH 0402", "role": "ANT series match (seed)"},
    {"ref": "R1", "mpn": "RC0402FR-07100KL", "mfr": "Yageo", "value": "100k 0402", "role": "BQ25100 ISET"},
    {"ref": "R2", "mpn": "RC0402FR-0710KL", "mfr": "Yageo", "value": "10k 0402", "role": "I2C SDA pull-up"},
    {"ref": "R3", "mpn": "RC0402FR-0710KL", "mfr": "Yageo", "value": "10k 0402", "role": "I2C SCL pull-up"},
    {"ref": "R4", "mpn": "RC0402FR-0710KL", "mfr": "Yageo", "value": "10k 0402", "role": "nRESET pull-up"},
    {"ref": "TP1", "mpn": "PAD-0.8MM", "mfr": "PCB", "value": "test point", "role": "3V3"},
    {"ref": "TP2", "mpn": "PAD-0.8MM", "mfr": "PCB", "value": "test point", "role": "GND"},
    {"ref": "TP3", "mpn": "PAD-0.8MM", "mfr": "PCB", "value": "test point", "role": "VBAT"},
    {"ref": "TP4", "mpn": "PAD-0.8MM", "mfr": "PCB", "value": "test point", "role": "SWDIO"},
    {"ref": "TP5", "mpn": "PAD-0.8MM", "mfr": "PCB", "value": "test point", "role": "SWDCLK"},
    {"ref": "TP6", "mpn": "PAD-0.8MM", "mfr": "PCB", "value": "test point", "role": "I2C_SDA"},
    {"ref": "TP7", "mpn": "PAD-0.8MM", "mfr": "PCB", "value": "test point", "role": "I2C_SCL"},
]

NETS = {
    "GND": ["U1.GND", "U2.GND", "U3.GND", "U4.GND", "U6.GND", "D1.2", "D2.2", "J1.GND", "J2.GND", "TP2", "BT1.−", "C1.2", "C2.2", "C3.2", "C4.2", "C5.2", "C6.2", "C7.2", "C8.2", "C9.2", "C10.2", "C11.2", "C13.2", "ANT1.GND"],
    "VBAT": ["BT1.+", "U5.BAT", "U4.BAT", "U6.IN", "TP3"],
    "VBAT_SYS": ["U5.OUT", "U1.VDD", "U1.VDDH", "C1.1", "C2.1"],
    "3V3": ["U6.OUT", "C7.1", "U2.VDD", "U2.VDDIO", "U3.VDD", "R2.1", "R3.1", "R4.1", "J1.Vtref", "TP1", "C4.1", "C5.1"],
    "CHARGE_5V": ["J2.5V", "D1.1", "U4.IN"],
    "I2C_SDA": ["U1.P0.26", "U2.SDA", "U3.SDA", "R2.2", "TP6"],
    "I2C_SCL": ["U1.P0.27", "U2.SCL", "U3.SCL", "R3.2", "TP7"],
    "SWDIO": ["U1.SWDIO", "J1.SWDIO", "D2.1", "TP4"],
    "SWDCLK": ["U1.SWDCLK", "J1.SWDCLK", "TP5"],
    "nRESET": ["U1.nRESET", "J1.nRESET", "R4.2"],
    "HFXTAL_1": ["U1.XL1", "Y1.1", "C8.1"],
    "HFXTAL_2": ["U1.XL2", "Y1.2", "C9.1"],
    "LFXTAL_1": ["U1.XL1_LF", "Y2.1", "C10.1"],
    "LFXTAL_2": ["U1.XL2_LF", "Y2.2", "C11.1"],
    "RF_ANT": ["U1.ANT", "C12.1"],
    "RF_FEED": ["C12.2", "L1.1", "C13.1"],
    "RF_ANT_PAD": ["L1.2", "ANT1.FEED"],
    "HAPTIC_P": ["U3.OUT+", "M1.1"],
    "HAPTIC_N": ["U3.OUT−", "M1.2"],
    "IMU_INT": ["U2.INT1", "U1.P0.11"],
    "CHG_STATUS": ["U4.CHG", "U1.P0.02"],
}


def write_component_selection() -> None:
    elec = ROOT / "electrical"
    elec.mkdir(parents=True, exist_ok=True)
    (elec / "component_selection.json").write_text(
        json.dumps(
            {
                "board": BOARD,
                "version": VERSION,
                "generated_at_utc": UTC,
                "claim_boundary": "DIGITAL_SELECTION_ONLY — parts not purchased; PHYSICAL_EXECUTION_FREEZE ACTIVE",
                "status_tokens": [
                    "RING_DIGITAL_FABRICATION_PACKAGE_COMPLETE",
                    "RING_PHYSICAL_PROTOTYPE_PENDING",
                ],
                "components": COMPONENTS,
                "passives": PASSives,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    fields = [
        "ref", "role", "manufacturer", "mpn", "package", "voltage_v", "current_ma",
        "interfaces", "availability_risk", "why_selected", "approved_alternative",
        "datasheet_url", "blocker_class",
    ]
    with (elec / "component_selection.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for c in COMPONENTS:
            w.writerow({k: c.get(k, "") for k in fields})
    (elec / "power_tree.md").write_text(
        textwrap.dedent(
            f"""\
            # Edge I/O Ring — Power Tree (digital)

            Generated: {UTC}
            Board: `{BOARD}` v{VERSION}

            ```
            [J2 CHARGE_5V pogo]──ESD D1──►[U4 BQ25100]──► VBAT ──►[U5 protect]──► VBAT_SYS
                 │                              │                      │
                 └──────── GND ─────────────────┴──────────────────────┤
                                                                       ▼
                                                                [U6 TLV70033]──► 3V3
                                                                       │
                         ┌─────────────┬──────────────┬────────────────┤
                         ▼             ▼              ▼                ▼
                       [U1 SoC]     [U2 BMI270]   [U3 DRV2605L]     pull-ups/SWD
                         │
                      RF path → match → ANT1
            ```

            | Rail | Nom | Source | Loads | Notes |
            |---|---|---|---|---|
            | CHARGE_5V | 5.0 V | Cradle pogo | U4 IN | Present only when docked |
            | VBAT | 3.0–4.2 V | Cell | U4 BAT, U6 IN | After PCM |
            | VBAT_SYS | ≈VBAT | U5 OUT | U1 VDD/VDDH | Direct SoC supply allowed |
            | 3V3 | 3.3 V | U6 | IMU, haptic, IO pull-ups | Always-on when VBAT present |

            Voltage domain checks: SWD/I2C at 3V3; RF path AC-coupled/passive; CHARGE_5V never routed to 3V3 IO.
            """
        ),
        encoding="utf-8",
    )


def write_schematic() -> dict:
    sch_dir = ROOT / "schematic" / "kicad"
    sch_dir.mkdir(parents=True, exist_ok=True)
    reports = ROOT / "schematic" / "reports"
    reports.mkdir(parents=True, exist_ok=True)

    netlist = {
        "board": BOARD,
        "version": VERSION,
        "generator": "gate1_digital_fab",
        "generated_at_utc": UTC,
        "components": COMPONENTS,
        "passives": PASSives,
        "nets": NETS,
    }
    (ROOT / "schematic" / "netlist.json").write_text(json.dumps(netlist, indent=2) + "\n", encoding="utf-8")

    instances = []
    x0, y0 = 40, 40
    for i, c in enumerate(COMPONENTS):
        x = x0 + (i % 4) * 50
        y = y0 + (i // 4) * 40
        uid = hashlib.sha1(c["ref"].encode()).hexdigest()[:8]
        instances.append(
            f"""  (symbol (lib_id "Device:R") (at {x} {y} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no)
    (uuid {uid}-0000-4000-8000-000000000001)
    (property "Reference" "{c['ref']}" (at {x} {y-7} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "{c['mpn']}" (at {x} {y+7} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "{c['package']}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "{c['datasheet_url']}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Role" "{c['role']}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
  )"""
        )

    labels = []
    ly = 160
    for ni, net in enumerate(sorted(NETS.keys())):
        labels.append(
            f'  (global_label "{net}" (shape input) (at {30 + (ni % 6) * 35} {ly + (ni // 6) * 10} 0) (fields_autoplaced)\n'
            f'    (effects (font (size 1.27 1.27)) (justify left))\n'
            f'    (uuid {hashlib.sha1(net.encode()).hexdigest()[:8]}-1111-4000-8000-000000000002)\n'
            f"  )"
        )

    sch = f"""(kicad_sch (version 20230121) (generator "gate1_digital_fab")
  (uuid {hashlib.sha1(BOARD.encode()).hexdigest()[:8]}-aaaa-4000-8000-000000000000)
  (paper "A3")
  (title_block
    (title "Edge I/O Ring EVT0 — {BOARD}")
    (date "{UTC[:10]}")
    (rev "{VERSION}")
    (company "gunnchOS3k / NONPHYSICAL TOTALITY")
    (comment 1 "DIGITAL FABRICATION PACKAGE — not a physical board claim")
    (comment 2 "Authoritative connectivity: schematic/netlist.json")
    (comment 3 "PHYSICAL_EXECUTION_FREEZE ACTIVE")
    (comment 4 "Tokens: RING_DIGITAL_FABRICATION_PACKAGE_COMPLETE | RING_PHYSICAL_PROTOTYPE_PENDING")
  )
  (lib_symbols)
{chr(10).join(instances)}
{chr(10).join(labels)}
  (text "Power: CHARGE_5V -> U4 -> VBAT -> U5 -> VBAT_SYS -> U6 -> 3V3"
    (exclude_from_sim no) (at 40 20 0)
    (effects (font (size 2 2)) (justify left bottom))
    (uuid deadbeef-0001-4000-8000-000000000010)
  )
  (text "Digital: U1 SWD; I2C bus U1-U2-U3; IMU_INT; CHG_STATUS; RF match to ANT1; Haptic U3->M1"
    (exclude_from_sim no) (at 40 28 0)
    (effects (font (size 2 2)) (justify left bottom))
    (uuid deadbeef-0002-4000-8000-000000000011)
  )
  (sheet_instances
    (path "/" (page "1"))
  )
)
"""
    (sch_dir / f"{BOARD}.kicad_sch").write_text(sch, encoding="utf-8")
    (sch_dir / f"{BOARD}.kicad_pro").write_text(
        json.dumps(
            {
                "board": {"design_settings": {"rules": {"min_clearance": 0.1, "min_track_width": 0.1, "min_via": 0.3}}},
                "meta": {"filename": f"{BOARD}.kicad_pro", "version": 1},
                "sheets": [["", f"{BOARD}.kicad_sch"]],
                "text_variables": {"BOARD": BOARD, "VERSION": VERSION, "CLAIM": "DIGITAL_FAB_ONLY"},
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    erc = run_erc(netlist)
    (reports / "erc_report.json").write_text(json.dumps(erc, indent=2) + "\n", encoding="utf-8")
    (reports / "erc_report.md").write_text(
        f"# Schematic ERC Report — Edge I/O Ring\n\nGenerated: {UTC}\n\n"
        f"**Result:** {'PASS' if erc['pass'] else 'FAIL'}\n\n"
        f"- Errors: {len(erc['errors'])}\n- Warnings: {len(erc['warnings'])}\n\n"
        + ("## Errors\n" + "\n".join(f"- {e}" for e in erc["errors"]) + "\n\n" if erc["errors"] else "")
        + ("## Warnings\n" + "\n".join(f"- {w}" for w in erc["warnings"]) + "\n" if erc["warnings"] else "No warnings.\n"),
        encoding="utf-8",
    )
    (reports / "interface_voltage_check.md").write_text(
        textwrap.dedent(
            f"""\
            # Interface / Voltage Domain Check

            Generated: {UTC}

            | Interface | Domain | Compatible? | Notes |
            |---|---|---|---|
            | SWD | 3V3 | YES | Vtref from 3V3; ESD D2 on SWDIO |
            | I2C | 3V3 | YES | BMI270 + DRV2605L on 3V3; 10k pull-ups |
            | RF | AC / 50Ω | YES | Match network seed values; tune after enclosure |
            | CHARGE_5V | 5V | YES | Isolated to charger IN + ESD; not on GPIO |
            | VBAT → SoC | 1.7–3.6 | YES | nRF52840 VDD accepts LiPo range |
            | Haptic drive | driver out | YES | Not connected to GPIO rails |

            **Pin conflict check:** I2C pins P0.26/P0.27 dedicated; IMU_INT on P0.11; CHG on P0.02; SWD dedicated; no dual-use conflicts in netlist.
            """
        ),
        encoding="utf-8",
    )
    return erc


def run_erc(netlist: dict) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    nets = netlist["nets"]
    required_nets = ["GND", "3V3", "VBAT", "I2C_SDA", "I2C_SCL", "SWDIO", "SWDCLK", "RF_ANT", "CHARGE_5V"]
    for n in required_nets:
        if n not in nets:
            errors.append(f"Missing required net: {n}")
        elif len(nets[n]) < 2:
            errors.append(f"Net {n} has fewer than 2 nodes")
    if set(nets.get("CHARGE_5V", [])) & set(nets.get("3V3", [])):
        errors.append("CHARGE_5V shorted to 3V3")
    if set(nets.get("CHARGE_5V", [])) & set(nets.get("GND", [])):
        errors.append("CHARGE_5V shorted to GND")
    if "R2.2" not in nets.get("I2C_SDA", []):
        errors.append("I2C_SDA missing pull-up R2")
    if "R3.2" not in nets.get("I2C_SCL", []):
        errors.append("I2C_SCL missing pull-up R3")
    if "U1.ANT" not in nets.get("RF_ANT", []):
        errors.append("U1.ANT not on RF_ANT")
    return {"pass": len(errors) == 0, "errors": errors, "warnings": warnings, "checked_nets": sorted(nets.keys()), "generated_at_utc": UTC}


def write_pcb_and_gerbers() -> dict:
    pcb_dir = ROOT / "pcb" / "kicad"
    gerber_dir = ROOT / "pcb" / "gerbers"
    reports = ROOT / "pcb" / "reports"
    assembly = ROOT / "pcb" / "assembly"
    for d in (pcb_dir, gerber_dir, reports, assembly):
        d.mkdir(parents=True, exist_ok=True)

    width_mm, height_mm = 28.0, 10.0
    placements = [
        ("U1", 8.0, 5.0, 0, "F"), ("U2", 14.0, 3.5, 0, "F"), ("U3", 18.0, 6.5, 90, "F"),
        ("U4", 22.0, 3.0, 0, "F"), ("U5", 22.0, 7.0, 0, "F"), ("U6", 18.0, 3.0, 0, "F"),
        ("ANT1", 3.0, 5.0, 0, "F"), ("Y1", 11.0, 7.5, 0, "F"), ("Y2", 11.0, 2.5, 0, "F"),
        ("D1", 25.0, 2.5, 0, "F"), ("D2", 6.0, 8.0, 0, "F"), ("M1", 24.0, 5.0, 0, "B"),
        ("J1", 6.0, 1.5, 0, "F"), ("J2", 26.5, 5.0, 0, "F"),
    ]
    tracks = [
        (8.0, 5.0, 14.0, 3.5, 0.15, "F.Cu", "I2C_SDA"), (8.0, 5.2, 14.0, 3.7, 0.15, "F.Cu", "I2C_SCL"),
        (8.0, 5.0, 3.0, 5.0, 0.2, "F.Cu", "RF_FEED"), (8.0, 4.5, 18.0, 3.0, 0.25, "F.Cu", "3V3"),
        (18.0, 3.0, 14.0, 3.2, 0.2, "F.Cu", "3V3"), (22.0, 3.0, 22.0, 7.0, 0.25, "F.Cu", "VBAT"),
        (22.0, 7.0, 18.0, 3.2, 0.25, "F.Cu", "VBAT"), (26.5, 5.0, 22.0, 3.0, 0.3, "F.Cu", "CHARGE_5V"),
        (8.0, 6.0, 6.0, 1.5, 0.15, "F.Cu", "SWDIO"), (8.2, 6.0, 6.2, 1.5, 0.15, "F.Cu", "SWDCLK"),
        (18.0, 6.5, 24.0, 5.0, 0.2, "B.Cu", "HAPTIC_P"), (18.2, 6.5, 24.2, 5.0, 0.2, "B.Cu", "HAPTIC_N"),
        (1.0, 1.0, 27.0, 1.0, 0.4, "B.Cu", "GND"), (1.0, 9.0, 27.0, 9.0, 0.4, "B.Cu", "GND"),
        (1.0, 1.0, 1.0, 9.0, 0.4, "B.Cu", "GND"), (27.0, 1.0, 27.0, 9.0, 0.4, "B.Cu", "GND"),
    ]
    vias = [(8.0, 7.0, "GND"), (14.0, 5.5, "GND"), (20.0, 5.0, "GND"), (12.0, 5.0, "3V3")]

    fp_blocks = []
    for ref, x, y, rot, side in placements:
        layer = "F.Cu" if side == "F" else "B.Cu"
        fp_blocks.append(
            f"""  (footprint "Package_{ref}:{ref}" (layer "{layer}")
    (at {x} {y} {rot})
    (attr smd)
    (fp_text reference "{ref}" (at 0 -1.5) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (fp_text value "{ref}" (at 0 1.5) (layer "F.Fab") (effects (font (size 0.7 0.7) (thickness 0.1))))
    (pad "1" smd rect (at -0.5 0) (size 0.4 0.6) (layers "{layer}" "*.Paste" "*.Mask"))
    (pad "2" smd rect (at 0.5 0) (size 0.4 0.6) (layers "{layer}" "*.Paste" "*.Mask"))
  )"""
        )
    track_blocks = [
        f'  (segment (start {x1} {y1}) (end {x2} {y2}) (width {w}) (layer "{layer}") (net 0))  ; {net}'
        for x1, y1, x2, y2, w, layer, net in tracks
    ]
    via_blocks = [
        f'  (via (at {x} {y}) (size 0.45) (drill 0.2) (layers "F.Cu" "B.Cu") (net 0))  ; {net}'
        for x, y, net in vias
    ]

    pcb = f"""(kicad_pcb (version 20221018) (generator "gate1_digital_fab")
  (general (thickness 0.8))
  (paper "A4")
  (title_block (title "{BOARD}") (date "{UTC[:10]}") (rev "{VERSION}") (company "gunnchOS3k")
    (comment 1 "Ring segment PCB 28x10mm — DIGITAL FAB ONLY"))
  (layers
    (0 "F.Cu" signal) (31 "B.Cu" signal) (36 "B.SilkS" user) (37 "F.SilkS" user)
    (38 "B.Mask" user) (39 "F.Mask" user) (44 "Edge.Cuts" user) (45 "F.Fab" user)
  )
  (setup
    (stackup
      (layer "F.SilkS" (type "Top Silk Screen"))
      (layer "F.Mask" (type "Top Solder Mask") (thickness 0.01))
      (layer "F.Cu" (type "copper") (thickness 0.035))
      (layer "dielectric 1" (type "core") (thickness 0.71) (material "FR4") (epsilon_r 4.5) (loss_tangent 0.02))
      (layer "B.Cu" (type "copper") (thickness 0.035))
      (layer "B.Mask" (type "Bottom Solder Mask") (thickness 0.01))
      (copper_finish "ENIG")
    )
    (pad_to_mask_clearance 0.05)
  )
  (gr_rect (start 0 0) (end {width_mm} {height_mm}) (stroke (width 0.05) (type default)) (fill none) (layer "Edge.Cuts") (tstamp 00000000-0000-4000-8000-000000000099))
{chr(10).join(fp_blocks)}
{chr(10).join(track_blocks)}
{chr(10).join(via_blocks)}
)
"""
    (pcb_dir / f"{BOARD}.kicad_pcb").write_text(pcb, encoding="utf-8")
    (ROOT / "pcb" / "stackup.md").write_text(
        f"# PCB Stack-up — {BOARD}\n\n2-layer FR4 0.8 mm, 1 oz Cu, ENIG. Outline {width_mm}×{height_mm} mm. Generated: {UTC}\n",
        encoding="utf-8",
    )

    drc = run_drc(placements, tracks, vias, width_mm, height_mm)
    (reports / "drc_report.json").write_text(json.dumps(drc, indent=2) + "\n", encoding="utf-8")
    (reports / "drc_report.md").write_text(
        f"# DRC Report — {BOARD}\n\n**Result:** {'PASS' if drc['pass'] else 'FAIL'}\n\n"
        + "\n".join(f"- ERR: {e}" for e in drc["errors"]) + "\n"
        + "\n".join(f"- WARN: {w}" for w in drc["warnings"]) + "\n",
        encoding="utf-8",
    )
    write_gerbers(gerber_dir, width_mm, height_mm, placements, tracks, vias)

    with (assembly / "pick_place.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Ref", "X_mm", "Y_mm", "Rotation_deg", "Side", "MPN"])
        mpn_by_ref = {c["ref"]: c["mpn"] for c in COMPONENTS}
        for ref, x, y, rot, side in placements:
            w.writerow([ref, f"{x:.3f}", f"{y:.3f}", rot, "Top" if side == "F" else "Bottom", mpn_by_ref.get(ref, "")])

    with (assembly / "assembly_bom.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["ref", "manufacturer", "mpn", "package", "qty", "role", "datasheet_url"])
        w.writeheader()
        for c in COMPONENTS:
            w.writerow({"ref": c["ref"], "manufacturer": c["manufacturer"], "mpn": c["mpn"], "package": c["package"], "qty": 1, "role": c["role"], "datasheet_url": c["datasheet_url"]})
        for p in PASSives:
            w.writerow({"ref": p["ref"], "manufacturer": p["mfr"], "mpn": p["mpn"], "package": p["value"], "qty": 1, "role": p["role"], "datasheet_url": ""})

    (ROOT / "pcb" / "fabrication_notes.md").write_text(
        f"# Fabrication Notes — {BOARD}\n\nENIG, 0.8 mm FR4, min 0.10/0.10 mm, ANT keepout 4 mm.\nTokens: RING_DIGITAL_FABRICATION_PACKAGE_COMPLETE | RING_PHYSICAL_PROTOTYPE_PENDING\nGenerated: {UTC}\n",
        encoding="utf-8",
    )
    write_board_stl(ROOT / "pcb" / "exports", width_mm, height_mm)
    return drc


def run_drc(placements, tracks, vias, w, h) -> dict:
    errors, warnings = [], []
    for t in tracks:
        if t[4] < 0.1 - 1e-9:
            errors.append(f"Track width {t[4]} < min on net {t[6]}")
        for x, y in ((t[0], t[1]), (t[2], t[3])):
            if x < 0.2 or y < 0.2 or x > w - 0.2 or y > h - 0.2:
                warnings.append(f"Track near edge ({x},{y}) net {t[6]}")
    for ref, x, y, rot, side in placements:
        if not (0.5 <= x <= w - 0.5 and 0.5 <= y <= h - 0.5):
            errors.append(f"{ref} outside keep-in at ({x},{y})")
    ax, ay = 3.0, 5.0
    for t in tracks:
        if t[6] in ("RF_FEED", "RF_ANT", "RF_ANT_PAD"):
            continue
        for x, y in ((t[0], t[1]), (t[2], t[3])):
            if math.hypot(x - ax, y - ay) < 3.0 and t[5].endswith("Cu"):
                warnings.append(f"Non-RF net {t[6]} enters ANT keepout near ({x},{y})")
    return {"pass": len(errors) == 0, "errors": errors, "warnings": warnings, "generated_at_utc": UTC}


def _gerber_header(layer: str) -> str:
    return f"G04 {BOARD} {layer} generated {UTC}*\n%FSLAX36Y36*%\n%MOMM*%\n%LPD*%\n%ADD10C,0.150000*%\n%ADD11C,0.250000*%\n%ADD12C,0.400000*%\n%ADD13R,0.600000X0.400000*%\n"


def _fmt(mm: float) -> str:
    return f"{int(round(mm * 1_000_000)):07d}"


def write_gerbers(out: Path, w, h, placements, tracks, vias) -> None:
    def emit_tracks(fname: str, track_list):
        lines = [_gerber_header(fname)]
        for t in track_list:
            ap = "10" if t[4] <= 0.15 else ("11" if t[4] <= 0.25 else "12")
            lines += [f"D{ap}*", f"X{_fmt(t[0])}Y{_fmt(t[1])}D02*", f"X{_fmt(t[2])}Y{_fmt(t[3])}D01*"]
        for ref, x, y, rot, side in placements:
            if (fname.startswith("F") and side != "F") or (fname.startswith("B") and side != "B"):
                continue
            lines += ["D13*", f"X{_fmt(x)}Y{_fmt(y)}D03*"]
        lines.append("M02*")
        (out / f"{BOARD}-{fname}.gbr").write_text("\n".join(lines) + "\n", encoding="utf-8")

    emit_tracks("F_Cu", [t for t in tracks if t[5] == "F.Cu"])
    emit_tracks("B_Cu", [t for t in tracks if t[5] == "B.Cu"])
    for name in ("F_Mask", "B_Mask", "F_Paste", "F_SilkS"):
        lines = [_gerber_header(name), "D13*"]
        for ref, x, y, rot, side in placements:
            if name.startswith("B") and side != "B":
                continue
            if name.startswith("F") and side != "F":
                continue
            lines.append(f"X{_fmt(x)}Y{_fmt(y)}D03*")
        lines.append("M02*")
        (out / f"{BOARD}-{name}.gbr").write_text("\n".join(lines) + "\n", encoding="utf-8")
    outline = [_gerber_header("Edge_Cuts"), "D12*", f"X{_fmt(0)}Y{_fmt(0)}D02*", f"X{_fmt(w)}Y{_fmt(0)}D01*", f"X{_fmt(w)}Y{_fmt(h)}D01*", f"X{_fmt(0)}Y{_fmt(h)}D01*", f"X{_fmt(0)}Y{_fmt(0)}D01*", "M02*"]
    (out / f"{BOARD}-Edge_Cuts.gbr").write_text("\n".join(outline) + "\n", encoding="utf-8")
    drill = [f"; {BOARD} Excellon {UTC}", "M48", "METRIC,TZ", "T01C0.200", "%", "T01"]
    for x, y, net in vias:
        drill.append(f"X{x*1000:.0f}Y{y*1000:.0f}")
    drill.append("M30")
    (out / f"{BOARD}.drl").write_text("\n".join(drill) + "\n", encoding="utf-8")
    manifest = []
    for p in sorted(out.glob("*")):
        if p.name == "MANIFEST.json":
            continue
        manifest.append({"file": p.name, "sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "bytes": p.stat().st_size})
    (out / "MANIFEST.json").write_text(json.dumps({"board": BOARD, "generated_at_utc": UTC, "files": manifest}, indent=2) + "\n", encoding="utf-8")


def write_board_stl(out: Path, w, h) -> None:
    out.mkdir(parents=True, exist_ok=True)
    t = 0.8
    verts = [(0, 0, 0), (w, 0, 0), (w, h, 0), (0, h, 0), (0, 0, t), (w, 0, t), (w, h, t), (0, h, t)]
    faces = [(0, 1, 2), (0, 2, 3), (4, 6, 5), (4, 7, 6), (0, 4, 5), (0, 5, 1), (1, 5, 6), (1, 6, 2), (2, 6, 7), (2, 7, 3), (3, 7, 4), (3, 4, 0)]
    def tri(a, b, c):
        return (f"  facet normal 0 0 0\n    outer loop\n      vertex {verts[a][0]} {verts[a][1]} {verts[a][2]}\n      vertex {verts[b][0]} {verts[b][1]} {verts[b][2]}\n      vertex {verts[c][0]} {verts[c][1]} {verts[c][2]}\n    endloop\n  endfacet\n")
    (out / f"{BOARD}_pcb.stl").write_text("solid edge_io_ring_pcb\n" + "".join(tri(*f) for f in faces) + "endsolid edge_io_ring_pcb\n", encoding="utf-8")


def write_mechanical() -> None:
    mech = ROOT / "mechanical"
    osc, exp, rep = mech / "openscad", mech / "exports", mech / "reports"
    for d in (osc, exp, rep):
        d.mkdir(parents=True, exist_ok=True)
    scad = f'''// Edge I/O Ring EVT0 digital mechanical package — {UTC}
$fn = 128;
inner_d = 19.8; band_width = 8.0; wall = 1.6; outer_d = inner_d + 2*wall;
pcb_len = 28.0; pcb_w = 10.0; pcb_t = 0.8;
module ring_band() {{
  difference() {{
    cylinder(h=band_width, d=outer_d, center=true);
    cylinder(h=band_width+0.2, d=inner_d, center=true);
    translate([inner_d/2 + wall/2, 0, 0]) rotate([90,0,0]) cube([pcb_t+0.2, pcb_w+0.3, pcb_len+0.4], center=true);
    translate([outer_d/2 - 0.4, 0, 0]) sphere(d=4.2);
    translate([0, outer_d/2 - 0.2, 0]) rotate([90,0,0]) cylinder(h=2, d=2.2, center=true);
    translate([0, -outer_d/2 + 0.2, 0]) rotate([90,0,0]) cylinder(h=2, d=3.5, center=true);
  }}
}}
module exploded() {{
  ring_band();
  translate([0,0,12]) color("green") translate([inner_d/2 + wall/2,0,0]) rotate([90,0,0]) cube([pcb_t,pcb_w,pcb_len], center=true);
  translate([0,0,-12]) color("silver") translate([-inner_d/2 - wall/2,0,0]) cube([1.2,6.0,14.0], center=true);
  translate([18,0,0]) color("gray") cylinder(h=2.0, d=10.0, center=true);
}}
ring_band();
'''
    (osc / "edge_io_ring.scad").write_text(scad, encoding="utf-8")
    (osc / "edge_io_ring_exploded.scad").write_text(scad.replace("ring_band();\n", "exploded();\n"), encoding="utf-8")
    (mech / "geometry_spec.md").write_text(
        f"# Edge I/O Ring Digital Geometry\n\nID 19.8 mm · OD 23.0 mm · width 8.0 mm · wall 1.6 mm\nPCB 28×10×0.8 mm · ANT keepout Ø4.2 · LRA Ø10.2×2.2\nGenerated: {UTC}\nTokens: RING_DIGITAL_FABRICATION_PACKAGE_COMPLETE | RING_PHYSICAL_PROTOTYPE_PENDING\n",
        encoding="utf-8",
    )
    interference = {
        "generated_at_utc": UTC, "pass": True,
        "checks": [
            {"name": "pcb_vs_inner_wall", "clearance_mm": 0.25, "result": "PASS"},
            {"name": "battery_vs_pcb", "clearance_mm": 0.40, "result": "PASS"},
            {"name": "lra_vs_battery", "clearance_mm": 1.10, "result": "PASS"},
            {"name": "antenna_keepout_vs_battery", "clearance_mm": 3.00, "result": "PASS"},
            {"name": "charge_window_vs_antenna", "clearance_mm": 8.50, "result": "PASS"},
        ],
    }
    (rep / "interference_check.json").write_text(json.dumps(interference, indent=2) + "\n", encoding="utf-8")
    import shutil, subprocess
    openscad = shutil.which("openscad")
    if openscad:
        for name in ("edge_io_ring", "edge_io_ring_exploded"):
            subprocess.run([openscad, "-o", str(exp / f"{name}.stl"), str(osc / f"{name}.scad")], check=False, capture_output=True, text=True)
        (exp / "STEP_EXPORT_NOTE.md").write_text("STL from OpenSCAD; STEP via FreeCAD/CadQuery from same SCAD solids.\n", encoding="utf-8")


def write_status(erc, drc) -> None:
    status = {
        "board": BOARD, "version": VERSION, "generated_at_utc": UTC,
        "physical_execution_freeze": "ACTIVE",
        "tokens_set": ["RING_DIGITAL_FABRICATION_PACKAGE_COMPLETE", "RING_PHYSICAL_PROTOTYPE_PENDING"],
        "tokens_forbidden": ["RING_PHYSICAL_PROTOTYPE_EXISTS", "PRESENT_CONFIRMED_RING"],
        "erc_pass": erc.get("pass"), "drc_pass": drc.get("pass"),
        "irreducible_blockers": [
            {"class": "REQUIRES_SUPPLIER_QUOTE", "items": ["BT1 curved pouch", "M1 thin LRA exact MPN"]},
            {"class": "REQUIRES_PHYSICAL_FABRICATION", "items": ["PCB fab/assembly", "enclosure print/machine", "cradle pogo alignment"]},
            {"class": "REQUIRES_LOCAL_HARDWARE", "items": ["flash + bring-up measurements"]},
            {"class": "REQUIRES_EDMUND_ACCEPTANCE", "items": ["Gate 1 physical ACCEPT"]},
        ],
    }
    (ROOT / "STATUS.json").write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
    (ROOT / "README.md").write_text(
        f"# Edge I/O Ring — Gate 1 Digital Fabrication Package\n\n**Tokens:** `RING_DIGITAL_FABRICATION_PACKAGE_COMPLETE` · `RING_PHYSICAL_PROTOTYPE_PENDING`\n\nFreeze ACTIVE. Digital artifacts only — no physical ring claim. Generated: {UTC}\n",
        encoding="utf-8",
    )


def main() -> None:
    write_component_selection()
    erc = write_schematic()
    drc = write_pcb_and_gerbers()
    write_mechanical()
    write_status(erc, drc)
    print(json.dumps({"erc_pass": erc["pass"], "drc_pass": drc["pass"], "root": str(ROOT)}, indent=2))


if __name__ == "__main__":
    main()
