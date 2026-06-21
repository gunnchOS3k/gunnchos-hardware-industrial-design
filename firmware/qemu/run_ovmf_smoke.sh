#!/usr/bin/env bash
# QEMU/OVMF smoke — dry run when qemu-system-x86_64 unavailable
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
python3 "$ROOT/run_device_profile_vm.py" --dry-run --device student_14_5
