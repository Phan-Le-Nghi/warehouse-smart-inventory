# Technical Story Spec — US-PUT-001

## Status and authority

`HUMAN-REVIEWED TECHNICAL SPEC — DOCUMENTATION ONLY`

Canonical product wording and Acceptance Criteria remain authoritative at [`../../04-product/stories/US-PUT-001.md`](../../04-product/stories/US-PUT-001.md). This spec does not modify them.

Owner: Phan Lê Nghi.

## Goal

Demonstrate a minimal end-to-end Putaway path from UI to FastAPI to PostgreSQL and back, with test evidence, while preserving open product boundaries.

## Traceability chain

```text
REQ-002/003/004 + CAND-REQ-003/007/010
  + CAND-BR-003/004
  + DEC-006/010/011/017/020/021/022/023
    -> US-PUT-001
      -> AC-PUT-001/002/003 (unchanged)
        -> SCR-03 / PF-01 boundary
          -> proposed POST /api/v1/putaways
            -> Putaway allocation + location stock effect
              -> unit + PostgreSQL integration + Playwright evidence
```

## Canonical Acceptance Criteria mapping

| Canonical AC | Figma/UI state | Proposed API behavior | Data effect | Planned test evidence |
|---|---|---|---|---|
| `AC-PUT-001` — confirm destination allocation | `SCR-03`: show SKU and eligible quantity; select `BACKROOM` or `SALES_SHELF`; confirm; show committed result | Validate request and confirm allocation atomically | Create Putaway allocation and increment confirmed destination balance | API/integration tests for both tracked destinations; Playwright happy path |
| `AC-PUT-002` — tracked internal location | Selection contains only the two MVP tracked locations | Reject any destination outside the tracked-location contract | Allocation references the tracked location in the MVP Warehouse | Request validation test; assert zero data effect on failure |
| `AC-PUT-003` — no automatic Movement record | Success copy identifies Putaway allocation, not Transfer/Movement | Endpoint has no Transfer/Movement side effect | No Transfer row; no generic Movement table is introduced | Integration assertion that Transfer data is unchanged/absent |

## UI states

- Loading Putaway context.
- Ready with SKU, eligible quantity and destination selection.
- Confirming; repeated UI submission disabled while the request is pending.
- Confirmed with destination and committed quantity summary.
- Validation/conflict failure with no claimed stock change.

`SCR-03` remains a separate flow. The `PF-01` transition is a facilitator transition only, not an automatic production CTA or a Receive completion rule.

## Proposed API contract

`POST /api/v1/putaways` with an idempotency key; exact URL is a technical contract, not a product requirement.

```json
{
  "receive_line_id": "<fixture receive line>",
  "sku_id": "<fixture SKU>",
  "quantity": 16,
  "destination_location_id": "<BACKROOM fixture id>"
}
```

The backend injects a Warehouse Staff actor through the actor/auth dependency boundary for this test. Production authentication remains `TBD`.

The operation must reject malformed/non-positive quantity, missing/mismatched references, invalid destination and allocation exceeding eligible remaining quantity. A failed request has no allocation or balance effect.

Duplicate handling:

- replaying the same idempotency key and payload returns the original committed result;
- the replay does not increment stock again;
- reusing a key with a different payload is a conflict;
- Receive-line locking and the eligible-remaining check protect against concurrent double-count.

## Vertical-slice fixture and expected effect

Precondition:

- one `receive_line` exists;
- `actual_quantity = 16` integer units;
- previously posted quantity is `0`;
- initial Backroom and Sales Shelf balances are captured by the test fixture;
- no new Receive completion state is assumed.

Action: Warehouse Staff selects `BACKROOM` and confirms Putaway for the 16 eligible units.

Expected committed result:

- one Putaway allocation for 16 units is created;
- Backroom stock increases by 16;
- Sales Shelf stock is unchanged;
- derived Warehouse total increases by 16;
- Receive actual quantity remains 16;
- no Transfer record is created;
- no generic Movement record is created;
- duplicate request replay does not double-count.

This full-quantity fixture is only the selected slice happy path. It is not a rule that partial Putaway is forbidden, and it adds no Acceptance Criterion. `OQ-014` remains open.

## Planned test cases

| Test ID | Level | Scenario / evidence |
|---|---|---|
| `T-PUT-U-001` | Unit | Eligible remaining equals actual quantity minus confirmed allocations |
| `T-PUT-U-002` | Unit | Invalid destination and non-positive quantity produce no command effect |
| `T-PUT-I-001` | PostgreSQL integration | Fixture 16 → Backroom: allocation created, Backroom +16, Sales Shelf unchanged, derived total +16 |
| `T-PUT-I-002` | PostgreSQL integration | Receive actual quantity remains unchanged; no Transfer/Movement side effect |
| `T-PUT-I-003` | PostgreSQL integration | Same idempotency request is replayed without a second increment |
| `T-PUT-I-004` | PostgreSQL concurrency | Competing requests cannot post more than eligible remaining quantity |
| `T-PUT-E-001` | Playwright | Warehouse Staff context → `SCR-03` → select Backroom → confirm → committed success state |

No test is claimed as executed until new command output exists in the implementation phase.

## Preserved TBD/open items

- `OQ-012`: integer quantity is a Round 1 slice simplification only.
- `OQ-013`: Receive completion/handoff and Putaway exception/downstream lifecycle.
- `OQ-014`: partial Putaway.
- Production authentication, deployment, advanced pagination/filtering and NFR targets.

