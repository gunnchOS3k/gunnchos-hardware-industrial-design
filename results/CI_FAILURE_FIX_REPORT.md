# CI Failure Fix Report

## Root cause

1. **QEMU dry-run unknown device:** When PyYAML was unavailable in CI, `run_device_profile_vm.py` returned empty profiles and rejected valid device IDs.
2. **Capsule manifest verify:** `verify_capsule_manifest.py` exited with `FAIL pyyaml required` when PyYAML was not installed.

## Files changed

- `firmware/_device_util.py` — canonical device IDs, aliases, YAML/JSON loader with stdlib fallback
- `firmware/qemu/run_device_profile_vm.py` — normalized IDs, embedded default profiles + JSON fallback
- `firmware/qemu/qemu_device_profiles.json` — stdlib-safe profile source
- `firmware/capsule_update/verify_capsule_manifest.py` — JSON fallback, no hard PyYAML dependency
- `firmware/capsule_update/sample_capsule_manifest.json` — JSON mirror
- `requirements.txt` — pytest, pyyaml
- `.github/workflows/hardware-package-ci.yml` — install requirements.txt

## Commands run

```bash
python firmware/qemu/run_device_profile_vm.py --dry-run --device student_14_5
python firmware/capsule_update/verify_capsule_manifest.py
pytest -q tests/
```

## Before/after

| Check | Before | After |
|---|---|---|
| QEMU dry-run student_14_5 | fail unknown device (no yaml) | pass |
| Capsule verify (no yaml) | FAIL pyyaml required | pass via JSON |
| Aliases student_14, student-14-5 | n/a | resolve to student_14_5 |

## Dependency fix

`requirements.txt` adds `pyyaml>=6.0`; CI installs via `pip install -r requirements.txt`. Scripts also work without PyYAML using JSON fallbacks.

## Device ID normalization

Canonical: `student_14_5`, `handheld_hybrid`, `ds_xl_coder`, `wearables_arena_set`. Aliases: `student_14`, `student-14-5`, `wearables_arena`, etc.
