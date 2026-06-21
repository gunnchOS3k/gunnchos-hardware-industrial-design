#!/usr/bin/env python3
"""Validate printability readiness — STL presence and optional admesh check."""
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "results" / "PRINTABILITY_VALIDATION.md"
STATUS = ROOT / "printability" / "PRINTABILITY_STATUS.md"

STL_FILES = [
    "exports/stl/student_14_placeholder.stl",
    "exports/stl/handheld_hybrid_placeholder.stl",
    "exports/stl/ds_xl_coder_placeholder.stl",
    "exports/stl/wearables_arena_set_placeholder.stl",
]


def run_admesh(stl: Path) -> tuple[bool, str]:
    admesh = shutil.which("admesh")
    if not admesh:
        return False, "admesh not installed"
    try:
        r = subprocess.run(
            [admesh, str(stl)],
            capture_output=True,
            text=True,
            timeout=120,
        )
        out = (r.stdout or "") + (r.stderr or "")
        return r.returncode == 0, out.strip()[:500]
    except Exception as e:
        return False, str(e)


def main() -> int:
    rows = []
    any_missing = False
    admesh_available = shutil.which("admesh") is not None
    admesh_results = []

    for rel in STL_FILES:
        p = ROOT / rel
        if not p.exists() or p.stat().st_size == 0:
            any_missing = True
            rows.append((rel, "fail", "missing or empty"))
            continue
        if admesh_available:
            ok, msg = run_admesh(p)
            admesh_results.append((rel, ok, msg))
            rows.append((rel, "basic_pass" if ok else "needs_external_review", msg[:80]))
        else:
            rows.append((rel, "needs_external_review", "admesh not available"))

    if any_missing:
        overall = "fail"
    elif admesh_available and all(r[1] == "basic_pass" for r in rows):
        overall = "basic_pass"
    else:
        overall = "needs_external_review"

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Printability Validation",
        "",
        f"**Generated:** {ts}",
        "",
        f"**Overall status:** `{overall}`",
        "",
        "> STL existence validated. Print-ready status **not claimed** without mesh/manifold/wall-thickness "
        "checks and first-article print evidence.",
        "",
        "| STL | Status | Notes |",
        "|-----|--------|-------|",
    ]
    for r in rows:
        lines.append(f"| {r[0]} | {r[1]} | {r[2]} |")
    if not admesh_available:
        lines += [
            "",
            "**Warning:** `admesh` not installed. Printability requires external mesh/manifold validation.",
        ]
    lines += [
        "",
        "## Required next evidence",
        "",
        "Mesh/manifold validation, wall-thickness validation, slicer review, first-article print, "
        "fit check, and vendor/engineer review.",
        "",
    ]
    REPORT.write_text("\n".join(lines) + "\n")

    if overall == "fail":
        print("FAIL printability validation — missing STL files")
        return 1
    print(f"PASS printability validation (overall: {overall})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
