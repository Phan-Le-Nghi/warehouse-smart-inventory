# API Contract — Bản phục vụ báo cáo

## Trạng thái

`PROPOSED TECHNICAL CONTRACT — DOCUMENTATION ONLY`

Canonical technical proposal: [`../../vault/06-technical/api-contract.md`](../../vault/06-technical/api-contract.md). Exact route và JSON shape là technical contract, không phải product requirement.

## MVP route map đề xuất

| Route | Purpose | Story/boundary |
|---|---|---|
| `GET /api/v1/locations` | Tracked-location selection | Supporting `CAND-REQ-003` |
| `GET /api/v1/stock?sku_id={id}` | Location balances + derived Warehouse total | `CAND-REQ-003` |
| `POST /api/v1/receives` | Actual quantity + discrepancy/reference context | `US-REC-001`; completion/handoff remains OPEN |
| `POST /api/v1/putaways` | Initial destination allocation | `US-PUT-001`; detailed below |
| `POST /api/v1/picks` | Multi-location/full/`PARTIAL / INSUFFICIENT` Pick | `US-PICK-001` |
| `POST /api/v1/transfers` | Atomic internal Transfer confirmation | `US-TRF-001` |
| `GET /api/v1/transfers` | Confirmed Transfer history | `US-TRF-002` |
| `POST /api/v1/audits` | Selected-scope count and comparison | `US-AUD-001` |
| `POST /api/v1/audit-discrepancies/{id}/rechecks` | Mandatory re-check context; no auto Adjust | `US-AUD-002` |
| `POST /api/v1/adjustments` | Re-checked request with reason; no pre-decision stock change | `US-ADJ-001` |
| `POST /api/v1/adjustments/{id}/decision` | Manager approve/reject | `US-ADJ-002` |

Routes ngoài Putaway vẫn conceptual và cần story-specific technical review.

## POST /api/v1/putaways

Proposed request:

```json
{
  "receive_line_id": "<id>",
  "sku_id": "<id>",
  "quantity": 16,
  "destination_location": "BACKROOM"
}
```

Request dùng proposed `Idempotency-Key` header. Success trả Putaway ID, Receive line, SKU, quantity, destination, confirmation time, committed destination balance và derived Warehouse total.

Error cases gồm missing/mismatched Receive/SKU, non-positive or malformed Round 1 integer quantity, invalid destination, allocation vượt eligible remaining và idempotency conflict. Tất cả failure đều không có data effect. Same-key/same-payload replay trả original result và không increment lần hai.

Transaction tạo Putaway allocation và tăng destination balance atomically; Receive actual quantity không đổi; không tạo Transfer hoặc generic Movement record.

Quantity thấp hơn remaining không bị contract này reject chỉ vì có thể là partial. Partial Putaway vẫn OPEN tại `OQ-014`; first slice chỉ test happy path dùng toàn bộ 16 eligible units.

## Contract boundaries

- Actor/auth dependency phải giữ canonical permission; production authentication TBD.
- Adjust target-vs-delta, attachment storage, advanced pagination/filtering, deployment và NFR còn TBD.
- `OQ-012`, `OQ-013` và `OQ-014` vẫn OPEN.
