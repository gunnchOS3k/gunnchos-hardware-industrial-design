# Supply-chain fields — claim boundary

Machine-readable **fields** for BOM / AVL / alternates / sole-source /
NRND-EOL / lead-time / MOQ.

| Token | Value |
| --- | --- |
| PRODUCTION_RELEASE_CLAIMED | false |
| RFQ / purchase / fab | NOT_THIS_STREAM |
| Quoted stock | never invented — `UNKNOWN` |
| Quoted unit price | never invented — `UNKNOWN` |
| Real lead time / MOQ | `UNKNOWN` until a supplier quote exists |
| Sole-source | `false` only when an alternate MPN is listed; otherwise `UNKNOWN` (not inferred true) |

Unknown stays unknown. This overlay does not place an RFQ, buy parts, or
lock an AVL quote.
