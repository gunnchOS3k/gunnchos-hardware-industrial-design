# Hardware Experience Contract guide

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.


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
