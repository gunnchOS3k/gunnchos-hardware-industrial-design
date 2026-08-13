from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "manufacturing" / "supply_chain"


def _compile() -> None:
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "compile_supply_chain_fields.py")],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_compile_and_validate():
    _compile()
    validate = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_supply_chain_fields.py")],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert validate.returncode == 0, validate.stdout + validate.stderr


def test_handheld_fields_are_unknown_not_invented():
    _compile()
    data = json.loads((DIR / "handheld_hybrid.json").read_text(encoding="utf-8"))
    assert data["PRODUCTION_RELEASE_CLAIMED"] is False
    assert data["rfq_purchase_fab"] == "NOT_THIS_STREAM"
    assert data["parts"]
    for part in data["parts"]:
        assert part["unit_price"] == "UNKNOWN"
        assert part["stock_qty"] == "UNKNOWN"
        assert part["lead_time_weeks"] == "UNKNOWN"
        assert part["moq"] == "UNKNOWN"
        assert part["sole_source"] is not True
        assert "avl" in part
        assert "alternate_mpn" in part
        assert part["lifecycle_status"] in ("ACTIVE", "NRND", "EOL", "UNKNOWN")


def test_alternate_listed_is_not_sole_source():
    _compile()
    data = json.loads((DIR / "handheld_hybrid.json").read_text(encoding="utf-8"))
    som = next(p for p in data["parts"] if p["mpn"] == "RM121-D8E32")
    assert som["alternate_mpn"] == "RM121-D8E16"
    assert som["sole_source"] is False


def test_validator_rejects_invented_price(tmp_path):
    _compile()
    import importlib.util

    src = json.loads((DIR / "dock.json").read_text(encoding="utf-8"))
    src["parts"][0]["unit_price"] = 12.50
    fake = tmp_path / "dock.json"
    fake.write_text(json.dumps(src))
    spec = importlib.util.spec_from_file_location(
        "validate_supply_chain_fields",
        ROOT / "scripts" / "validate_supply_chain_fields.py",
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    errors = mod.validate_doc(fake)
    assert any("unit_price" in e and "invented" in e for e in errors)
