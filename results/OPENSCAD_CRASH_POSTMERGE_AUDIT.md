# OpenSCAD Crash Post-Merge Audit

**Audit date:** 2026-06-21  
**Branch audited:** `main` (post PR #29 merge)  
**Audit branch:** `postmerge-openscad-export-audit`

## OpenSCAD version

- **Documented export version:** OpenSCAD 2026.06.12 (`openscad@snapshot` via Homebrew)
- **Post-merge local check:** OpenSCAD CLI crashes in sandboxed environments with `Incompatible processor` (Qt/neon); STL artifacts on `main` were produced in a non-sandboxed run during PR #29.

## Whether OpenSCAD crashed

**Yes, during PR #29 generation:**

1. First export attempt in sandbox: `Abort trap: 6` / `Incompatible processor` before any STL was written.
2. Retry outside sandbox with `/opt/homebrew/bin/openscad`: **success** — all four STLs exported with `Status: NoError` and manifold geometry reports.

**Post-merge audit:** Did not re-run OpenSCAD export (CLI still fails in sandbox). Audit validates **committed artifacts on `main`**, not a fresh export run.

## Whether STL files exist

| File | Exists | Size | Format |
|------|--------|------|--------|
| `exports/stl/student_14_placeholder.stl` | Yes | 157,427 bytes | ASCII STL (`solid OpenSCAD_Model`) |
| `exports/stl/handheld_hybrid_placeholder.stl` | Yes | 184,462 bytes | ASCII STL |
| `exports/stl/ds_xl_coder_placeholder.stl` | Yes | 113,445 bytes | ASCII STL |
| `exports/stl/wearables_arena_set_placeholder.stl` | Yes | 47,351 bytes | ASCII STL |

All files exceed 1 KB and are referenced in `exports/OPENSCAD_EXPORT_STATUS.md`.

## Validation command results

| Command | Result |
|---------|--------|
| `python scripts/check_required_files.py` | PASS (136 files) |
| `python scripts/validate_bom.py` | PASS |
| `python scripts/validate_power_budget.py` | PASS |
| `python scripts/validate_issue_closure_matrix.py` | PASS |
| `python scripts/validate_production_track.py` | PASS |
| `python scripts/validate_stl_exports.py` | PASS (4 STL exports) |
| `pytest -q` | PASS (9 tests) |

## What this audit proves

- STL files **exist** on merged `main`.
- STL files are **non-empty** and **> 1 KB**.
- STL files are **plausibly STL-like** (ASCII `solid` header verified).
- Paths are documented in `exports/OPENSCAD_EXPORT_STATUS.md`.
- Package validation still passes.
- No new production-ready or certification claims were introduced in export/status docs.

## What this audit does not prove

- Mechanical correctness, fit, or tolerance accuracy
- Printability or enclosure DFM
- DVT/PVT readiness
- Production readiness or manufacturing release
- FCC/CE/UKCA or battery certification

## Claim boundary

**Production release is still not claimed.** These STLs are EVT-1 placeholder geometry for vendor review only.

## Conclusion

PR #29 reported a crash during sandboxed OpenSCAD execution, but the **merged artifacts on `main` are real, non-empty ASCII STL files** produced by a successful non-sandbox export. This post-merge audit adds `scripts/validate_stl_exports.py` to detect missing, empty, or non-STL-like files in future merges.
