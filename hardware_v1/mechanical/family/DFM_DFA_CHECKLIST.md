# Family DFM / DFA Checklist (digital)

| Check | Criteria | Digital evidence | Physical |
|---|---|---|---|
| Wall thickness | >= 1.2 mm nominal for PC/ABS; local ribs OK | OpenSCAD params + notes | First-article micrometer |
| Draft angles | >= 1° exterior moldable faces | Drawing callouts | Tooling review |
| Boss design | ID/OD ratio + screw engagement | Fastener plan | Torque study |
| Snap fits | Retention force modeled | Spec sheet | Cycle test |
| Cable dress | Bend radius + service loop | Exploded notes | Assembly time study |
| Connector float | Misalignment allowance | Keepout ICD | Gauge pin check |
| Thermal vents | Inlet/outlet area + finger hazard | Thermal/vent note | Thermal chamber |
| Antenna keepout | Non-metal zone + glue line | Keepout drawing | OTA chamber |
| Service access | Battery/SSD/module path | Service plan | Teardown timer |

`DFM_DIGITAL_COMPLETE` may be true while `DFM_PHYSICAL_PASS` remains false.
