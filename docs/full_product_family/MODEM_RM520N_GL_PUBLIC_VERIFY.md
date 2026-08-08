# RM520N-GL public verification (no inferred NTN)

Updated: 2026-08-08T19:40:00Z  
Evidence class: **PUBLIC_VENDOR_DOCS** (not lab MEASURED)

## Frozen claim
Quectel **RM520N-GL** is a **5G NR Sub-6 (FR1)** M.2 module supporting SA/NSA + LTE + WCDMA per Quectel RM520N Series Specification V1.4 and product page.

## What public docs support
- Form factor: M.2, ~30×52 mm class, Key B WWAN
- 3GPP Release 16; SA peak class ~2.4 Gbps DL / 900 Mbps UL (spec sheet rates — not a product throughput claim)
- Host: USB 3.x and/or PCIe 3.0 per SKU/design guide (carrier must follow Quectel HW design)
- GNSS option: GPS/GLONASS/BDS/Galileo/QZSS (modem-integrated) — optional enablement
- Industrial temperature class listed by Quectel for the series

## Explicit NON-claims (verified against public sources)
| Claim | Status | Source basis |
|---|---|---|
| 6G / IMT-2030 radio | **FORBIDDEN** | Spec is 5G NR Sub-6 Rel-16 |
| NTN / satellite | **NOT supported / not claimed** | Verizon Open Development module page lists **NTN (Satellite) Capable** unchecked for RM520N-GL; Quectel public RM520N materials describe terrestrial Sub-6 bands only |
| mmWave FR2 | **Not this SKU** | RM520N-GL is Sub-6 series |
| Carrier certification complete for gunnchOS product | **Not claimed** | Module may have carrier listings; end-product cert pending |

## Product applicability
Unchanged from `MODEM_ARCHITECTURE_FREEZE.md`: required fleet path for Student/DS-XL; optional/thermal-gated on Handheld; absent on Rings/Dock.
