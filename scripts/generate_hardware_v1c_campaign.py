#!/usr/bin/env python3
"""HARDWARE 1.0C — Custom-First Mainline Pivot artifact generator (digital only)."""
from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HV1 = ROOT / "hardware_v1"
CM = HV1 / "custom_mainline"
CPB0 = CM / "cpb0"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
CAMPAIGN = "HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT"
CLAIM = (
    "digital architecture / EVT preparation only — not physical pass, "
    "not certification, not fab release, not purchased."
)
HDR = (
    f"**Generated:** {NOW}  \n"
    f"**Campaign:** `{CAMPAIGN}`  \n"
    f"**Claim boundary:** {CLAIM}\n"
)


def w(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")


def wj(path: Path, obj: object) -> None:
    w(path, json.dumps(obj, indent=2) + "\n")


def write_csv(path: Path, headers: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow({h: row.get(h, "") for h in headers})


def write_doctrine() -> None:
    w(
        CM / "CUSTOM_FIRST_ARCHITECTURE_DOCTRINE.md",
        f"""# Custom-First Architecture Doctrine

{HDR}

> **Mainline = maximum practical customization and ownership of the platform.**
>
> **Simpler modular/COTS implementations become reference/control or experimental variants.**

This does **not** mean designing CPU, cellular baseband, Wi-Fi, or closed PHY IP from scratch.
It means the mainline owns the **board around the silicon**.

## MAINLINE_CUSTOM

Production-intent Gen-1 path owns:

- motherboard / carrier PCB
- SoC package integration
- memory topology
- power tree / VRM / sequencing
- EC / supervisory MCU
- USB4 routing
- PCIe routing
- display routing
- NVMe
- Wi-Fi module integration
- optional cellular module integration
- audio, camera, sensors
- battery / BMS / charging
- TPM / root of trust
- firmware interfaces
- recovery/debug
- thermal solution
- antenna placement
- industrial/mechanical integration
- DFM/DFT/serviceability

Primary compute mainline: **gunnchOS Platform Core v1** (AMD Ryzen Embedded 8000 FP7r2 BGA custom motherboard family).

## REFERENCE_CONTROL

Simpler COTS platforms exist to provide:

- known-good comparison
- software validation
- bring-up isolation
- performance baseline
- driver/reference behavior
- fallback if custom board slips

They do **not** define the final product architecture.

Examples:

- ADLINK COM-HPC Mini mMTL + Mini Base → `REFERENCE_CONTROL_MODULAR_X86`
- COTS TB4/USB4 dock → `REFERENCE_CONTROL_DOCK`
- nRF54L15 DK → `REFERENCE_CONTROL_RING`

## EXPERIMENTAL_VARIANT

Alternative architectures may be better for specific SKUs, but can only replace mainline after measured comparison evidence.

Fail-closed rules:

- COM-HPC cannot be marked production mainline
- COTS/reference-control evidence cannot mark custom-board pass
- AMD custom pin/power/DDR collateral cannot be invented
- CPB0 cannot be READY_FOR_FAB without net-accurate vendor collateral + real EDA
- experimental variant cannot silently promote
- public package family equality ≠ pin compatibility without vendor confirmation
""",
    )


def write_platform_core() -> None:
    w(
        CM / "PLATFORM_CORE_V1.md",
        f"""# gunnchOS Platform Core v1

{HDR}

## Definition

**gunnchOS Platform Core v1** is the custom motherboard platform family built around AMD embedded x86 SoCs.

## Primary silicon family

`AMD Ryzen Embedded 8000 Series — FP7r2 BGA`

### Why this family (decision rationale)

- x86 compatibility with Windows/Linux ecosystem
- integrated RDNA 3 graphics
- integrated NPU (public product-brief class)
- up to four displays (vendor-confirmed topology required before freeze)
- USB4
- PCIe Gen4
- DDR5 with ECC capability (topology pending vendor rules)
- BGA package suitable for custom boards
- low-to-mid power envelopes suitable for portable devices
- embedded lifecycle / longevity positioning

### Explicit non-claims

- Pin compatibility among SKUs is **NOT assumed** until AMD design collateral proves it.
- No net-accurate pinout, ball map, power sequencing, or DDR rules are present in this repo.
- Platform Core v1 is architecture doctrine + learning/EVT plan, not fab release.

### Product boards sharing Platform Core blocks

| Board | Role |
|---|---|
| `Student-MB-v1` | Student 14.5 production-intent mainboard |
| `Handheld-MB-v1` | Handheld Hybrid production-intent mainboard |
| `DSXL-MB-v1` | DS-XL Coder production-intent mainboard |
| `CPB0` | Custom Platform Board 0 — debug-friendly learning/reference board |

Replaces previous product mainline label: `COM-HPC Mini x86` (now REFERENCE_CONTROL only).
""",
    )


def write_soc_matrix() -> None:
    w(
        CM / "DEVICE_SOC_SELECTION_MATRIX.md",
        f"""# Device SoC selection matrix

{HDR}

Selections are **mainline candidates**, subject to exact AMD embedded design-collateral confirmation.
Public OPNs below are from public product briefs — not proof of pin compatibility. Pin compatibility across SKUs is **not assumed**.

| Device | Main candidate | Public OPN (reference) | Package | Nominal / config TDP (public brief class) | Notes |
|---|---|---|---|---|---|
| Student 14.5 | Ryzen Embedded 8840U | `100-000001317E` | FP7r2 BGA | ~28 W; 15–30 W class | Balanced education/work/gaming; commonality with Handheld |
| Handheld Hybrid | Ryzen Embedded 8840U | `100-000001317E` | FP7r2 BGA | lower sustained within supported envelope | Compact custom MB; COM-HPC mule = REFERENCE_CONTROL only |
| DS-XL Coder | Ryzen Embedded 8845HS | `100-000001316E` | FP7r2 BGA | ~45 W; 35–54 W class | Higher sustained for creation/build/deploy |
| CPB0 learning board | Ryzen Embedded 8845HS preferred | `100-000001316E` | FP7r2 BGA | debug-friendly envelope | Fallback to 8840U only if vendor-access requires |

## Commonality intent

- Maximum reuse of Platform Core schematic blocks across Student / Handheld / DS-XL
- Do **not** force identical PCB dimensions
- Do **not** treat 8840U and 8845HS as drop-in pin-compatible without AMD confirmation

## Experimental higher-AI / higher-perf alternatives

| Experiment | Candidate class | vs mainline |
|---|---|---|
| EXP-DSXL-X100-001 | Ryzen AI Embedded X100 / X168i-class | DS-XL 8845HS |
| EXP-P100-AI-001 | Ryzen AI Embedded P132 / P132i-class | Student 8840U |
""",
    )


def write_blocks_and_reuse() -> None:
    blocks = [
        "SoC power",
        "DDR5",
        "SPI/boot flash",
        "TPM",
        "EC",
        "USB4",
        "PCIe/NVMe",
        "Wi-Fi",
        "optional 5G",
        "audio",
        "camera",
        "display",
        "USB-C/PD",
        "debug/recovery",
    ]
    w(
        CM / "COMMON_PLATFORM_BLOCKS.md",
        f"""# Common Platform Core schematic/architecture blocks

{HDR}

Reusable blocks intended for Student-MB-v1 / Handheld-MB-v1 / DSXL-MB-v1 / CPB0:

{chr(10).join(f'- {b}' for b in blocks)}

## Ownership rule

Each block is MAINLINE_CUSTOM architecture documentation until vendor collateral + EDA make nets accurate.
Block reuse does **not** imply identical PCB layout or proven SI/PI closure.
""",
    )
    w(
        CM / "BOARD_REUSE_STRATEGY.md",
        f"""# Board reuse strategy

{HDR}

## Shared

- Platform Core v1 schematic blocks
- EC firmware architecture
- boot policy / Secure Boot key management patterns
- bring-up instrumentation philosophy
- AVL classes for NVMe / Wi-Fi / optional cellular / TPM

## Product-specific

| Board | Drivers of divergence |
|---|---|
| Student-MB-v1 | 14.5\" thermal/mechanical, serviceability, battery capacity |
| Handheld-MB-v1 | compactness, controls, vapor chamber, M.2 2230 if packaging permits |
| DSXL-MB-v1 | dual-display eDP+DDI, higher sustained power, cooling |
| CPB0 | oversized debug headers, rail test points, bench power, battery emulator |

Do **not** force identical PCB dimensions across products.
""",
    )


def write_cpb0() -> None:
    w(
        CPB0 / "PRD.md",
        f"""# CPB0 — gunnchOS Custom Platform Board 0 PRD

{HDR}

## Purpose

Primary pre-product motherboard learning platform. Deliberately debug-friendly, not pretty.

## Primary SoC candidate

`AMD Ryzen Embedded 8845HS` (OPN ref `100-000001316E`)  
Fallback: `8840U` only if vendor-access constraints require it.

## Required subsystems

BGA SoC, DDR5, full power tree, VRM, EC, SPI flash, TPM, NVMe, Wi-Fi, optional cellular,
USB4, USB 3.x/2, display outputs (min one eDP + DDI/DP), audio, camera, I2C/SPI/UART/GPIO,
USB-C PD, fan control, current sensing, rail test points, JTAG/SWD/UART, POST/debug LEDs,
board-revision straps, recovery switch, firmware recovery header, external bench power,
battery emulator input, thermistor headers.

## Fab readiness

`CPB0_READY_FOR_FAB=false` until net-accurate AMD collateral and actual EDA outputs exist.
""",
    )
    w(
        CPB0 / "SYSTEM_BLOCK_DIAGRAM.md",
        f"""# CPB0 system block diagram (logical)

{HDR}

```
                 +---------------------------+
 Bench PSU / Batt Emulator ----> | Power tree / VRM / PD    |
                 +-------------+-------------+
                               |
                 +-------------v-------------+
                 | AMD Ryzen Emb. 8845HS BGA |
                 | Platform Core SoC         |
                 +--+----+----+----+----+----+
                    |    |    |    |    |
                 DDR5  PCIe USB4 Display Debug
                    |    |    |    |    |
                 SODIMM NVMe USB-C eDP/DDI UART/JTAG
                 /solder Wi-Fi Dock DP    EC / TPM / SPI
                         (opt 5G)
```

Logical only — not a netlist. Pin/rail names require AMD collateral.
""",
    )
    w(
        CPB0 / "POWER_TREE.md",
        f"""# CPB0 power tree (planning)

{HDR}

## Intent

Document ownership of sequencing, VRM domains, USB-C PD sink/source roles, battery emulator path, current sense, and rail test points.

## Status

`CUSTOM_POWER_TREE_UNDERSTOOD=false` — AMD power sequencing / VRM requirements not in-repo (vendor-gated).
Do not invent rail names, current limits, or sequencing delays.
""",
    )
    w(
        CPB0 / "CLOCK_RESET_MAP.md",
        f"""# CPB0 clock / reset map (planning)

{HDR}

Planning placeholders only. Exact crystal/PLL/reset tree requires AMD platform collateral.
`CUSTOM_BOOT_CHAIN_UNDERSTOOD=false` until SPI/boot and reset requirements are vendor-confirmed.
""",
    )
    write_csv(
        CPB0 / "INTERFACE_MATRIX.csv",
        ["interface", "direction", "owner", "status", "notes"],
        [
            {"interface": "DDR5", "direction": "SoC↔DRAM", "owner": "MAINLINE_CUSTOM", "status": "PENDING_VENDOR_TOPOLOGY", "notes": "Do not freeze"},
            {"interface": "USB4", "direction": "SoC↔USB-C", "owner": "MAINLINE_CUSTOM", "status": "PENDING_VENDOR_GUIDANCE", "notes": ""},
            {"interface": "PCIe Gen4", "direction": "SoC↔NVMe/slots", "owner": "MAINLINE_CUSTOM", "status": "PENDING_VENDOR_GUIDANCE", "notes": ""},
            {"interface": "eDP", "direction": "SoC→panel", "owner": "MAINLINE_CUSTOM", "status": "ARCH_INTENT", "notes": "min one eDP"},
            {"interface": "DDI/DP", "direction": "SoC→DP", "owner": "MAINLINE_CUSTOM", "status": "ARCH_INTENT", "notes": ""},
            {"interface": "SPI flash", "direction": "SoC↔flash", "owner": "MAINLINE_CUSTOM", "status": "PENDING_VENDOR", "notes": ""},
            {"interface": "EC UART/I2C", "direction": "EC↔SoC", "owner": "MAINLINE_CUSTOM", "status": "ARCH_INTENT", "notes": "Zephyr EC"},
            {"interface": "TPM", "direction": "SoC↔TPM", "owner": "MAINLINE_CUSTOM", "status": "ARCH_INTENT", "notes": "TPM2 / fTPM where supported"},
            {"interface": "Wi-Fi M.2", "direction": "PCIe/CNVi class TBD", "owner": "MAINLINE_CUSTOM", "status": "PENDING_VENDOR", "notes": ""},
            {"interface": "optional 5G M.2", "direction": "PCIe/USB", "owner": "MAINLINE_CUSTOM", "status": "OPTIONAL", "notes": "FN990B40 class AVL preserved"},
            {"interface": "JTAG/SWD/UART", "direction": "debug", "owner": "MAINLINE_CUSTOM", "status": "REQUIRED_ON_CPB0", "notes": "debug-friendly"},
        ],
    )
    w(
        CPB0 / "DEBUG_PLAN.md",
        f"""# CPB0 debug plan

{HDR}

## Required debug affordances

- UART console, JTAG/SWD where applicable
- POST/debug LEDs, board-revision straps
- recovery switch + firmware recovery header
- rail test points + current sensing
- external bench power + battery emulator input
- thermistor headers

`CUSTOM_DEBUG_ARCHITECTURE_UNDERSTOOD=false` until vendor debug tool requirements are acquired.
""",
    )
    write_csv(
        CPB0 / "PRELIMINARY_BOM.csv",
        ["item_id", "description", "class", "mpn_or_class", "qty", "status", "price", "notes"],
        [
            {"item_id": "CPB0-SOC", "description": "Ryzen Embedded 8845HS FP7r2", "class": "MAINLINE_CUSTOM", "mpn_or_class": "100-000001316E (ref)", "qty": "1", "status": "PENDING_VENDOR_CONFIRMATION", "price": "VERIFY_AT_PURCHASE", "notes": "not ordered"},
            {"item_id": "CPB0-DDR", "description": "DDR5 topology TBD", "class": "MAINLINE_CUSTOM", "mpn_or_class": "PENDING_VENDOR_TOPOLOGY", "qty": "0", "status": "UNFROZEN", "price": "VERIFY_AT_PURCHASE", "notes": "do not invent devices"},
            {"item_id": "CPB0-EC", "description": "EC / supervisory MCU", "class": "MAINLINE_CUSTOM", "mpn_or_class": "PENDING_SELECTION", "qty": "0", "status": "ARCH_INTENT", "price": "VERIFY_AT_PURCHASE", "notes": "Zephyr+MCUboot"},
            {"item_id": "CPB0-TPM", "description": "TPM 2.0 discrete or fTPM", "class": "MAINLINE_CUSTOM", "mpn_or_class": "PENDING_SELECTION", "qty": "0", "status": "ARCH_INTENT", "price": "VERIFY_AT_PURCHASE", "notes": ""},
            {"item_id": "CPB0-NVME", "description": "M.2 NVMe", "class": "MAINLINE_CUSTOM", "mpn_or_class": "AVL_CLASS", "qty": "0", "status": "ARCH_INTENT", "price": "VERIFY_AT_PURCHASE", "notes": ""},
            {"item_id": "CPB0-WIFI", "description": "M.2 Wi-Fi", "class": "MAINLINE_CUSTOM", "mpn_or_class": "AVL_CLASS", "qty": "0", "status": "ARCH_INTENT", "price": "VERIFY_AT_PURCHASE", "notes": ""},
        ],
    )
    w(
        CPB0 / "SCHEMATIC_SHEET_PLAN.md",
        f"""# CPB0 schematic sheet plan

{HDR}

Planned sheets (titles only; no invented nets): SoC, Power/VRM, DDR, EC/TPM/SPI, USB4/PD, PCIe/NVMe, Display, RF modules, Audio/Camera/Sensors, Debug/Recovery.

`CPB0_SCHEMATIC_READY=false` — no EDA schematic exists in this campaign.
""",
    )
    w(
        CPB0 / "PCB_CONSTRAINT_PLAN.md",
        f"""# CPB0 PCB constraint plan

{HDR}

Intent: multilayer BGA escape, controlled-impedance DDR/USB4/PCIe/DP, keep-outs for antennas, oversized debug connectors.

`CPB0_PCB_READY=false` — no board file / Gerbers / ODB++ generated.
""",
    )
    w(
        CPB0 / "BRINGUP_PLAN.md",
        f"""# CPB0 bring-up plan

{HDR}

Stages (all UNTESTED_PENDING_PHYSICAL): power rails → clocks/reset → EC → SPI/boot → memory training → PCIe/NVMe → USB4 → display → RF → thermal.

Physical bring-up cannot start without fab boards. Digital plan only.
""",
    )


def write_amd_access() -> None:
    rows = [
        ("Ryzen Embedded 8000 pinout", "NDA_REQUIRED", "blocks CPB0 nets"),
        ("FP7r2 package/mechanical", "AMD_PARTNER_ACCESS", "or NDA_REQUIRED"),
        ("power sequencing", "NDA_REQUIRED", ""),
        ("VRM requirements", "NDA_REQUIRED", ""),
        ("DDR5 routing/topology", "NDA_REQUIRED", ""),
        ("supported memory devices/topologies", "NDA_REQUIRED", ""),
        ("USB4 implementation guidance", "AMD_PARTNER_ACCESS", "may be NDA"),
        ("PCIe implementation guidance", "AMD_PARTNER_ACCESS", ""),
        ("display/DDI/eDP guidance", "AMD_PARTNER_ACCESS", ""),
        ("clock/reset requirements", "NDA_REQUIRED", ""),
        ("boot/SPI requirements", "AMD_PARTNER_ACCESS", ""),
        ("platform security requirements", "AMD_PARTNER_ACCESS", ""),
        ("thermal design guidance", "PUBLIC", "partial public; detailed TBD"),
        ("reference schematic", "NDA_REQUIRED", ""),
        ("reference board/layout", "NDA_REQUIRED", ""),
        ("signal-integrity constraints", "NDA_REQUIRED", ""),
        ("BIOS/UEFI / AGESA enablement path", "IBV_REQUIRED", "vendor-supported path"),
        ("manufacturing/programming requirements", "AMD_PARTNER_ACCESS", ""),
        ("debug tools", "AMD_DEVELOPER_LOGIN", "tool access TBD"),
        ("reference validation checklist", "AMD_PARTNER_ACCESS", ""),
        ("public product brief / OPN identity", "PUBLIC", "8840U/8845HS OPNs cited as reference only"),
    ]
    lines = [
        f"# AMD custom platform access packet",
        "",
        HDR,
        "",
        "`CUSTOM_PLATFORM_VENDOR_ACCESS_READY=false` — Cursor does not submit/accept NDAs or partner agreements.",
        "",
        "## Required collateral categories",
        "",
        "| Artifact | Classification | Notes |",
        "|---|---|---|",
    ]
    for name, cls, notes in rows:
        lines.append(f"| {name} | `{cls}` | {notes} |")
    lines += [
        "",
        "## Owner steps (human only)",
        "",
        "1. Create/login AMD Embedded Developer Hub account (owner).",
        "2. Request Embedded partner/sales engagement for Ryzen Embedded 8000 custom board design access.",
        "3. Complete any required NDA/partner workflow **as owner** (Cursor will not accept/sign).",
        "4. Obtain pinout, package, power, DDR, USB4/PCIe/display, boot, SI, reference schematic/layout packages.",
        "5. Inquire BIOS/IBV support path (AGESA / vendor UEFI) for selected OPNs.",
        "6. Deposit non-public files only in an owner-controlled vault; do not invent contents into this public repo.",
        "",
        "## Cursor boundary",
        "",
        "- Does not invent restricted data",
        "- Does not submit agreements",
        "- Does not purchase silicon or eval boards",
        "- Stops honestly if collateral cannot be obtained (does not silently revert COM-HPC to mainline)",
        "",
        f"`NEXT_OWNER_ACTION=ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL`",
    ]
    w(HV1 / "vendor_access" / "AMD_CUSTOM_PLATFORM_ACCESS_PACKET.md", "\n".join(lines) + "\n")


def write_firmware_memory() -> None:
    w(
        CM / "FIRMWARE_OWNERSHIP_BOUNDARY.md",
        f"""# Firmware ownership boundary (custom mainline)

{HDR}

## Mainline firmware stack

- custom motherboard
- vendor-supported AMD silicon-init path
- UEFI
- Secure Boot
- TPM 2.0 / fTPM where supported
- measured boot
- signed updates
- custom EC firmware (Zephyr + MCUboot)

coreboot / AMD openSIL are **experimental only** — not production blockers.

## We own

- board configuration
- ACPI/platform tables where accessible
- EC
- boot policy
- recovery UX
- Secure Boot keys/policy
- update orchestration
- telemetry
- hardware inventory
- board-revision configuration

## Silicon vendor / IBV owns or supplies

- proprietary silicon initialization not publicly implementable
- vendor binary firmware where required
- AGESA or equivalent supported silicon-init path
""",
    )
    w(
        CM / "MEMORY_TOPOLOGY_DECISION.md",
        f"""# Memory topology decision (UNFROZEN)

{HDR}

Do **not** freeze until AMD topology rules are available.

## Evaluation axes

routing difficulty, SI margin, capacity, repairability, power, board area, cost, availability, production assembly, product thickness.

## Intent by board (not frozen)

| Board | Preference if vendor allows |
|---|---|
| CPB0 | easiest to instrument/debug (prefer SO-DIMM if supported) |
| Student | serviceability favored if physically practical |
| DS-XL | capacity favored |
| Handheld | compactness/power favored |

Evaluate SO-DIMM vs soldered DDR5; LPDDR only if selected SoC/platform supports it.

`CUSTOM_DDR_TOPOLOGY_UNDERSTOOD=false`
""",
    )


def write_knowledge_map() -> None:
    subs = [
        "SoC",
        "DDR",
        "VRM",
        "clocks",
        "reset",
        "SPI/boot",
        "EC",
        "TPM",
        "NVMe",
        "PCIe",
        "USB4",
        "USB-C PD",
        "Wi-Fi",
        "cellular",
        "antennas",
        "display",
        "camera",
        "audio",
        "sensors",
        "fan",
        "battery",
        "charger",
        "BMS",
        "input controls",
        "debug",
        "update/recovery",
    ]
    parts = [f"# Custom motherboard knowledge map", "", HDR, ""]
    for s in subs:
        parts += [
            f"## {s}",
            "",
            f"- **What it does:** Platform Core / product board function for {s} (architecture intent).",
            f"- **Why it exists:** Required for owned custom motherboard behavior around AMD silicon.",
            f"- **Inputs / outputs / electrical / firmware / software interfaces:** PENDING vendor collateral where applicable; public interfaces documented at architecture level only.",
            f"- **Failure modes / measurements / debug:** See CPB0 debug plan; physical methods pending hardware.",
            f"- **Manufacturing / compliance implications:** DFM/DFT pending EDA; RF/EMC pending design.",
            f"- **Vendor-owned:** silicon IP, restricted pin/power/SI data, AGESA/binary blobs as applicable.",
            f"- **gunnchOS owns:** board integration, EC policy, boot policy, recovery UX, inventory, serviceability.",
            f"- **Replaceable / revalidation:** changing {s} requires revalidation of dependent electrical, firmware, thermal, and compliance gates.",
            "",
        ]
    w(CM / "KNOWLEDGE_MAP.md", "\n".join(parts))


def write_complexity() -> None:
    items = [
        ("BGA SoC escape", "open/short, SI", "fanout rules + review", "PCB layout", "CAD + microscope", "AMD package data", "EVT"),
        ("DDR routing", "training fail", "length match + sim", "SI eng", "SI tools", "AMD DDR rules", "EVT"),
        ("high-current power", "brownout", "sense + margin", "power eng", "electronic load", "VRM docs", "EVT"),
        ("VRM tuning", "instability", "vendor design guide", "power eng", "scope", "AMD VRM req", "EVT"),
        ("boot firmware", "no-POST", "IBV path + serial", "FW eng", "SPI programmer", "AGESA/IBV", "EVT"),
        ("SI/PI", "eye collapse", "sim + measurement", "SI eng", "VNA/scope", "vendor constraints", "DVT"),
        ("USB4", "link fail", "retimer strategy", "SI/FW", "USB4 analyzer", "AMD+USB-IF", "EVT"),
        ("display", "no image", "eDP+DDI bring-up", "display eng", "panel fixture", "AMD display guide", "EVT"),
        ("EMI", "fail pre-scan", "filter/stackup", "EMC eng", "chamber", "lab", "DVT"),
        ("thermal", "throttle", "chamber + skin", "thermal eng", "TC/IR", "heatsink fab", "EVT"),
        ("bring-up", "stuck rail", "CPB0 instrumentation", "systems", "bench", "debug tools", "EVT"),
        ("debug", "blind failure", "headers/LEDs", "systems", "JTAG/UART", "vendor tools", "EVT"),
        ("manufacturing", "yield loss", "DFT/fixtures", "NPI", "ICT/FCT", "CM", "PVT"),
        ("BIOS/IBV", "enablement gap", "engage IBV early", "FW", "build env", "IBV", "EVT"),
        ("board spins", "schedule slip", "CPB0 first", "PM", "fab house", "CM", "EVT"),
    ]
    lines = [
        "# Custom mainline complexity register",
        "",
        HDR,
        "",
        "No dollar estimates without sourced quotes.",
        "",
        "| Area | Complexity | Likely failure | Mitigation | Expertise | Tooling | External dependency | Validation stage |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for a, f, m, e, t, x, v in items:
        lines.append(f"| {a} | high | {f} | {m} | {e} | {t} | {x} | {v} |")
    w(CM / "CUSTOM_MAINLINE_COMPLEXITY_REGISTER.md", "\n".join(lines) + "\n")


def write_learning_gates_doc() -> None:
    gates = [
        "CUSTOM_SOC_PINMAP_UNDERSTOOD",
        "CUSTOM_POWER_TREE_UNDERSTOOD",
        "CUSTOM_DDR_TOPOLOGY_UNDERSTOOD",
        "CUSTOM_PCIE_TOPOLOGY_UNDERSTOOD",
        "CUSTOM_USB4_TOPOLOGY_UNDERSTOOD",
        "CUSTOM_DISPLAY_TOPOLOGY_UNDERSTOOD",
        "CUSTOM_EC_ARCHITECTURE_UNDERSTOOD",
        "CUSTOM_BOOT_CHAIN_UNDERSTOOD",
        "CUSTOM_DEBUG_ARCHITECTURE_UNDERSTOOD",
        "CUSTOM_MANUFACTURING_FLOW_UNDERSTOOD",
    ]
    lines = [
        "# Board design learning gates",
        "",
        HDR,
        "",
        "These gates mean **documentation/design understanding only**.",
        "They remain false where required vendor collateral is missing.",
        "",
    ]
    for g in gates:
        lines.append(f"- `{g}=false`")
    w(CM / "LEARNING_GATES.md", "\n".join(lines) + "\n")


def write_boms() -> None:
    write_csv(
        HV1 / "bom" / "MAINLINE_CUSTOM_BOM.csv",
        ["item_id", "sku", "description", "class", "mpn_or_class", "qty", "status", "notes"],
        [
            {"item_id": "MC-SOC-STU", "sku": "student_14_5", "description": "Ryzen Embedded 8840U", "class": "MAINLINE_CUSTOM", "mpn_or_class": "100-000001317E (ref)", "qty": "0", "status": "PENDING_VENDOR_CONFIRMATION", "notes": "not ordered"},
            {"item_id": "MC-SOC-HH", "sku": "handheld_hybrid", "description": "Ryzen Embedded 8840U", "class": "MAINLINE_CUSTOM", "mpn_or_class": "100-000001317E (ref)", "qty": "0", "status": "PENDING_VENDOR_CONFIRMATION", "notes": "not ordered"},
            {"item_id": "MC-SOC-DSXL", "sku": "ds_xl_coder", "description": "Ryzen Embedded 8845HS", "class": "MAINLINE_CUSTOM", "mpn_or_class": "100-000001316E (ref)", "qty": "0", "status": "PENDING_VENDOR_CONFIRMATION", "notes": "not ordered"},
            {"item_id": "MC-MB-STU", "sku": "student_14_5", "description": "Student-MB-v1 custom motherboard", "class": "MAINLINE_CUSTOM", "mpn_or_class": "GUNNCHOS-STUDENT-MB-V1", "qty": "0", "status": "ARCH_INTENT", "notes": "no fab"},
            {"item_id": "MC-MB-HH", "sku": "handheld_hybrid", "description": "Handheld-MB-v1 custom motherboard", "class": "MAINLINE_CUSTOM", "mpn_or_class": "GUNNCHOS-HANDHELD-MB-V1", "qty": "0", "status": "ARCH_INTENT", "notes": "no fab"},
            {"item_id": "MC-MB-DSXL", "sku": "ds_xl_coder", "description": "DSXL-MB-v1 custom motherboard", "class": "MAINLINE_CUSTOM", "mpn_or_class": "GUNNCHOS-DSXL-MB-V1", "qty": "0", "status": "ARCH_INTENT", "notes": "no fab"},
            {"item_id": "MC-DOCK", "sku": "dock", "description": "CUSTOM_GUNNCHOS_DOCK_GEN1", "class": "MAINLINE_CUSTOM", "mpn_or_class": "CUSTOM_DOCK", "qty": "0", "status": "VENDOR_GATED_BALLMAP", "notes": "JHL8440/9040R still gated"},
            {"item_id": "MC-RING", "sku": "rings", "description": "Custom nRF54L15 ring PCB", "class": "MAINLINE_CUSTOM", "mpn_or_class": "nRF54L15 class", "qty": "0", "status": "ARCH_INTENT", "notes": "DK is reference only"},
        ],
    )
    write_csv(
        HV1 / "bom" / "REFERENCE_CONTROL_BOM.csv",
        ["item_id", "description", "class", "mpn_or_class", "qty", "status", "price", "physical_purchase_status", "notes"],
        [
            {"item_id": "RC-COM-HPC-MOD", "description": "ADLINK COM-HPC Mini mMTL", "class": "REFERENCE_CONTROL", "mpn_or_class": "COM-HPC-mMTL-155H-32G", "qty": "0", "status": "PROCUREMENT_READY", "price": "VERIFY_AT_PURCHASE", "physical_purchase_status": "NOT_PURCHASED", "notes": "not product mainline"},
            {"item_id": "RC-COM-HPC-BASE", "description": "ADLINK COM-HPC Mini Base", "class": "REFERENCE_CONTROL", "mpn_or_class": "COM-HPC Mini Base COTS", "qty": "0", "status": "PROCUREMENT_READY", "price": "VERIFY_AT_PURCHASE", "physical_purchase_status": "NOT_PURCHASED", "notes": "RP0-A"},
            {"item_id": "RC-NRF-DK", "description": "nRF54L15 DK", "class": "REFERENCE_CONTROL", "mpn_or_class": "PCA10156", "qty": "0", "status": "PROCUREMENT_READY", "price": "VERIFY_AT_PURCHASE", "physical_purchase_status": "NOT_PURCHASED", "notes": "REFERENCE_CONTROL_RING"},
            {"item_id": "RC-COTS-DOCK", "description": "COTS TB4/USB4 dock", "class": "REFERENCE_CONTROL", "mpn_or_class": "COTS_USB4_DOCK", "qty": "0", "status": "PROCUREMENT_READY", "price": "VERIFY_AT_PURCHASE", "physical_purchase_status": "NOT_PURCHASED", "notes": "REFERENCE_CONTROL_DOCK"},
        ],
    )
    w(
        HV1 / "bom" / "EXPERIMENTAL_BOM_INDEX.md",
        f"""# Experimental BOM index

{HDR}

Class: `EXPERIMENTAL` / `DEFERRED_GEN2` only. Must not mix into MAINLINE_CUSTOM BOM with orderable qty>0.

| Experiment | Baseline | Variant |
|---|---|---|
| EXP-ARM-IQX-001 | Custom AMD Platform Core v1 | ARM IQX-class SoM |
| EXP-STUDENT-OLED-001 | IPS | OLED |
| EXP-DSXL-OLED-HYBRID-001 | Dual IPS (eDP+DDI) | OLED+IPS |
| EXP-DOCK-USB4-80-001 | USB4 40 | USB4 80 |
| EXP-RINGS-INDUCTIVE-001 | Mag contacts | Inductive |
| EXP-RINGS-SEMG-001 | IMU/cap ring | sEMG wrist |
| EXP-COREBOOT-001 | Vendor UEFI | coreboot/openSIL |
| EXP-RAUC-001 | Vendor capsule/EC | RAUC A/B |
| EXP-DSXL-X100-001 | 8845HS | X100/X168i-class |
| EXP-P100-AI-001 | 8840U | P132/P132i-class |
| EXP-COM-HPC-MODULAR-001 | Custom MB mainline | COM-HPC modular product |
""",
    )
    w(
        HV1 / "bom" / "MAINLINE_BOM_INDEX.md",
        f"""# Hardware v1 mainline BOM index

{HDR}

## BOM classes (fail-closed)

| Class | File / location | May define product architecture? |
|---|---|---|
| `MAINLINE_CUSTOM` | `hardware_v1/bom/MAINLINE_CUSTOM_BOM.csv` | YES |
| `REFERENCE_CONTROL` | `hardware_v1/bom/REFERENCE_CONTROL_BOM.csv` | NO |
| `EXPERIMENTAL` | `hardware_v1/bom/EXPERIMENTAL_BOM_INDEX.md` + EXP packages | NO |
| `DEFERRED_GEN2` | experimental index / ledger | NO |

## Rule

- Mainline BOM must **not** contain COM-HPC module/baseboard as product architecture.
- COM-HPC may appear only under REFERENCE_CONTROL equipment.
- Experimental MPNs must not appear in mainline with qty>0.

## SKU mapping (custom mainline intent)

| SKU | Mainline compute | Notes |
|---|---|---|
| Student 14.5 | 8840U custom Student-MB-v1 | COM-HPC retained as reference control |
| DS-XL Coder | 8845HS custom DSXL-MB-v1 | one eDP + DDI preserved |
| Handheld | 8840U custom Handheld-MB-v1 | COM-HPC mule = reference only |
| Dock Gen-1 | CUSTOM_GUNNCHOS_DOCK_GEN1 | COTS dock = REFERENCE_CONTROL_DOCK |
| Rings | custom nRF54L15 | DK = REFERENCE_CONTROL_RING |

## AVL
See `hardware_v1/bom/AVL.md`. Unknown fields stay unknown.
""",
    )


def write_experiments() -> None:
    # Update registry with hierarchy + new experiments
    new_exps = [
        {
            "id": "EXP-COM-HPC-MODULAR-001",
            "branch": "hardware/exp-com-hpc-modular-product",
            "title": "COM-HPC modular product architecture vs custom motherboard mainline",
            "hypothesis": "COM-HPC modular path matches product goals with lower board complexity; measure whether giving up motherboard ownership is justified",
            "baseline": "CUSTOM AMD Platform Core v1 (8840U/8845HS)",
            "variant": "ADLINK COM-HPC Mini mMTL + Mini Base REFERENCE_CONTROL_MODULAR_X86",
            "metrics": [
                "time_to_bringup",
                "bom_complexity",
                "thermal_skin_c",
                "usb4_behavior",
                "os_compat",
                "ownership_score",
                "schedule_risk",
            ],
            "promotion_gate": "Measured evidence that modular path meets product goals AND owner explicitly accepts reduced motherboard ownership; cannot silently become mainline",
            "not_in_main_bom": True,
            "hierarchy": "REFERENCE_CONTROL_COMPARE",
        },
        {
            "id": "EXP-DSXL-X100-001",
            "branch": "hardware/exp-dsxl-x100",
            "title": "DS-XL Ryzen AI Embedded X100-class vs 8845HS mainline",
            "hypothesis": "X100/X168i-class improves local AI/create workloads enough to justify LPDDR5X/PCB complexity and power",
            "baseline": "Ryzen Embedded 8845HS Platform Core",
            "variant": "Ryzen AI Embedded X168i-class (PENDING_VENDOR_CONFIRMATION)",
            "metrics": [
                "cpu_perf",
                "gpu_perf",
                "npu_perf",
                "compile",
                "local_ai",
                "gaming",
                "power",
                "thermal",
                "lpddr5x_integration",
                "pcb_complexity",
                "cost",
                "battery_impact",
                "charger_requirement",
                "cooling",
                "longevity",
                "firmware",
                "compatibility",
            ],
            "promotion_gate": "Physical comparison n>=3; do not promote without measured data",
            "not_in_main_bom": True,
            "hierarchy": "PRODUCT_EXPERIMENT",
        },
        {
            "id": "EXP-P100-AI-001",
            "branch": "hardware/exp-student-p100-ai",
            "title": "Student P132/P132i AI-first vs 8840U mainline",
            "hypothesis": "Higher NPU prioritization beats 8840U for gunnchAI local workloads without unacceptable GPU/game/battery regression",
            "baseline": "Ryzen Embedded 8840U Platform Core",
            "variant": "Ryzen AI Embedded P132 / P132i-class (PENDING_VENDOR_CONFIRMATION)",
            "metrics": [
                "npu_perf",
                "gunnchai_local",
                "cpu",
                "gpu",
                "battery",
                "usb4",
                "networking",
                "memory_options",
                "thermal",
                "windows_linux",
                "game_perf",
                "board_complexity",
            ],
            "promotion_gate": "Physical comparison; AI-first SKU only after evidence; does not replace mainline now",
            "not_in_main_bom": True,
            "hierarchy": "PRODUCT_EXPERIMENT",
        },
    ]

    # Rewrite existing experiment baselines toward custom mainline where compute-related
    existing = [
        {
            "id": "EXP-ARM-IQX-001",
            "branch": "hardware/exp-arm-iqx",
            "title": "ARM IQX-class SoM vs custom AMD Platform Core v1",
            "hypothesis": "ARM SoM reduces idle power and BOM cost at equal desk productivity vs owned custom AMD motherboard",
            "baseline": "CUSTOM AMD Platform Core v1 (8840U/8845HS)",
            "variant": "ARM IQX-class SoM (vendor TBD — PENDING_VENDOR_CONFIRMATION)",
            "metrics": ["idle_power_w", "sustained_compile_time_s", "thermal_skin_c", "bom_delta_usd_quote", "os_driver_gap_count", "ownership_score"],
            "promotion_gate": "All metrics meet or beat baseline on EVT sample n>=3 AND Device OS RC1 interface register shows zero P0 breaks; owner accepts reduced x86 ownership",
            "not_in_main_bom": True,
            "hierarchy": "REFERENCE_CONTROL_COMPARE",
        },
        {
            "id": "EXP-STUDENT-OLED-001",
            "branch": "hardware/exp-student-oled",
            "title": "Student OLED panel vs IPS",
            "hypothesis": "OLED improves contrast/weight without exceeding power/thermal budget",
            "baseline": "IPS eDP panel on custom Student-MB-v1",
            "variant": "OLED eDP panel class",
            "metrics": ["contrast_ratio", "avg_power_w", "burnin_risk_score", "cost_delta_usd", "nit_hdr"],
            "promotion_gate": "Power <= IPS+10% at 200 nits office; burn-in mitigation plan owner-approved",
            "not_in_main_bom": True,
            "hierarchy": "PRODUCT_EXPERIMENT",
        },
        {
            "id": "EXP-DSXL-OLED-HYBRID-001",
            "branch": "hardware/exp-dsxl-oled-hybrid",
            "title": "DS-XL OLED+IPS hybrid vs dual IPS",
            "hypothesis": "Primary OLED + secondary IPS improves creator UX without dual-OLED cost/thermal",
            "baseline": "IPS eDP + DDI/DP on custom DSXL-MB-v1",
            "variant": "OLED primary + IPS secondary",
            "metrics": ["dual_edp_si_margin", "thermal_delta_c", "cost_delta_usd", "color_delta_e"],
            "promotion_gate": "SI margin maintained on eDP+DDI/DP; do not mislabel as dual native eDP",
            "not_in_main_bom": True,
            "hierarchy": "PRODUCT_EXPERIMENT",
        },
        {
            "id": "EXP-DOCK-USB4-80-001",
            "branch": "hardware/exp-dock-usb4-80",
            "title": "Dock USB4 80 vs USB4 40",
            "hypothesis": "USB4 80 improves external display/storage UX enough to justify controller cost/SI risk",
            "baseline": "CUSTOM_GUNNCHOS_DOCK_GEN1 USB4 40 (JHL8440 + JHL9040R class)",
            "variant": "USB4 80-class controller (vendor TBD — PENDING_VENDOR_CONFIRMATION)",
            "metrics": ["link_rate_gbps", "eye_margin", "bom_delta_usd", "cable_interop_pass_rate"],
            "promotion_gate": "Measured eye margin; no mainline mix until DVT",
            "not_in_main_bom": True,
            "hierarchy": "PRODUCT_EXPERIMENT",
        },
        {
            "id": "EXP-RINGS-INDUCTIVE-001",
            "branch": "hardware/exp-rings-inductive-charge",
            "title": "Inductive ring charge vs magnetic cradle contacts",
            "hypothesis": "Inductive charge improves durability/UX with acceptable efficiency and EMI",
            "baseline": "Magnetic cradle pogo/contacts (custom ring mainline)",
            "variant": "Qi-class or proprietary inductive coil",
            "metrics": ["charge_efficiency_pct", "emi_delta_db", "wear_cycles", "alignment_fail_rate"],
            "promotion_gate": "Efficiency >=70% at EVT coil; EMI does not fail pre-scan relative to baseline",
            "not_in_main_bom": True,
            "hierarchy": "PRODUCT_EXPERIMENT",
        },
        {
            "id": "EXP-RINGS-SEMG-001",
            "branch": "hardware/exp-rings-semg-wrist",
            "title": "sEMG wrist band vs IMU/cap ring input",
            "hypothesis": "sEMG adds gesture bandwidth without unsafe skin current / privacy regression",
            "baseline": "IMU + capacitive/touch custom ring",
            "variant": "sEMG wrist accessory",
            "metrics": ["gesture_f1", "skin_current_ua", "false_positive_rate", "privacy_review_pass"],
            "promotion_gate": "Safety current limits met; youth privacy review pass; not medical claim",
            "not_in_main_bom": True,
            "hierarchy": "PRODUCT_EXPERIMENT",
        },
        {
            "id": "EXP-COREBOOT-001",
            "branch": "hardware/exp-coreboot",
            "title": "coreboot/openSIL vs vendor UEFI on custom Platform Core",
            "hypothesis": "Reproducible host firmware is achievable without blocking production on vendor UEFI/AGESA path",
            "baseline": "Vendor-supported UEFI + AGESA on custom AMD motherboard",
            "variant": "coreboot and/or AMD openSIL when production-capable for selected platform",
            "metrics": ["boot_time_s", "secure_boot_coverage", "repro_build", "platform_enablement_gaps"],
            "promotion_gate": "Must not block mainline; only promote after production-capable platform support",
            "not_in_main_bom": True,
            "hierarchy": "PRODUCT_EXPERIMENT",
        },
        {
            "id": "EXP-RAUC-001",
            "branch": "hardware/exp-rauc-update",
            "title": "RAUC A/B vs vendor capsule/EC update",
            "hypothesis": "RAUC improves update safety/ops for custom platforms vs vendor capsule-only flows",
            "baseline": "Vendor capsule + custom EC update orchestration",
            "variant": "RAUC A/B",
            "metrics": ["update_success_rate", "rollback_time_s", "bandwidth", "field_ops_complexity"],
            "promotion_gate": "No P0 Device OS RC1 breaks; measured field-ops improvement",
            "not_in_main_bom": True,
            "hierarchy": "PRODUCT_EXPERIMENT",
        },
    ]

    all_exps = existing + new_exps
    reg = {
        "schema": "gunnchos.hardware_v1.campaign.v1",
        "generated_at_utc": NOW,
        "campaign": CAMPAIGN,
        "hierarchy": {
            "mainline": "CUSTOM AMD EMBEDDED X86 MOTHERBOARD (Platform Core v1)",
            "simpler_reference_alternatives": [
                "COM-HPC Mini modular x86",
                "ARM/IQ-X SoM",
                "ODM-customized x86",
                "COTS dock",
                "nRF54L15 DK",
            ],
            "product_experiments": [
                "OLED",
                "USB4 80",
                "inductive ring charging",
                "sEMG",
                "coreboot/openSIL",
                "RAUC",
                "DS-XL X100",
                "Student P100 AI-first",
            ],
            "guiding_question": "Does the simpler or specialized variant outperform the custom mainline enough to justify giving up some control or increasing specialization?",
        },
        "experiments": all_exps,
    }
    wj(HV1 / "experiments" / "REGISTRY.json", reg)

    md = [
        "# Experiments registry",
        "",
        HDR,
        "",
        "## Hierarchy",
        "",
        "### Mainline",
        "`CUSTOM AMD EMBEDDED X86 MOTHERBOARD` (gunnchOS Platform Core v1)",
        "",
        "### Simpler/reference alternatives",
        "- COM-HPC Mini modular x86",
        "- ARM/IQ-X SoM",
        "- ODM-customized x86",
        "- COTS dock",
        "- nRF54L15 DK",
        "",
        "### Product experiments",
        "- OLED, USB4 80, inductive ring charging, sEMG, coreboot/openSIL, RAUC, DS-XL X100, Student P100 AI-first",
        "",
        "> Does the simpler or specialized variant outperform the custom mainline enough to justify giving up some control or increasing specialization?",
        "",
        "| ID | Branch | Baseline | Variant |",
        "|---|---|---|---|",
    ]
    for e in all_exps:
        md.append(f"| {e['id']} | `{e['branch']}` | {e['baseline']} | {e['variant']} |")
    w(HV1 / "experiments" / "REGISTRY.md", "\n".join(md) + "\n")

    for e in all_exps:
        d = HV1 / "experiments" / e["id"]
        d.mkdir(parents=True, exist_ok=True)
        pkg = dict(e)
        pkg.update(
            {
                "schema": "gunnchos.hardware_v1.experiment.v1",
                "generated_at_utc": NOW,
                "state": "EXPERIMENTAL_COMPARE",
                "campaign": CAMPAIGN,
            }
        )
        wj(d / "COMPARISON_PACKAGE.json", pkg)
        w(
            d / "COMPARISON_PACKAGE.md",
            f"""# {e['id']} comparison package

{HDR}

## Title
{e['title']}

## Hypothesis
{e['hypothesis']}

## Baseline (mainline)
{e['baseline']}

## Variant
{e['variant']}

## Metrics
{chr(10).join('- ' + m for m in e['metrics'])}

## Promotion gate
{e['promotion_gate']}

## Isolation
`not_in_main_bom=true` — experimental parts must not mix into MAINLINE_CUSTOM with qty>0.
""",
        )
        write_csv(
            d / "BOM_DELTA.csv",
            ["item", "baseline", "variant", "qty_delta", "class", "notes"],
            [
                {
                    "item": "compute_or_feature",
                    "baseline": e["baseline"][:80],
                    "variant": e["variant"][:80],
                    "qty_delta": "0",
                    "class": "EXPERIMENTAL",
                    "notes": "digital compare only; not purchased",
                }
            ],
        )
        w(
            d / "METRICS.md",
            f"""# {e['id']} metrics

{HDR}

All metrics `UNMEASURED_PENDING_PHYSICAL`.

{chr(10).join(f'- `{m}`: UNMEASURED_PENDING_PHYSICAL' for m in e['metrics'])}
""",
        )


def update_decision_ledger() -> None:
    path = HV1 / "decisions" / "DECISION_LEDGER.json"
    ledger = json.loads(path.read_text(encoding="utf-8"))
    # Pivot compute decisions
    by_id = {d["id"]: d for d in ledger["decisions"]}
    by_id["DEC-COMPUTE-001"] = {
        "id": "DEC-COMPUTE-001",
        "topic": "Student 14.5 / DS-XL compute (custom mainline)",
        "state": "ADOPTED_MAINLINE",
        "mainline": "gunnchOS Platform Core v1 — AMD Ryzen Embedded 8000 FP7r2 BGA custom motherboard (Student 8840U OPN ref 100-000001317E; DS-XL 8845HS OPN ref 100-000001316E). Pin compatibility NOT assumed.",
        "rationale": "HW1C custom-first doctrine: own the board around the silicon. COM-HPC Mini reclassified REFERENCE_CONTROL_MODULAR_X86.",
        "evidence": [
            "hardware_v1/custom_mainline/PLATFORM_CORE_V1.md",
            "hardware_v1/custom_mainline/DEVICE_SOC_SELECTION_MATRIX.md",
            "hardware_v1/custom_mainline/CUSTOM_FIRST_ARCHITECTURE_DOCTRINE.md",
        ],
        "experiment_alt": "EXP-ARM-IQX-001, EXP-COM-HPC-MODULAR-001, EXP-DSXL-X100-001, EXP-P100-AI-001",
        "owner_gate": "ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL",
        "secondary_state": "PENDING_VENDOR_CONFIRMATION",
    }
    by_id["DEC-COMPUTE-002"] = {
        "id": "DEC-COMPUTE-002",
        "topic": "Handheld Hybrid compute",
        "state": "ADOPTED_MAINLINE",
        "mainline": "Custom Handheld-MB-v1 with Ryzen Embedded 8840U (same family target as Student). COM-HPC Handheld mule = REFERENCE_CONTROL only.",
        "rationale": "Custom-first ownership; lower sustained power within supported envelope; compact topology pending vendor docs.",
        "evidence": [
            "hardware_v1/custom_mainline/DEVICE_SOC_SELECTION_MATRIX.md",
            "hardware_v1/custom_mainline/BOARD_REUSE_STRATEGY.md",
        ],
        "experiment_alt": "EXP-COM-HPC-MODULAR-001",
        "owner_gate": "ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL",
        "secondary_state": "PENDING_VENDOR_CONFIRMATION",
    }
    by_id["DEC-COMPUTE-003"] = {
        "id": "DEC-COMPUTE-003",
        "topic": "Handheld production board geometry",
        "state": "PENDING_PHYSICAL_MEASUREMENT",
        "mainline": "Handheld-MB-v1 geometry PENDING_PHYSICAL_MEASUREMENT after CPB0/EVT data",
        "rationale": "Cannot freeze production board without measured thermal/power/fit",
        "evidence": ["hardware_v1/custom_mainline/cpb0/PRD.md", "physical_evidence/README.md"],
        "experiment_alt": None,
        "owner_gate": "CPB0/EVT bring-up measurements",
    }
    by_id["DEC-STORAGE-001"]["mainline"] = (
        "M.2 NVMe + M.2 Key E Wi-Fi on custom Platform Core boards (field replaceable where packaging permits)"
    )
    by_id["DEC-STORAGE-001"]["rationale"] = "Custom motherboard ownership of PCIe/NVMe/Wi-Fi integration"
    # Add new decisions
    extras = [
        {
            "id": "DEC-DOCTRINE-001",
            "topic": "Architecture doctrine",
            "state": "ADOPTED_MAINLINE",
            "mainline": "MAINLINE_CUSTOM owns board around silicon; COTS/modular = REFERENCE_CONTROL; experiments need measured evidence to promote",
            "rationale": "Owner-directed HW1C custom-first pivot",
            "evidence": ["hardware_v1/custom_mainline/CUSTOM_FIRST_ARCHITECTURE_DOCTRINE.md"],
            "experiment_alt": None,
            "owner_gate": None,
        },
        {
            "id": "DEC-COMHPC-001",
            "topic": "COM-HPC role",
            "state": "EXPERIMENTAL_COMPARE",
            "mainline": "ADLINK COM-HPC Mini mMTL + Mini Base classified REFERENCE_CONTROL_MODULAR_X86 (not product mainline)",
            "rationale": "Preserve RP0-A COTS packet for software/bring-up isolation; optional owner order",
            "evidence": [
                "hardware_v1/reference_platform_0/REFERENCE_PLATFORM_0.md",
                "hardware_v1/bom/REFERENCE_CONTROL_BOM.csv",
            ],
            "experiment_alt": "EXP-COM-HPC-MODULAR-001",
            "owner_gate": "OPTIONAL_OWNER_ACTION=ORDER_RP0_A_COTS_CONTROL_KIT",
        },
        {
            "id": "DEC-CPB0-001",
            "topic": "Custom Platform Board 0",
            "state": "ADOPTED_MAINLINE",
            "mainline": "CPB0 debug-friendly learning board on 8845HS preferred; READY_FOR_FAB=false without collateral+EDA",
            "rationale": "Primary learning path for custom motherboard ownership",
            "evidence": ["hardware_v1/custom_mainline/cpb0/PRD.md"],
            "experiment_alt": None,
            "owner_gate": "ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL",
            "secondary_state": "PENDING_VENDOR_CONFIRMATION",
        },
        {
            "id": "DEC-MEMORY-001",
            "topic": "DDR topology",
            "state": "PENDING_VENDOR_CONFIRMATION",
            "mainline": "UNFROZEN — prefer debug-friendly on CPB0, serviceability on Student, capacity on DS-XL, compactness on Handheld if vendor allows",
            "rationale": "Must not freeze without AMD topology rules",
            "evidence": ["hardware_v1/custom_mainline/MEMORY_TOPOLOGY_DECISION.md"],
            "experiment_alt": None,
            "owner_gate": "AMD DDR topology collateral",
        },
        {
            "id": "DEC-FW-001",
            "topic": "Host firmware path",
            "state": "ADOPTED_MAINLINE",
            "mainline": "Vendor-supported UEFI/AGESA + Secure Boot + TPM; Zephyr+MCUboot EC; coreboot/openSIL experimental only",
            "rationale": "Do not make open firmware a production blocker",
            "evidence": ["hardware_v1/custom_mainline/FIRMWARE_OWNERSHIP_BOUNDARY.md"],
            "experiment_alt": "EXP-COREBOOT-001",
            "owner_gate": None,
        },
    ]
    # rebuild ordered list: extras first for doctrine visibility, then rest
    ordered_ids = [
        "DEC-DOCTRINE-001",
        "DEC-COMPUTE-001",
        "DEC-COMPUTE-002",
        "DEC-COMPUTE-003",
        "DEC-CPB0-001",
        "DEC-COMHPC-001",
        "DEC-MEMORY-001",
        "DEC-FW-001",
    ]
    decisions = []
    seen = set()
    for i in ordered_ids:
        if i in by_id:
            decisions.append(by_id[i])
            seen.add(i)
        else:
            for e in extras:
                if e["id"] == i:
                    decisions.append(e)
                    seen.add(i)
    for e in extras:
        if e["id"] not in seen:
            decisions.append(e)
            seen.add(e["id"])
    for d in ledger["decisions"]:
        if d["id"] not in seen:
            # update display decision note about COM-HPC if needed
            if d["id"] == "DEC-DISPLAY-001":
                d = dict(d)
                d["mainline"] = (
                    "IPS LCD panels on custom Platform Core boards "
                    "(Student: single eDP; DS-XL: one native eDP + DDI/DP). "
                    "Not dual native eDP unless authoritative SoC docs prove it."
                )
                d["rationale"] = (
                    "Preserve HW1B architecture correction; apply to custom AMD boards. OLED remains experiment."
                )
            decisions.append(d)
            seen.add(d["id"])
    ledger["decisions"] = decisions
    ledger["generated_at_utc"] = NOW
    ledger["campaign"] = CAMPAIGN
    wj(path, ledger)

    # Markdown mirror (compact)
    lines = ["# Decision ledger", "", HDR, ""]
    for d in decisions:
        lines += [
            f"## {d['id']} — {d['topic']}",
            f"- **state:** `{d['state']}`",
            f"- **mainline:** {d['mainline']}",
            f"- **rationale:** {d.get('rationale','')}",
            "",
        ]
    w(HV1 / "decisions" / "DECISION_LEDGER.md", "\n".join(lines))


def update_reference_platform() -> None:
    w(
        HV1 / "reference_platform_0" / "REFERENCE_PLATFORM_0.md",
        f"""# Reference Platform 0 (reclassified)

{HDR}

## Role after HW1C

ADLINK COM-HPC Mini mMTL + Mini Base is **`REFERENCE_CONTROL_MODULAR_X86`**, not product mainline.

Uses:

- validate gunnchOS
- validate Windows compatibility
- establish USB4 behavior
- validate NVMe/Wi-Fi/cellular
- compare thermals/performance
- isolate custom motherboard failures
- provide fallback/demo platform

## Gates preserved

- `RP0_A_COTS_PROCUREMENT_PACKET_READY=true`
- `RP0_A_READY_TO_ORDER=true`

Owner intent rename: `OPTIONAL_REFERENCE_CONTROL_PURCHASE` / `OPTIONAL_OWNER_ACTION=ORDER_RP0_A_COTS_CONTROL_KIT`

This is **no longer** the main hardware milestone. Mainline learning board is **CPB0** (custom AMD).

## Stages

- **RP0-A:** COTS Integration Bench (unchanged procurement packet)
- **RP0-B:** historical custom COM-HPC carrier path — still vendor-gated; subordinated to Platform Core / CPB0 custom-first path

Do not delete HW1B public closures.
""",
    )
    rp0 = {
        "schema": "gunnchos.hardware_v1.rp0.v1",
        "classification": "REFERENCE_CONTROL_MODULAR_X86",
        "product_mainline": False,
        "READY_FOR_FAB": False,
        "RP0_B_CUSTOM_READY_FOR_FAB": False,
        "RP0_A_COTS_PROCUREMENT_PACKET_READY": True,
        "RP0_A_READY_TO_ORDER": True,
        "RP0_A_PHYSICAL_BUILD_PENDING": True,
        "RP0_A_BRINGUP_PENDING": True,
        "PHYSICAL_PENDING": True,
        "OPTIONAL_OWNER_ACTION": "ORDER_RP0_A_COTS_CONTROL_KIT",
        "stages": {
            "RP0_A": {
                "type": "COTS_INTEGRATION_BENCH",
                "role": "REFERENCE_CONTROL",
                "components": [
                    "adlink_com_hpc_mmtl_155h_32g",
                    "adlink_com_hpc_mini_base",
                    "nrf54l15_dk_pca10156",
                    "cots_usb4_dock",
                ],
            },
            "RP0_B": {
                "type": "CUSTOM_COM_HPC_CARRIER_HISTORICAL",
                "role": "DEFERRED_RELATIVE_TO_PLATFORM_CORE",
                "blockers": [
                    "EXT-COM-HPC-400PIN",
                    "EXT-JHL8440-BALLMAP",
                    "EXT-JHL9040R-BALLMAP",
                ],
            },
            "CPB0": {
                "type": "CUSTOM_PLATFORM_BOARD_0",
                "role": "MAINLINE_LEARNING_BOARD",
                "soc": "8845HS preferred",
                "READY_FOR_FAB": False,
            },
        },
        "generated_at_utc": NOW,
        "campaign": CAMPAIGN,
    }
    wj(HV1 / "reference_platform_0" / "REFERENCE_PLATFORM_0.json", rp0)

    # Annotate procurement guide intent
    guide = HV1 / "reference_platform_0" / "RP0_A_PROCUREMENT_GUIDE.md"
    if guide.is_file():
        text = guide.read_text(encoding="utf-8")
        banner = (
            f"\n\n## HW1C reclassification\n\n{HDR}\n"
            "This packet remains valid for **REFERENCE_CONTROL** purchase only.\n"
            "`OPTIONAL_OWNER_ACTION=ORDER_RP0_A_COTS_CONTROL_KIT`\n"
            "Preferred mainline owner action is `ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL`.\n"
            "Cursor will not purchase.\n"
        )
        if "HW1C reclassification" not in text:
            w(guide, text.rstrip() + banner)


def write_gates() -> None:
    learning_false = {
        "CUSTOM_SOC_PINMAP_UNDERSTOOD": False,
        "CUSTOM_POWER_TREE_UNDERSTOOD": False,
        "CUSTOM_DDR_TOPOLOGY_UNDERSTOOD": False,
        "CUSTOM_PCIE_TOPOLOGY_UNDERSTOOD": False,
        "CUSTOM_USB4_TOPOLOGY_UNDERSTOOD": False,
        "CUSTOM_DISPLAY_TOPOLOGY_UNDERSTOOD": False,
        "CUSTOM_EC_ARCHITECTURE_UNDERSTOOD": False,
        "CUSTOM_BOOT_CHAIN_UNDERSTOOD": False,
        "CUSTOM_DEBUG_ARCHITECTURE_UNDERSTOOD": False,
        "CUSTOM_MANUFACTURING_FLOW_UNDERSTOOD": False,
    }
    gates = {
        "schema": "gunnchos.hardware_v1.gates.v1",
        "generated_at_utc": NOW,
        "campaign": CAMPAIGN,
        "campaign_overlay": CAMPAIGN,
        # New custom mainline gates
        "CUSTOM_MAINLINE_ARCHITECTURE_FROZEN": True,
        "CUSTOM_PLATFORM_VENDOR_ACCESS_READY": False,
        **learning_false,
        "CPB0_SCHEMATIC_READY": False,
        "CPB0_PCB_READY": False,
        "CPB0_READY_FOR_FAB": False,
        "CUSTOM_MAINLINE_READY_FOR_EVT_BUILD": False,
        # Legacy alias
        "HARDWARE_V1_READY_FOR_EVT_BUILD": False,
        "HARDWARE_V1_DIGITAL_ARCHITECTURE_COMPLETE": True,
        "REFERENCE_PLATFORM_0_READY_FOR_FAB": False,
        "RP0_A_COTS_PROCUREMENT_PACKET_READY": True,
        "RP0_A_READY_TO_ORDER": True,
        "RP0_A_PHYSICAL_BUILD_PENDING": True,
        "RP0_A_BRINGUP_PENDING": True,
        "RP0_B_CUSTOM_READY_FOR_FAB": False,
        "PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING": True,
        "UNRES_NRF54L15_FOOTPRINT_CLOSED": True,
        "UNRES_FN990B40_AVL_CLOSED": True,
        "EXT_DSXL_DUAL_EDP_CLOSED": True,
        "EXT_COM_HPC_400PIN_RP0_A_BLOCKING": False,
        "EXT_COM_HPC_400PIN_RP0_B_BLOCKING": True,
        "EXT_JHL8440_BALLMAP_RP0_A_BLOCKING": False,
        "EXT_JHL8440_BALLMAP_RP0_B_BLOCKING": True,
        "EXT_JHL9040R_BALLMAP_RP0_A_BLOCKING": False,
        "EXT_JHL9040R_BALLMAP_RP0_B_BLOCKING": True,
        "EVT_PENDING": True,
        "DVT_PENDING": True,
        "PVT_PENDING": True,
        "PHYSICAL_HARDWARE_VALIDATED": False,
        "CERTIFICATION_COMPLETE": False,
        "MANUFACTURING_VALIDATED": False,
        "DIGITAL_FABRICATION_PASS": False,
        "RFQ_SENT": False,
        "PHYSICAL_PENDING": True,
        "EXTERNAL_PENDING": True,
        "DIGITAL_ARCHITECTURE_PACKAGE_COMPLETE": True,
        "MAINLINE_DECISION_LEDGER_COMPLETE": True,
        "EXPERIMENTS_REGISTRY_COMPLETE": True,
        "SOFTWARE_RC1_BASELINES_UNTOUCHED": True,
        "COM_HPC_IS_PRODUCT_MAINLINE": False,
        "COM_HPC_CLASSIFICATION": "REFERENCE_CONTROL_MODULAR_X86",
        "MAINLINE_COMPUTE": "CUSTOM_AMD_PLATFORM_CORE_V1",
        "blockers": [
            {
                "id": "EXT-AMD-CUSTOM-COLLATERAL",
                "severity": "AMD Ryzen Embedded 8000 custom platform collateral (pinout/power/DDR/USB4/display/boot/SI/reference design)",
                "classification": "OWNER_ACTION_REQUIRED",
                "blocks": [
                    "CUSTOM_PLATFORM_VENDOR_ACCESS_READY",
                    "CPB0_READY_FOR_FAB",
                    "CUSTOM_MAINLINE_READY_FOR_EVT_BUILD",
                    "HARDWARE_V1_READY_FOR_EVT_BUILD",
                ],
            },
            {
                "id": "EXT-AMD-EDA-OUTPUTS",
                "severity": "Net-accurate schematic/PCB/DRC/ERC/SI-PI outputs for CPB0",
                "classification": "OWNER_ACTION_REQUIRED",
                "blocks": ["CPB0_SCHEMATIC_READY", "CPB0_PCB_READY", "CPB0_READY_FOR_FAB"],
            },
            {
                "id": "EXT-COM-HPC-400PIN",
                "severity": "PICMG/ADLINK COM-HPC Mini net-accurate pin map for historical RP0-B carrier",
                "classification": "STILL_VENDOR_GATED_FOR_RP0_B",
                "blocks": ["RP0_B_CUSTOM_READY_FOR_FAB", "REFERENCE_PLATFORM_0_READY_FOR_FAB"],
                "rp0_a_blocking": False,
                "rp0_b_blocking": True,
            },
            {
                "id": "EXT-JHL8440-BALLMAP",
                "severity": "Intel JHL8440 ball map (NDA) for pin-accurate custom dock fanout",
                "classification": "STILL_VENDOR_GATED_FOR_RP0_B",
                "blocks": ["DOCK_HW_DIGITAL_RELEASE_PACKAGE"],
                "rp0_a_blocking": False,
                "rp0_b_blocking": True,
            },
            {
                "id": "EXT-JHL9040R-BALLMAP",
                "severity": "Intel JHL9040R retimer ball map (NDA)",
                "classification": "STILL_VENDOR_GATED_FOR_RP0_B",
                "blocks": ["DOCK_HW_DIGITAL_RELEASE_PACKAGE"],
                "rp0_a_blocking": False,
                "rp0_b_blocking": True,
            },
        ],
        "closed_blockers": [
            {
                "id": "EXT-DSXL-DUAL-EDP",
                "classification": "CLOSED_BY_ARCHITECTURE_CHANGE",
                "evidence": "hardware_v1/devices/ds_xl/DUAL_DISPLAY_ARCHITECTURE.md",
            },
            {
                "id": "UNRES-NRF54L15-FOOTPRINT",
                "classification": "CLOSED_PUBLIC_EVIDENCE",
                "evidence": "hardware_v1/devices/rings/NRF54L15_PACKAGE_STRATEGY.md",
            },
            {
                "id": "UNRES-FN990B40-AVL",
                "classification": "CLOSED_PUBLIC_EVIDENCE",
                "evidence": "hardware_v1/radio/FN990B40_RP0_A_AVL.md",
            },
        ],
        "NEXT_OWNER_ACTION": "ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL",
        "OPTIONAL_OWNER_ACTION": "ORDER_RP0_A_COTS_CONTROL_KIT",
        "NEXT_OWNER_ACTION_NOTE": (
            "Preferred: acquire AMD custom platform collateral for Platform Core / CPB0. "
            "Optional parallel: order RP0-A COTS control kit. Cursor will not purchase or accept NDAs. "
            "COTS readiness must not flip CUSTOM_MAINLINE_READY_FOR_EVT_BUILD."
        ),
        "NEXT_GATE": None,
        "legacy_alias": {
            "HARDWARE_V1_READY_FOR_EVT_BUILD": "CUSTOM_MAINLINE_READY_FOR_EVT_BUILD",
            "REFERENCE_PLATFORM_0_READY_FOR_FAB": "RP0_B_CUSTOM_READY_FOR_FAB",
        },
    }
    wj(HV1 / "GATES.json", gates)

    md_lines = [
        "# Hardware v1 gates (HW1C)",
        "",
        HDR,
        "",
        "| Token | Value |",
        "|---|---|",
    ]
    for k, v in gates.items():
        if k in {"schema", "generated_at_utc", "campaign", "campaign_overlay", "blockers", "closed_blockers", "legacy_alias", "NEXT_OWNER_ACTION_NOTE"}:
            continue
        if isinstance(v, bool):
            md_lines.append(f"| `{k}` | `{str(v).lower()}` |")
        elif isinstance(v, (str, type(None))):
            md_lines.append(f"| `{k}` | `{v}` |")
    md_lines += [
        "",
        f"**Note:** {gates['NEXT_OWNER_ACTION_NOTE']}",
        "",
        "`HARDWARE_V1_READY_FOR_EVT_BUILD` aliases `CUSTOM_MAINLINE_READY_FOR_EVT_BUILD`. COTS cannot flip it true.",
    ]
    w(HV1 / "GATES.md", "\n".join(md_lines) + "\n")


def write_owner_packet() -> None:
    w(
        HV1 / "OWNER_ACTION_PACKET.md",
        f"""# Owner action packet

{HDR}

## What Cursor completed (digital)
- Custom-first architecture doctrine + Platform Core v1
- Device SoC selection matrix (8840U / 8845HS candidates)
- CPB0 learning board digital package (not fab-ready)
- AMD custom platform access packet + owner steps
- Firmware ownership boundary; memory topology UNFROZEN
- COM-HPC reclassified REFERENCE_CONTROL; RP0-A packet preserved
- BOM class split MAINLINE_CUSTOM / REFERENCE_CONTROL / EXPERIMENTAL
- Knowledge map, learning gates, complexity register
- Experiment hierarchy + EXP-COM-HPC-MODULAR / EXP-DSXL-X100 / EXP-P100-AI packages
- Gate model: CUSTOM_MAINLINE_READY_FOR_EVT_BUILD (aliases HARDWARE_V1_READY_FOR_EVT_BUILD)
- HW1B public closures preserved

## What Cursor did NOT do
- Send RFQs / purchase / contact suppliers / accept NDAs
- Invent AMD pin/power/DDR restricted collateral
- Claim physical validation, certification, or fab release
- Merge any PR
- Modify software RC1 baselines
- Fabricate Gerbers/ODB++/quotes

## Preferred next action
`NEXT_OWNER_ACTION=ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL`

## Optional parallel action
`OPTIONAL_OWNER_ACTION=ORDER_RP0_A_COTS_CONTROL_KIT`

## Honest gate highlights
- `CUSTOM_MAINLINE_READY_FOR_EVT_BUILD=false`
- `HARDWARE_V1_READY_FOR_EVT_BUILD=false`
- `CPB0_READY_FOR_FAB=false`
- `CUSTOM_PLATFORM_VENDOR_ACCESS_READY=false`
- Learning gates all `false` where collateral missing
- `RP0_A_COTS_PROCUREMENT_PACKET_READY=true` / `RP0_A_READY_TO_ORDER=true` (reference control only)
""",
    )


def write_dock_rings_notes() -> None:
    dock = HV1 / "dock" / "DOCK_PRD.md"
    if dock.is_file():
        t = dock.read_text(encoding="utf-8")
        if "HW1C" not in t:
            w(
                dock,
                t.rstrip()
                + f"\n\n## HW1C classification\n\n{HDR}\n"
                "- Production-intent mainline: `CUSTOM_GUNNCHOS_DOCK_GEN1`\n"
                "- COTS TB4/USB4 dock: `REFERENCE_CONTROL_DOCK`\n"
                "- JHL8440/JHL9040R ball maps remain external blockers for pin-accurate custom dock\n"
                "- Do not demote custom Dock because COTS control is easier\n",
            )
    rings = HV1 / "rings" / "RINGS_PRD.md"
    if rings.is_file():
        t = rings.read_text(encoding="utf-8")
        if "HW1C" not in t:
            w(
                rings,
                t.rstrip()
                + f"\n\n## HW1C classification\n\n{HDR}\n"
                "- Ring remains fully custom mainline (nRF54L15, IMU, sense, power, antenna, Zephyr, MCUboot, enclosure)\n"
                "- nRF54L15 DK = `REFERENCE_CONTROL_RING` (not product mainline)\n"
                "- Keep inductive / sEMG experiments\n",
            )


def update_manifest() -> None:
    path = HV1 / "MANIFEST.json"
    if path.is_file():
        m = json.loads(path.read_text(encoding="utf-8"))
    else:
        m = {}
    m.update(
        {
            "campaign": CAMPAIGN,
            "generated_at_utc": NOW,
            "mainline_compute": "CUSTOM_AMD_PLATFORM_CORE_V1",
            "com_hpc_classification": "REFERENCE_CONTROL_MODULAR_X86",
            "custom_mainline_dir": "hardware_v1/custom_mainline/",
            "next_owner_action": "ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL",
            "optional_owner_action": "ORDER_RP0_A_COTS_CONTROL_KIT",
        }
    )
    wj(path, m)


def write_report() -> None:
    w(
        HV1 / "REPORT_SECTION_24_HW1C_A_TO_Z.md",
        f"""# HW1C final report A–Z

{HDR}

## A. #68 starting/final head
Starting (expected): `3730a98bb1285a86553cf4e38f5c7c6e4406a049` (no drift at preflight).  
Final: see git after push on `hardware/v1-mainline-ready-for-evt` (DRAFT #68).

## B. Architecture doctrine pivot
`hardware_v1/custom_mainline/CUSTOM_FIRST_ARCHITECTURE_DOCTRINE.md` — MAINLINE_CUSTOM / REFERENCE_CONTROL / EXPERIMENTAL_VARIANT.

## C. Mainline custom compute family
gunnchOS Platform Core v1 — AMD Ryzen Embedded 8000 FP7r2 BGA.

## D. Student SoC
8840U (`100-000001317E` public OPN ref) — PENDING_VENDOR_CONFIRMATION for pin/power/DDR.

## E. Handheld SoC
8840U same family; COM-HPC mule = REFERENCE_CONTROL only.

## F. DS-XL SoC
8845HS (`100-000001316E` public OPN ref) — pin compatibility with 8840U NOT assumed.

## G. CPB0 architecture
Debug-friendly Custom Platform Board 0; 8845HS preferred; digital package under `custom_mainline/cpb0/`; not fab-ready.

## H. AMD collateral needs
`hardware_v1/vendor_access/AMD_CUSTOM_PLATFORM_ACCESS_PACKET.md` — PUBLIC/LOGIN/PARTNER/NDA/IBV/UNKNOWN classifications; no invented restricted data.

## I. AMD owner-access steps
Developer Hub → partner/sales → NDA/partner workflow (owner only) → IBV/BIOS inquiry. Cursor does not submit agreements.

## J. Firmware ownership boundary
Vendor UEFI/AGESA mainline; Zephyr+MCUboot EC; coreboot/openSIL experimental only.

## K. Memory topology plan
UNFROZEN — CPB0 debug-friendly preference; product intents documented; `CUSTOM_DDR_TOPOLOGY_UNDERSTOOD=false`.

## L. COM-HPC reclassification
`REFERENCE_CONTROL_MODULAR_X86` — not product mainline.

## M. RP0-A status
Procurement packet preserved; `RP0_A_COTS_PROCUREMENT_PACKET_READY=true`; `RP0_A_READY_TO_ORDER=true`; optional order only.

## N. DS-XL X100 experiment
`EXP-DSXL-X100-001` package created.

## O. P100 AI experiment
`EXP-P100-AI-001` package created.

## P. Custom Dock mainline
`CUSTOM_GUNNCHOS_DOCK_GEN1` remains mainline; COTS dock = REFERENCE_CONTROL_DOCK.

## Q. Custom Ring mainline
Custom nRF54L15 ring remains mainline; DK = REFERENCE_CONTROL_RING.

## R. BOM class split
MAINLINE_CUSTOM / REFERENCE_CONTROL / EXPERIMENTAL / DEFERRED_GEN2 with fail-closed isolation.

## S. Knowledge map
`hardware_v1/custom_mainline/KNOWLEDGE_MAP.md`

## T. Learning gates
All understanding gates false where AMD collateral missing (see GATES.json).

## U. Complexity register
`hardware_v1/custom_mainline/CUSTOM_MAINLINE_COMPLEXITY_REGISTER.md`

## V. Existing experimental PR refresh
#69–#76 refreshed onto updated #68 head after push (DRAFT, unmerged).

## W. New experimental PRs
DRAFT PRs for COM-HPC modular / DSXL-X100 / P100-AI opened only with real packages (see campaign closeout).

## X. Validation
`make hardware-v1-validate` / `make hardware-v1-all` — see closeout log.

## Y. Remaining blockers
AMD custom collateral + EDA for CPB0; dock JHL ballmaps for pin-accurate custom dock; cellular antenna design pending; physical EVT/DVT/PVT pending.

## Z. Exactly one next owner action
`NEXT_OWNER_ACTION=ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL`  
Optional: `OPTIONAL_OWNER_ACTION=ORDER_RP0_A_COTS_CONTROL_KIT`

## Printed tokens
See `hardware_v1/GATES.json` / campaign closeout.
""",
    )


def write_readme_pointer() -> None:
    readme = HV1 / "README.md"
    if readme.is_file():
        t = readme.read_text(encoding="utf-8")
        if "HW1C" not in t and "Platform Core" not in t:
            w(
                readme,
                t.rstrip()
                + f"\n\n## HW1C custom-first pivot\n\n{HDR}\n"
                "- Product mainline compute: **gunnchOS Platform Core v1** (custom AMD Ryzen Embedded 8000 FP7r2)\n"
                "- COM-HPC Mini path: **REFERENCE_CONTROL_MODULAR_X86** (RP0-A packet preserved)\n"
                "- Learning board: **CPB0** (`hardware_v1/custom_mainline/cpb0/`)\n"
                "- Doctrine: `hardware_v1/custom_mainline/CUSTOM_FIRST_ARCHITECTURE_DOCTRINE.md`\n"
                "- Preferred owner action: `ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL`\n",
            )


def main() -> int:
    write_doctrine()
    write_platform_core()
    write_soc_matrix()
    write_blocks_and_reuse()
    write_cpb0()
    write_amd_access()
    write_firmware_memory()
    write_knowledge_map()
    write_complexity()
    write_learning_gates_doc()
    write_boms()
    write_experiments()
    update_decision_ledger()
    update_reference_platform()
    write_gates()
    write_owner_packet()
    write_dock_rings_notes()
    update_manifest()
    write_report()
    write_readme_pointer()
    print(f"HW1C_GENERATE: OK @ {NOW}")
    print("CUSTOM_MAINLINE_ARCHITECTURE_FROZEN=true")
    print("CUSTOM_MAINLINE_READY_FOR_EVT_BUILD=false")
    print("NEXT_OWNER_ACTION=ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
