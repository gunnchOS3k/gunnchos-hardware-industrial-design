#!/usr/bin/env python3
"""HARDWARE 1.0B — RP0 COTS bring-up + digital blocker closure artifacts.

Honest digital package only. Does not purchase, RFQ-send, invent ball maps,
stock, lead times, or claim physical/cert/fab pass.
"""
from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HV1 = ROOT / "hardware_v1"
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
CAMPAIGN = "HARDWARE_1_0B_RP0_COTS_BLOCKER_CLOSURE"
STARTING_HEAD = "bd65bc67b413597a7d5534bc8dddaa9d7513b0c3"

# Live-verified public evidence (2026-09-18 audit). DigiKey/Mouser catalog scrape blocked.
NORDIC_HW_ZIP_URL = (
    "https://nsscprodmedia.blob.core.windows.net/prod/software-and-other-downloads/"
    "dev-kits/nrf54l15-dk/pca10156-nrf54l15-dk-1_0_0.zip"
)
NORDIC_HW_ZIP_SHA256 = "ed70a2233d009e7e4dd31a20f66527ef206b23bd357623850a9f3228a089e1d4"
NORDIC_HW_ZIP_BYTES = 14098311

FN990_MPN = "FN990B40W01T010300"
COM_MODULE_MPN = "COM-HPC-mMTL-155H-32G"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not content.endswith("\n"):
        content += "\n"
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def md(title: str, body: str) -> str:
    return (
        f"# {title}\n\n"
        f"**Generated:** {UTC}  \n"
        f"**Campaign:** `{CAMPAIGN}`  \n"
        f"**Claim boundary:** digital architecture / EVT preparation only — "
        f"not physical pass, not certification, not fab release, not purchased.\n\n"
        f"{body.strip()}\n"
    )


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def starting_blocker_snapshot() -> None:
    write_json(
        HV1 / "rp0b" / "HW1B_STARTING_BLOCKER_SNAPSHOT.json",
        {
            "schema": "gunnchos.hardware_v1.hw1b.starting_blocker_snapshot.v1",
            "campaign": CAMPAIGN,
            "captured_at_utc": UTC,
            "pr_68_state": {
                "number": 68,
                "state": "OPEN",
                "isDraft": True,
                "merged": False,
                "headRefOid_expected": STARTING_HEAD,
                "headRefOid_observed": STARTING_HEAD,
                "head_advanced_from_expected": False,
                "baseRefName": "main",
                "headRefName": "hardware/v1-mainline-ready-for-evt",
            },
            "experimental_prs_69_76_base": "hardware/v1-mainline-ready-for-evt",
            "SOFTWARE_RC1_BASELINES_UNTOUCHED": True,
            "starting_gates": {
                "HARDWARE_V1_READY_FOR_EVT_BUILD": False,
                "REFERENCE_PLATFORM_0_READY_FOR_FAB": False,
                "NEXT_OWNER_ACTION": "QUOTE_AND_BUILD_REFERENCE_PLATFORM_0",
            },
            "starting_blockers": [
                "EXT-COM-HPC-400PIN",
                "EXT-DSXL-DUAL-EDP",
                "EXT-JHL8440-BALLMAP",
                "EXT-JHL9040R-BALLMAP",
                "UNRES-NRF54L15-FOOTPRINT",
                "UNRES-FN990B40-AVL",
                "OWNER-RP0-QUOTE-AUTH",
            ],
            "doctrine": [
                "Do not order custom PCB that is not fabrication-ready",
                "Use COTS for RP0-A; vendor-gated pin maps block RP0-B only",
                "No RFQ send / purchase / supplier contact / NDA acceptance",
                "No software RC1 mutation",
            ],
        },
    )


def blocker_matrix() -> list[dict]:
    return [
        {
            "id": "EXT-COM-HPC-400PIN",
            "classification": "STILL_VENDOR_GATED_FOR_RP0_B",
            "also": ["NOT_NEEDED_FOR_RP0_A"],
            "rp0_a_blocking": False,
            "rp0_b_blocking": True,
            "evidence_path": "hardware_v1/reference_platform_0/RP0_A_COMPUTE_PLATFORM.md",
            "rationale": (
                "ADLINK COM-HPC Mini Base + mMTL COTS path enables RP0-A bring-up without "
                "a custom carrier. Authoritative COM-HPC Mini 400-pin net map for custom "
                "gunnchOS carrier remains vendor/PICMG gated; COTS reference board does not "
                "close custom pin-accurate fab."
            ),
        },
        {
            "id": "EXT-DSXL-DUAL-EDP",
            "classification": "CLOSED_BY_ARCHITECTURE_CHANGE",
            "also": [],
            "rp0_a_blocking": False,
            "rp0_b_blocking": False,
            "evidence_path": "hardware_v1/devices/ds_xl/DUAL_DISPLAY_ARCHITECTURE.md",
            "rationale": (
                "COM-HPC-mMTL family documents one native eDP + two DDI interfaces. "
                "DS-XL dual-display requirement retained as eDP + DDI/DP; no product "
                "requirement mandates two native eDP ports."
            ),
        },
        {
            "id": "EXT-JHL8440-BALLMAP",
            "classification": "STILL_VENDOR_GATED_FOR_RP0_B",
            "also": ["NOT_NEEDED_FOR_RP0_A"],
            "rp0_a_blocking": False,
            "rp0_b_blocking": True,
            "evidence_path": "hardware_v1/devices/dock/CUSTOM_DOCK_VENDOR_COLLATERAL_REQUIREMENTS.md",
            "rationale": (
                "Public functional capability/package class may exist, but pin-accurate "
                "ball map for custom dock PCB is not public. RP0-A uses COTS USB4 dock."
            ),
        },
        {
            "id": "EXT-JHL9040R-BALLMAP",
            "classification": "STILL_VENDOR_GATED_FOR_RP0_B",
            "also": ["NOT_NEEDED_FOR_RP0_A"],
            "rp0_a_blocking": False,
            "rp0_b_blocking": True,
            "evidence_path": "hardware_v1/devices/dock/CUSTOM_DOCK_VENDOR_COLLATERAL_REQUIREMENTS.md",
            "rationale": (
                "JHL9040R retimer ball map remains NDA/vendor-gated for custom fanout. "
                "Not required for RP0-A COTS dock behavioral validation."
            ),
        },
        {
            "id": "UNRES-NRF54L15-FOOTPRINT",
            "classification": "CLOSED_PUBLIC_EVIDENCE",
            "also": ["NOT_NEEDED_FOR_RP0_A"],
            "rp0_a_blocking": False,
            "rp0_b_blocking": False,
            "rp0_b_note": (
                "Wearable CSP47/HDI form-factor remains a separate feasibility gate; "
                "QFN48/DK evidence does not equal wearable geometry validation."
            ),
            "evidence_path": "hardware_v1/devices/rings/NRF54L15_PACKAGE_STRATEGY.md",
            "rationale": (
                "Nordic public nRF54L15 DK (PCA10156) uses QFN48; official hardware files "
                f"zip checksummed ({NORDIC_HW_ZIP_SHA256}). Closed for RP0-A / digital "
                "reference; CSP47 form-factor remains separate."
            ),
        },
        {
            "id": "UNRES-FN990B40-AVL",
            "classification": "CLOSED_PUBLIC_EVIDENCE",
            "also": [],
            "rp0_a_blocking": False,
            "rp0_b_blocking": False,
            "evidence_path": "hardware_v1/radio/FN990B40_RP0_A_AVL.md",
            "rationale": (
                f"Exact MPN {FN990_MPN} live-verified on Rutronik distributor listing and "
                "Telit manufacturer family pages. DigiKey/Mouser live catalog scrape blocked "
                "(bot/403); treat DigiKey/Mouser as VERIFY_AT_PURCHASE. "
                "PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING=true."
            ),
        },
        {
            "id": "OWNER-RP0-QUOTE-AUTH",
            "classification": "OWNER_ACTION_REQUIRED",
            "also": ["NOT_NEEDED_FOR_RP0_A"],
            "rp0_a_blocking": False,
            "rp0_b_blocking": True,
            "evidence_path": "hardware_v1/OWNER_ACTION_PACKET.md",
            "rationale": (
                "Reframed: preferred owner action is ORDER_RP0_A_COTS_BRINGUP_KIT "
                "(procurement packet ready; Cursor does not purchase). Owner quote/auth "
                "for custom RP0-B fab remains separate and cannot set READY_FOR_FAB."
            ),
            "superseded_next_action": "QUOTE_AND_BUILD_REFERENCE_PLATFORM_0",
            "preferred_next_action": "ORDER_RP0_A_COTS_BRINGUP_KIT",
        },
    ]


def build_blocker_matrix() -> None:
    rows = blocker_matrix()
    write_json(
        HV1 / "rp0b" / "BLOCKER_CLOSURE_MATRIX.json",
        {
            "schema": "gunnchos.hardware_v1.hw1b.blocker_closure_matrix.v1",
            "generated_at_utc": UTC,
            "campaign": CAMPAIGN,
            "starting_head": STARTING_HEAD,
            "blockers": rows,
        },
    )
    lines = [
        "## Classifications",
        "",
        "| ID | Classification | RP0-A blocking | RP0-B blocking | Evidence |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| `{r['id']}` | `{r['classification']}` | `{r['rp0_a_blocking']}` | "
            f"`{r['rp0_b_blocking']}` | `{r['evidence_path']}` |"
        )
    lines.append("")
    lines.append("## Rationales")
    for r in rows:
        lines.append(f"### `{r['id']}`")
        lines.append(r["rationale"])
        if r.get("rp0_b_note"):
            lines.append(f"Note: {r['rp0_b_note']}")
        lines.append("")
    write(HV1 / "rp0b" / "BLOCKER_CLOSURE_MATRIX.md", md("Blocker closure matrix (HW1B)", "\n".join(lines)))


def build_stage_model() -> None:
    write(
        HV1 / "reference_platform_0" / "RP0_STAGE_MODEL.md",
        md(
            "Reference Platform 0 stage model",
            f"""
## RP0-A — COTS Integration Bench
Purpose:
- physically exercise the mainline architecture without a custom PCB
- use commercially available reference/development platforms
- collect power, thermal, I/O, OS, driver, radio and workflow data
- unblock custom design decisions

No custom fabrication required.

## RP0-B — Custom gunnchOS Reference Carrier
Purpose:
- implement the net-accurate gunnchOS custom carrier/dock/ring EVT electronics
- requires vendor/PICMG pin maps and complete EDA outputs
- **only this stage may become READY_FOR_FAB**

## Tokens
| Token | Value | Meaning |
|---|---|---|
| `RP0_A_COTS_PROCUREMENT_PACKET_READY` | `true` | Exact COTS kit list + guide exist; not purchased |
| `RP0_A_READY_TO_ORDER` | `true` | Owner may order; Cursor will not purchase |
| `RP0_A_PHYSICAL_BUILD_PENDING` | `true` | No physical kit assembled yet |
| `RP0_A_BRINGUP_PENDING` | `true` | Bring-up matrix rows remain untested |
| `RP0_B_CUSTOM_READY_FOR_FAB` | `false` | Pin-accurate custom package incomplete |
| `REFERENCE_PLATFORM_0_READY_FOR_FAB` | `false` | **Legacy alias of** `RP0_B_CUSTOM_READY_FOR_FAB` |

## Hard rules
- COTS orderability ≠ custom fab readiness
- Owner purchase authorization ≠ `READY_FOR_FAB`
- COTS dock behavioral results ≠ custom dock PCB certification
- nRF DK/QFN evidence ≠ wearable CSP47 validation
- Development antennas ≠ production antenna design
""",
        ),
    )


def build_nordic() -> None:
    write(
        HV1 / "devices" / "rings" / "NRF54L15_PACKAGE_STRATEGY.md",
        md(
            "nRF54L15 package strategy",
            f"""
## DEC-RINGS-001 split
| Token | Value |
|---|---|
| `RING_EVT_ELECTRICAL_PLATFORM` | `QFN48/DK reference` |
| `RING_FORM_FACTOR_CANDIDATE` | `CSP47` (WLCSP production-size candidate) |
| `DK_HARDWARE_ID` | `PCA10156` |

## RP0-A path
- Use **nRF54L15 DK** (PCA10156) with SoC in **QFN48** for firmware, sensor-fusion, power, BLE, and haptics bring-up.
- Use Nordic official reference layout / hardware files — do not hand-invent RF matching.
- Hardware files zip (not redistributed in-repo; license/size):
  - URL: `{NORDIC_HW_ZIP_URL}`
  - sha256: `{NORDIC_HW_ZIP_SHA256}`
  - bytes: `{NORDIC_HW_ZIP_BYTES}`
  - version: `PCA10156-nRF54L15-DK 1.0.0`

## Wearable form-factor
- Keep **CSP47 / WLCSP** as compact Ring candidate.
- Require separate HDI/assembly feasibility gate before wearable board promotion.
- **nRF DK evidence cannot be called wearable-form-factor validation.**

## Blocker
`UNRES-NRF54L15-FOOTPRINT` → `CLOSED_PUBLIC_EVIDENCE` for RP0-A / digital reference.
""",
        ),
    )
    write(
        HV1 / "vendor_evidence" / "nordic" / "README.md",
        md(
            "Nordic vendor evidence index",
            f"""
## Policy
Do not commit Nordic binaries/PDFs if redistribution is restricted. Store URL + hash + metadata.

## Captured metadata (live fetch 2026-09-18)
| Artifact | URL | Notes |
|---|---|---|
| nRF54L15 DK product | https://www.nordicsemi.com/Products/Development-hardware/nRF54L15-DK | QFN48 DK |
| Hardware files page | https://www.nordicsemi.com/Products/Development-hardware/nRF54L15-DK/Hardware-files | PCA10156 |
| PCA10156 HW zip 1.0.0 | `{NORDIC_HW_ZIP_URL}` | sha256 `{NORDIC_HW_ZIP_SHA256}` ({NORDIC_HW_ZIP_BYTES} bytes) |

## Verified identifiers
- DK: `PCA10156`
- EVT electrical package: `QFN48`
- Form-factor candidate: `CSP47` / WLCSP (separate gate)
""",
        ),
    )
    write_json(
        HV1 / "vendor_evidence" / "nordic" / "PCA10156_HW_FILES_METADATA.json",
        {
            "artifact": "PCA10156-nRF54L15-DK 1_0_0.zip",
            "url": NORDIC_HW_ZIP_URL,
            "sha256": NORDIC_HW_ZIP_SHA256,
            "bytes": NORDIC_HW_ZIP_BYTES,
            "dk_id": "PCA10156",
            "soc_package_on_dk": "QFN48",
            "redistributed_in_repo": False,
            "captured_at_utc": UTC,
        },
    )


def build_fn990() -> None:
    write(
        HV1 / "radio" / "FN990B40_RP0_A_AVL.md",
        md(
            "FN990B40 RP0-A AVL",
            f"""
## Exact reference MPN
| Field | Value |
|---|---|
| Manufacturer | Telit Cinterion |
| Family | FN990B40 |
| Exact MPN | `{FN990_MPN}` |
| Form factor | M.2 Key-B cellular data card |
| Status | AVL identity closed for RP0-A; **NOT_PURCHASED** |

## Live distributor / manufacturer evidence
| Source | Status | Notes |
|---|---|---|
| Telit product family | LIVE_VERIFIED | https://www.telit.com/devices/fn990b40/ |
| Rutronik | LIVE_VERIFIED | lists `{FN990_MPN}` (https://www.rutronik24.com/product/telit/fn990b40w01t010300/24844173.html) |
| Round Solutions | LIVE_VERIFIED | SKU `{FN990_MPN}` |
| DigiKey | LIVE_SCRAPE_BLOCKED_403 | treat as `VERIFY_AT_PURCHASE` |
| Mouser | LIVE_SCRAPE_BLOCKED | treat as `VERIFY_AT_PURCHASE` |

## Prices / stock / lead
`VERIFY_AT_PURCHASE` — do not invent.

## Antenna
| Token | Value |
|---|---|
| `PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING` | `true` |
| Dev antenna kit | Development-only; **not** production antenna validation |

## Blocker
`UNRES-FN990B40-AVL` → `CLOSED_PUBLIC_EVIDENCE` for RP0-A (exact MPN + active distributor/manufacturer evidence).
""",
        ),
    )


def build_compute() -> None:
    write(
        HV1 / "reference_platform_0" / "RP0_A_COMPUTE_PLATFORM.md",
        md(
            "RP0-A compute platform (ADLINK COTS)",
            f"""
## Mainline binding
COM-HPC Mini x86 Meteor Lake-class remains mainline.

## RP0-A COTS path
| Item | Selection | Evidence |
|---|---|---|
| Module family | COM-HPC-mMTL | https://www.adlinktech.com/products/computer_on_modules/com-hpc_mini_module/com-hpc-mmtl |
| Module SKU | `{COM_MODULE_MPN}` | ADLINK ordering information (live page hit) |
| Reference carrier | COM-HPC Mini Base (ATX) | ADLINK reference carrier |
| Cooling | Released heat spreader / fan for mMTL | VERIFY_AT_PURCHASE exact accessory SKU |
| Display interfaces | **1x eDP 1.4b + 2x DDI** (DP/HDMI/DVI) | ADLINK wiki/module docs — **not dual native eDP** |

## Required RP0-A capabilities
gunnchOS boot, NVMe, Wi-Fi, optional M.2 cellular, native eDP test, second-display DDI/DP test,
USB4 test, camera path where carrier supports, audio, GPIO/I2C/SPI, power measurement, debug/recovery.

## EXT-COM-HPC-400PIN
`STILL_VENDOR_GATED_FOR_RP0_B` — COTS base does **not** unlock custom 400-pin net-accurate fab.
`EXT_COM_HPC_400PIN_RP0_A_BLOCKING=false`
`EXT_COM_HPC_400PIN_RP0_B_BLOCKING=true`
""",
        ),
    )


def build_display() -> None:
    write(
        HV1 / "devices" / "ds_xl" / "DUAL_DISPLAY_ARCHITECTURE.md",
        md(
            "DS-XL dual-display architecture",
            """
## Authoritative module display map (COM-HPC-mMTL)
- Display interfaces: **one native eDP** + **two DDI** (DP/HDMI/DVI class)
- Do **not** label this configuration as “dual native eDP”

## RP0-A / early EVT
| Display | Path |
|---|---|
| Display A | Native eDP |
| Display B | DDI / DisplayPort |

Validate: dual independent operation, suspend/resume, hotplug, compositor layout, power, sustained workload.

## Product-form-factor DS-XL
Second internal panel remains an engineering decision among:
- DDI/DP-native panel/controller
- qualified DP-to-panel bridge
- alternate module mapping if authoritative docs support it

## Requirement retained
Two **functional** displays remain required.

## Blocker
`EXT-DSXL-DUAL-EDP` → `CLOSED_BY_ARCHITECTURE_CHANGE`
""",
        ),
    )


def build_dock() -> None:
    write(
        HV1 / "reference_platform_0" / "RP0_A_DOCK_VALIDATION_PATH.md",
        md(
            "RP0-A dock validation path (COTS USB4)",
            """
## Mainline Dock Gen-1 (unchanged intent)
USB4 40 Gb/s, USB PD EPR, 2.5 GbE, display, downstream USB, field-updatable controller.

## RP0-A approach
Use a commercially available USB4/TB4 dock/reference platform to validate gunnchOS USB4,
display, Ethernet, USB, suspend/resume, power-policy, and recovery.

## Hard boundary
- RP0-A COTS dock results **do not** prove / certify the custom gunnchOS dock PCB
- Capture VID/PID/controller/firmware when accessible during physical bring-up
- Ball maps remain vendor-gated for RP0-B

## Requirements-equivalence matrix (behavioral)
| Intended Dock v1 behavior | RP0-A COTS proxy | Equivalence class |
|---|---|---|
| USB4 host link | COTS USB4/TB4 dock uplink | BEHAVIORAL_PROXY |
| External display | COTS dock DP/HDMI | BEHAVIORAL_PROXY |
| 2.5 GbE | COTS dock Ethernet (note if 1G only) | PARTIAL_IF_1G |
| Downstream USB | COTS dock USB-A/C | BEHAVIORAL_PROXY |
| PD / power policy | Certified PD supply + meter | BEHAVIORAL_PROXY |
| Custom JHL8440 fanout | — | NOT_COVERED (RP0-B) |
| Custom JHL9040R retimer | — | NOT_COVERED (RP0-B) |

## Tokens
`EXT_JHL8440_BALLMAP_RP0_A_BLOCKING=false`
`EXT_JHL8440_BALLMAP_RP0_B_BLOCKING=true`
`EXT_JHL9040R_BALLMAP_RP0_A_BLOCKING=false`
`EXT_JHL9040R_BALLMAP_RP0_B_BLOCKING=true`
""",
        ),
    )
    write(
        HV1 / "devices" / "dock" / "CUSTOM_DOCK_VENDOR_COLLATERAL_REQUIREMENTS.md",
        md(
            "Custom dock vendor collateral requirements (RP0-B)",
            """
## Still required before custom dock PCB fab
| Item | Access class | Blocks RP0-A? | Blocks RP0-B? |
|---|---|---|---|
| Intel JHL8440 pin-accurate / ball-map design collateral | NDA likely / vendor support | no | yes |
| Intel JHL9040R pin-accurate / ball-map design collateral | NDA likely / vendor support | no | yes |
| Reference schematic/layout for USB4 40 dock class | NDA / account | no | yes |
| PD controller integration requirements | often public + vendor app notes | no | yes |
| Firmware/NVM programming collateral | vendor | no | yes |
| Thunderbolt/USB4 design & certification requirements | public overview + vendor/cert labs | no | yes (for cert path) |

## Classification
`EXT-JHL8440-BALLMAP` = `STILL_VENDOR_GATED_FOR_RP0_B`
`EXT-JHL9040R-BALLMAP` = `STILL_VENDOR_GATED_FOR_RP0_B`

Do not invent Intel ball maps.
""",
        ),
    )


def procurement_rows() -> list[dict]:
    common = {
        "price": "VERIFY_AT_PURCHASE",
        "stock": "VERIFY_AT_PURCHASE",
        "lead_time": "VERIFY_AT_PURCHASE",
        "physical_purchase_status": "NOT_PURCHASED",
    }

    def row(**kwargs):
        out = dict(common)
        out.update(kwargs)
        return out

    return [
        row(
            item_id="RP0A-CPU-001",
            category="compute",
            manufacturer="ADLINK",
            mpn=COM_MODULE_MPN,
            distributor_vendor="ADLINK / authorized distributor",
            vendor_url="https://www.adlinktech.com/products/computer_on_modules/com-hpc_mini_module/com-hpc-mmtl",
            qty="1",
            purpose="COM-HPC Mini Meteor Lake module for RP0-A",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="Same COM-HPC-mMTL family; memory/SKU delta documented; eDP+DDI retained",
        ),
        row(
            item_id="RP0A-CPU-002",
            category="compute",
            manufacturer="ADLINK",
            mpn="COM-HPC Mini Base",
            distributor_vendor="ADLINK / authorized distributor",
            vendor_url="https://www.adlinktech.com/en/com-hpc-mini",
            qty="1",
            purpose="COTS reference carrier (no custom PCB)",
            required_or_optional="required",
            substitutes_allowed="no",
            substitute_qualification_rule="Must be official ADLINK COM-HPC Mini Base or owner-approved equivalent with documented I/O",
        ),
        row(
            item_id="RP0A-CPU-003",
            category="compute",
            manufacturer="ADLINK",
            mpn="mMTL heatspreader/fan kit (VERIFY exact released SKU)",
            distributor_vendor="ADLINK",
            vendor_url="https://www.adlinktech.com/products/computer_on_modules/com-hpc_mini_module/com-hpc-mmtl",
            qty="1",
            purpose="Thermal solution for module",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="Must meet ADLINK thermal guidance for selected SKU",
        ),
        row(
            item_id="RP0A-CPU-004",
            category="compute",
            manufacturer="Generic / ADLINK-specified",
            mpn="ATX/module PSU per Mini Base requirements",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="Compatible power supply",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="Meets carrier voltage/current; safety certified",
        ),
        row(
            item_id="RP0A-STO-001",
            category="storage",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="M.2 NVMe 2280 reference SSD",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="NVMe boot/storage bring-up",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="PCIe NVMe; capacity >=256GB preferred",
        ),
        row(
            item_id="RP0A-WIFI-001",
            category="wifi",
            manufacturer="Intel",
            mpn="BE200 class M.2 Key E",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="Wi-Fi 7 / BT mainline class",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="Intel BE200-class or documented Key E alternate",
        ),
        row(
            item_id="RP0A-WIFI-002",
            category="wifi",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="M.2 Wi-Fi antenna cable kit (bench)",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="Bench RF antennas for Wi-Fi/BT",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="Development use only; not production antenna design",
        ),
        row(
            item_id="RP0A-CELL-001",
            category="cellular_optional",
            manufacturer="Telit Cinterion",
            mpn=FN990_MPN,
            distributor_vendor="Rutronik (live); DigiKey/Mouser VERIFY_AT_PURCHASE",
            vendor_url="https://www.rutronik24.com/product/telit/fn990b40w01t010300/24844173.html",
            qty="1",
            purpose="Optional 5G Sub-6 M.2 module",
            required_or_optional="optional",
            substitutes_allowed="yes",
            substitute_qualification_rule="Quectel RM520N-GL approved alternate; document delta",
        ),
        row(
            item_id="RP0A-CELL-002",
            category="cellular_optional",
            manufacturer="Telit Cinterion",
            mpn="FN990 EVB/test board (VERIFY public PN)",
            distributor_vendor="Telit / authorized",
            vendor_url="https://www.telit.com/devices/fn990b40/",
            qty="1",
            purpose="Module evaluation if M.2 slot path insufficient",
            required_or_optional="optional",
            substitutes_allowed="yes",
            substitute_qualification_rule="Official Telit FN990 evaluation path",
        ),
        row(
            item_id="RP0A-CELL-003",
            category="cellular_optional",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="Development cellular antenna kit",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="Development antennas only",
            required_or_optional="optional",
            substitutes_allowed="yes",
            substitute_qualification_rule="PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING=true — not production validation",
        ),
        row(
            item_id="RP0A-RING-001",
            category="rings",
            manufacturer="Nordic Semiconductor",
            mpn="nRF54L15-DK (PCA10156)",
            distributor_vendor="Nordic / DigiKey VERIFY_AT_PURCHASE",
            vendor_url="https://www.nordicsemi.com/Products/Development-hardware/nRF54L15-DK",
            qty="1",
            purpose="Ring EVT electrical / firmware platform (QFN48)",
            required_or_optional="required",
            substitutes_allowed="no",
            substitute_qualification_rule="Must be official PCA10156 DK",
        ),
        row(
            item_id="RP0A-RING-002",
            category="rings",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="IMU breakout (BMI270-class or documented alt)",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="IMU bring-up with DK",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="I2C/SPI IMU with published datasheet",
        ),
        row(
            item_id="RP0A-RING-003",
            category="rings",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="Capacitive/touch sensing eval hardware",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="Touch/contact sensing prototype",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="Compatible with nRF54L15 GPIO/peripherals",
        ),
        row(
            item_id="RP0A-RING-004",
            category="rings",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="LRA + driver evaluation kit",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="Haptics evaluation",
            required_or_optional="optional",
            substitutes_allowed="yes",
            substitute_qualification_rule="Document driver IC and drive voltage",
        ),
        row(
            item_id="RP0A-RING-005",
            category="rings",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="Programmable PSU / power measurement accessory",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="Ring power characterization",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="mA-resolution current measurement preferred",
        ),
        row(
            item_id="RP0A-RING-006",
            category="rings",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="Magnetic contact charging prototype components",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="Magnetic cradle charge prototype",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="Pogo/magnetic contacts; not inductive experiment mix",
        ),
        row(
            item_id="RP0A-DOCK-001",
            category="dock",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="COTS USB4/TB4 dock (40 Gb/s class preferred)",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="Behavioral USB4/display/Ethernet/USB validation",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="Must expose USB4 uplink + display + Ethernet + USB; document VID/PID",
        ),
        row(
            item_id="RP0A-DOCK-002",
            category="dock",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="Certified USB4 cable(s)",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="2",
            purpose="USB4 link integrity",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="USB4-certified cable markings",
        ),
        row(
            item_id="RP0A-DOCK-003",
            category="dock",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="USB-C PD EPR-capable supply",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="PD power policy tests",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="PD certified; document wattage",
        ),
        row(
            item_id="RP0A-DOCK-004",
            category="dock",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="2.5 GbE endpoint (or 1G with PARTIAL note)",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="Dock Ethernet validation",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="Prefer 2.5G NIC; if 1G only mark PARTIAL",
        ),
        row(
            item_id="RP0A-DOCK-005",
            category="dock",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="External display endpoint(s)",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="2",
            purpose="Dock + DDI dual-display tests",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="DP and/or HDMI panels/monitors",
        ),
        row(
            item_id="RP0A-LAB-001",
            category="lab_debug",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="USB power meter",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="USB-C power measurement",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="Measures V/I on USB-C",
        ),
        row(
            item_id="RP0A-LAB-002",
            category="lab_debug",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="Bench PSU",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="Controlled power bring-up",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="Adjustable CC/CV preferred",
        ),
        row(
            item_id="RP0A-LAB-003",
            category="lab_debug",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="Logic analyzer",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="I2C/SPI/UART debug",
            required_or_optional="optional",
            substitutes_allowed="yes",
            substitute_qualification_rule=">=8 channels preferred",
        ),
        row(
            item_id="RP0A-LAB-004",
            category="lab_debug",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="USB-UART adapter",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="Serial console",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="3.3V UART",
        ),
        row(
            item_id="RP0A-LAB-005",
            category="lab_debug",
            manufacturer="SEGGER / Nordic OB",
            mpn="SWD/J-Link (if not included on DK)",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="MCU debug (DK includes OB J-Link)",
            required_or_optional="optional",
            substitutes_allowed="yes",
            substitute_qualification_rule="Not required if using PCA10156 OB debugger",
        ),
        row(
            item_id="RP0A-LAB-006",
            category="lab_debug",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="Thermal probes",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="Skin/module thermal measurement",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="Thermocouple or calibrated IR",
        ),
        row(
            item_id="RP0A-LAB-007",
            category="lab_debug",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="Current measurement shunt/ammeter",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="Idle/compile/AI/game power",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="Adequate range for module + dock loads",
        ),
        row(
            item_id="RP0A-LAB-008",
            category="lab_debug",
            manufacturer="VERIFY_AT_PURCHASE",
            mpn="ESD-safe mat/strap accessories",
            distributor_vendor="VERIFY_AT_PURCHASE",
            vendor_url="VERIFY_AT_PURCHASE",
            qty="1",
            purpose="ESD-safe bench practice",
            required_or_optional="required",
            substitutes_allowed="yes",
            substitute_qualification_rule="Standard ESD workstation kit",
        ),
    ]


def build_procurement() -> None:
    fields = [
        "item_id",
        "category",
        "manufacturer",
        "mpn",
        "distributor_vendor",
        "vendor_url",
        "qty",
        "purpose",
        "required_or_optional",
        "substitutes_allowed",
        "substitute_qualification_rule",
        "price",
        "stock",
        "lead_time",
        "physical_purchase_status",
    ]
    rows = procurement_rows()
    write_csv(HV1 / "reference_platform_0" / "RP0_A_PROCUREMENT_BOM.csv", fields, rows)
    write(
        HV1 / "reference_platform_0" / "RP0_A_PROCUREMENT_GUIDE.md",
        md(
            "RP0-A procurement guide",
            f"""
## Purpose
Exact owner-facing COTS bring-up kit list. Cursor does **not** purchase.

## Status tokens
| Token | Value |
|---|---|
| `RP0_A_COTS_PROCUREMENT_PACKET_READY` | `true` |
| `RP0_A_READY_TO_ORDER` | `true` |
| `physical_purchase_status` (all rows) | `NOT_PURCHASED` |
| `price` / `stock` / `lead_time` | `VERIFY_AT_PURCHASE` |

## BOM
See `RP0_A_PROCUREMENT_BOM.csv` ({len(rows)} line items).

## Exact MPN anchors (verified where noted)
- Compute module: `{COM_MODULE_MPN}`
- Cellular optional: `{FN990_MPN}`
- Rings DK: `nRF54L15-DK` / `PCA10156`

## Order of operations
1. Order required compute + storage + Wi-Fi + cooling + PSU
2. Order rings DK + sensing/charge prototype parts
3. Order COTS USB4 dock + cables + displays + lab meters
4. Optionally order FN990 + development antennas
5. Do **not** order custom carrier/dock/ring PCBs until RP0-B pin-accurate files exist

## Preferred next action
`NEXT_OWNER_ACTION=ORDER_RP0_A_COTS_BRINGUP_KIT`
""",
        ),
    )


def build_vendor_access() -> None:
    write(
        HV1 / "vendor_access" / "RP0_B_VENDOR_ACCESS_PACKET.md",
        md(
            "RP0-B vendor access packet",
            """
## Purpose
Exact materials still needed before **custom** fabrication. No credentials. No NDA acceptance by Cursor.

## PICMG / ADLINK
| Material | Access | Owner action | Blocks RP0-A? | Blocks RP0-B? |
|---|---|---|---|---|
| COM-HPC Mini authoritative pin assignment / base spec for custom carrier | public overview may exist; full pin/net for custom often member/vendor | obtain PICMG/ADLINK design collateral | no | yes |
| ADLINK selected-module user manual (`COM-HPC-mMTL-155H-32G`) | account/login likely | request/download | no | yes |
| Reference carrier schematics/layout where permitted | vendor / NDA possible | request permissioned package | no | yes |
| Connector mechanical model | often public CAD / vendor | download | no | yes |
| Carrier design guide | vendor | request | no | yes |

## Intel dock silicon
| Material | Access | Owner action | Blocks RP0-A? | Blocks RP0-B? |
|---|---|---|---|---|
| JHL8440 design collateral (pin-accurate) | NDA likely | vendor support / NDA path | no | yes |
| JHL9040R design collateral (pin-accurate) | NDA likely | vendor support / NDA path | no | yes |
| Reference schematic/layout | NDA / account | request | no | yes |
| PD/controller integration requirements | mixed public/vendor | collect app notes | no | yes |
| Firmware/NVM programming collateral | vendor | request | no | yes |
| Thunderbolt/USB4 design & certification requirements | public + cert labs | plan cert path | no | yes (for cert) |

## If owner declines RP0-A order
`NEXT_GATE=ACQUIRE_RP0_B_VENDOR_COLLATERAL`
""",
        ),
    )


def bringup_rows() -> list[dict]:
    tests = [
        ("power-on", "compute", "PSU + module + base", "rails within spec", "boot LED/POST present"),
        ("BIOS/UEFI", "compute", "module + display", "enter setup", "setup reachable"),
        ("TPM", "compute", "module TPM", "tpm2 presence", "TPM enumerated"),
        ("Secure Boot", "compute", "UEFI", "secure boot state read", "state documented"),
        ("gunnchOS boot", "compute", "NVMe image", "boot to shell/UI", "OS boots"),
        ("NVMe", "storage", "NVMe SSD", "enumerate + R/W", "device usable"),
        ("Wi-Fi", "wifi", "BE200 + antennas", "associate + iperf/smoke", "link up"),
        ("Bluetooth", "wifi", "BE200", "scan/pair smoke", "BT up"),
        ("optional cellular", "cellular", "FN990 + antennas", "enumerate modem", "modem present if installed"),
        ("eDP", "display", "eDP panel/path", "image stable", "Display A works"),
        ("second display over DDI/DP", "display", "DDI/DP monitor", "independent output", "Display B works"),
        ("USB4", "dock", "USB4 cable + dock", "link rate / device tree", "USB4 link up"),
        ("USB-C PD behavior", "power", "PD supply + meter", "contract negotiation", "expected PDO"),
        ("audio", "compute", "carrier audio", "playback/record smoke", "audio path works"),
        ("camera", "compute", "carrier CSI if present", "capture frame", "frame or N/A documented"),
        ("sleep/wake", "os", "compute", "S3/S0ix cycle", "resume OK"),
        ("suspend/resume", "os", "compute+dock", "cycle with dock", "resume OK"),
        ("recovery", "os", "recovery media", "recover boot", "recovery path works"),
        ("firmware update", "fw", "vendor capsule/EC path", "apply + reboot", "update succeeds or fail closed"),
        ("thermals", "thermal", "probes", "skin/module temps", "within provisional limits"),
        ("idle/compile/AI/game power", "power", "meter", "power samples", "profiles recorded"),
        ("dock display", "dock", "COTS dock + display", "external display", "image OK"),
        ("dock Ethernet", "dock", "COTS dock + NIC", "ping/throughput", "link OK or PARTIAL"),
        ("dock USB", "dock", "COTS dock USB", "enumerate peripherals", "USB OK"),
        ("Ring BLE", "rings", "PCA10156", "advertise/connect", "BLE OK"),
        ("Ring IMU", "rings", "DK + IMU", "sample stream", "IMU OK"),
        ("Ring touch/contact", "rings", "cap eval", "touch events", "events OK"),
        ("Ring latency", "rings", "DK + host", "end-to-end latency", "latency recorded"),
        ("Ring false-positive measurements", "rings", "cap eval", "FP rate", "rate recorded"),
        ("Ring haptics", "rings", "LRA eval", "actuation", "haptics OK or deferred"),
        ("Ring charging", "rings", "magnetic contacts", "charge current", "charge path OK"),
    ]
    rows = []
    for name, evidence_class, hw, measurement, criterion in tests:
        rows.append(
            {
                "test": name,
                "evidence_class": evidence_class,
                "required_hardware": hw,
                "measurement": measurement,
                "pass_criterion": criterion,
                "current_state": "UNTESTED_PENDING_PHYSICAL",
                "owner_lab_action": "Execute after RP0-A kit arrives; record evidence artifacts",
            }
        )
    return rows


def build_bringup() -> None:
    fields = [
        "test",
        "evidence_class",
        "required_hardware",
        "measurement",
        "pass_criterion",
        "current_state",
        "owner_lab_action",
    ]
    rows = bringup_rows()
    write_csv(HV1 / "reference_platform_0" / "RP0_A_BRINGUP_MATRIX.csv", fields, rows)
    assert all(r["current_state"] == "UNTESTED_PENDING_PHYSICAL" for r in rows)


def build_hw1b_report() -> None:
    write(
        HV1 / "REPORT_SECTION_15_HW1B_A_TO_T.md",
        md(
            "HW1B final report A–T",
            f"""
## A. #68 starting/final head
Starting (expected): `{STARTING_HEAD}`  
Final: see git after push (must remain on `hardware/v1-mainline-ready-for-evt`, DRAFT #68).

## B. Blocker closure matrix
`hardware_v1/rp0b/BLOCKER_CLOSURE_MATRIX.md`

## C. nRF54L15 public blocker result
`UNRES_NRF54L15_FOOTPRINT_CLOSED=true` (QFN48/DK PCA10156 public files checksummed; CSP47 separate)

## D. FN990B40 AVL result
`UNRES_FN990B40_AVL_CLOSED=true` (exact MPN `{FN990_MPN}`; DigiKey/Mouser scrape blocked → VERIFY_AT_PURCHASE)  
`PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING=true`

## E. COM-HPC public/COTS result
ADLINK `{COM_MODULE_MPN}` + Mini Base COTS path documented for RP0-A.

## F. Remaining COM-HPC vendor-gated data
`EXT_COM_HPC_400PIN_RP0_A_BLOCKING=false`  
`EXT_COM_HPC_400PIN_RP0_B_BLOCKING=true`

## G. DS-XL display architecture correction
One eDP + DDI/DP; `EXT_DSXL_DUAL_EDP_CLOSED=true` via `CLOSED_BY_ARCHITECTURE_CHANGE`.

## H. Intel dock public data result
Functional USB4 40 class retained; COTS dock path for RP0-A.

## I. Remaining dock NDA/vendor collateral
`EXT_JHL8440_BALLMAP_RP0_A_BLOCKING=false` / `..._RP0_B_BLOCKING=true`  
`EXT_JHL9040R_BALLMAP_RP0_A_BLOCKING=false` / `..._RP0_B_BLOCKING=true`

## J. RP0-A architecture
COTS Integration Bench — no custom PCB.

## K. RP0-A procurement packet
`RP0_A_PROCUREMENT_BOM.csv` + `RP0_A_PROCUREMENT_GUIDE.md`

## L. Exact MPN list
`{COM_MODULE_MPN}`, `{FN990_MPN}`, `nRF54L15-DK/PCA10156` (+ VERIFY_AT_PURCHASE accessories)

## M. RP0-A bring-up matrix
`RP0_A_BRINGUP_MATRIX.csv` — all rows `UNTESTED_PENDING_PHYSICAL`

## N. RP0-B custom-fab blockers
400-pin map, JHL8440/9040R ballmaps, owner custom fab auth, complete EDA

## O. Experiment PR status
#69–#76 remain DRAFT targeting mainline; refresh after #68 head advances

## P. Validation results
See `make hardware-v1-validate` / `make hardware-v1-all`

## Q. Updated gates
See `hardware_v1/GATES.json`

## R. Software RC1 firewall
`SOFTWARE_RC1_BASELINES_UNTOUCHED=true`

## S. Owner action packet
`hardware_v1/OWNER_ACTION_PACKET.md`

## T. Exactly one next action
`NEXT_OWNER_ACTION=ORDER_RP0_A_COTS_BRINGUP_KIT`
""",
        ),
    )


def hw1b_gate_overlay() -> dict:
    """Gate tokens for HW1B — applied by campaign generator."""
    active_blockers = [
        {
            "id": "EXT-COM-HPC-400PIN",
            "severity": "PICMG/ADLINK COM-HPC Mini net-accurate pin map for custom RP0-B carrier",
            "classification": "STILL_VENDOR_GATED_FOR_RP0_B",
            "blocks": ["RP0_B_CUSTOM_READY_FOR_FAB", "REFERENCE_PLATFORM_0_READY_FOR_FAB"],
            "rp0_a_blocking": False,
            "rp0_b_blocking": True,
        },
        {
            "id": "EXT-JHL8440-BALLMAP",
            "severity": "Intel JHL8440 ball map (NDA) for pin-accurate custom dock fanout",
            "classification": "STILL_VENDOR_GATED_FOR_RP0_B",
            "blocks": ["DOCK_HW_DIGITAL_RELEASE_PACKAGE", "RP0_B_CUSTOM_READY_FOR_FAB"],
            "rp0_a_blocking": False,
            "rp0_b_blocking": True,
        },
        {
            "id": "EXT-JHL9040R-BALLMAP",
            "severity": "Intel JHL9040R retimer ball map (NDA)",
            "classification": "STILL_VENDOR_GATED_FOR_RP0_B",
            "blocks": ["DOCK_HW_DIGITAL_RELEASE_PACKAGE", "RP0_B_CUSTOM_READY_FOR_FAB"],
            "rp0_a_blocking": False,
            "rp0_b_blocking": True,
        },
        {
            "id": "OWNER-RP0-B-FAB-AUTH",
            "severity": "Owner authorization for custom RP0-B fabrication after pin-accurate package exists",
            "classification": "OWNER_ACTION_REQUIRED",
            "blocks": ["HARDWARE_V1_READY_FOR_EVT_BUILD"],
            "rp0_a_blocking": False,
            "rp0_b_blocking": True,
        },
    ]
    closed = [
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
    ]
    return {
        "HARDWARE_V1_DIGITAL_ARCHITECTURE_COMPLETE": True,
        "DIGITAL_ARCHITECTURE_PACKAGE_COMPLETE": True,
        "HARDWARE_V1_READY_FOR_EVT_BUILD": False,
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
        "SOFTWARE_RC1_BASELINES_UNTOUCHED": True,
        "blockers": active_blockers,
        "closed_blockers": closed,
        "NEXT_OWNER_ACTION": "ORDER_RP0_A_COTS_BRINGUP_KIT",
        "NEXT_OWNER_ACTION_NOTE": (
            "RP0-A COTS procurement packet is ready. Cursor will not purchase. "
            "RP0-B custom fab remains blocked on vendor pin/ball maps. "
            "COTS orderability does not set READY_FOR_FAB."
        ),
        "NEXT_GATE": None,
        "NEXT_GATE_IF_OWNER_DECLINES_ORDER": "ACQUIRE_RP0_B_VENDOR_COLLATERAL",
    }


def build_all() -> None:
    starting_blocker_snapshot()
    build_blocker_matrix()
    build_stage_model()
    build_nordic()
    build_fn990()
    build_compute()
    build_display()
    build_dock()
    build_procurement()
    build_vendor_access()
    build_bringup()
    build_hw1b_report()
    write_json(HV1 / "rp0b" / "HW1B_GATE_OVERLAY.json", hw1b_gate_overlay())
    print(f"OK HW1B artifacts at {UTC}")


if __name__ == "__main__":
    build_all()
