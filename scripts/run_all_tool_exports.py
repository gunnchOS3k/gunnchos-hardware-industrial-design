#!/usr/bin/env python3
import subprocess, sys
from pathlib import Path
subprocess.check_call([sys.executable, 'scripts/generate_validation_toolchain_matrix.py'], cwd=Path(__file__).resolve().parents[1])
