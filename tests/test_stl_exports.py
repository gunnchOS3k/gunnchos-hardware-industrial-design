from pathlib import Path
import subprocess
import sys


def test_validate_stl_exports():
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run([sys.executable, "scripts/validate_stl_exports.py"], cwd=root)
    assert r.returncode == 0


def test_stl_files_present_and_large():
    root = Path(__file__).resolve().parents[1]
    files = [
        "exports/stl/student_14_placeholder.stl",
        "exports/stl/handheld_hybrid_placeholder.stl",
        "exports/stl/ds_xl_coder_placeholder.stl",
        "exports/stl/wearables_arena_set_placeholder.stl",
    ]
    for rel in files:
        p = root / rel
        assert p.exists(), rel
        assert p.stat().st_size > 1024, rel


def test_stl_files_ascii_solid_header():
    root = Path(__file__).resolve().parents[1]
    p = root / "exports/stl/student_14_placeholder.stl"
    assert p.read_bytes()[:5] == b"solid"
