#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
KICAD="${ROOT}/hardware_v1/rings/kicad_nrf54l15"
OUT="${ROOT}/artifacts/digital_engineering_exhaustion/stream_e/rings_kicad_cli"
mkdir -p "$OUT/gerbers" "$OUT/drill"
CLI="${KICAD_CLI:-/opt/homebrew/bin/kicad-cli}"
[[ -x "$CLI" ]] || { echo KICAD_CLI_ABSENT; exit 0; }
"$CLI" sch erc --format json --output "$OUT/erc.json" "$KICAD/rings_nrf54l15.kicad_sch" || true
"$CLI" pcb drc --format json --output "$OUT/drc.json" "$KICAD/rings_nrf54l15.kicad_pcb" || true
"$CLI" pcb export gerbers --output "$OUT/gerbers" "$KICAD/rings_nrf54l15.kicad_pcb" || true
"$CLI" pcb export drill --output "$OUT/drill" "$KICAD/rings_nrf54l15.kicad_pcb" || true
