#!/usr/bin/env python3
"""Validate STL mechanical plausibility against broad bounding-box targets."""
import json
import math
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ROOT / "mechanical_correctness" / "device_mechanical_targets.json"
REPORT = ROOT / "results" / "MECHANICAL_CORRECTNESS_VALIDATION.md"
STATUS = ROOT / "mechanical_correctness" / "MECHANICAL_CORRECTNESS_STATUS.md"


def parse_ascii_stl(path: Path) -> tuple[list[tuple], tuple, tuple, int]:
    """Return vertices list, bbox min, bbox max, triangle count."""
    text = path.read_text(errors="replace")
    if not text.lstrip().startswith("solid"):
        raise ValueError("not ASCII STL")

    verts: list[tuple[float, float, float]] = []
    tri_count = len(re.findall(r"\bfacet\b", text))
    for m in re.finditer(
        r"vertex\s+([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)\s+"
        r"([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)\s+"
        r"([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)",
        text,
    ):
        x, y, z = float(m.group(1)), float(m.group(2)), float(m.group(3))
        if any(math.isnan(v) or math.isinf(v) for v in (x, y, z)):
            raise ValueError("NaN/Inf vertex")
        verts.append((x, y, z))

    if tri_count == 0 or len(verts) == 0:
        raise ValueError("no triangles")

    xs = [v[0] for v in verts]
    ys = [v[1] for v in verts]
    zs = [v[2] for v in verts]
    bb_min = (min(xs), min(ys), min(zs))
    bb_max = (max(xs), max(ys), max(zs))
    dims = tuple(bb_max[i] - bb_min[i] for i in range(3))
    if any(d <= 0 for d in dims):
        raise ValueError("zero-size bounding box")
    return verts, bb_min, bb_max, tri_count


def bbox_in_range(dims: tuple, lo: list, hi: list) -> bool:
    return all(lo[i] <= dims[i] <= hi[i] for i in range(3))


def main() -> int:
    if not TARGETS.exists():
        print(f"FAIL missing {TARGETS}")
        return 1
    targets = json.loads(TARGETS.read_text())
    rows = []
    failures = []

    for key, meta in targets.items():
        stl_rel = meta["stl_file"]
        stl = ROOT / stl_rel
        label = meta.get("device_label", key)
        if not stl.exists() or stl.stat().st_size == 0:
            failures.append(f"{label}: missing or empty STL")
            rows.append((label, "FAIL", "missing/empty", "-", "not proven"))
            continue
        try:
            _, bb_min, bb_max, tri_count = parse_ascii_stl(stl)
            dims = tuple(bb_max[i] - bb_min[i] for i in range(3))
            ok = bbox_in_range(dims, meta["bbox_mm_min"], meta["bbox_mm_max"])
            status = "PASS bbox in broad range" if ok else "WARN bbox outside broad range"
            if not ok:
                failures.append(
                    f"{label}: dims {dims} outside {meta['bbox_mm_min']}-{meta['bbox_mm_max']}"
                )
            rows.append(
                (label, status, f"{tri_count} tris", f"{dims[0]:.1f}×{dims[1]:.1f}×{dims[2]:.1f} mm", "not proven")
            )
        except Exception as e:
            failures.append(f"{label}: {e}")
            rows.append((label, "FAIL", str(e), "-", "not proven"))

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Mechanical Correctness Validation",
        "",
        f"**Generated:** {ts}",
        "",
        "> Validates artifact presence and broad bounding-box plausibility only. "
        "**Mechanical correctness is not proven.**",
        "",
        "| Device | Check | Triangles | BBox dims | Mechanical correctness |",
        "|--------|-------|-----------|-----------|------------------------|",
    ]
    for r in rows:
        lines.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |")
    lines += [
        "",
        "## Status",
        "",
        "Mechanical correctness status: **Not yet proven.**",
        "",
        "Required next evidence: dimensional review, interference checks, tolerance review, "
        "print test, physical assembly review, and engineer signoff.",
        "",
    ]
    REPORT.write_text("\n".join(lines) + "\n")

    hard_fail = any(r[1] == "FAIL" for r in rows)
    if hard_fail:
        for f in failures:
            print(f"FAIL {f}")
        return 1

    print(f"PASS mechanical correctness validation ({len(rows)} devices)")
    for w in failures:
        print(f"WARN {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
