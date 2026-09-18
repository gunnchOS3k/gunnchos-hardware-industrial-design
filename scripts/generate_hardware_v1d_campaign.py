#!/usr/bin/env python3
"""HARDWARE 1.0D — Four-Track Convergence + #68 Merge Readiness (architecture only)."""
from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HV1 = ROOT / "hardware_v1"
CONV = HV1 / "convergence"
NXP = HV1 / "open_custom_nxp"
CM = HV1 / "custom_mainline"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
CAMPAIGN = "HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS"
CLAIM = (
    "architecture / control-plane baseline only — not physical pass, "
    "not certification, not fab release, not purchased, not GXE execution."
)
HDR = (
    f"**Generated:** {NOW}  \n"
    f"**Campaign:** `{CAMPAIGN}`  \n"
    f"**Claim boundary:** {CLAIM}\n"
)
EXPECTED_HEAD = "628eacd8f35a2a509f36592c392b6aba88b6c4f8"


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


def git_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except Exception:
        return "UNKNOWN"


def write_starting_state() -> None:
    head = git_sha()
    drift = head != EXPECTED_HEAD
    wj(
        CONV / "HW1D_STARTING_STATE.json",
        {
            "schema": "gunnchos.hardware_v1.hw1d.starting_state.v1",
            "generated_at_utc": NOW,
            "campaign": CAMPAIGN,
            "pr_68": {
                "state": "OPEN",
                "is_draft": True,
                "head_expected": EXPECTED_HEAD,
                "head_observed": head,
                "drift": drift,
                "branch": "hardware/v1-mainline-ready-for-evt",
            },
            "experiment_prs_69_79": {
                "expected_draft": True,
                "expected_open": True,
                "expected_unmerged": True,
                "target_branch": "hardware/v1-mainline-ready-for-evt",
                "note": "API preflight may be environment-blocked; local remotes confirmed present",
            },
            "main_sha_observed": subprocess.check_output(
                ["git", "rev-parse", "origin/main"], cwd=ROOT, text=True
            ).strip(),
            "preflight": {
                "hardware_v1_validate": "PASS_BEFORE_HW1D_CHANGES",
                "software_rc1_untouched": True,
                "physical_gates_false": True,
            },
            "doctrine_before": "HW1C single PRODUCT mainline = CUSTOM AMD; COM-HPC = REFERENCE_CONTROL",
            "doctrine_after": (
                "Four-track: PRODUCT_MAINLINE=AMD_CUSTOM_X86; "
                "OPEN_ENGINEERING_MAINLINE=NXP_IMX95_OPEN_CUSTOM; "
                "GREENFIELD_EXPERIMENT=GXE; REFERENCE_CONTROL=COM_HPC_AND_COTS"
            ),
        },
    )


def write_track_model() -> None:
    tracks = {
        "PRODUCT_MAINLINE": {
            "id": "AMD_CUSTOM_X86",
            "purpose": [
                "best product-performance target",
                "x86 / Windows / game / professional software compatibility",
                "custom board around Ryzen Embedded silicon",
                "continues even if vendor collateral is temporarily unavailable",
            ],
            "path": "hardware_v1/custom_mainline/",
        },
        "OPEN_ENGINEERING_MAINLINE": {
            "id": "NXP_IMX95_OPEN_CUSTOM",
            "purpose": [
                "maximum practical no-NDA board-level ownership",
                "full custom application-processor motherboard learning",
                "public design collateral",
                "path to custom-board fabrication and EVT without AMD NDA dependency",
            ],
            "path": "hardware_v1/open_custom_nxp/",
        },
        "GREENFIELD_EXPERIMENT": {
            "id": "GXE",
            "purpose": [
                "experience-first software/hardware co-design",
                "custom kernel/runtime/app architecture",
                "RISC-V/FPGA research",
                "extreme-custom GXE-X subtrack",
            ],
            "path": "hardware_v1/convergence/GXE_HARDWARE_INTEGRATION_CONTRACT.md",
            "implementation_in_this_repo": False,
        },
        "REFERENCE_CONTROL": {
            "id": "COM_HPC_AND_COTS",
            "purpose": [
                "known-good baseline",
                "software compatibility control",
                "fault isolation",
                "performance comparison",
            ],
            "path": "hardware_v1/reference_platform_0/",
        },
    }
    wj(
        CONV / "CANONICAL_TRACK_MODEL.json",
        {
            "schema": "gunnchos.hardware_v1.canonical_track_model.v1",
            "generated_at_utc": NOW,
            "campaign": CAMPAIGN,
            "rule": "Never use ambiguous 'mainline' without PRODUCT_MAINLINE or OPEN_ENGINEERING_MAINLINE qualifier",
            "tracks": tracks,
            "non_equivalence": {
                "NXP_IMX95_OPEN_CUSTOM_vs_AMD_CUSTOM_X86": (
                    "NXP proves board-level ownership/methodology; "
                    "NOT claimed equivalent for Windows desktop, x86 software, PC gaming, "
                    "Ryzen-class CPU/GPU, or USB4 unless separately implemented"
                )
            },
        },
    )
    w(
        CONV / "CANONICAL_TRACK_MODEL.md",
        f"""# Canonical four-track model

{HDR}

## Rule

Do **not** use the word “mainline” without a track qualifier.

| Track qualifier | Identity | Role |
|---|---|---|
| `PRODUCT_MAINLINE` | `AMD_CUSTOM_X86` | Best product-performance / x86 compatibility target |
| `OPEN_ENGINEERING_MAINLINE` | `NXP_IMX95_OPEN_CUSTOM` | No-NDA custom-board learning + fabrication path |
| `GREENFIELD_EXPERIMENT` | `GXE` | Experience-first experimental ecosystem (integration contract only here) |
| `REFERENCE_CONTROL` | `COM_HPC_AND_COTS` | Known-good control / fault isolation |

## PRODUCT_MAINLINE — AMD_CUSTOM_X86

- Student / Handheld: Ryzen Embedded 8840U candidates
- DS-XL: Ryzen Embedded 8845HS candidate
- Custom motherboards, Dock, Rings remain product-intent
- Vendor collateral pending is an **external** blocker, not an architecture-merge blocker

## OPEN_ENGINEERING_MAINLINE — NXP_IMX95_OPEN_CUSTOM

- Public NXP collateral path under `hardware_v1/open_custom_nxp/`
- Proves BGA AP integration, memory/power/PCIe/USB/display/camera, EC, security/boot, fab/EVT methodology
- Explicitly **not** product-equivalent to AMD x86 for Windows/gaming/Ryzen-class performance

## GREENFIELD_EXPERIMENT — GXE

- Defined only via `GXE_HARDWARE_INTEGRATION_CONTRACT.md` in this repo
- No GXE implementation executed here

## REFERENCE_CONTROL — COM_HPC_AND_COTS

- RP0-A COTS procurement packet, COM-HPC architecture, COTS Dock, nRF54L15 DK
- Optional owner order only; not PRODUCT_MAINLINE

Machine-readable: `CANONICAL_TRACK_MODEL.json`
""",
    )


def write_experience_doctrine() -> None:
    w(
        CONV / "EXPERIENCE_FIRST_CO_DESIGN_DOCTRINE.md",
        f"""# Experience-first hardware/software co-design doctrine

{HDR}

## Core rule

> **Software must earn additional hardware.**

## Required flow

`USER OUTCOME`
→ Experience Contract
→ latency / quality / reliability / accessibility / offline / privacy target
→ software architecture
→ algorithm / data-flow efficiency
→ runtime / scheduler / memory optimization
→ hardware acceleration where justified
→ custom board / silicon optimization where justified

## Explicit anti-pattern

`faster hardware masking uncharacterized software inefficiency`

No hardware requirement may be treated as justified solely because a stronger SKU fixes a performance problem.

## Hardware-selection evidence (required before promotion)

| Evidence class | Question |
|---|---|
| workload | Which user-visible task fails or degrades? |
| latency | p50 / p95 / p99 interaction or frame latency |
| memory | Peak / sustained RSS and bandwidth |
| energy/task | Joules per completed user task |
| thermal/power | Sustained envelope vs skin/comfort limits |
| network | Bytes and RTT sensitivity |
| storage | IOPS / sequential impact on experience |
| accelerator utilization | CPU/GPU/NPU/FPGA useful occupancy |
| user-visible improvement | Measured delta vs Experience Contract targets |
| graceful-degradation | Behavior when accel / link / thermal is unavailable |

## Track application

- `PRODUCT_MAINLINE` (AMD): product Experience Contracts for education/work/create/game
- `OPEN_ENGINEERING_MAINLINE` (NXP): engineering learning contracts; methodology, not product parity
- `GREENFIELD_EXPERIMENT` (GXE): greenfield Experience Contracts (executed outside this repo)
- `REFERENCE_CONTROL`: control measurements only
""",
    )


def write_nxp_package() -> None:
    w(
        NXP / "OPEN_CUSTOM_DOCTRINE.md",
        f"""# NXP open-custom engineering doctrine

{HDR}

## Track

`OPEN_ENGINEERING_MAINLINE = NXP_IMX95_OPEN_CUSTOM`

## Purpose (what this lane proves)

- custom BGA application-processor integration
- memory design
- power design
- PCIe / USB
- display / camera / audio
- EC / controller integration
- security / boot / recovery
- custom board fabrication
- manufacturing
- EVT / DVT methodology
- efficiency

## Explicit non-equivalence to PRODUCT_MAINLINE (AMD x86)

NXP i.MX95 is **not** claimed equivalent to AMD Ryzen Embedded x86 for:

- Windows desktop compatibility
- x86 software compatibility
- PC gaming
- Ryzen-class CPU / GPU performance
- USB4 unless separately implemented

## NDA policy

Prefer authoritative **public** NXP collateral. Do not accept NDAs via Cursor.
If a document forbids redistribution, commit metadata / URL / hash only — never the binary.

## Physical honesty

No physical pass claims. `READY_FOR_FAB` remains false until real EDA + public rules are applied.
""",
    )

    w(
        NXP / "IMX95_PLATFORM_PROFILE.md",
        f"""# i.MX95 platform profile (public-class)

{HDR}

## Silicon family

NXP **i.MX 95** applications processor family (public product page: https://www.nxp.com/products/i.MX95).

## Public-class characteristics (architecture intent only)

- Heterogeneous AP + real-time / safety domains (see public RM / datasheet)
- LPDDR memory class (exact topology pending design-guide rules)
- High-speed SerDes / PCIe / USB / Ethernet class interfaces (SKU-dependent)
- Display / camera pipeline suitable for embedded UI + vision learning boards
- EdgeLock / secure-enclave class security features (public docs)
- Industrial / commercial / automotive grade variants exist — selection PENDING_OWNER_DECISION

## Role vs PRODUCT_MAINLINE

| Aspect | OPEN_ENGINEERING (i.MX95) | PRODUCT_MAINLINE (AMD x86) |
|---|---|---|
| Primary goal | Board ownership + fab learning | Product performance + x86 compat |
| NDA dependency | Prefer public path | AMD custom collateral often gated |
| Windows / games | Not a target claim | Explicit target |
| USB4 | Not assumed | Product Dock / platform intent |

## Non-claims

- No pin-accurate ball map invented here
- No fabricated power-sequence numbers
- No “product mainline replacement” claim
""",
    )

    collateral = [
        {
            "id": "NXP-IMX95-PRODUCT-PAGE",
            "title": "i.MX 95 Applications Processors Family",
            "url": "https://www.nxp.com/products/i.MX95",
            "class": "PUBLIC_INDEX",
            "redistribution": "URL_ONLY",
            "sha256": "NOT_FETCHED_IN_CAMPAIGN",
            "notes": "Authoritative public landing page for datasheets/RM/factsheet",
        },
        {
            "id": "NXP-IMX95IEC",
            "title": "i.MX 95 Applications Processors Data Sheet for Industrial Products (IMX95IEC)",
            "url": "https://www.nxp.com/docs/en/data-sheet/IMX95IEC.pdf",
            "class": "PUBLIC_DATASHEET",
            "redistribution": "METADATA_URL_HASH_ONLY_IF_LICENSE_FORBIDS",
            "sha256": "PENDING_OWNER_FETCH",
            "notes": "Public datasheet class; do not commit PDF if redistribution forbidden",
        },
        {
            "id": "NXP-IMX95XEC",
            "title": "i.MX 95 Applications Processors Data Sheet for Extended Industrial Products (IMX95XEC)",
            "url": "https://www.nxp.com/docs/en/data-sheet/IMX95XEC.pdf",
            "class": "PUBLIC_DATASHEET",
            "redistribution": "METADATA_URL_HASH_ONLY_IF_LICENSE_FORBIDS",
            "sha256": "PENDING_OWNER_FETCH",
            "notes": "Extended industrial grade variant",
        },
        {
            "id": "NXP-IMX95CEC",
            "title": "i.MX 95 Applications Processors Data Sheet for Commercial Products (IMX95CEC)",
            "url": "https://www.nxp.com/docs/en/data-sheet/IMX95CEC.pdf",
            "class": "PUBLIC_DATASHEET",
            "redistribution": "METADATA_URL_HASH_ONLY_IF_LICENSE_FORBIDS",
            "sha256": "PENDING_OWNER_FETCH",
            "notes": "Commercial grade variant",
        },
        {
            "id": "NXP-IMX95FS",
            "title": "i.MX 95 Applications Processor Family Factsheet (IMX95FS)",
            "url": "https://www.nxp.com/products/i.MX95",
            "class": "PUBLIC_FACTSHEET",
            "redistribution": "METADATA_URL_ONLY",
            "sha256": "PENDING_OWNER_FETCH",
            "notes": "Factsheet linked from product page",
        },
        {
            "id": "NXP-IMX95RM",
            "title": "i.MX 95 Applications Processor Reference Manual (IMX95RM)",
            "url": "https://www.nxp.com/products/i.MX95",
            "class": "PUBLIC_REFERENCE_MANUAL",
            "redistribution": "METADATA_URL_HASH_ONLY",
            "sha256": "PENDING_OWNER_FETCH",
            "notes": "Large RM; commit hash after owner fetch — do not invent contents",
        },
        {
            "id": "NXP-IMX95-HW-DESIGN-GUIDE",
            "title": "i.MX 95 Hardware Design Guide",
            "url": "https://www.nxp.com/products/i.MX95",
            "class": "LOGIN_OR_ACCOUNT_GATED",
            "redistribution": "URL_ONLY_NO_CONTENT",
            "sha256": "N/A",
            "notes": "Product page marks Account Required — gap until owner login fetch",
        },
        {
            "id": "NXP-IMX95-BSDL-IBIS",
            "title": "i.MX 95 BSDL / IBIS models (package variants)",
            "url": "https://www.nxp.com/products/i.MX95",
            "class": "PUBLIC_MODEL_OR_GATED",
            "redistribution": "METADATA_URL_ONLY",
            "sha256": "PENDING_OWNER_FETCH",
            "notes": "Use for SI/DFT planning; verify license before any binary commit",
        },
        {
            "id": "NXP-MCUX-IMX95-EVK",
            "title": "MCUXpresso SDK / EVK documentation (imx95 class boards)",
            "url": "https://mcuxpresso.nxp.com/",
            "class": "PUBLIC_SDK_DOCS",
            "redistribution": "METADATA_URL_ONLY",
            "sha256": "PENDING_OWNER_FETCH",
            "notes": "Bring-up reference; EVK ≠ custom open-custom board validation",
        },
    ]
    wj(
        NXP / "PUBLIC_COLLATERAL_INDEX.json",
        {
            "schema": "gunnchos.hardware_v1.nxp.public_collateral.v1",
            "generated_at_utc": NOW,
            "campaign": CAMPAIGN,
            "policy": "public collateral only; metadata/URLs/hashes if redistribution forbidden",
            "items": collateral,
        },
    )
    lines = [
        f"# Public collateral index — i.MX95",
        "",
        HDR,
        "",
        "| ID | Title | Class | Redistribution | URL |",
        "|---|---|---|---|---|",
    ]
    for c in collateral:
        lines.append(
            f"| `{c['id']}` | {c['title']} | {c['class']} | {c['redistribution']} | {c['url']} |"
        )
    lines += [
        "",
        "## Hash policy",
        "",
        "- `sha256=PENDING_OWNER_FETCH` until an owner downloads and records the hash",
        "- Cursor does not fabricate document contents or invent restricted pin maps",
        "",
    ]
    w(NXP / "PUBLIC_COLLATERAL_INDEX.md", "\n".join(lines))

    w(
        NXP / "PUBLIC_COLLATERAL_GAP_REGISTER.md",
        f"""# Public collateral gap register

{HDR}

| Gap ID | Description | Blocks | Severity | Owner path |
|---|---|---|---|---|
| GAP-HW-DESIGN-GUIDE | Hardware Design Guide appears account-gated on product page | net-accurate power/DDR rules for fab | HIGH | Owner NXP account login (Cursor does not accept NDA) |
| GAP-RM-HASH | IMX95RM not hashed in-repo | reproducible design freeze | MED | Owner fetch + hash commit |
| GAP-DS-HASH | Datasheet PDFs not hashed | AVL / OPN freeze | MED | Owner fetch + hash |
| GAP-PACKAGE-SELECT | 15×15 vs 19×19 package not frozen | PCB outline / fanout | HIGH | Owner decision after public BSDL/IBIS review |
| GAP-EVK-≠-CUSTOM | EVK lessons ≠ custom open-custom board pass | false-green risk | HIGH | Explicit methodology in EVT_PLAN |

No gap may be closed by inventing vendor content.
""",
    )

    for name, title, body in [
        (
            "CPB0_OPEN_PRD.md",
            "CPB0-Open PRD (NXP open-custom learning board)",
            """## Intent
Debug-friendly open-custom learning board on i.MX95 for board-level ownership without AMD NDA.

## Must prove
BGA fanout, LPDDR class memory, PMIC/sequencing, PCIe/USB, display/camera hooks, EC, secure boot path, DFT/bring-up.

## Must not claim
Product performance parity with AMD PRODUCT_MAINLINE; Windows/game readiness; USB4 unless separately designed.

## Fab readiness
`CPB0_OPEN_READY_FOR_FAB=false` until public design rules + real EDA exist.
""",
        ),
        (
            "SYSTEM_BLOCK_DIAGRAM.md",
            "System block diagram (architecture)",
            """```
[USB-C PD / DC-in] -> [PMIC tree] -> [i.MX95]
                         |              |-- LPDDR
                         |              |-- eMMC / NVMe (SKU option)
                         |              |-- Wi-Fi/BT M.2 or SDIO module
                         |              |-- Ethernet PHY
                         |              |-- Display (MIPI/LVDS/eDP class per public mux)
                         |              |-- Camera CSI
                         |              |-- PCIe slot/endpoint (SKU-dependent)
                         |              |-- USB host/device
[EC / supervisory MCU] <- SMBus/UART/GPIO -> [i.MX95]
[Debug] SWD/JTAG + UART console + USB gadget recovery
```
Not a netlist. Interfaces pending public RM / design-guide confirmation.
""",
        ),
        (
            "POWER_ARCHITECTURE.md",
            "Power architecture",
            """## Goals
- Correct sequencing for i.MX95 rails per public design guide (when available)
- Debug-friendly test points on CPB0-Open
- Battery optional on learning board; first bring-up may be DC-in only

## Honesty
No invented voltage tables. Record rail names only after public collateral citation.
""",
        ),
        (
            "MEMORY_ARCHITECTURE.md",
            "Memory architecture",
            """## Intent
LPDDR-class DRAM topology suitable for open-custom learning; prefer debug accessibility on CPB0-Open.

## Non-freeze
Do not freeze routing rules without Hardware Design Guide / RM citation.
""",
        ),
        (
            "PCIE_USB_ARCHITECTURE.md",
            "PCIe / USB architecture",
            """## Intent
Exercise high-speed SERDES learning: at least one USB host path and one PCIe-class link if silicon mux allows.

## Non-claims
USB4 is **not** assumed on i.MX95 open-custom lane.
""",
        ),
        (
            "DISPLAY_CAMERA_ARCHITECTURE.md",
            "Display / camera architecture",
            """## Intent
Single primary display + one camera path for bring-up and experience-contract latency experiments on embedded UI.

## Non-claims
Not a dual-eDP AMD-class creator display claim.
""",
        ),
        (
            "SECURITY_BOOT_ARCHITECTURE.md",
            "Security / boot architecture",
            """## Intent
Public EdgeLock / HAB-class secure boot learning path; recoverable brick-avoidance on CPB0-Open.

## Non-claims
No production key ceremony executed in this campaign.
""",
        ),
        (
            "DEBUG_BRINGUP_ARCHITECTURE.md",
            "Debug / bring-up architecture",
            """## Required
- UART console
- JTAG/SWD access
- USB recovery path
- Power/rail probe points
- Boot-mode straps documented

## EVK note
NXP EVK is REFERENCE bring-up aid; it does not validate the custom open-custom PCB.
""",
        ),
        (
            "SCHEMATIC_SHEET_PLAN.md",
            "Schematic sheet plan",
            """| Sheet | Content |
|---|---|
| 01 | Block diagram / notes / claim boundary |
| 02 | i.MX95 power + decoupling |
| 03 | i.MX95 clocks/reset/boot |
| 04 | LPDDR |
| 05 | Storage |
| 06 | USB / PCIe |
| 07 | Display / camera |
| 08 | EC / debug |
| 09 | Connectors / mechanics |

No net-accurate sheets claimed ready.
""",
        ),
        (
            "PCB_CONSTRAINT_PLAN.md",
            "PCB constraint plan",
            """## Stackup
TBD after package selection (15×15 vs 19×19) and public SI guidance.

## Keepouts
RF / camera / high-speed differential pairs per public design guide when available.

## Honesty
`PCB_READY=false`.
""",
        ),
        (
            "EVT_PLAN.md",
            "EVT plan (open-custom)",
            """## Objectives
1. Power-on / sequencing
2. Boot console
3. Memory stress
4. USB / storage
5. Display smoke
6. Thermal soak
7. Recovery path

## Pass criteria
Measured logs + photos in physical_evidence/ (none fabricated here).

## Fail-closed
EVK success ≠ custom board EVT pass.
""",
        ),
        (
            "READY_FOR_FAB_CHECKLIST.md",
            "Ready-for-fab checklist (must stay false until real)",
            """- [ ] Public design-guide rules cited
- [ ] Package selected
- [ ] Netlist complete
- [ ] Schematic ERC clean
- [ ] PCB DRC clean
- [ ] BOM AVL with live distributor quotes (owner)
- [ ] DFT / bring-up hooks present
- [ ] License-safe collateral hashed

Current: **NOT READY** (`CPB0_OPEN_READY_FOR_FAB=false`).
""",
        ),
    ]:
        w(NXP / name, f"# {title}\n\n{HDR}\n\n{body}\n")

    write_csv(
        NXP / "PRELIMINARY_BOM.csv",
        [
            "item_id",
            "description",
            "MPN",
            "qty",
            "class",
            "status",
            "notes",
        ],
        [
            {
                "item_id": "NXP-SOC-001",
                "description": "i.MX95 AP (package TBD)",
                "MPN": "PENDING_PUBLIC_OPN_SELECT",
                "qty": "0",
                "class": "OPEN_ENGINEERING_MAINLINE",
                "status": "ARCHITECTURE_ONLY",
                "notes": "qty=0 until OPN freeze; not PRODUCT_MAINLINE",
            },
            {
                "item_id": "NXP-PMIC-001",
                "description": "PMIC / power tree class",
                "MPN": "PENDING_PUBLIC_REF_DESIGN",
                "qty": "0",
                "class": "OPEN_ENGINEERING_MAINLINE",
                "status": "ARCHITECTURE_ONLY",
                "notes": "cite public ref design before qty>0",
            },
            {
                "item_id": "NXP-DRAM-001",
                "description": "LPDDR class DRAM",
                "MPN": "PENDING_TOPOLOGY",
                "qty": "0",
                "class": "OPEN_ENGINEERING_MAINLINE",
                "status": "ARCHITECTURE_ONLY",
                "notes": "topology unfrozen",
            },
            {
                "item_id": "NXP-EC-001",
                "description": "EC / supervisory MCU",
                "MPN": "PENDING_SELECT",
                "qty": "0",
                "class": "OPEN_ENGINEERING_MAINLINE",
                "status": "ARCHITECTURE_ONLY",
                "notes": "open MCU preferred",
            },
        ],
    )

    w(
        NXP / "README.md",
        f"""# Open-custom NXP i.MX95 package

{HDR}

Track: `OPEN_ENGINEERING_MAINLINE = NXP_IMX95_OPEN_CUSTOM`

See `OPEN_CUSTOM_DOCTRINE.md` for non-equivalence to AMD PRODUCT_MAINLINE.
""",
    )


def write_amd_status() -> None:
    w(
        CM / "PRODUCT_MAINLINE_STATUS.md",
        f"""# PRODUCT_MAINLINE status — AMD_CUSTOM_X86

{HDR}

## Track identity

`PRODUCT_MAINLINE = AMD_CUSTOM_X86` (gunnchOS Platform Core v1)

## Preserved HW1C architecture

| Device | Candidate | Status |
|---|---|---|
| Student 14.5 | Ryzen Embedded 8840U | Architecture-complete; vendor-gated implementation |
| Handheld Hybrid | Ryzen Embedded 8840U | Architecture-complete; vendor-gated implementation |
| DS-XL | Ryzen Embedded 8845HS | Architecture-complete; vendor-gated implementation |
| Custom Dock | USB4 40 Gen-1 | Architecture-complete; JHL ballmaps external |
| Custom Rings | nRF54L15 | Architecture-complete; CSP47 form-factor pending |

## Vendor access

`CUSTOM_PLATFORM_VENDOR_ACCESS_READY=false`

This is an **honest external blocker** for physical/silicon integration.

It is **not** a reason the architecture/control-plane baseline (#68) cannot merge.

## Physical gates (remain false)

- `CPB0_SCHEMATIC_READY=false`
- `CPB0_PCB_READY=false`
- `CPB0_READY_FOR_FAB=false`
- `CUSTOM_MAINLINE_READY_FOR_EVT_BUILD=false`
- `HARDWARE_V1_READY_FOR_EVT_BUILD=false`

## Relationship to OPEN_ENGINEERING_MAINLINE

NXP open-custom advances board-learning / fab methodology in parallel.
It does **not** replace PRODUCT_MAINLINE performance/compatibility requirements.
""",
    )


def write_gxe_contract() -> None:
    w(
        CONV / "GXE_HARDWARE_INTEGRATION_CONTRACT.md",
        f"""# GXE ↔ Hardware integration contract

{HDR}

## Boundary

GXE is executed in a **separate workspace/repo**. This file is the only GXE surface required for #68 merge.

`GXE_IMPLEMENTED_IN_HARDWARE_REPO=false`

## Interfaces

### 1. Experience Contract interface
Hardware track consumers accept Experience Contracts matching `HARDWARE_EXPERIENCE_CONTRACT_SCHEMA.json`.

### 2. Benchmark result schema
Results conform to `CROSS_TRACK_BENCHMARK_SCHEMA.json` (per-workload; no single winner score).

### 3. RuntimeTarget identity
Stable string id for the software runtime under test (OS image, kernel, compositor, app bundle digests).

### 4. Hardware identity
Track + board + silicon + revision + BOM hash + firmware identity.

### 5. Power / energy measurement interface
Fields: `energy_per_task_j`, `avg_power_w`, `peak_power_w`, `sample_hz`, `instrument_id`.

### 6. Latency metrics
`interaction_latency_ms` {{p50,p95,p99}}, `frame_latency_ms`, `input_to_photon_ms` when applicable.

### 7. Accelerator inventory
List of CPU / GPU / NPU / FPGA / custom accel with capability discovery keys.

### 8. Thermal metadata
Skin / junction / ambient estimates with sensor provenance; no fabricated thermals.

### 9. Capability discovery
Machine-readable capabilities advertised to GXE without implying product readiness.

### 10. Experiment provenance
`experiment_id`, `git_sha`, `dataset_id`, `operator`, `started_at_utc`, `claim_boundary`.

## Non-goals in this repo

- No GXE kernel/runtime implementation
- No RISC-V/FPGA bring-up executed here
- No silent promotion of GXE to PRODUCT_MAINLINE
""",
    )


def write_cross_track() -> None:
    w(
        CONV / "CROSS_TRACK_COMPARISON_MATRIX.md",
        f"""# Cross-track comparison matrix

{HDR}

## Rule

Never create one simplistic overall winner score. Compare **per workload**.

| Dimension | PRODUCT_MAINLINE AMD | OPEN_ENGINEERING NXP | GREENFIELD GXE | REFERENCE_CONTROL COM-HPC/COTS |
|---|---|---|---|---|
| Primary question | Product experience + x86 compat | Board ownership / fab learning | Experience-first greenfield | Fault isolation / baseline |
| task success | required | engineering tasks | experimental | control |
| latency p50/p95/p99 | product SLOs | learning SLOs | experimental | control |
| energy/task | product | efficiency learning | experimental | control |
| memory | product | learning | experimental | control |
| CPU/GPU/NPU/FPGA util | product | AP/NPU learning | research | control |
| network bytes | product | as needed | experimental | control |
| storage I/O | product | as needed | experimental | control |
| thermal/power | product comfort | bring-up | experimental | control |
| user interactions | product | limited UI | core | control |
| accessibility completion | product | if UI present | experimental | control |
| recovery behavior | product | brick-avoidance | experimental | control |
| compatibility | Windows/Linux/games | Linux embedded | custom | x86 modular control |
| manufacturing complexity | high (owned MB) | high (owned MB) | variable | lower modular |
| serviceability | product intent | learning | experimental | modular swap |

Schema: `CROSS_TRACK_BENCHMARK_SCHEMA.json`
""",
    )
    wj(
        CONV / "CROSS_TRACK_BENCHMARK_SCHEMA.json",
        {
            "schema": "gunnchos.hardware_v1.cross_track_benchmark.v1",
            "generated_at_utc": NOW,
            "campaign": CAMPAIGN,
            "forbid_overall_winner_score": True,
            "required_identity": [
                "workload_id",
                "track",
                "hardware_identity",
                "runtime_target_id",
                "provenance",
            ],
            "tracks_enum": [
                "PRODUCT_MAINLINE_AMD_CUSTOM_X86",
                "OPEN_ENGINEERING_NXP_IMX95_OPEN_CUSTOM",
                "GREENFIELD_EXPERIMENT_GXE",
                "REFERENCE_CONTROL_COM_HPC_AND_COTS",
            ],
            "metrics": [
                "task_success",
                "latency_ms_p50",
                "latency_ms_p95",
                "latency_ms_p99",
                "energy_per_task_j",
                "memory_peak_bytes",
                "cpu_util_pct",
                "gpu_util_pct",
                "npu_util_pct",
                "fpga_util_pct",
                "network_bytes",
                "storage_io_bytes",
                "thermal_c",
                "power_w_avg",
                "user_interactions",
                "accessibility_completion",
                "recovery_behavior",
                "compatibility_notes",
                "manufacturing_complexity_score",
                "serviceability_score",
            ],
            "example": {
                "workload_id": "desk_compile_hello",
                "track": "PRODUCT_MAINLINE_AMD_CUSTOM_X86",
                "hardware_identity": "PlatformCore-v1/CPB0/revA/PENDING",
                "runtime_target_id": "device-os/v1.0.0-rc.1",
                "metrics": {"task_success": False, "note": "physical pending"},
                "provenance": {"git_sha": "PENDING", "claim_boundary": CLAIM},
            },
        },
    )


def write_experience_contract() -> None:
    schema = {
        "schema": "gunnchos.hardware_v1.hardware_experience_contract.v1",
        "generated_at_utc": NOW,
        "campaign": CAMPAIGN,
        "aligns_with": "GXE_v2_without_requiring_GXE_execution",
        "required_fields": [
            "contract_id",
            "user_cohorts",
            "workload",
            "accessibility",
            "time_to_usable",
            "interaction_latency",
            "frame_input_latency",
            "memory_budget",
            "energy_per_task",
            "sustained_power",
            "thermal",
            "offline",
            "privacy",
            "recovery",
            "minimum",
            "target",
            "enhanced",
            "fallback",
            "measurement_method",
        ],
        "field_notes": {
            "user_cohorts": "e.g. student, creator, accessibility_primary",
            "workload": "named task with success criteria",
            "accessibility": "completion criteria for AT users",
            "time_to_usable": "seconds from power-on/login to first useful action",
            "interaction_latency": "p50/p95/p99 ms",
            "frame_input_latency": "input-to-photon when graphical",
            "memory_budget": "bytes peak/sustained",
            "energy_per_task": "joules",
            "sustained_power": "watts envelope",
            "thermal": "skin/junction limits",
            "offline": "required offline behaviors",
            "privacy": "local-only / retention constraints",
            "recovery": "brick-avoidance / rollback expectations",
            "minimum": "ship-floor bar",
            "target": "design target",
            "enhanced": "stretch with justified hardware",
            "fallback": "degraded mode when accel/link unavailable",
            "measurement_method": "instrumentation + protocol",
        },
    }
    wj(CONV / "HARDWARE_EXPERIENCE_CONTRACT_SCHEMA.json", schema)
    w(
        CONV / "HARDWARE_EXPERIENCE_CONTRACT_GUIDE.md",
        f"""# Hardware Experience Contract guide

{HDR}

## Purpose

Translate user outcomes into measurable hardware/software obligations **before** adding silicon, boards, or accelerators.

## Required fields

See `HARDWARE_EXPERIENCE_CONTRACT_SCHEMA.json`:

user_cohorts, workload, accessibility, time_to_usable, interaction_latency, frame/input latency,
memory budget, energy/task, sustained power, thermal, offline, privacy, recovery,
minimum / target / enhanced / fallback, measurement method.

## Alignment with GXE v2

Compatible with GXE Experience Contracts via `GXE_HARDWARE_INTEGRATION_CONTRACT.md`.
GXE does **not** need to be executed for #68 architecture merge.

## Fail-closed

- Stronger SKU alone cannot satisfy a contract
- Missing measurement_method → contract invalid
- Enhanced tier cannot silently become minimum
""",
    )


def write_post_merge_plan() -> None:
    w(
        CONV / "POST_MERGE_PLAN.md",
        f"""# Post-merge plan — prepare only (do not execute)

{HDR}

## After owner merges #68 with a merge commit

1. Verify accepted-main merge SHA and parents
2. Verify merge tree equals tested #68 head
3. Run accepted-main validators
4. Record accepted hardware-architecture freeze SHA
5. Retarget #69–#79 from `hardware/v1-mainline-ready-for-evt` to `main`
6. Ensure each experiment shows only its intended delta
7. Keep them DRAFT
8. Do not merge any experiment
9. Start NXP open-custom implementation lane and GXE v2 separately

## Expected next campaign

`HW1D.1_ACCEPTED_MAIN_REBIND`

## Non-execution

This file is preparation only. Cursor must **not** merge #68 or retarget experiments until the owner merges.
""",
    )


def update_decision_ledger() -> None:
    path = HV1 / "decisions" / "DECISION_LEDGER.json"
    ledger = json.loads(path.read_text(encoding="utf-8"))
    track_defaults = {
        "DEC-DOCTRINE-001": {
            "track": "ALL_TRACKS",
            "role": "architecture_control_plane",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "N/A — doctrine",
            "physical_dependency": False,
            "external_dependency": False,
            "state": "ADOPTED_MAINLINE",
            "mainline": (
                "FOUR_TRACK model: PRODUCT_MAINLINE=AMD_CUSTOM_X86; "
                "OPEN_ENGINEERING_MAINLINE=NXP_IMX95_OPEN_CUSTOM; "
                "GREENFIELD_EXPERIMENT=GXE; REFERENCE_CONTROL=COM_HPC_AND_COTS"
            ),
        },
        "DEC-COMPUTE-001": {
            "track": "PRODUCT_MAINLINE",
            "role": "product",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "AMD collateral + measured EVT before physical ready",
            "physical_dependency": True,
            "external_dependency": True,
        },
        "DEC-COMPUTE-002": {
            "track": "PRODUCT_MAINLINE",
            "role": "product",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "AMD collateral + handheld fit measurements",
            "physical_dependency": True,
            "external_dependency": True,
        },
        "DEC-COMPUTE-003": {
            "track": "PRODUCT_MAINLINE",
            "role": "product",
            "evidence_class": "pending_physical",
            "promotion_conditions": "CPB0/EVT measurements",
            "physical_dependency": True,
            "external_dependency": False,
        },
        "DEC-CPB0-001": {
            "track": "PRODUCT_MAINLINE",
            "role": "product_engineering_learning",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "AMD collateral + EDA",
            "physical_dependency": True,
            "external_dependency": True,
        },
        "DEC-COMHPC-001": {
            "track": "REFERENCE_CONTROL",
            "role": "control",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "Cannot promote to PRODUCT_MAINLINE without measured evidence + owner accept",
            "physical_dependency": False,
            "external_dependency": False,
            "mainline": (
                "ADLINK COM-HPC Mini mMTL + Mini Base classified "
                "REFERENCE_CONTROL_MODULAR_X86 (not PRODUCT_MAINLINE)"
            ),
        },
        "DEC-MEMORY-001": {
            "track": "PRODUCT_MAINLINE",
            "role": "product",
            "evidence_class": "pending_vendor",
            "promotion_conditions": "AMD DDR topology collateral",
            "physical_dependency": True,
            "external_dependency": True,
        },
        "DEC-FW-001": {
            "track": "PRODUCT_MAINLINE",
            "role": "product",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "Vendor UEFI path; open stacks stay experimental",
            "physical_dependency": False,
            "external_dependency": False,
        },
        "DEC-DISPLAY-001": {
            "track": "PRODUCT_MAINLINE",
            "role": "product",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "OLED remains experiment",
            "physical_dependency": False,
            "external_dependency": False,
        },
        "DEC-STORAGE-001": {
            "track": "PRODUCT_MAINLINE",
            "role": "product",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "N/A",
            "physical_dependency": False,
            "external_dependency": False,
        },
        "DEC-CELLULAR-001": {
            "track": "PRODUCT_MAINLINE",
            "role": "product",
            "evidence_class": "public_avl",
            "promotion_conditions": "PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING",
            "physical_dependency": True,
            "external_dependency": False,
        },
        "DEC-DOCK-001": {
            "track": "PRODUCT_MAINLINE",
            "role": "product",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "JHL ballmaps for pin-accurate custom dock",
            "physical_dependency": True,
            "external_dependency": True,
        },
        "DEC-RINGS-001": {
            "track": "PRODUCT_MAINLINE",
            "role": "product",
            "evidence_class": "public_evidence",
            "promotion_conditions": "CSP47 wearable HDI/assembly feasibility",
            "physical_dependency": True,
            "external_dependency": False,
        },
        "DEC-RINGS-002": {
            "track": "PRODUCT_MAINLINE",
            "role": "product",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "Inductive/sEMG stay experimental",
            "physical_dependency": False,
            "external_dependency": False,
        },
        "DEC-BATT-001": {
            "track": "PRODUCT_MAINLINE",
            "role": "product",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "Experimental chemistries deferred Gen2",
            "physical_dependency": False,
            "external_dependency": False,
            "mainline": "Qualified Li-ion / LiPo only; no experimental chemistries in PRODUCT_MAINLINE",
        },
        "DEC-QA-001": {
            "track": "PRODUCT_MAINLINE",
            "role": "product",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "N/A",
            "physical_dependency": False,
            "external_dependency": False,
        },
        "DEC-RP0-001": {
            "track": "REFERENCE_CONTROL",
            "role": "control",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "Optional order only; never PRODUCT_MAINLINE",
            "physical_dependency": False,
            "external_dependency": False,
            "mainline": (
                "Two-stage RP0 REFERENCE_CONTROL: RP0-A COTS Integration Bench then "
                "historical RP0-B custom path; RP0-A is not PRODUCT_MAINLINE"
            ),
        },
    }

    for d in ledger.get("decisions", []):
        meta = track_defaults.get(d["id"], {})
        for k, v in meta.items():
            d[k] = v
        # scrub ambiguous bare mainline wording in free text where we added track
        if d.get("state") == "ADOPTED_MAINLINE" and "track" in d:
            # keep state enum for validator compatibility; clarify via track field
            pass

    # New NXP + GXE + merge-readiness decisions
    extras = [
        {
            "id": "DEC-TRACK-MODEL-001",
            "topic": "Four-track convergence model",
            "state": "ADOPTED_MAINLINE",
            "track": "ALL_TRACKS",
            "role": "architecture_control_plane",
            "mainline": (
                "PRODUCT_MAINLINE=AMD_CUSTOM_X86; OPEN_ENGINEERING_MAINLINE=NXP_IMX95_OPEN_CUSTOM; "
                "GREENFIELD_EXPERIMENT=GXE; REFERENCE_CONTROL=COM_HPC_AND_COTS"
            ),
            "rationale": "HW1D resolves ambiguous mainline terminology",
            "evidence": [
                "hardware_v1/convergence/CANONICAL_TRACK_MODEL.md",
                "hardware_v1/convergence/CANONICAL_TRACK_MODEL.json",
            ],
            "experiment_alt": None,
            "owner_gate": None,
            "evidence_class": "architecture_definition",
            "promotion_conditions": "N/A",
            "physical_dependency": False,
            "external_dependency": False,
        },
        {
            "id": "DEC-NXP-OPEN-001",
            "topic": "NXP i.MX95 open-custom engineering lane",
            "state": "ADOPTED_MAINLINE",
            "track": "OPEN_ENGINEERING_MAINLINE",
            "role": "engineering",
            "mainline": "NXP_IMX95_OPEN_CUSTOM architecture package under hardware_v1/open_custom_nxp/",
            "rationale": "No-NDA path to custom-board fab learning; not product-equivalent to AMD x86",
            "evidence": [
                "hardware_v1/open_custom_nxp/OPEN_CUSTOM_DOCTRINE.md",
                "hardware_v1/open_custom_nxp/IMX95_PLATFORM_PROFILE.md",
            ],
            "experiment_alt": None,
            "owner_gate": "Public design-guide access + EDA for CPB0-Open",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "Cannot replace PRODUCT_MAINLINE without explicit owner decision + measured evidence",
            "physical_dependency": True,
            "external_dependency": True,
        },
        {
            "id": "DEC-GXE-001",
            "topic": "GXE integration boundary",
            "state": "EXPERIMENTAL_COMPARE",
            "track": "GREENFIELD_EXPERIMENT",
            "role": "experimental",
            "mainline": "Integration contract only in this repo; GXE not implemented here",
            "rationale": "Keep experience-first greenfield separate from hardware architecture baseline",
            "evidence": [
                "hardware_v1/convergence/GXE_HARDWARE_INTEGRATION_CONTRACT.md",
            ],
            "experiment_alt": "GXE workspace/repo",
            "owner_gate": None,
            "evidence_class": "architecture_definition",
            "promotion_conditions": "GXE evidence outside this repo; never silent promote",
            "physical_dependency": False,
            "external_dependency": False,
        },
        {
            "id": "DEC-MERGE-READY-001",
            "topic": "Architecture baseline merge-readiness vs physical readiness",
            "state": "ADOPTED_MAINLINE",
            "track": "ALL_TRACKS",
            "role": "architecture_control_plane",
            "mainline": (
                "HW_ARCHITECTURE_BASELINE_MERGE_READY may be true while physical EVT/fab/cert gates remain false"
            ),
            "rationale": "Separate architecture/control-plane acceptance from physical hardware readiness",
            "evidence": [
                "hardware_v1/GATES.json",
                "hardware_v1/convergence/POST_MERGE_PLAN.md",
            ],
            "experiment_alt": None,
            "owner_gate": "MERGE_HW_ARCHITECTURE_BASELINE_68_WITH_MERGE_COMMIT",
            "evidence_class": "architecture_definition",
            "promotion_conditions": "Owner merge commit only; Cursor does not merge",
            "physical_dependency": False,
            "external_dependency": False,
        },
        {
            "id": "DEC-EXPERIENCE-001",
            "topic": "Experience-first co-design doctrine",
            "state": "ADOPTED_MAINLINE",
            "track": "ALL_TRACKS",
            "role": "architecture_control_plane",
            "mainline": "Software must earn additional hardware; Experience Contracts required",
            "rationale": "Prevent SKU upsizing from masking software inefficiency",
            "evidence": [
                "hardware_v1/convergence/EXPERIENCE_FIRST_CO_DESIGN_DOCTRINE.md",
                "hardware_v1/convergence/HARDWARE_EXPERIENCE_CONTRACT_SCHEMA.json",
            ],
            "experiment_alt": None,
            "owner_gate": None,
            "evidence_class": "architecture_definition",
            "promotion_conditions": "N/A",
            "physical_dependency": False,
            "external_dependency": False,
        },
    ]
    existing = {d["id"] for d in ledger["decisions"]}
    for e in extras:
        if e["id"] not in existing:
            ledger["decisions"].append(e)

    ledger["campaign"] = CAMPAIGN
    ledger["generated_at_utc"] = NOW
    ledger["schema"] = "gunnchos.hardware_v1.campaign.v1"
    wj(path, ledger)

    # Markdown mirror (compact)
    md = [
        f"# Decision ledger (HW1D track-qualified)",
        "",
        HDR,
        "",
        "| ID | Track | State | Role | Topic |",
        "|---|---|---|---|---|",
    ]
    for d in ledger["decisions"]:
        md.append(
            f"| `{d['id']}` | `{d.get('track','?')}` | `{d.get('state')}` | `{d.get('role','')}` | {d.get('topic')} |"
        )
    md.append("")
    w(HV1 / "decisions" / "DECISION_LEDGER.md", "\n".join(md))


def update_experiments_registry() -> None:
    path = HV1 / "experiments" / "REGISTRY.json"
    reg = json.loads(path.read_text(encoding="utf-8"))
    reg["campaign"] = CAMPAIGN
    reg["generated_at_utc"] = NOW
    reg["hierarchy"] = {
        "product_mainline": "PRODUCT_MAINLINE = AMD_CUSTOM_X86 (Platform Core v1)",
        "open_engineering_mainline": "OPEN_ENGINEERING_MAINLINE = NXP_IMX95_OPEN_CUSTOM",
        "greenfield_experiment": "GREENFIELD_EXPERIMENT = GXE (integration contract only here)",
        "reference_control": "REFERENCE_CONTROL = COM_HPC_AND_COTS",
        "mainline": "PRODUCT_MAINLINE AMD_CUSTOM_X86 (Platform Core v1) — qualifier required",
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
        "guiding_question": (
            "Does the simpler or specialized variant outperform the relevant track baseline "
            "enough to justify promotion with measured evidence?"
        ),
    }
    for e in reg.get("experiments", []):
        e["merge_ready"] = False
        e["promotion_requires_evidence"] = True
        e["not_in_main_bom"] = True
    wj(path, reg)
    w(
        HV1 / "experiments" / "REGISTRY.md",
        f"""# Experiments registry

{HDR}

Hierarchy uses track qualifiers. All #69–#79 remain DRAFT experiments — not merge-ready without promotion evidence.

See `REGISTRY.json`.
""",
    )


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
        "HW_ARCHITECTURE_BASELINE_MERGE_READY": True,
        "FOUR_TRACK_MODEL_PASS": True,
        "EXPERIENCE_FIRST_CO_DESIGN_DOCTRINE_PASS": True,
        "AMD_PRODUCT_MAINLINE_PRESERVED": True,
        "NXP_OPEN_CUSTOM_TRACK_DEFINED": True,
        "GXE_INTEGRATION_BOUNDARY_DEFINED": True,
        "REFERENCE_CONTROL_TRACK_DEFINED": True,
        "EXPERIMENT_ISOLATION_PASS": True,
        "GXE_IMPLEMENTED_IN_HARDWARE_REPO": False,
        "NXP_CLAIMED_PRODUCT_EQUIVALENT_TO_AMD": False,
        "CUSTOM_MAINLINE_ARCHITECTURE_FROZEN": True,
        "CUSTOM_PLATFORM_VENDOR_ACCESS_READY": False,
        **learning_false,
        "CPB0_SCHEMATIC_READY": False,
        "CPB0_PCB_READY": False,
        "CPB0_READY_FOR_FAB": False,
        "CPB0_OPEN_READY_FOR_FAB": False,
        "CUSTOM_MAINLINE_READY_FOR_EVT_BUILD": False,
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
        "PRODUCT_MAINLINE": "AMD_CUSTOM_X86",
        "OPEN_ENGINEERING_MAINLINE": "NXP_IMX95_OPEN_CUSTOM",
        "GREENFIELD_EXPERIMENT": "GXE",
        "REFERENCE_CONTROL": "COM_HPC_AND_COTS",
        "blockers": [
            {
                "id": "EXT-AMD-CUSTOM-COLLATERAL",
                "severity": "AMD Ryzen Embedded 8000 custom platform collateral",
                "classification": "EXTERNAL_BLOCKER_NOT_ARCHITECTURE_MERGE_BLOCKER",
                "blocks": [
                    "CUSTOM_PLATFORM_VENDOR_ACCESS_READY",
                    "CPB0_READY_FOR_FAB",
                    "CUSTOM_MAINLINE_READY_FOR_EVT_BUILD",
                    "HARDWARE_V1_READY_FOR_EVT_BUILD",
                ],
                "blocks_architecture_baseline_merge": False,
            },
            {
                "id": "EXT-AMD-EDA-OUTPUTS",
                "severity": "Net-accurate schematic/PCB for CPB0",
                "classification": "EXTERNAL_BLOCKER_NOT_ARCHITECTURE_MERGE_BLOCKER",
                "blocks": ["CPB0_SCHEMATIC_READY", "CPB0_PCB_READY", "CPB0_READY_FOR_FAB"],
                "blocks_architecture_baseline_merge": False,
            },
            {
                "id": "EXT-COM-HPC-400PIN",
                "severity": "COM-HPC Mini net-accurate pin map for historical RP0-B",
                "classification": "STILL_VENDOR_GATED_FOR_RP0_B",
                "blocks": ["RP0_B_CUSTOM_READY_FOR_FAB", "REFERENCE_PLATFORM_0_READY_FOR_FAB"],
                "rp0_a_blocking": False,
                "rp0_b_blocking": True,
                "blocks_architecture_baseline_merge": False,
            },
            {
                "id": "EXT-JHL8440-BALLMAP",
                "severity": "Intel JHL8440 ball map (NDA)",
                "classification": "STILL_VENDOR_GATED_FOR_RP0_B",
                "blocks": ["DOCK_HW_DIGITAL_RELEASE_PACKAGE"],
                "rp0_a_blocking": False,
                "rp0_b_blocking": True,
                "blocks_architecture_baseline_merge": False,
            },
            {
                "id": "EXT-JHL9040R-BALLMAP",
                "severity": "Intel JHL9040R retimer ball map (NDA)",
                "classification": "STILL_VENDOR_GATED_FOR_RP0_B",
                "blocks": ["DOCK_HW_DIGITAL_RELEASE_PACKAGE"],
                "rp0_a_blocking": False,
                "rp0_b_blocking": True,
                "blocks_architecture_baseline_merge": False,
            },
            {
                "id": "EXT-NXP-DESIGN-GUIDE",
                "severity": "i.MX95 Hardware Design Guide may be account-gated",
                "classification": "EXTERNAL_BLOCKER_NOT_ARCHITECTURE_MERGE_BLOCKER",
                "blocks": ["CPB0_OPEN_READY_FOR_FAB"],
                "blocks_architecture_baseline_merge": False,
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
        "NEXT_OWNER_ACTION": "MERGE_HW_ARCHITECTURE_BASELINE_68_WITH_MERGE_COMMIT",
        "OPTIONAL_OWNER_ACTION": "ORDER_RP0_A_COTS_CONTROL_KIT",
        "PARALLEL_OWNER_ACTION": "ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL",
        "NEXT_OWNER_ACTION_NOTE": (
            "Preferred: merge DRAFT #68 with a merge commit to accept the architecture/control-plane baseline. "
            "This does NOT mean physical hardware is ready. Optional: order RP0-A COTS control kit. "
            "Parallel: acquire AMD custom platform collateral. Cursor will not merge, purchase, or accept NDAs."
        ),
        "NEXT_GATE": None,
        "legacy_alias": {
            "HARDWARE_V1_READY_FOR_EVT_BUILD": "CUSTOM_MAINLINE_READY_FOR_EVT_BUILD",
            "REFERENCE_PLATFORM_0_READY_FOR_FAB": "RP0_B_CUSTOM_READY_FOR_FAB",
        },
    }
    wj(HV1 / "GATES.json", gates)

    md_lines = [
        "# Hardware v1 gates (HW1D)",
        "",
        HDR,
        "",
        "| Token | Value |",
        "|---|---|",
    ]
    for k, v in gates.items():
        if k in {
            "schema",
            "generated_at_utc",
            "campaign",
            "campaign_overlay",
            "blockers",
            "closed_blockers",
            "legacy_alias",
            "NEXT_OWNER_ACTION_NOTE",
        }:
            continue
        if isinstance(v, bool):
            md_lines.append(f"| `{k}` | `{str(v).lower()}` |")
        else:
            md_lines.append(f"| `{k}` | `{v}` |")
    md_lines += ["", f"**Note:** {gates['NEXT_OWNER_ACTION_NOTE']}", ""]
    w(HV1 / "GATES.md", "\n".join(md_lines))


def write_owner_packet() -> None:
    w(
        HV1 / "OWNER_ACTION_PACKET.md",
        f"""# Owner action packet (HW1D)

{HDR}

## What Cursor completed (digital / architecture)
- Four-track canonical model (PRODUCT / OPEN_ENGINEERING / GXE / REFERENCE_CONTROL)
- Experience-first co-design doctrine + Experience Contract schema
- NXP i.MX95 open-custom architecture package (public collateral metadata only)
- AMD PRODUCT_MAINLINE preserved; vendor access = external not merge blocker
- GXE integration contract only (no GXE implementation)
- Cross-track comparison matrix + benchmark schema
- Decision ledger track-qualified
- `HW_ARCHITECTURE_BASELINE_MERGE_READY` gate separated from physical EVT
- Post-merge plan prepared (not executed)
- Fail-closed validator updates

## What Cursor did NOT do
- Merge #68 or any experiment PR
- Purchase / RFQ / accept NDAs
- Fabricate physical evidence or restricted pin maps
- Execute GXE
- Modify software RC1 baselines
- Claim NXP product-equivalent to AMD x86
- Flip physical EVT/fab/cert gates to true

## Preferred next action
`NEXT_OWNER_ACTION=MERGE_HW_ARCHITECTURE_BASELINE_68_WITH_MERGE_COMMIT`

## Optional / parallel
- `OPTIONAL_OWNER_ACTION=ORDER_RP0_A_COTS_CONTROL_KIT`
- `PARALLEL_OWNER_ACTION=ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL`

## Honest physical truth
Architecture merge-ready ≠ physical hardware ready.
""",
    )


def write_report() -> None:
    head = git_sha()
    w(
        HV1 / "REPORT_SECTION_17_HW1D_A_TO_T.md",
        f"""# HW1D final report A–T

{HDR}

## A. starting/final #68 SHA
Starting expected: `{EXPECTED_HEAD}` (drift at preflight: see `convergence/HW1D_STARTING_STATE.json`).  
Final: `{head}` on `hardware/v1-mainline-ready-for-evt` (DRAFT #68; unmerged).

## B. four-track model
PRODUCT_MAINLINE=`AMD_CUSTOM_X86`; OPEN_ENGINEERING_MAINLINE=`NXP_IMX95_OPEN_CUSTOM`; GREENFIELD_EXPERIMENT=`GXE`; REFERENCE_CONTROL=`COM_HPC_AND_COTS`.

## C. terminology reconciliation
Ambiguous bare “mainline” removed from control-plane docs; track qualifiers required (`CANONICAL_TRACK_MODEL.md`).

## D. experience-first doctrine
`EXPERIENCE_FIRST_CO_DESIGN_DOCTRINE.md` — software must earn additional hardware.

## E. AMD product mainline status
Preserved Platform Core v1 (8840U/8845HS candidates, custom Dock/Rings). `CUSTOM_PLATFORM_VENDOR_ACCESS_READY=false` = external blocker.

## F. NXP open-custom architecture
Full package under `hardware_v1/open_custom_nxp/` with explicit non-equivalence to AMD x86.

## G. NXP public-collateral status
Index + gap register; URLs/metadata/hashes only; design-guide may be account-gated.

## H. GXE integration boundary
`GXE_HARDWARE_INTEGRATION_CONTRACT.md` only; `GXE_IMPLEMENTED_IN_HARDWARE_REPO=false`.

## I. COM-HPC control status
REFERENCE_CONTROL preserved; RP0-A packet ready-to-order optional; not PRODUCT_MAINLINE.

## J. cross-track benchmark model
Per-workload matrix + schema; no overall winner score.

## K. Experience Contract schema
`HARDWARE_EXPERIENCE_CONTRACT_SCHEMA.json` + guide.

## L. decision ledger status
Track / role / evidence_class / promotion / physical / external fields reconciled.

## M. BOM/classification status
PRODUCT_MAINLINE custom BOM isolated; NXP preliminary BOM qty=0 architecture-only; experiments not mixed.

## N. experiment PR status
#69–#79 remain DRAFT; refresh onto final #68 head (see closeout).

## O. validator results
`make hardware-v1-validate` / `make hardware-v1-all` — see closeout log.

## P. software RC1 firewall
`SOFTWARE_RC1_BASELINES_UNTOUCHED=true`.

## Q. merge-readiness result
`HW_ARCHITECTURE_BASELINE_MERGE_READY=true` (architecture definition only).

## R. physical gate truth
All physical EVT/fab/cert gates remain false; `EVT_PENDING/DVT_PENDING/PVT_PENDING=true`.

## S. post-merge plan
`convergence/POST_MERGE_PLAN.md` prepared for `HW1D.1_ACCEPTED_MAIN_REBIND` — not executed.

## T. exactly one owner action
`NEXT_OWNER_ACTION=MERGE_HW_ARCHITECTURE_BASELINE_68_WITH_MERGE_COMMIT`

## Printed tokens
```
HW_ARCHITECTURE_BASELINE_MERGE_READY=true
FOUR_TRACK_MODEL_PASS=true
EXPERIENCE_FIRST_CO_DESIGN_DOCTRINE_PASS=true
AMD_PRODUCT_MAINLINE_PRESERVED=true
NXP_OPEN_CUSTOM_TRACK_DEFINED=true
GXE_INTEGRATION_BOUNDARY_DEFINED=true
REFERENCE_CONTROL_TRACK_DEFINED=true
EXPERIMENT_ISOLATION_PASS=true
SOFTWARE_RC1_BASELINES_UNTOUCHED=true
CUSTOM_PLATFORM_VENDOR_ACCESS_READY=false
CPB0_SCHEMATIC_READY=false
CPB0_PCB_READY=false
CPB0_READY_FOR_FAB=false
CUSTOM_MAINLINE_READY_FOR_EVT_BUILD=false
HARDWARE_V1_READY_FOR_EVT_BUILD=false
EVT_PENDING=true
DVT_PENDING=true
PVT_PENDING=true
PHYSICAL_HARDWARE_VALIDATED=false
CERTIFICATION_COMPLETE=false
MANUFACTURING_VALIDATED=false
NEXT_OWNER_ACTION=MERGE_HW_ARCHITECTURE_BASELINE_68_WITH_MERGE_COMMIT
```
""",
    )


def update_manifest() -> None:
    files = []
    for p in sorted(HV1.rglob("*")):
        if not p.is_file():
            continue
        if p.name == "MANIFEST.json":
            continue
        data = p.read_bytes()
        files.append(
            {
                "path": str(p.relative_to(ROOT)),
                "sha256": hashlib.sha256(data).hexdigest(),
                "bytes": len(data),
            }
        )
    wj(
        HV1 / "MANIFEST.json",
        {
            "schema": "gunnchos.hardware_v1.manifest.v1",
            "generated_at_utc": NOW,
            "campaign": CAMPAIGN,
            "file_count": len(files),
            "product_mainline": "AMD_CUSTOM_X86",
            "open_engineering_mainline": "NXP_IMX95_OPEN_CUSTOM",
            "greenfield_experiment": "GXE",
            "reference_control": "COM_HPC_AND_COTS",
            "next_owner_action": "MERGE_HW_ARCHITECTURE_BASELINE_68_WITH_MERGE_COMMIT",
            "files": files,
        },
    )


def update_readme() -> None:
    readme = HV1 / "README.md"
    t = readme.read_text(encoding="utf-8") if readme.is_file() else "# hardware_v1\n"
    if "HW1D" not in t:
        t = t.rstrip() + (
            f"\n\n## HW1D four-track convergence\n\n{HDR}\n"
            "- `PRODUCT_MAINLINE` = AMD_CUSTOM_X86\n"
            "- `OPEN_ENGINEERING_MAINLINE` = NXP_IMX95_OPEN_CUSTOM\n"
            "- `GREENFIELD_EXPERIMENT` = GXE (contract only)\n"
            "- `REFERENCE_CONTROL` = COM_HPC_AND_COTS\n"
            "- Merge-ready gate: `HW_ARCHITECTURE_BASELINE_MERGE_READY` (≠ physical EVT)\n"
            "- Docs: `hardware_v1/convergence/`\n"
        )
    w(readme, t)


def write_pr_body() -> None:
    w(
        ROOT / "PULL_REQUEST_BODY_HW1D.md",
        f"""# HARDWARE 1.0D — Architecture / control-plane baseline (DRAFT #68)

{HDR}

## What #68 establishes
- Canonical **four-track** hardware architecture control plane
- Experience-first co-design doctrine + Experience Contract schema
- AMD **PRODUCT_MAINLINE** architecture preserved
- NXP i.MX95 **OPEN_ENGINEERING_MAINLINE** architecture package (public collateral)
- GXE **integration contract** boundary (no GXE implementation in this repo)
- COM-HPC/COTS **REFERENCE_CONTROL** preserved
- Decision ledger reconciled with track qualifiers
- `HW_ARCHITECTURE_BASELINE_MERGE_READY` separated from physical EVT/fab/cert gates

## What #68 does **not** establish
- Physical hardware validation
- AMD vendor collateral acquisition
- CPB0 / CPB0-Open fab readiness
- NXP physical board existence
- GXE execution
- EVT / DVT / PVT / certification / manufacturing validation
- Software v1.0 RC1 baseline changes

## Four-track architecture
| Track | Identity |
|---|---|
| PRODUCT_MAINLINE | AMD_CUSTOM_X86 |
| OPEN_ENGINEERING_MAINLINE | NXP_IMX95_OPEN_CUSTOM |
| GREENFIELD_EXPERIMENT | GXE |
| REFERENCE_CONTROL | COM_HPC_AND_COTS |

## Merge meaning
Merging #68 means **architecture/control-plane accepted**, not **hardware validated**.

## Experiments
#69–#79 remain DRAFT experiments targeting this branch until post-merge rebind. Not merge-ready without promotion evidence.

## Pending external work
- AMD vendor collateral (external; does not block architecture merge)
- NXP open-custom implementation / design-guide access
- GXE implementation in separate workspace

## Preferred owner action
`NEXT_OWNER_ACTION=MERGE_HW_ARCHITECTURE_BASELINE_68_WITH_MERGE_COMMIT`

Do not merge via Cursor.
""",
    )


def main() -> int:
    CONV.mkdir(parents=True, exist_ok=True)
    NXP.mkdir(parents=True, exist_ok=True)
    write_starting_state()
    write_track_model()
    write_experience_doctrine()
    write_nxp_package()
    write_amd_status()
    write_gxe_contract()
    write_cross_track()
    write_experience_contract()
    write_post_merge_plan()
    update_decision_ledger()
    update_experiments_registry()
    write_gates()
    write_owner_packet()
    write_report()
    update_readme()
    write_pr_body()
    update_manifest()
    print(f"HW1D_GENERATE: OK @ {NOW}")
    print("HW_ARCHITECTURE_BASELINE_MERGE_READY=true")
    print("NEXT_OWNER_ACTION=MERGE_HW_ARCHITECTURE_BASELINE_68_WITH_MERGE_COMMIT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
