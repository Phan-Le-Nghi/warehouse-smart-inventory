# API Contract — MVP Technical Proposal

## Status and authority boundary

`PROPOSED TECHNICAL CONTRACT — DOCUMENTATION ONLY`

Canonical behavior comes from requirements, Business Rules, decisions and canonical User Story Acceptance Criteria. HTTP routes and JSON shapes in this document are technical contracts proposed for implementation review; they are not product requirements.

Base path proposal: `/api/v1`.

Production authentication remains `TBD`. API routes depend on an actor/auth boundary that can enforce the canonical roles in `DEC-017`; the `US-PUT-001` test may inject a Warehouse Staff actor.

## Common error shape

```json
{
  "error": {
    "code": "STABLE_TECHNICAL_CODE",
    "message": "Human-readable summary",
    "details": {}
  }
}
```

Proposed mapping: `403` for a known actor without the canonical permission, `404` for a missing reference, `409` for a state/idempotency/concurrency conflict and `422` for malformed request data. Authentication-specific `401` behavior remains `TBD` with the production mechanism.

## Proposed MVP route map

| Method and route | Request/response purpose | Canonical behavior traced | Contract gaps |
|---|---|---|---|
| `GET /api/v1/locations` | Return the two tracked locations for selection | `CAND-REQ-003`, `DEC-006/010` | Catalog administration not defined |
| `GET /api/v1/stock?sku_id={id}` | Return location balances and derived Warehouse total | `CAND-REQ-003`, `CAND-BR-003` | Advanced filtering/pagination TBD |
| `POST /api/v1/receives` | Record actual quantity and discrepancy/reference context | `US-REC-001` | Completion/handoff remains `OQ-013`; exact reference shape needs story-contract review |
| `POST /api/v1/putaways` | Confirm initial allocation into a tracked destination | `US-PUT-001` | Detailed contract below |
| `POST /api/v1/picks` | Confirm one-or-many source allocations and report full or `PARTIAL / INSUFFICIENT` | `US-PICK-001` | Retry/cancel lifecycle remains open |
| `POST /api/v1/transfers` | Atomically reduce source, increase destination and record confirmation | `US-TRF-001` | Partial/failure/reversal remain open |
| `GET /api/v1/transfers` | Return confirmed Transfer history fields | `US-TRF-002` | Advanced filter/sort/export TBD |
| `POST /api/v1/audits` | Record selected-scope count/comparison and match/mismatch | `US-AUD-001` | Mismatch completion/schedule remain open |
| `POST /api/v1/audit-discrepancies/{id}/rechecks` | Record required re-check context without automatic Adjust | `US-AUD-002` | Exact lifecycle/handoff remains `OQ-013` |
| `POST /api/v1/adjustments` | Record re-checked discrepancy request and required reason; stock unchanged | `US-ADJ-001` | Target quantity vs signed delta and attachment storage TBD |
| `POST /api/v1/adjustments/{id}/decision` | Manager approve/reject; only valid approved apply may change stock | `US-ADJ-002` | Rejected-case closure remains open |

Routes other than Putaway remain conceptual and require story-specific technical review before implementation.

## US-PUT-001 — POST /api/v1/putaways

### Request

Header proposal:

```http
Idempotency-Key: <client-generated opaque value>
```

```json
{
  "receive_line_id": "<id>",
  "sku_id": "<id>",
  "quantity": 16,
  "destination_location": "BACKROOM"
}
```

Round 1 quantity is an integer-unit simplification; this request shape does not resolve `OQ-012`. `destination_location` accepts only `BACKROOM` or `SALES_SHELF` in the MVP.

### Success response

Proposed status: `201 Created` for the first successful confirmation and `200 OK` when replaying the same idempotent request.

```json
{
  "putaway_id": "<id>",
  "receive_line_id": "<id>",
  "sku_id": "<id>",
  "quantity": 16,
  "destination_location": "BACKROOM",
  "confirmed_at": "<timestamp>",
  "stock": {
    "destination_quantity": 16,
    "warehouse_total": 16
  }
}
```

Warehouse total is derived from committed location balances.

### Validation and errors

| Condition | Proposed result | Data effect |
|---|---|---|
| Missing Receive line or SKU | `404 RECEIVE_LINE_NOT_FOUND` / `SKU_NOT_FOUND` | None |
| Quantity is not a positive Round 1 integer | `422 INVALID_QUANTITY` | None |
| SKU does not match Receive line | `409 RECEIVE_LINE_SKU_MISMATCH` | None |
| Destination is not a tracked MVP location or belongs outside the MVP Warehouse | `422 INVALID_DESTINATION` | None |
| Quantity exceeds the not-yet-posted quantity for the Receive line | `409 PUTAWAY_EXCEEDS_ELIGIBLE_QUANTITY` | None |
| Same idempotency key and same payload is replayed | Return the original committed result | No additional effect |
| Same idempotency key is reused with a different payload | `409 IDEMPOTENCY_KEY_REUSED` | None |

Quantity below eligible remaining is not rejected merely because it could be partial. Partial Putaway behavior remains open at `OQ-014`; the first slice exercises only a full-quantity happy-path fixture.

### Transaction effect

Within one PostgreSQL transaction:

1. lock the referenced Receive line;
2. calculate previously posted and remaining eligible quantity;
3. validate request and idempotency state;
4. create one Putaway allocation;
5. increment the destination `stock_balances` row;
6. commit and derive the Warehouse total.

The transaction does not modify Receive actual quantity and does not create a Transfer or generic Movement record. Any failure rolls back the allocation and stock update together.

## Open contract decisions

- `OQ-012`, `OQ-013` and `OQ-014` remain open.
- Production authentication mechanism is `TBD`.
- Idempotency key retention and storage detail are technical follow-up decisions.
- Adjust representation, attachment storage, advanced pagination/filtering, deployment and NFR targets remain `TBD`.

