# Traceability v4 — PRD / MVP / Consolidated Flow Baseline

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
| `US-PUT-001` | destination allocation; tracked location; no automatic Movement record | Not started |
| `US-PICK-001` | full Pick; multi-location; `PARTIAL / INSUFFICIENT`; negative-stock guard | Not started |
| `US-TRF-001` | source/destination effects; Warehouse total; minimum record; negative-stock guard | Technical contract still TBD |
| `US-TRF-002` | Manager history access; history fields; confirmation time | Technical contract still TBD |
| `US-AUD-001` | selected scope; count/compare; result; match completion | Not started |
| `US-AUD-002` | discrepancy context; mandatory re-check; no auto Adjust | Not started |
| `US-ADJ-001` | request/reason; re-check; optional attachment; no pre-decision change | Not started |
| `US-ADJ-002` | approve/apply; reject/no change; no-discrepancy/no change; negative-stock guard | Not started |

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
| Design/Figma/Prototype | Chưa tạo |
| Taiga | Chưa tạo item; URL/access TBD |
| Architecture/Data Model/API | Still subject to separate human approval |
| Implementation/Test | Chưa bắt đầu |
