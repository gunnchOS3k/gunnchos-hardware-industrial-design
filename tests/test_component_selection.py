from pathlib import Path
import subprocess
import sys


def test_component_selection_simulation():
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run([sys.executable, "component_selection/simulations/simulate_component_fit.py"], cwd=root)
    assert r.returncode == 0
    assert (root / "component_selection/results/component_fit_results.json").exists()


def test_secure_boot_simulation():
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run([sys.executable, "secure_boot/scripts/simulate_secure_boot_chain.py"], cwd=root)
    assert r.returncode == 0


def test_no_stale_language_validator():
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run([sys.executable, "scripts/validate_no_stale_not_implemented_language.py"], cwd=root)
    assert r.returncode == 0
