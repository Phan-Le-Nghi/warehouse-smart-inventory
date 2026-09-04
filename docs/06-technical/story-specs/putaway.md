# Story Spec — US-PUT-001 Putaway

## Trạng thái

`IMPLEMENTATION COMPLETED — VERIFIED BY GITHUB ACTIONS`

Canonical technical spec: [`../../../vault/06-technical/story-specs/US-PUT-001.md`](../../../vault/06-technical/story-specs/US-PUT-001.md). Canonical product Story/AC remains [`../../../vault/04-product/stories/US-PUT-001.md`](../../../vault/04-product/stories/US-PUT-001.md) and is unchanged.

## Traceability

| Requirement/decision | Story/AC | UI/prototype | Implemented API | Data effect | Test evidence |
|---|---|---|---|---|---|
| `CAND-REQ-003/007`, `CAND-BR-003/004`, `DEC-006/010/011/017/021/023` | `US-PUT-001`, `AC-PUT-001/002/003` | `SCR-03`; `PF-01` facilitator boundary only | `POST /api/v1/putaways` | Allocation + destination balance in one transaction; derived total | `TEST-PUT-001`…`TEST-PUT-005` PASS on PostgreSQL 18; `TEST-PUT-E2E-001` PASS through React → FastAPI → PostgreSQL 18 |

## Vertical-slice fixture

- Existing Receive line: `actual_quantity = 16`, previously posted `0`.
- Warehouse Staff actor is injected through the auth boundary.
- Staff selects `BACKROOM` and confirms all 16 eligible units.

Expected result:

- create one Putaway allocation;
- Backroom `+16`;
- Sales Shelf unchanged;
- derived Warehouse total `+16`;
- Receive actual quantity unchanged;
- no Transfer or generic Movement record;
- duplicate replay does not double-count.

This is a test fixture, not a business rule requiring full-only Putaway. `OQ-014` remains OPEN. The spec does not add or edit canonical Acceptance Criteria and does not resolve the Receive completion/handoff at `OQ-013`.

## Verification evidence

| Evidence | Result |
|---|---|
| `TEST-PUT-001`…`TEST-PUT-005` in `apps/backend/tests/test_putaway.py` | PASS on PostgreSQL 18 in GitHub Actions `backend-checks`; includes unchanged Receive quantity, no Transfer/Movement write path, and duplicate request without double-counting |
| Frontend lint, typecheck, unit tests and build | PASS in GitHub Actions `frontend-checks` |
| `TEST-PUT-E2E-001` in `apps/frontend/e2e/putaway.spec.ts` | PASS in GitHub Actions `putaway-e2e` through React → FastAPI → PostgreSQL 18 |
| Alembic migration upgrade/downgrade/upgrade | PASS against PostgreSQL 18 in GitHub Actions `backend-checks` |

Both push and pull-request CI runs were successful after correcting test-fixture foreign-key ordering to flush `Warehouse` before `InternalLocation`, followed by the dependent SKU/Receive/ReceiveLine/StockBalance records. This was a test-fixture correction, not a business-rule or canonical-AC change. Implementation and consolidated evidence are recorded in [`../../TRACEABILITY.md`](../../TRACEABILITY.md). No local Docker/PostgreSQL pass is claimed.
