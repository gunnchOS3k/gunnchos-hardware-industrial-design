# PCB Red-Team Completeness — Continuation VII §12

Updated: 2026-08-09T17:16:18Z  
Branch: `cursor/full-product-continuation-vii-eda-release-clean`

A rectangular PCB that exports Gerbers is **not** a finished carrier.

## student_14_5

```json
{
  "product": "student_14_5",
  "schematic_symbol_count": 16,
  "production_component_count_est": 16,
  "footprint_count": 21,
  "net_count_est": 6,
  "required_net_count_est": 6,
  "routed_net_count": 0,
  "unrouted_net_count": 6,
  "track_count": 0,
  "via_count": 0,
  "copper_zones": 0,
  "layers": 4,
  "differential_pairs": 0,
  "high_speed_constraints": 0,
  "power_planes": "STRUCTURAL_GND_ZONE_ONLY",
  "test_points": 0,
  "mounting_features": 4,
  "component_side_population": "F.Cu_structural_blocks",
  "wires_sch": 6,
  "verdict": "STRUCTURAL_PLACEHOLDER_NOT_RELEASE_COMPLETE"
}
```

**Verdict:** `STRUCTURAL_PLACEHOLDER_NOT_RELEASE_COMPLETE`

## ds_xl_coder

```json
{
  "product": "ds_xl_coder",
  "schematic_symbol_count": 10,
  "production_component_count_est": 10,
  "footprint_count": 15,
  "net_count_est": 5,
  "required_net_count_est": 5,
  "routed_net_count": 0,
  "unrouted_net_count": 5,
  "track_count": 0,
  "via_count": 0,
  "copper_zones": 0,
  "layers": 4,
  "differential_pairs": 0,
  "high_speed_constraints": 0,
  "power_planes": "STRUCTURAL_GND_ZONE_ONLY",
  "test_points": 0,
  "mounting_features": 4,
  "component_side_population": "F.Cu_structural_blocks",
  "wires_sch": 5,
  "verdict": "STRUCTURAL_PLACEHOLDER_NOT_RELEASE_COMPLETE"
}
```

**Verdict:** `STRUCTURAL_PLACEHOLDER_NOT_RELEASE_COMPLETE`

## handheld_hybrid

```json
{
  "product": "handheld_hybrid",
  "schematic_symbol_count": 18,
  "production_component_count_est": 18,
  "footprint_count": 23,
  "net_count_est": 17,
  "required_net_count_est": 17,
  "routed_net_count": 0,
  "unrouted_net_count": 17,
  "track_count": 0,
  "via_count": 0,
  "copper_zones": 0,
  "layers": 4,
  "differential_pairs": 0,
  "high_speed_constraints": 0,
  "power_planes": "STRUCTURAL_GND_ZONE_ONLY",
  "test_points": 0,
  "mounting_features": 4,
  "component_side_population": "F.Cu_structural_blocks",
  "wires_sch": 17,
  "verdict": "STRUCTURAL_PLACEHOLDER_NOT_RELEASE_COMPLETE"
}
```

**Verdict:** `STRUCTURAL_PLACEHOLDER_NOT_RELEASE_COMPLETE`

## edge_io_rings

```json
{
  "product": "edge_io_rings",
  "schematic_symbol_count": 12,
  "production_component_count_est": 12,
  "footprint_count": 17,
  "net_count_est": 10,
  "required_net_count_est": 10,
  "routed_net_count": 0,
  "unrouted_net_count": 10,
  "track_count": 0,
  "via_count": 0,
  "copper_zones": 0,
  "layers": 4,
  "differential_pairs": 0,
  "high_speed_constraints": 0,
  "power_planes": "STRUCTURAL_GND_ZONE_ONLY",
  "test_points": 0,
  "mounting_features": 4,
  "component_side_population": "F.Cu_structural_blocks",
  "wires_sch": 10,
  "verdict": "STRUCTURAL_PLACEHOLDER_NOT_RELEASE_COMPLETE"
}
```

**Verdict:** `STRUCTURAL_PLACEHOLDER_NOT_RELEASE_COMPLETE`

## dock

```json
{
  "product": "dock",
  "schematic_symbol_count": 21,
  "production_component_count_est": 21,
  "footprint_count": 24,
  "net_count_est": 24,
  "required_net_count_est": 24,
  "routed_net_count": 0,
  "unrouted_net_count": 24,
  "track_count": 0,
  "via_count": 0,
  "copper_zones": 0,
  "layers": 4,
  "differential_pairs": 0,
  "high_speed_constraints": 0,
  "power_planes": "STRUCTURAL_GND_ZONE_ONLY",
  "test_points": 0,
  "mounting_features": 4,
  "component_side_population": "F.Cu_structural_blocks",
  "wires_sch": 24,
  "verdict": "STRUCTURAL_PLACEHOLDER_NOT_RELEASE_COMPLETE"
}
```

**Verdict:** `STRUCTURAL_PLACEHOLDER_NOT_RELEASE_COMPLETE`

## Family conclusion

All five boards remain **structural EDA packages**: functional nets are now
wired in schematic (Cont VII fix for dangling labels), footprints resolve via
local library (Cont VII fix for fp-lib warnings), mounting holes and a GND zone
exist — but production routing, differential pairs, vendor footprints, and
test points are **not** complete. Do **not** certify release-complete.
