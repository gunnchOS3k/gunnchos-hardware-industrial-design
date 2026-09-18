# Antenna Keepout ICD (mechanical ↔ RF/electrical)

Stream F owns enclosure keepout volumes and non-metal zones.  
Stream E owns PCB antenna feed, matching, and ground clearance in KiCad.

| Interface field | Owner | Notes |
|---|---|---|
| Keepout volume XYZ | Mechanical | Plastic-only zone |
| Ground cutback on PCB | Electrical (Stream E) | Not edited here |
| Glue/paint exclusion | Mechanical | Cosmetic + RF |
| Module placement envelope | Joint | ICD revision lock required |

Status: `ICD_DRAFT_DIGITAL` — not RF-validated.
