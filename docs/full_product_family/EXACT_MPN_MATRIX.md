# Exact orderable MPN matrix — five-product family

Updated: 2026-08-15T00:45:00Z (HW-FW-RC-001 vendor refresh)  
Branch: `stream-c/hw-fw-rc-001`  
Prior freeze base retained from Cont V / Cont IX.  
PHYSICAL_EXECUTION_FREEZE ACTIVE — MPNs frozen for **design**, not purchase.

Evidence class: **PUBLIC_VENDOR_DOCS** for compute/modem/dock role MPNs below.  
HW-FW-RC-001 re-confirmed ADLINK COM-HPC-mMTL-155H-32G, Radxa NX5 RM121-D8E32, Quectel RM520N-GL Rel-16 Sub-6 NSA+SA (not NTN/6G), Dock JHL8440 + JHL9040R @ 40G (not TB5).

## Compute / SoM / MCU (primary freezes)

| Product | Role | Vendor | Exact MPN | Notes |
|---|---|---|---|---|
| Student 14.5 | COM module | ADLINK | **COM-HPC-mMTL-155H-32G** | Ultra 7 155H + 32GB LPDDR5x; COM-HPC Mini 95×70 |
| DS-XL Coder | COM module (shared) | ADLINK | **COM-HPC-mMTL-155H-32G** | Same module as Student; dual-eDP is **carrier** differentiator |
| Handheld Hybrid | SoM | Radxa | **RM121-D8E32** | Radxa NX5 RK3588S; 8GB LPDDR4X + 32GB eMMC; 260-pin SODIMM |
| Edge I/O Rings | MCU | Nordic | **nRF52840-QIAA-R** | Already exact; aQFN-73 |
| Dock | USB4/TB4 **controller** | Intel | **JHL8440** | Goshen Ridge peripheral/dock controller @ **40 Gbps** (ADR-HW-002) |
| Dock | TB4 **retimer** | Intel | **JHL9040R** | Hayden Bridge retimer — **not** the dock controller; **not** Maple Ridge |

## Approved alternates (compute / dock)

| Product | Alternate MPN | When |
|---|---|---|
| Student / DS-XL | ADLINK **COM-HPC-mMTL-155H-64G** | Higher memory SKU |
| Handheld | Radxa **RM121-D8E16** / **RM121-D8E8** / **RM121-D8E0** | Same NX5 family; eMMC variants from official brief |
| Handheld | Firefly **Core-3588SJD4** (SODIMM RK3588S) | Only if NX5 AVL fails — requires carrier pinout re-check ADR amendment |
| Dock | VIA Labs **VL108** | Handheld-first USB3+DP Alt cost-down SKU (no USB4 40G claim) |

## Forbidden / rejected
- Invented proprietary Intel/Rockchip **bare CPU BGA** fanout in-repo
- Vague `COM-HPC-Mini-Ultra7-155H-32GB` class strings as if they were orderable MPNs
- Vague `RK3588S-SoM-16GB` without vendor order code
- Congatec Panther Lake `conga-HPC/mPTL-*` as primary (wrong CPU generation vs ADR-FP-001 Ultra 7 **155H**)
- Labeling **JHL9040R** as Maple Ridge / dock controller
- **Thunderbolt 5** dock silicon: **JHL9480** / **JHL9580** (Barlow Ridge) — out of normative 40G scope
- Mislabeling TB4 as TB5 (or vice versa)

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

See also: `COMPONENT_TRUTH_VERIFY_CONTINUATION_V.md`, `DOCK_ARCHITECTURE_FREEZE_USB4_TB4.md`, `COM_HPC_NX5_FEASIBILITY_PINOUT.md`.
