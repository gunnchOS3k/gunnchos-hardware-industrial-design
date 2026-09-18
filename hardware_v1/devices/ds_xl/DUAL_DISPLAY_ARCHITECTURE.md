# DS-XL dual-display architecture

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0B_RP0_COTS_BLOCKER_CLOSURE`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.

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
