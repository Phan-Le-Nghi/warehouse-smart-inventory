# Traceability v2 — Round 2 Human Decisions

Traceability sử dụng stable IDs đã được ghi trong Vault. Các quyết định `DEC-010` đến `DEC-017` là HUMAN PRODUCT DECISIONS / MVP ASSUMPTIONS, không phải verified research findings và không tạo `EVD-*` mới. Draft story IDs không làm story hoặc AC trở thành canonical.

## Product foundation

| Source | Requirement/Rule | Story/Flow impact | Classification |
|---|---|---|---|
| `DEC-005` | One-Warehouse MVP | Tất cả workflow stories | HUMAN PRODUCT DECISION |
| `DEC-006`, `DEC-010` | `CAND-REQ-003`, `CAND-BR-003` | Putaway, Pick, Transfer, Audit, Adjust use per-location quantity | HUMAN PRODUCT DECISION / MVP ASSUMPTION |
| `DEC-011` | `CAND-REQ-007`, `CAND-BR-004` | `DRAFT-US-PUT-001` | HUMAN PRODUCT DECISION / MVP ASSUMPTION |
| `DEC-012` | `CAND-REQ-006`, `CAND-BR-005`, `CAND-BR-006` | `DRAFT-US-PICK-001` | HUMAN PRODUCT DECISION / MVP ASSUMPTION |
| `DEC-007`, `DEC-013` | `CAND-REQ-004`, `CAND-BR-007`, `CAND-BR-008` | `DRAFT-US-TRF-001` | HUMAN PRODUCT DECISION / MVP ASSUMPTION |
| `DEC-014` | `CAND-REQ-005`, `CAND-BR-009`, `CAND-BR-010` | `DRAFT-US-AUD-001` | HUMAN PRODUCT DECISION / MVP ASSUMPTION |
| `DEC-015` | `CAND-REQ-008`, `CAND-BR-011`–`CAND-BR-013` | `DRAFT-US-ADJ-001`; Audit discrepancy path | HUMAN PRODUCT DECISION / MVP ASSUMPTION |
| `DEC-016` | `CAND-REQ-009`, `CAND-BR-014` | `US-REC-001` proposed Round 2 additions | HUMAN PRODUCT DECISION / MVP ASSUMPTION |
| `DEC-017` | `CAND-REQ-010` | Actors/permissions across workflow stories | HUMAN PRODUCT DECISION / MVP ASSUMPTION |

## Receive

| Requirement/Rule | Story/AC | Flow | Downstream | Evidence/decision |
|---|---|---|---|---|
| `CAND-REQ-001` | `US-REC-001`: `AC-01`, `AC-02` | Receive flow | Design/Spec/Implementation/Test: chưa bắt đầu | `EVD-002`, `EVD-003` |
| `CAND-REQ-002`, `CAND-BR-001` | `US-REC-001`: `AC-03` | Quantity discrepancy branch | Chưa bắt đầu | `EVD-002`–`EVD-005` |
| `CAND-REQ-009`, `CAND-BR-014` | Proposed additions; canonical story unchanged | Reference source/mismatch branch | Story review required | `DEC-016`; not verified research evidence |
| `CAND-REQ-010` | Warehouse Staff actor; Purchasing/Manager constraints | Permission summary | Story review required | `DEC-017` |

`US-REC-001` remains BA CONFIRMED. Receive completion/exact Putaway handoff remains under `OQ-013 — PARTIALLY DECIDED / OPEN`. Full Purchase Order lifecycle is outside MVP.

## Putaway

```text
CAND-REQ-003 + CAND-REQ-007
  + CAND-BR-003 + CAND-BR-004
  + DEC-010 + DEC-011 + DEC-017
    -> DRAFT-US-PUT-001
    -> DRAFT AC-PUT-001 / AC-PUT-002
    -> Putaway flow DRAFT
    -> Design / Spec / Implementation / Test: Chưa bắt đầu
```

Exception/downstream handoff remains `OQ-013`; partial Putaway remains `OQ-014`. Putaway does not automatically create Transfer or Movement system record.

## Pick

```text
CAND-REQ-003 + CAND-REQ-006
  + CAND-BR-003 + CAND-BR-005 + CAND-BR-006
  + DEC-010 + DEC-012 + DEC-017
    -> DRAFT-US-PICK-001
    -> DRAFT AC-PICK-001 / AC-PICK-002 / AC-PICK-003
    -> Pick flow DRAFT
    -> Design / Spec / Implementation / Test: Chưa bắt đầu
```

FIFO/FEFO/reservation/scanning are outside the current Pick MVP. Negative-stock behavior remains `OQ-015`; cancellation/retry beyond the approved exception remains `OQ-013`.

## Transfer

```text
CAND-REQ-003 + CAND-REQ-004
  + CAND-BR-003 + CAND-BR-007 + CAND-BR-008
  + DEC-007 + DEC-013 + DEC-017
    -> DRAFT-US-TRF-001
    -> DRAFT AC-TRF-001 / AC-TRF-002 / AC-TRF-003
    -> Transfer flow DRAFT
    -> Transfer technical spec requires separate technical review
    -> Design / Implementation / Test: Chưa bắt đầu
```

`CAND-REQ-004` is `APPROVED — HUMAN PRODUCT DECISION`. Cross-Warehouse Transfer is outside MVP. Partial Transfer remains `OQ-014`; negative stock remains `OQ-015`; exception/reversal remains `OQ-013`.

## Audit

```text
CAND-REQ-005
  + CAND-BR-002 + CAND-BR-009 + CAND-BR-010
  + DEC-010 + DEC-014 + DEC-017
    -> DRAFT-US-AUD-001
    -> DRAFT AC-AUD-001 / AC-AUD-002 / AC-AUD-003
    -> Audit flow DRAFT
    -> Design / Spec / Implementation / Test: Chưa bắt đầu
```

`OQ-018` is resolved by `DEC-014`. Audit does not auto-adjust. Mismatch completion/schedule remains `OQ-013`; device behavior remains `OQ-022`.

## Adjust

```text
CAND-REQ-008 + CAND-REQ-010
  + CAND-BR-002 + CAND-BR-011 + CAND-BR-012 + CAND-BR-013
  + DEC-015 + DEC-017
    -> DRAFT-US-ADJ-001
    -> DRAFT AC-ADJ-001 / AC-ADJ-002 / AC-ADJ-003 / AC-ADJ-004
    -> Adjust flow DRAFT
    -> Design / Spec / Implementation / Test: Chưa bắt đầu
```

`OQ-017` and `OQ-020` are resolved by human decisions. Rejected-case closure remains `OQ-013`; negative-stock behavior remains `OQ-015`.

## OQ decision trace

| OQ | Current status | Decision |
|---|---|---|
| `OQ-011` | RESOLVED — HUMAN PRODUCT DECISION | `DEC-010`–`DEC-015` |
| `OQ-013` | PARTIALLY DECIDED / OPEN | Remaining lifecycle gaps retained in workflow artifacts |
| `OQ-017` | RESOLVED — HUMAN PRODUCT DECISION | `DEC-014`, `DEC-015` |
| `OQ-018` | RESOLVED — HUMAN PRODUCT DECISION | `DEC-014` |
| `OQ-019` | RESOLVED — HUMAN PRODUCT DECISION | `DEC-016`, `DEC-017` |
| `OQ-020` | RESOLVED — HUMAN PRODUCT DECISION | `DEC-017` |
| `OQ-014`, `OQ-015`, `OQ-022` | OPEN QUESTION | No broader Round 2 resolution |

## Downstream status

| Artifact | Current truthful status |
|---|---|
| Canonical stories | `US-REC-001` only |
| Draft stories | Five; all remain DRAFT / READY FOR HUMAN CANONICAL REVIEW |
| Canonical user flows | Chưa tạo trong `vault/04-product/user-flows/` |
| Report user flow | Updated DRAFT reflecting approved decisions and remaining OQs |
| Design/Figma/Prototype | Chưa tạo |
| Taiga | Chưa tạo item; URL/access TBD |
| Architecture/Data Model/API | No Round 2 design added; existing status remains subject to technical approval |
| Implementation/Test | Chưa bắt đầu |
