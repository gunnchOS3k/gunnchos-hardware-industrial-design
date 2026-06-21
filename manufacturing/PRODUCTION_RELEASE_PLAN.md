# PRODUCTION RELEASE PLAN

Production release plan — gates and evidence. Not production released.

## OS compatibility blocking gates

- OS profile export manifest exists (`os_compatibility/device_class_exports/`)
- OS repo consumed device profiles (gunnchos-device-os hardware_compat/)
- Simulated OS compatibility exists on OS side
- Hardware-side validation plan exists (`hardware_os_validation/`)
- Real hardware boot: **not yet proven** (evidence placeholders only)
- HLK-style readiness: planned (`hlk_readiness/`)
- Real hardware compatibility: **blocking production release**
