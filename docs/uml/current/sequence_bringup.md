# Diagnostic / bring-up sequence — current (planned physical)

Sequence for an owner/lab operator after an EVT unit exists. Until then this is a **procedure diagram**, not an executed test.

```mermaid
sequenceDiagram
  autonumber
  actor Op as Operator
  participant T as Traveler SHA
  participant PSU as Current-limited PSU
  participant DUT as Assembled EVT
  participant M as Meter
  participant UART as Debug UART
  participant Log as artifacts/evt
  Op->>T: record board ID + git SHA + FW hash
  Op->>PSU: set limit for named SKU input
  PSU->>DUT: apply VBUS or adapter
  Op->>M: measure public carrier rails
  M-->>Log: measured_V not YAML copy
  alt overcurrent or missing rail
    Op->>PSU: stop
    Op->>Log: fail traveler
  else rails in lab procedure
    Op->>UART: capture boot log
    UART-->>Log: boot.log required
    Op->>Log: test-point pass/fail
  end
```

Skip NDA-only module internals (`UNRES-COM-HPC-*`, `UNRES-JHL*`). Full prose: [PHYSICAL_EVT_BRINGUP_PACKET.md](../../packets/PHYSICAL_EVT_BRINGUP_PACKET.md).
