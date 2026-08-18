# Future — physical EVT lab and CM line

Not deployed. Shown so reviewers can see what is **out of scope** for the digital packet.

```mermaid
flowchart LR
  CM[CM SMT / fab]
  EVT[Assembled EVT]
  LAB[ESD bench + PSU]
  CERT[FCC CE USB-IF labs]
  OS[device-os on silicon]
  CM --> EVT
  EVT --> LAB
  LAB --> OS
  LAB --> CERT
```

Each node is `PHYSICAL_PENDING` or `EXTERNAL_PENDING` until owner-executed evidence exists.
