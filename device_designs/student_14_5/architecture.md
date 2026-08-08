# Student 14.5 — electrical architecture

Updated: 2026-08-08T01:15:00Z  
Evidence: MODELED / DIGITAL

## Strategy
**Module/COM + carrier** per ADR-HW-001. Performance target remains ADR-FP-001 (Intel Core Ultra 7 155H class, 32 GB LPDDR5x on-module, NVMe on carrier).

## Blocks
1. **COM module (purchased):** CPU/iGPU/NPU, LPDDR5x, module PMICs for VCCCORE/GT/SA, USB4 PHYs as exposed by COM, PCIe roots to carrier.
2. **Carrier (ours):** system power from battery/PD, EC, storage socket, radios, display/touch, audio, cameras, sensors, I/O, dock.
3. **Power path:** Pack → BQ40Z50 gauge → BQ25792 NVDC → VSYS → COM VIN + carrier bucks (5V/3V3/1V8) + IMVP on-module.
4. **Dock:** dual USB-C with PD + USB4/DP Alt toward ADR-FP-006 dock.

## Non-claims
No proprietary Ultra 7 BGA layout. No 6G modem. No fab.
