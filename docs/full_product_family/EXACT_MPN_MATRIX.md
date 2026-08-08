# Exact orderable MPN matrix — five-product family

Updated: 2026-08-08T19:40:00Z  
Branch: `cursor/full-product-hardware-design-release`  
Base: `79b11aba3ca9d4db7051b6d5ccb3571e72503396`  
PHYSICAL_EXECUTION_FREEZE ACTIVE — MPNs frozen for **design**, not purchase.

Evidence class: **PUBLIC_VENDOR_DOCS** for compute/modem MPNs below.

## Compute / SoM / MCU (primary freezes)

| Product | Role | Vendor | Exact MPN | Notes |
|---|---|---|---|---|
| Student 14.5 | COM module | ADLINK | **COM-HPC-mMTL-155H-32G** | Ultra 7 155H + 32GB LPDDR5x; COM-HPC Mini 95×70 |
| DS-XL Coder | COM module (shared) | ADLINK | **COM-HPC-mMTL-155H-32G** | Same module as Student; dual-eDP is **carrier** differentiator |
| Handheld Hybrid | SoM | Radxa | **RM121-D8E32** | Radxa NX5 RK3588S; 8GB LPDDR4X + 32GB eMMC; 260-pin SODIMM |
| Edge I/O Rings | MCU | Nordic | **nRF52840-QIAA-R** | Already exact; aQFN-73 |
| Dock | USB4 controller | Intel | **JHL9040** | Maple Ridge class; cost-down alt VL108 |

## Approved alternates (compute)

| Product | Alternate MPN | When |
|---|---|---|
| Student / DS-XL | ADLINK **COM-HPC-mMTL-155H-64G** | Higher memory SKU |
| Handheld | Radxa **RM121-D8E16** / **RM121-D8E8** / **RM121-D8E0** | Same NX5 family; eMMC variants from official brief |
| Handheld | Firefly **Core-3588SJD4** (SODIMM RK3588S) | Only if NX5 AVL fails — requires carrier pinout re-check ADR amendment |

## Forbidden / rejected
- Invented proprietary Intel/Rockchip **bare CPU BGA** fanout in-repo
- Vague `COM-HPC-Mini-Ultra7-155H-32GB` class strings as if they were orderable MPNs
- Vague `RK3588S-SoM-16GB` without vendor order code
- Congatec Panther Lake `conga-HPC/mPTL-*` as primary (wrong CPU generation vs ADR-FP-001 Ultra 7 **155H**)

## Radios / power / security (cross-product exact where frozen)

| Product | Subsystem | Exact MPN |
|---|---|---|
| Student / DS-XL | Wi-Fi 7 | Intel **BE200** |
| Student / DS-XL / Handheld(opt) | WWAN | Quectel **RM520N-GL** |
| Student / DS-XL | TPM | Infineon **SLB9672XQ2.0** |
| Student / DS-XL / Dock | PD | TI **TPS65994ADFBRQ1** (Dock: TPS65994 class) |
| Student / DS-XL | Charger | TI **BQ25792RQMR** |
| Student / DS-XL | Fuel gauge | TI **BQ40Z50-R2** |
| Rings | Cap touch | Azoteq **IQS7222A** |
| Rings / Dock | UWB | Qorvo **DWM3001C** (DNP OK → companion) |
| Rings | SE | NXP **SE050C1HQ1** |
| Dock | Ethernet | Realtek **RTL8156** |
| Dock | USB hub | VIA **VL817** |

## Honesty
Distributor listings that advertise NX5 **16GB** configs without a matching row in Radxa NX5 product brief Rev 1.1 order table are **not** frozen here. Primary handheld freeze is **RM121-D8E32** (public brief).
