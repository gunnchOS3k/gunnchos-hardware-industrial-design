# Blocker closure matrix (HW1B)

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0B_RP0_COTS_BLOCKER_CLOSURE`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.

## Classifications

| ID | Classification | RP0-A blocking | RP0-B blocking | Evidence |
|---|---|---|---|---|
| `EXT-COM-HPC-400PIN` | `STILL_VENDOR_GATED_FOR_RP0_B` | `False` | `True` | `hardware_v1/reference_platform_0/RP0_A_COMPUTE_PLATFORM.md` |
| `EXT-DSXL-DUAL-EDP` | `CLOSED_BY_ARCHITECTURE_CHANGE` | `False` | `False` | `hardware_v1/devices/ds_xl/DUAL_DISPLAY_ARCHITECTURE.md` |
| `EXT-JHL8440-BALLMAP` | `STILL_VENDOR_GATED_FOR_RP0_B` | `False` | `True` | `hardware_v1/devices/dock/CUSTOM_DOCK_VENDOR_COLLATERAL_REQUIREMENTS.md` |
| `EXT-JHL9040R-BALLMAP` | `STILL_VENDOR_GATED_FOR_RP0_B` | `False` | `True` | `hardware_v1/devices/dock/CUSTOM_DOCK_VENDOR_COLLATERAL_REQUIREMENTS.md` |
| `UNRES-NRF54L15-FOOTPRINT` | `CLOSED_PUBLIC_EVIDENCE` | `False` | `False` | `hardware_v1/devices/rings/NRF54L15_PACKAGE_STRATEGY.md` |
| `UNRES-FN990B40-AVL` | `CLOSED_PUBLIC_EVIDENCE` | `False` | `False` | `hardware_v1/radio/FN990B40_RP0_A_AVL.md` |
| `OWNER-RP0-QUOTE-AUTH` | `OWNER_ACTION_REQUIRED` | `False` | `True` | `hardware_v1/OWNER_ACTION_PACKET.md` |

## Rationales
### `EXT-COM-HPC-400PIN`
ADLINK COM-HPC Mini Base + mMTL COTS path enables RP0-A bring-up without a custom carrier. Authoritative COM-HPC Mini 400-pin net map for custom gunnchOS carrier remains vendor/PICMG gated; COTS reference board does not close custom pin-accurate fab.

### `EXT-DSXL-DUAL-EDP`
COM-HPC-mMTL family documents one native eDP + two DDI interfaces. DS-XL dual-display requirement retained as eDP + DDI/DP; no product requirement mandates two native eDP ports.

### `EXT-JHL8440-BALLMAP`
Public functional capability/package class may exist, but pin-accurate ball map for custom dock PCB is not public. RP0-A uses COTS USB4 dock.

### `EXT-JHL9040R-BALLMAP`
JHL9040R retimer ball map remains NDA/vendor-gated for custom fanout. Not required for RP0-A COTS dock behavioral validation.

### `UNRES-NRF54L15-FOOTPRINT`
Nordic public nRF54L15 DK (PCA10156) uses QFN48; official hardware files zip checksummed (ed70a2233d009e7e4dd31a20f66527ef206b23bd357623850a9f3228a089e1d4). Closed for RP0-A / digital reference; CSP47 form-factor remains separate.
Note: Wearable CSP47/HDI form-factor remains a separate feasibility gate; QFN48/DK evidence does not equal wearable geometry validation.

### `UNRES-FN990B40-AVL`
Exact MPN FN990B40W01T010300 live-verified on Rutronik distributor listing and Telit manufacturer family pages. DigiKey/Mouser live catalog scrape blocked (bot/403); treat DigiKey/Mouser as VERIFY_AT_PURCHASE. PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING=true.

### `OWNER-RP0-QUOTE-AUTH`
Reframed: preferred owner action is ORDER_RP0_A_COTS_BRINGUP_KIT (procurement packet ready; Cursor does not purchase). Owner quote/auth for custom RP0-B fab remains separate and cannot set READY_FOR_FAB.
