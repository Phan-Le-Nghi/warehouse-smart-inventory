# Traceability v1

Traceability sử dụng stable ID canonical và các draft ID đã được human-approved cho mục đích theo dõi. Artifact downstream còn thiếu phải hiển thị rõ `TBD` hoặc `Chưa bắt đầu`; không tạo link giả. Một draft ID không làm cho story, AC, flow hoặc behavior trở thành canonical.

## Nền tảng sản phẩm đã xác nhận

| Requirement/Hướng | User Story/AC | Flow/Design/Spec | Taiga | Implementation | Test | Bằng chứng |
|---|---|---|---|---|---|---|
| `REQ-001` | Bao phủ một phần bởi các workflow stories | User Flow DRAFT | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận |
| `REQ-002` | 1 BA-confirmed + 5 DRAFT workflow stories | Chuỗi cấp cao CONFIRMED; sáu flow chi tiết DRAFT | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận; `EVD-002..017`, giới hạn `EVD-019` |
| `REQ-003` | Actor/permission vẫn TBD | Role names CONFIRMED; permission model TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận; `OQ-020` |
| `REQ-004` | Liên quan các story Pick/Transfer/Audit; behavior TBD | Glossary mới có một phần; Data Model/API TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận |
| `AI-DIR-001` | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Hướng được giảng viên xác nhận |
| `AI-DIR-002` | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Hướng được giảng viên xác nhận |
| `AI-DIR-003` | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Hướng được giảng viên xác nhận |

Deliverable môn học/báo cáo được theo dõi trong `docs/00-project-index.md`, không được gán ID yêu cầu sản phẩm tại đây.

## Receive — BA CONFIRMED story / DRAFT flow

| Requirement/Rule | Story/AC | Flow | Downstream | Evidence |
|---|---|---|---|---|
| `CAND-REQ-001` — APPROVED | `US-REC-001`: `AC-01`, `AC-02` | Receive flow DRAFT | Taiga/Design/Spec/Implementation/Test: chưa bắt đầu | `EVD-002`, `EVD-003` |
| `CAND-REQ-002` — APPROVED | `US-REC-001`: `AC-03` | Receive flow DRAFT | Taiga/Design/Spec/Implementation/Test: chưa bắt đầu | `EVD-004`, `EVD-005` |
| `CAND-BR-001` — APPROVED | `US-REC-001`: `AC-03` | Receive flow DRAFT | Taiga/Design/Spec/Implementation/Test: chưa bắt đầu | `EVD-002`, `EVD-003`, `EVD-004` |

`OQ-013`, `OQ-019` và `OQ-020` vẫn mở. Không có `AC-04`; evidence hiện có chưa xác nhận hành vi tra cứu/xem lại Receive.

## Putaway — DRAFT trace

```text
REQ-002
  + EVD-006 / EVD-007 / EVD-008
  + EVD-010 / EVD-011 (Putaway/Transfer boundary remains OPEN)
  + EVD-019 (research limitation)
  + CAND-REQ-003 (DRAFT)
    -> DRAFT-US-PUT-001
    -> Product Acceptance Criteria: TBD
    -> Putaway cautious flow: DRAFT
    -> Taiga / Design / Spec / Implementation / Test: Chưa bắt đầu
```

`CAND-REQ-003` không được sử dụng như approval cho record/lookup location. Trigger, completion, partial Putaway, location cardinality, Putaway/Transfer classification, role permission, Stock/Movement effect và device interaction vẫn là `TBD` / `OPEN QUESTION`. Câu hỏi location cardinality chưa có canonical OQ ID.

## Pick — DRAFT trace

```text
REQ-002
  + REQ-004 (domain concepts only; behavior TBD)
  + EVD-006 / EVD-007 / EVD-008 / EVD-009
    (current-state context; not confirmed Pick behavior)
  + CAND-REQ-003 (related, DRAFT)
    -> DRAFT-US-PICK-001
    -> AC-PICK-001: scope-level / non-functional
    -> Functional Acceptance Criteria: TBD
    -> Pick flow: DRAFT
    -> Taiga / Design / Spec / Implementation / Test: Chưa bắt đầu
```

`OQ-011`, `OQ-012`, `OQ-013`, `OQ-014`, `OQ-015`, `OQ-016`, `OQ-020` và `OQ-022` vẫn mở. Trace không xác nhận location support, reservation, stock deduction, Movement, Transfer, FIFO/FEFO, device behavior hoặc permission.

## Transfer — DRAFT trace

```text
REQ-002
  + REQ-004 (Movement and Transfer are core concepts; behavior TBD)
  + CAND-REQ-004 (DRAFT)
  + EVD-010 (physical movement exists)
  + EVD-011 (separate transaction is not confirmed)
  + EVD-019 (research limitation)
    -> DRAFT-US-TRF-001
    -> AC-TRF-001: scope-level only
    -> Functional Acceptance Criteria: TBD
    -> Transfer cautious flow: DRAFT
    -> Transfer Story Spec: DRAFT / not implementation-ready
    -> Taiga / Design / Implementation / Test: Chưa bắt đầu
```

`CAND-REQ-004` không được sử dụng như approval cho system Transfer behavior. `OQ-013`, `OQ-014`, `OQ-015`, `OQ-016`, `OQ-020` và `OQ-022` vẫn mở. Trace không xác nhận transaction, source/destination fields, Stock/location update, multi-Warehouse behavior hoặc permission.

## Adjust — DRAFT trace

```text
REQ-002
  + CAND-BR-002 (APPROVED — re-check before stock adjustment)
  + EVD-012 / EVD-017 (direct evidence)
  + CAND-REQ-005 (related to Audit; not a required Adjust trigger)
  + EVD-013 (current-state role context only)
    -> DRAFT-US-ADJ-001
    -> DRAFT AC-ADJ-001 / AC-ADJ-002
    -> Adjust cautious flow: DRAFT
    -> Taiga / Design / Spec / Implementation / Test: Chưa bắt đầu
```

Nguồn/trigger discrepancy, detailed recheck, completion, exception, adjustment mechanism, reason/evidence/approval, role/permission, Stock definition, negative-stock handling, anomaly definition và resulting Stock state vẫn là `TBD` / `OPEN QUESTION`. Trace không xác nhận Audit là trigger bắt buộc hoặc automatic Stock update.

## Audit — DRAFT trace

```text
REQ-002
  + REQ-004 (Audit is a core concept; detailed behavior TBD)
  + CAND-REQ-005 (APPROVED — compare physical count with system inventory data)
  + CAND-BR-002 (APPROVED — re-check before stock adjustment)
  + EVD-015 / EVD-016 / EVD-017
  + EVD-012 / EVD-013 / EVD-014 (related context and permission unknown)
  + EVD-019 (research limitation)
    -> DRAFT-US-AUD-001
    -> DRAFT AC-AUD-01 / AC-AUD-02
    -> Audit cautious flow: DRAFT
    -> Taiga / Design / Spec / Implementation / Test: Chưa bắt đầu
```

Audit type, trigger, precondition, completion, count scope, product schedule, role permission, reason/evidence/approval, device interaction, relationship to Adjust và result after re-check vẫn là `TBD` / `OPEN QUESTION`. Trace không xác nhận Audit tự động thay đổi Stock, tự động tạo Adjust hoặc áp dụng daily Audit cho mọi Warehouse.

## Downstream status

| Artifact | Current truthful status |
|---|---|
| Canonical stories | `US-REC-001` only; five workflow stories remain DRAFT |
| Canonical user flows | Chưa tạo trong `vault/04-product/user-flows/` |
| Design/Figma/Prototype | Chưa tạo |
| Taiga | Chưa tạo item; URL/access TBD |
| Story Specs | Transfer có một DRAFT spec; không implementation-ready |
| Architecture/Data Model/API | TBD; chưa được phê duyệt |
| Implementation/Test | Chưa bắt đầu |
