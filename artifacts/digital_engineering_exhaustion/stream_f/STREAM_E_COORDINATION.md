# Stream E Coordination

| Concern | Stream E path | Stream F path |
|---|---|---|
| PCB / schematic / Gerber | `device_designs/**`, `hardware_v1/electrical/` | do not edit |
| Connector pin map | KiCad / electrical ICD | mechanical envelope only |
| Antenna feed/matching | electrical/RF | keepout volumes in mechanical |
| Stackup impedance | electrical | fab notes reference only |
| Enclosure / DFM | — | `hardware_v1/mechanical/` |
| EVT physical packs | may consume EE bring-up | `evt_dvt_pvt/` |
| Cert matrix | radio module cert refs | `certification/stream_f/` |
| CM RFQ mech+mfg | EE attachments | `manufacturing/stream_f/` |

If a change requires both, split commits/PRs by directory ownership.
