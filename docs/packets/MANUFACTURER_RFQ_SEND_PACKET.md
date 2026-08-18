# Manufacturer RFQ send packet

**Status:** `EXTERNAL_PENDING`

**Owner sends the RFQ. This agent does not send email, upload to a CM portal, purchase parts, or place a fab PO.**

## Why blocked

RFQ **documents** exist. Sending, quoting, and purchasing are owner/external actions. Packet completeness is a separate gate from send.

## Digital packet (prepare only)

Review before any human send:

| Item | Path |
|---|---|
| Family digital readiness | `DIGITAL_MANUFACTURING_READINESS.md` |
| Claim boundary | `product/CLAIM_BOUNDARY.md`, `docs/MANUFACTURING_CLAIM_BOUNDARY.md` |
| EVT-1 templates | `prototype_rfq/` (`RFQ_COVER_LETTER_TEMPLATE.md`, `VENDOR_QUESTIONNAIRE.md`, `FILES_TO_SEND_CHECKLIST.md`, `NDA_AND_IP_NOTES.md`) |
| Handheld CM pack | `manufacturing/rfq/handheld_hybrid/` (`README_CM.md`, `PACKAGE_INDEX.md`) |
| Student CM pack | `manufacturing/rfq/student_14_5/` |
| DS-XL CM pack | `manufacturing/rfq/ds_xl_coder/` |
| Rings CM pack | `manufacturing/rfq/edge_io_rings/` |
| Dock CM pack | `manufacturing/rfq/dock/` |
| Cont IX engineering exports | `device_designs/<sku>/manufacturing/cont_ix_release/` (Gerber/drill/PnP/STEP **engineering copies**) |
| BOM / AVL | `device_designs/<sku>/bom/assembly_bom.csv` and `manufacturing/*/ASSEMBLY_BOM.csv` |
| Stackup | `device_designs/<sku>/manufacturing/stackup.yaml` |
| Unresolved specs | `DIGITAL_MANUFACTURING_READINESS.md` § Unresolved specifications |
| NDA collateral requests | `docs/full_product_family/EXTERNAL_VENDOR_COLLATERAL_REQUIRED_CONT_IX.md` |

`PHYSICAL_EXECUTION_FREEZE` remains until the owner explicitly lifts it outside this agent.

## Prerequisite for send (owner)

- Owner has read unresolved specs (`UNRES-*`). Do not ask a CM to invent COM-HPC or Intel ball maps.
- No invented electrical values in the outgoing zip; cite YAML evidence_class.
- Cover letter states: prototype / EVT engineering review; **not** FCC/CE/USB-IF complete; **not** production release.
- Document hash of the zip recorded by the owner.

## Owner action

1. Assemble the zip from the paths above for the SKU(s) being quoted.
2. Send via the owner’s procurement channel (email, CM portal, NDA room).
3. Record: vendor name, date, SKU list, git SHA, zip hash, ticket ID. Keep secrets out of git.
4. File vendor acknowledgement when it arrives. Do not fabricate acknowledgements.

## Questions already listed for CM (digital)

From `manufacturing/rfq/handheld_hybrid/README_CM.md` (apply analogously):

1. Confirm impedance coupons vs net classes / stackup notes.
2. Stencil + paste recommendation for listed packages.
3. X-ray policy for aQFN/WLCSP/QFN.
4. NDA collateral status (COM-HPC / Intel) — not inventing pins.

## Expected evidence

Vendor acknowledgement (external). Quote comparison may use `prototype_rfq/QUOTE_COMPARISON_MATRIX.md`.

## Status transition

Send ≠ manufacturing release ≠ FCC/CE/USB-IF. Digital packet completeness (`DIGITAL_MANUFACTURING_PACKET_PREPARED`) is independent of `RFQ_SENT`.
