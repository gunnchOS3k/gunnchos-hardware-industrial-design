#!/usr/bin/env python3
"""Validate STL export artifacts exist and are plausibly STL-like."""
import re
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STL_FILES = [
    "exports/stl/student_14_placeholder.stl",
    "exports/stl/handheld_hybrid_placeholder.stl",
    "exports/stl/ds_xl_coder_placeholder.stl",
    "exports/stl/wearables_arena_set_placeholder.stl",
]

MIN_SIZE_BYTES = 1024  # 1 KB

FORBIDDEN_CLAIMS = [
    r"\bFCC approved\b",
    r"\bCE approved\b",
    r"\bmanufacturing-ready\b",
    r"\bproduction-ready hardware\b",
    r"\bDVT complete\b",
    r"\bPVT complete\b",
    r"\bready for mass production\b",
    r"\bbattery certified\b",
    r"\bcertified hardware\b",
]

SCAN_PATHS = [
    ROOT / "exports/OPENSCAD_EXPORT_STATUS.md",
    ROOT / "results/OPENSCAD_CRASH_POSTMERGE_AUDIT.md",
]


def is_ascii_stl(data: bytes) -> bool:
    return data.lstrip().startswith(b"solid")


def is_binary_stl_plausible(data: bytes) -> bool:
    if len(data) < 84:
        return False
    if is_ascii_stl(data[:6]):
        return False
    tri_count = struct.unpack("<I", data[80:84])[0]
    if tri_count == 0:
        return False
    expected_min = 84 + tri_count * 50
    expected_max = 84 + tri_count * 52
    return expected_min <= len(data) <= expected_max + 1024


def is_stl_like(path: Path) -> bool:
    data = path.read_bytes()
    if is_ascii_stl(data):
        return True
    return is_binary_stl_plausible(data)


def status_references_stl(status_text: str, rel_path: str) -> bool:
    name = Path(rel_path).name
    return rel_path in status_text or name in status_text


def scan_forbidden_claims() -> list[str]:
    violations = []
    for p in SCAN_PATHS:
        if not p.exists():
            continue
        text = p.read_text()
        for pat in FORBIDDEN_CLAIMS:
            if re.search(pat, text, re.I):
                violations.append(f"{p}: matched {pat}")
    return violations


def main() -> int:
    status_path = ROOT / "exports/OPENSCAD_EXPORT_STATUS.md"
    if not status_path.exists():
        print("FAIL missing exports/OPENSCAD_EXPORT_STATUS.md")
        return 1
    status_text = status_path.read_text()

    for rel in STL_FILES:
        path = ROOT / rel
        if not path.exists():
            print(f"FAIL missing {rel}")
            return 1
        size = path.stat().st_size
        if size == 0:
            print(f"FAIL empty {rel}")
            return 1
        if size <= MIN_SIZE_BYTES:
            print(f"FAIL {rel} size {size} bytes — must exceed {MIN_SIZE_BYTES}")
            return 1
        if not is_stl_like(path):
            print(f"FAIL {rel} does not appear STL-like")
            return 1
        if not status_references_stl(status_text, rel):
            print(f"FAIL {rel} not referenced in OPENSCAD_EXPORT_STATUS.md")
            return 1
        print(f"PASS {rel} ({size} bytes, STL-like)")

    violations = scan_forbidden_claims()
    if violations:
        for v in violations:
            print(f"FAIL forbidden claim: {v}")
        return 1

    print(f"PASS {len(STL_FILES)} STL exports validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
