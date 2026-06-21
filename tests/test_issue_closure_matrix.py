from pathlib import Path
import subprocess
import sys


def test_issue_closure_matrix():
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run([sys.executable, "scripts/validate_issue_closure_matrix.py"], cwd=root)
    assert r.returncode == 0
