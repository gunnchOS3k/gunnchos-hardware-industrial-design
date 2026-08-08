# Dock architecture freeze — USB4 / Thunderbolt 4 (not TB5)

Updated: 2026-08-08T20:15:00Z  
Status: **FROZEN**  
Normative parents: field-kit `ADR-FP-006`, `ADR-FP-001` (USB4 40 Gbps; no 80G claim)

## Decision (Continuation V)

| Axis | Freeze |
|---|---|
| Link generation | **USB4 / Thunderbolt 4 @ 40 Gbps** |
| Not in scope | **Thunderbolt 5 / USB4v2 80 Gbps** (JHL9480 / JHL9580) |
| Primary dock controller (Student/DS-XL SKU) | Intel **JHL8440** (Goshen Ridge device/peripheral controller) |
| High-speed SI retimer (as needed) | Intel **JHL9040R** (Hayden Bridge TB4 retimer) |
| Cost-down Handheld-first SKU | VIA Labs **VL108** (USB3 + DP Alt) — no USB4 40G claim on that SKU |
| PD | TI **TPS65994** class |
| Hub / Ethernet | VL817 / RTL8156 |

## Why not TB5
1. ADR-FP-001 / ADR-FP-006 specify **40 Gbps** USB4 docking — not 80 Gbps.
2. Host COM (Meteor Lake Ultra 7 155H on ADLINK module) exposes USB4 paths consistent with **40G** generation; claiming TB5 dock would be a **silent scope shift**.
3. JHL9480/JHL9580 are publicly marketed as Thunderbolt **5** — must not be relabeled as TB4.

## Why not keep JHL9040 as “the controller”
Public Intel ARK: **JHL9040R = Thunderbolt 4 Retimer**. Retimers do not replace Goshen Ridge / Maple Ridge **controllers**. Prior BOM/schematic Value `JHL9040` with Role `USB4_CONTROLLER` is corrected to:
- `U1` = **JHL8440** Role `USB4_TB4_DOCK_CONTROLLER`
- `U1R` = **JHL9040R** Role `TB4_RETIMER` (SI)

## Explicit non-claims
- No USB-IF / Thunderbolt certification logo
- No fab, no silicon purchase (PHYSICAL_EXECUTION_FREEZE)
- No “TB5-ready” marketing language on this freeze

## Token
`DOCK_ARCHITECTURE_FROZEN_USB4_TB4_NOT_TB5`
