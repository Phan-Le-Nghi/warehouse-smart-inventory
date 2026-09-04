# Story Spec — US-PUT-001 Putaway

## Trạng thái

`IMPLEMENTED DOWNSTREAM — PENDING HUMAN DIFF REVIEW`

Canonical technical spec: [`../../../vault/06-technical/story-specs/US-PUT-001.md`](../../../vault/06-technical/story-specs/US-PUT-001.md). Canonical product Story/AC remains [`../../../vault/04-product/stories/US-PUT-001.md`](../../../vault/04-product/stories/US-PUT-001.md) and is unchanged.

## Traceability

| Requirement/decision | Story/AC | UI/prototype | Proposed API | Data effect | Test evidence plan |
|---|---|---|---|---|---|
| `CAND-REQ-003/007`, `CAND-BR-003/004`, `DEC-006/010/011/017/021/023` | `US-PUT-001`, `AC-PUT-001/002/003` | `SCR-03`; `PF-01` facilitator boundary only | `POST /api/v1/putaways` | Allocation + destination balance in one transaction; derived total | Unit, PostgreSQL integration, concurrency and Playwright tests |

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

Implementation và evidence hiện tại được ghi tại [`../../TRACEABILITY.md`](../../TRACEABILITY.md). Local component/frontend tests pass; PostgreSQL integration và Playwright chưa chạy local vì Docker runtime không khả dụng.
