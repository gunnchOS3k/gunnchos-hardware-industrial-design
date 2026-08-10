"""WP-002 Handheld storage headroom E2E (Outcome A) — implementer tests."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "npi" / "phase_xv" / "handheld_storage_headroom"
SIM = PKG / "simulate_handheld_storage_e2e.py"


def test_capacity_model_outcome_a_margins():
    model = json.loads((PKG / "HANDHELD_STORAGE_CAPACITY_MODEL.json").read_text())
    assert model["decision_outcome"] == "A"
    assert model["hardware_truth"]["onboard_storage"]["marketed_gb"] == 32.0
    assert model["hardware_truth"]["supported_expansion"]["microsd"]["supported"] is True
    assert model["hardware_truth"]["supported_expansion"]["larger_onboard_emmc_sku"]["available_in_exact_mpn_matrix"] is False
    assert model["hardware_truth"]["supported_expansion"]["nvme_carrier"]["supported_in_current_freeze"] is False
    onboard = model["onboard_emmc_placement"]
    assert onboard["meets_min_absolute_free_2gb"] is True
    assert onboard["meets_min_percent_free_10pct"] is True
    assert onboard["onboard_operational_slack_gb"] >= 2.0
    assert model["combined_mlp_fit"]["onboard_safe_under_outcome_a"] is True
    assert model["combined_mlp_fit"]["expansion_required"] is True
    # Do not accept marketed fit without usable/reserves
    assert model["margins"]["do_not_accept_required_lt_nominal"] is True


def test_growth_model_present():
    growth = json.loads((PKG / "HANDHELD_STORAGE_GROWTH_30_90_180.json").read_text())
    for day in ("day_30", "day_90", "day_180"):
        assert day in growth["projected_slack_gb"]
        assert growth["projected_slack_gb"][day]["onboard_still_meets_reserves"] is True
        assert growth["projected_slack_gb"][day]["expansion_still_positive"] is True


def test_defect_closure_outcome_a_not_class_e():
    closure = json.loads((PKG / "HANDHELD_STORAGE_DEFECT_CLOSURE.json").read_text())
    assert closure["decision_outcome"] == "A"
    assert closure["options"]["A"]["selected"] is True
    assert closure["options"]["B"]["selected"] is False
    assert closure["options"]["C"]["selected"] is False
    assert closure["class_e_cr"] is None
    assert "NOT_SELF_CERTIFIED" in closure["v1_certification"]

    defect = json.loads((PKG / "NPI_DEFECT-HANDHELD-STORAGE-HEADROOM-001.json").read_text())
    assert defect["status"] == "CLOSED_OUTCOME_A_PENDING_V1"
    assert defect["decision_outcome"] == "A"


def test_policy_doc_exists():
    text = (PKG / "HANDHELD_STORAGE_POLICY.md").read_text()
    assert "Outcome A" in text
    assert "microSD" in text
    assert "emergency save" in text.lower() or "Emergency save" in text
    assert "Class E" in text
    assert "silent" in text.lower()


def test_e2e_simulation_no_silent_data_loss():
    r = subprocess.run([sys.executable, str(SIM)], cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    out = PKG / "HANDHELD_STORAGE_E2E_SIM_RESULT.json"
    assert out.exists()
    bundle = json.loads(out.read_text())
    assert bundle["ok"] is True
    assert bundle["with_expansion"]["ok"] is True
    assert bundle["without_expansion"]["ok"] is True
    assert bundle["with_expansion"]["silent_data_loss"] is False
    assert bundle["without_expansion"]["silent_data_loss"] is False
    # Without expansion, installs must fail closed
    denied = [
        f
        for f in bundle["without_expansion"]["failures"]
        if f.get("error") == "volume_unmounted"
    ]
    assert len(denied) >= 4
    # Protected rollback slots remain
    steps = {s["step"]: s for s in bundle["with_expansion"]["steps"]}
    assert steps["rollback_slots_intact"]["ok"] is True
