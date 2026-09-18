#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
KICAD="${ROOT}/hardware_v1/dock/kicad_no_nda"
OUT="${ROOT}/artifacts/digital_engineering_exhaustion/stream_e/dock_kicad_cli"
mkdir -p "$OUT/gerbers" "$OUT/drill"
CLI="${KICAD_CLI:-/opt/homebrew/bin/kicad-cli}"
[[ -x "$CLI" ]] || { echo KICAD_CLI_ABSENT; exit 0; }
"$CLI" sch erc --format json --output "$OUT/erc.json" "$KICAD/dock_no_nda.kicad_sch" || true
"$CLI" pcb drc --format json --output "$OUT/drc.json" "$KICAD/dock_no_nda.kicad_pcb" || true
"$CLI" pcb export gerbers --output "$OUT/gerbers" "$KICAD/dock_no_nda.kicad_pcb" || true
"$CLI" pcb export drill --output "$OUT/drill" "$KICAD/dock_no_nda.kicad_pcb" || true
