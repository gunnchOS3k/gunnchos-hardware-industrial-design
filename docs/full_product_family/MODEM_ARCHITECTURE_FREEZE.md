# Modem architecture freeze notes

Updated: 2026-08-08T19:40:00Z  
Canonical ADR: field-kit `ADR-FP-005` (mirrored intent here).  
Public verification detail: `MODEM_RM520N_GL_PUBLIC_VERIFY.md`

## Frozen
- Primary WWAN: **Quectel RM520N-GL** (M.2 3052), **5G NR Sub-6** + LTE fallback
- Host interface: PCIe or USB3 per module SKU — carrier routes M.2 pins per Quectel HW design guide
- eSIM: GSMA **SGP.22** consumer eUICC architecture — **no compliance claim until lab**
- Antennas: 4× cellular MIMO + GNSS keep-outs in RF plan (MODELED)
- IMT-2030 / “6G” path: **replaceable M.2 modem bay only** — future module swap, not a current silicon claim

## Forbidden claims
- Not 6G certified
- Not “fake 6G modem” in BOM or marketing
- **No NTN/satellite claim** — RM520N-GL public listings do not support NTN; do not infer

## Product applicability
| Product | Modem |
|---|---|
| Student 14.5 | RM520N-GL on carrier M.2 (required for fleet SKU; Wi-Fi-only education SKU allowed) |
| DS-XL Coder | Shared Student WWAN bay |
| Handheld Hybrid | Optional M.2 if thermal allows; default Wi-Fi-first |
| Rings | No cellular |
| Dock | No cellular; may host UWB companion only |
