# Timing — digital packet vs physical gates

This is a **process timing** diagram (not a PCB SI timing closure). SI simulation is explicitly `false` on handheld stackup.

```mermaid
sequenceDiagram
  autonumber
  participant D as Digital design
  participant V as Validators / kicad-cli
  participant P as RFQ packet
  participant O as Owner
  participant CM as CM / fab
  participant L as EVT lab
  D->>V: CAD BOM KiCad firmware OS exports
  V-->>D: DIGITAL packet hygiene
  D->>P: manufacturing/rfq + docs/packets
  Note over P: RFQ_SENT = false
  P->>O: owner review
  O->>CM: send RFQ EXTERNAL_PENDING
  CM-->>O: quote / DFM
  O->>CM: PO (owner only)
  CM->>L: assembled EVT
  L->>L: measure rails + boot log
  Note over L: PHYSICAL_PENDING until evidence
```

No parallel claim that digital time equals fab time.
