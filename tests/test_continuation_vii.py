import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_continuation_vii_validator():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts/validate_continuation_vii.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_cont_vii_schematics_have_wires():
    """Cont VII required wired schematics. Cont VIII retired FuncBlock placeholders."""
    for prod in (
        "student_14_5",
        "ds_xl_coder",
        "handheld_hybrid",
        "edge_io_rings",
        "dock",
    ):
        sch = (ROOT / f"device_designs/{prod}/kicad/{prod}.kicad_sch").read_text(
            encoding="utf-8"
        )
        assert "(wire " in sch
        # Cont VIII manufacturer release: structural FuncBlock symbols must not remain.
        assert 'lib_id "FuncBlock"' not in sch


def test_cont_vii_ledger_statuses_only_allowed():
    import json

    ledger = json.loads(
        (
            ROOT / "artifacts/continuation_vii_eda_release_clean/EDA_VIOLATION_SEVERITY_LEDGER.json"
        ).read_text(encoding="utf-8")
    )
    allowed = {"FIXED", "FORMALLY_WAIVED_WARNING", "EXTERNAL_NDA_BLOCKED"}
    assert ledger["entries"]
    for e in ledger["entries"]:
        assert e["status"] in allowed
