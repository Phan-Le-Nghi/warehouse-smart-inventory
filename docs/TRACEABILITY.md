# Traceability v5 — Product / Prototype / Usability Baseline

Final backlog gồm 9 canonical stories đã được human approve. PRD, MVP Scope và Consolidated User Flow đã được baseline cho Report Round 1. Human Product Decisions / MVP Assumptions không được ghi như verified evidence và không tạo `EVD-*` mới.

## Product foundation

| Source | Requirement/rule | Story impact | Classification |
|---|---|---|---|
| `DEC-005` | One-Warehouse MVP | Tất cả workflow stories | HUMAN PRODUCT DECISION |
| `DEC-006`, `DEC-010` | `CAND-REQ-003`, `CAND-BR-003` | Putaway, Pick, Transfer, Audit, Adjust use per-location quantity | HUMAN PRODUCT DECISION |
| `DEC-008`, `DEC-009` | `system stock quantity`; Physical movement khác Movement system record; Putaway/Pick/Transfer boundaries | Putaway, Pick, Transfer và product vocabulary | HUMAN PRODUCT DECISION |
| `DEC-011` | `CAND-REQ-007`, `CAND-BR-004` | `US-PUT-001` | HUMAN PRODUCT DECISION |
| `DEC-012` | `CAND-REQ-006`, `CAND-BR-005/006` | `US-PICK-001` | HUMAN PRODUCT DECISION |
| `DEC-007`, `DEC-013` | `CAND-REQ-004`, `CAND-BR-007/008` | `US-TRF-001`, `US-TRF-002` | HUMAN PRODUCT DECISION |
| `DEC-014` | `CAND-REQ-005`, `CAND-BR-009/010` | `US-AUD-001`, `US-AUD-002` | HUMAN PRODUCT DECISION; `EVD-015/016` support current-state count/compare |
| `DEC-015` | `CAND-REQ-008`, `CAND-BR-011–013` | `US-ADJ-001`, `US-ADJ-002` | HUMAN PRODUCT DECISION; `EVD-012/013/017` support limited current-state context |
| `DEC-016` | `CAND-REQ-009`, `CAND-BR-014` | `US-REC-001` reference-mismatch AC | HUMAN PRODUCT DECISION |
| `DEC-017` | `CAND-REQ-010` | Actors and permissions across all stories | HUMAN PRODUCT DECISION |
| `DEC-018` | `REQ-002` interpretation | Receive may lead to Putaway; Pick/Transfer independent paths; Audit mismatch may lead to Adjust consideration after re-check | HUMAN PRODUCT DECISION |
| `DEC-019` | `CAND-REQ-011`, `CAND-BR-015` | Negative-stock guards in `US-PICK-001`, `US-TRF-001`, `US-ADJ-002` | HUMAN PRODUCT DECISION; resolves `OQ-015` |

## Technical foundation decisions

| Decision / ADR | Technical contract | Story impact | Boundary |
|---|---|---|---|
| `DEC-020` | React + TypeScript + Vite/npm; Python 3.13 + FastAPI/uv/pytest; PostgreSQL 18/Docker; SQLAlchemy 2/Alembic; Playwright; modular monolith | Foundation for all future implementation; first slice `US-PUT-001` | Supersedes technical TBD in `DEC-004`; production authentication/deployment remain TBD |
| `DEC-021` / `ADR-001` | Per-location stock is authoritative; Warehouse total is derived; no `warehouse_totals` | `US-PUT-001`, Pick, Transfer, Audit, Adjust | Does not add stock buckets or NFR assumptions |
| `DEC-022` / `ADR-002` | PostgreSQL transaction boundary, row locking when needed, application + DB non-negative guard | All stock-changing operations | Does not define retry/cancel or reservation semantics |
| `DEC-023` / `ADR-003` | Receive records actual quantity; Putaway performs initial posting; no Transfer/Movement side effect | `US-REC-001`, `US-PUT-001` | Does not resolve `OQ-013` or `OQ-014` |

## Repo scaffold / CI baseline

| Status | Artifact path | Verification evidence | Scope boundary |
|---|---|---|---|
| Implemented; pending human diff review | `apps/frontend/`, `apps/backend/`, `apps/docker/`, `apps/.env.example`, `apps/README.md`, `.github/workflows/ci.yml` | Baseline verification was recorded in `AI-USE-006`; current slice evidence is listed below | Scaffold baseline has been extended only by the `US-PUT-001` vertical slice |

## US-PUT-001 vertical-slice implementation

| Requirement / Story / delivery trace | Implementation artifact | Test IDs and current evidence | Scope boundary |
|---|---|---|---|
| `REQ-002/003/004`, `CAND-REQ-003/007/010` → `US-PUT-001` → Taiga [#8](https://tree.taiga.io/project/lenghi-group-07-project/us/8) → tasks [#19](https://tree.taiga.io/project/lenghi-group-07-project/task/19)/[#20](https://tree.taiga.io/project/lenghi-group-07-project/task/20)/[#21](https://tree.taiga.io/project/lenghi-group-07-project/task/21) → `PF-01` / `SCR-03` → Technical Story Spec | `POST /api/v1/putaways`; Putaway context read; actor dependency boundary; SQLAlchemy models; Alembic `20260905_0001`; React Putaway page | `TEST-PUT-001`…`TEST-PUT-005`: local component DB pass; frontend destination/submit/error: pass; `TEST-PUT-E2E-001`: not run locally because Docker/PostgreSQL runtime is unavailable | No Transfer/Movement table or write path; no persisted Warehouse total; Receive actual unchanged; full 16-unit placement is fixture scope only; `OQ-012/013/014` remain open |

Local evidence on 2026-09-05: Ruff lint and format-check pass; pytest `8 passed` (SQLite component database); frontend ESLint, TypeScript, Vitest `3 passed`, and Vite build pass; Alembic upgrade/downgrade smoke pass on a temporary SQLite database. PostgreSQL migration/integration and Playwright are **not claimed as passed locally**. CI now provisions PostgreSQL 18 for migration, API tests, and real-browser vertical-slice verification.

## Canonical story coverage

| Story | Requirement | Business Rule | Decision | Evidence classification | OQ boundary |
|---|---|---|---|---|---|
| `US-REC-001` | `REQ-001/002/003`, `CAND-REQ-001/002/009/010` | `CAND-BR-001/014` | `DEC-016/017/018` | `EVD-002–005` verify actual-vs-expected behavior; later additions are HUMAN PRODUCT DECISIONS | `OQ-013` final completion/handoff; `OQ-014`, `OQ-022` open |
| `US-PUT-001` | `REQ-002/003/004`, `CAND-REQ-003/007/010` | `CAND-BR-003/004` | `DEC-006/010/011/017` | HUMAN PRODUCT DECISION; `EVD-006/007` context only | `OQ-013` exception/handoff; `OQ-014`, `OQ-022` open |
| `US-PICK-001` | `REQ-002/003`, `CAND-REQ-003/006/010/011` | `CAND-BR-003/005/006/015` | `DEC-010/012/017/018/019` | HUMAN PRODUCT DECISION; `EVD-006–009` context only | `OQ-013` cancellation/retry; `OQ-022` open; negative-stock guard approved |
| `US-TRF-001` | `REQ-001/002/004`, `CAND-REQ-003/004/010/011` | `CAND-BR-003/007/008/015` | `DEC-005/007/009/010/013/017/018/019` | HUMAN PRODUCT DECISION; `EVD-010/011` context only | `OQ-013` failure/cancel/reversal; `OQ-014/022` open; negative-stock guard approved |
| `US-TRF-002` | `REQ-002/003/004`, `CAND-REQ-004/010` | `CAND-BR-008` | `DEC-013/017` | HUMAN PRODUCT DECISION; `EVD-010/011` context only | `OQ-013`, `OQ-022` remain open |
| `US-AUD-001` | `REQ-002/004`, `CAND-REQ-003/005/010` | `CAND-BR-003/009` | `DEC-010/014/017` | Verified evidence `EVD-015/016` + HUMAN PRODUCT DECISION | `OQ-013` mismatch completion/schedule; `OQ-022` open |
| `US-AUD-002` | `REQ-002/004`, `CAND-REQ-005/010` | `CAND-BR-002/010` | `DEC-014/017` | Verified evidence `EVD-012/017` + HUMAN PRODUCT DECISION | `OQ-013` mismatch closure open |
| `US-ADJ-001` | `REQ-001/002/003`, `CAND-REQ-008/010` | `CAND-BR-002/011/012` | `DEC-015/017/018` | Verified evidence `EVD-012/013/017` + HUMAN PRODUCT DECISION | `OQ-013`; this story does not apply quantity |
| `US-ADJ-002` | `REQ-001/002/003`, `CAND-REQ-003/008/010/011` | `CAND-BR-002/011/013/015` | `DEC-010/015/017/018/019` | Verified evidence `EVD-012/013/017` + HUMAN PRODUCT DECISION | `OQ-013` rejected closure; negative-stock guard approved |

## Story-to-AC mapping

| Story | Canonical AC coverage | Downstream status |
|---|---|---|
| `US-REC-001` | actual entry/compare; match; quantity discrepancy; reference mismatch review | Design/spec/implementation/test not started |
| `US-PUT-001` | destination allocation; tracked location; no automatic Movement record | Vertical slice implemented; local component/frontend tests pass; PostgreSQL integration and Playwright await CI or a local Docker runtime; pending human diff review |
| `US-PICK-001` | full Pick; multi-location; `PARTIAL / INSUFFICIENT`; negative-stock guard | Not started |
| `US-TRF-001` | source/destination effects; Warehouse total; minimum record; negative-stock guard | Technical contract still TBD |
| `US-TRF-002` | Manager history access; history fields; confirmation time | Technical contract still TBD |
| `US-AUD-001` | selected scope; count/compare; result; match completion | Not started |
| `US-AUD-002` | discrepancy context; mandatory re-check; no auto Adjust | Not started |
| `US-ADJ-001` | request/reason; re-check; optional attachment; no pre-decision change | Not started |
| `US-ADJ-002` | approve/apply; reject/no change; no-discrepancy/no change; negative-stock guard | Not started |

## Requirement → Canonical Story → Taiga → Design/Prototype → Implementation/Test

Taiga references dưới đây theo dõi thực thi và không thay thế nguồn yêu cầu canonical. Trạng thái implementation/test không được suy ra từ trạng thái Taiga.

| Requirement | Canonical Story | Taiga Story | Taiga Tasks | Design/Prototype | Implementation/Test status |
|---|---|---|---|---|---|
| `REQ-001/002/003`, `CAND-REQ-001/002/009/010` | `US-REC-001` | [#7](https://tree.taiga.io/project/lenghi-group-07-project/us/7) / ID `9523822` — Ready | `T-REC-01` [#16](https://tree.taiga.io/project/lenghi-group-07-project/task/16); `T-REC-02` [#17](https://tree.taiga.io/project/lenghi-group-07-project/task/17); `T-REC-03` [#18](https://tree.taiga.io/project/lenghi-group-07-project/task/18) — New | `PF-01 — Receive → Putaway`; screen inventory/Figma parity chờ human review | Chưa bắt đầu / Chưa bắt đầu |
| `REQ-002/003/004`, `CAND-REQ-003/007/010` | `US-PUT-001` | [#8](https://tree.taiga.io/project/lenghi-group-07-project/us/8) / ID `9523823` — Ready | `T-PUT-01` [#19](https://tree.taiga.io/project/lenghi-group-07-project/task/19); `T-PUT-02` [#20](https://tree.taiga.io/project/lenghi-group-07-project/task/20); `T-PUT-03` [#21](https://tree.taiga.io/project/lenghi-group-07-project/task/21) — New | `PF-01 — Receive → Putaway`; `SCR-03`; [`06-technical/story-specs/putaway.md`](06-technical/story-specs/putaway.md) | API/DB/migration/UI implemented; local component/frontend tests pass; PostgreSQL integration/E2E not run locally; pending human review |
| `REQ-002/003`, `CAND-REQ-003/006/010/011` | `US-PICK-001` | [#9](https://tree.taiga.io/project/lenghi-group-07-project/us/9) / ID `9523824` — Ready | `T-PICK-01` [#22](https://tree.taiga.io/project/lenghi-group-07-project/task/22); `T-PICK-02` [#23](https://tree.taiga.io/project/lenghi-group-07-project/task/23); `T-PICK-03` [#24](https://tree.taiga.io/project/lenghi-group-07-project/task/24) — New | `PF-02 — Pick`; screen inventory/Figma parity chờ human review | Chưa bắt đầu / Chưa bắt đầu |
| `REQ-001/002/004`, `CAND-REQ-003/004/010/011` | `US-TRF-001` | [#10](https://tree.taiga.io/project/lenghi-group-07-project/us/10) / ID `9523825` — New | `T-TRF1-01` [#25](https://tree.taiga.io/project/lenghi-group-07-project/task/25); `T-TRF1-02` [#26](https://tree.taiga.io/project/lenghi-group-07-project/task/26); `T-TRF1-03` [#27](https://tree.taiga.io/project/lenghi-group-07-project/task/27) — New | Consolidated User Flow; technical contract vẫn TBD | Chưa bắt đầu / Chưa bắt đầu |
| `REQ-002/003/004`, `CAND-REQ-004/010` | `US-TRF-002` | [#11](https://tree.taiga.io/project/lenghi-group-07-project/us/11) / ID `9523826` — New | `T-TRF2-01` [#28](https://tree.taiga.io/project/lenghi-group-07-project/task/28); `T-TRF2-02` [#29](https://tree.taiga.io/project/lenghi-group-07-project/task/29); `T-TRF2-03` [#30](https://tree.taiga.io/project/lenghi-group-07-project/task/30) — New | Consolidated User Flow; technical contract vẫn TBD | Chưa bắt đầu / Chưa bắt đầu |
| `REQ-002/004`, `CAND-REQ-003/005/010` | `US-AUD-001` | [#12](https://tree.taiga.io/project/lenghi-group-07-project/us/12) / ID `9523827` — Ready | `T-AUD1-01` [#31](https://tree.taiga.io/project/lenghi-group-07-project/task/31); `T-AUD1-02` [#32](https://tree.taiga.io/project/lenghi-group-07-project/task/32); `T-AUD1-03` [#33](https://tree.taiga.io/project/lenghi-group-07-project/task/33) — New | `PF-03 — Audit → Adjust`; screen inventory/Figma parity chờ human review | Chưa bắt đầu / Chưa bắt đầu |
| `REQ-002/004`, `CAND-REQ-005/010` | `US-AUD-002` | [#13](https://tree.taiga.io/project/lenghi-group-07-project/us/13) / ID `9523828` — Ready | `T-AUD2-01` [#34](https://tree.taiga.io/project/lenghi-group-07-project/task/34); `T-AUD2-02` [#35](https://tree.taiga.io/project/lenghi-group-07-project/task/35); `T-AUD2-03` [#36](https://tree.taiga.io/project/lenghi-group-07-project/task/36) — New | `PF-03 — Audit → Adjust`; screen inventory/Figma parity chờ human review | Chưa bắt đầu / Chưa bắt đầu |
| `REQ-001/002/003`, `CAND-REQ-008/010` | `US-ADJ-001` | [#14](https://tree.taiga.io/project/lenghi-group-07-project/us/14) / ID `9523829` — Ready | `T-ADJ1-01` [#37](https://tree.taiga.io/project/lenghi-group-07-project/task/37); `T-ADJ1-02` [#38](https://tree.taiga.io/project/lenghi-group-07-project/task/38); `T-ADJ1-03` [#39](https://tree.taiga.io/project/lenghi-group-07-project/task/39) — New | `PF-03 — Audit → Adjust`; screen inventory/Figma parity chờ human review | Chưa bắt đầu / Chưa bắt đầu |
| `REQ-001/002/003`, `CAND-REQ-003/008/010/011` | `US-ADJ-002` | [#15](https://tree.taiga.io/project/lenghi-group-07-project/us/15) / ID `9523830` — Ready | `T-ADJ2-01` [#40](https://tree.taiga.io/project/lenghi-group-07-project/task/40); `T-ADJ2-02` [#41](https://tree.taiga.io/project/lenghi-group-07-project/task/41); `T-ADJ2-03` [#42](https://tree.taiga.io/project/lenghi-group-07-project/task/42) — New | `PF-03 — Audit → Adjust`; screen inventory/Figma parity chờ human review | Chưa bắt đầu / Chưa bắt đầu |

## OQ decision trace

| OQ | Current status | Decision/impact |
|---|---|---|
| `OQ-011` | RESOLVED — HUMAN PRODUCT DECISION | `DEC-010–015`; per-location `system stock quantity` |
| `OQ-013` | PARTIALLY DECIDED / OPEN | Receive completion/handoff, Putaway exception/handoff, Transfer exception/reversal, Audit mismatch completion and Adjust rejected-case closure remain open |
| `OQ-017` | RESOLVED — HUMAN PRODUCT DECISION | `DEC-014/015` |
| `OQ-018` | RESOLVED — HUMAN PRODUCT DECISION | `DEC-014` |
| `OQ-019` | RESOLVED — HUMAN PRODUCT DECISION | `DEC-016/017` |
| `OQ-020` | RESOLVED — HUMAN PRODUCT DECISION | `DEC-017` |
| `OQ-015` | RESOLVED — HUMAN PRODUCT DECISION | `DEC-019`; location quantity cannot be negative; no retry/cancel semantics inferred |
| `OQ-014`, `OQ-021`, `OQ-022` | OPEN QUESTION | Partial workflow, Alert and device/integration behavior remain undecided |

AI-related OQs remain unchanged and are future/open directions, not canonical MVP requirements.

## Product Definition artifact mapping

| Artifact | Coverage | Canonical source |
|---|---|---|
| [`03-product/PRD.md`](03-product/PRD.md) | Product overview, scope, workflows, requirements, rules, stories, permissions, OQs, success criteria | Requirements, Business Rules, Domain, Decisions, canonical stories |
| [`03-product/mvp-scope.md`](03-product/mvp-scope.md) | IN MVP / OUT OF MVP / OPEN with ID-level trace | Requirements, Decisions, OQs |
| [`03-product/user-flow.md`](03-product/user-flow.md) | Independent Pick/Transfer paths; selected-scope Audit; discrepancy/re-check/Adjust relationship; negative-stock guards | `DEC-018/019`, canonical stories and AC |
| [`04-backlog/user-stories.md`](04-backlog/user-stories.md) | Report-facing summary of 9 canonical stories | `vault/04-product/stories/` |
| [`05-design/screen-inventory.md`](05-design/screen-inventory.md) | 10 base screens and 3 critical prototype flows | Canonical stories, consolidated flow and human-reviewed usability decisions |
| [`05-design/usability-test-script.md`](05-design/usability-test-script.md) | Task script for `P1`/`P2`/`P3` | Canonical stories and approved flow boundaries |
| [`05-design/usability-findings.md`](05-design/usability-findings.md) | Human-reviewed Observation → Issue → Decision findings | Findings supplied by human reviewer; no new Requirement/BR |

## Prototype → usability traceability

Các “Usability Decision” dưới đây là decision cục bộ của artifact về wording, state visibility hoặc prototype transition. Chúng không phải Requirement/Business Rule mới và không được gán `DEC-*` mới vì không thay đổi product behavior canonical.

| Prototype Flow | Story | Usability Finding | Usability Decision | Existing canonical decision |
|---|---|---|---|---|
| `PF-01 — Receive → Putaway` | `US-REC-001`, `US-PUT-001` | `P1`: expected/actual và discrepancy rõ; completion sau reference review và boundary sang Putaway chưa rõ | Giữ hai flow tách biệt; không production CTA tự động; prototype chỉ dùng facilitator transition | `DEC-016`, `DEC-018`; `OQ-013` vẫn mở |
| `PF-02 — Pick` | `US-PICK-001` | `P2`: multi-location/full/blocked rõ; partial có thể bị hiểu là fully completed | Giữ partial hợp lệ; thêm copy “Pick is not fully completed. 4 units remain unfulfilled.”; giữ blocked/no-change guard | `DEC-012`, `DEC-019` |
| `PF-03 — Audit → Adjust` | `US-AUD-001`, `US-AUD-002`, `US-ADJ-001`, `US-ADJ-002` | `P3`: mismatch và re-check rõ; thời điểm quantity đổi qua actor handoff chưa rõ | Hiển thị no-change sau mismatch/re-check/waiting/reject; chỉ approved/applied mới cập nhật quantity | `DEC-014`, `DEC-015`, `DEC-018`, `DEC-019` |

## Decomposition record

- `DRAFT-US-PUT-001` was promoted to `US-PUT-001`.
- `DRAFT-US-PICK-001` was promoted to `US-PICK-001`; insufficient Pick remains an AC/scenario.
- `DRAFT-US-TRF-001` was split into `US-TRF-001` and `US-TRF-002`.
- `DRAFT-US-AUD-001` was split into `US-AUD-001` and `US-AUD-002`.
- `DRAFT-US-ADJ-001` was split into `US-ADJ-001` and `US-ADJ-002`.
- Receive reference mismatch remains an AC/scenario in `US-REC-001`.

Historical draft references are valid only when explicitly labeled as promoted, split, historical or superseded.

## Downstream status

| Artifact | Current truthful status |
|---|---|
| Canonical stories | 9 HUMAN APPROVED stories |
| Historical drafts | Superseded; not active backlog items |
| PRD / MVP Scope | Baseline for Report Round 1; open questions preserved |
| Report user flow | Consolidated flow updated; independent operational paths and lifecycle gaps preserved |
| Design/Figma/Prototype | Figma URL đã được cung cấp; screen inventory ghi 10 base screens/3 flows; quyền truy cập và frame parity cần human review |
| Usability artifacts | Script và 3 human-reviewed findings đã được tổng hợp; không claim AI thực hiện participant test |
| Taiga | Project metadata và 6 Epic / 9 User Story / 27 Task references đã đồng bộ; quyền truy cập/người phụ trách công cụ vẫn TBD |
| Architecture/Data Model/API | Technical Foundation human reviewed; 3 accepted ADR; MVP route map proposed; Putaway contract documented |
| Implementation/Test | Repo scaffold + `US-PUT-001` vertical slice đã triển khai; local component/frontend checks pass; Docker/PostgreSQL/Playwright local bị blocked và không được ghi Pass; chờ human diff review |
