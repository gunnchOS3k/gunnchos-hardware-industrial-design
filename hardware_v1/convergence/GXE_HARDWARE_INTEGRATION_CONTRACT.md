# GXE ↔ Hardware integration contract

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.


## Boundary

GXE is executed in a **separate workspace/repo**. This file is the only GXE surface required for #68 merge.

`GXE_IMPLEMENTED_IN_HARDWARE_REPO=false`

## Interfaces

### 1. Experience Contract interface
Hardware track consumers accept Experience Contracts matching `HARDWARE_EXPERIENCE_CONTRACT_SCHEMA.json`.

### 2. Benchmark result schema
Results conform to `CROSS_TRACK_BENCHMARK_SCHEMA.json` (per-workload; no single winner score).

### 3. RuntimeTarget identity
Stable string id for the software runtime under test (OS image, kernel, compositor, app bundle digests).

### 4. Hardware identity
Track + board + silicon + revision + BOM hash + firmware identity.

### 5. Power / energy measurement interface
Fields: `energy_per_task_j`, `avg_power_w`, `peak_power_w`, `sample_hz`, `instrument_id`.

### 6. Latency metrics
`interaction_latency_ms` {p50,p95,p99}, `frame_latency_ms`, `input_to_photon_ms` when applicable.

### 7. Accelerator inventory
List of CPU / GPU / NPU / FPGA / custom accel with capability discovery keys.

### 8. Thermal metadata
Skin / junction / ambient estimates with sensor provenance; no fabricated thermals.

### 9. Capability discovery
Machine-readable capabilities advertised to GXE without implying product readiness.

### 10. Experiment provenance
`experiment_id`, `git_sha`, `dataset_id`, `operator`, `started_at_utc`, `claim_boundary`.

## Non-goals in this repo

- No GXE kernel/runtime implementation
- No RISC-V/FPGA bring-up executed here
- No silent promotion of GXE to PRODUCT_MAINLINE
