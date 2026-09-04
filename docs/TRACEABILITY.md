# Traceability v1

Traceability sử dụng stable ID canonical. Artifact downstream còn thiếu phải hiển thị rõ `TBD` hoặc `Chưa bắt đầu`; không được tạo link giả.

## Nền tảng sản phẩm đã xác nhận

| Requirement/Hướng | User Story/AC | Flow/Design/Spec | Taiga | Implementation | Test | Bằng chứng |
|---|---|---|---|---|---|---|
| REQ-001 | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận |
| REQ-002 | [`DRAFT-US-PUT-001`](04-backlog/user-stories.md) — AC sản phẩm: TBD | Chuỗi cấp cao đã xác nhận; [Putaway cautious flow](03-product/user-flow.md) là DRAFT | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận; `EVD-006`, `EVD-007`, `EVD-008`, `EVD-010`, `EVD-011`, `EVD-019` |
| REQ-003 | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận |
| REQ-004 | TBD | Bảng thuật ngữ domain mới có một phần | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận |
| CAND-REQ-005 | [`DRAFT-US-AUD-001`](04-backlog/user-stories.md) — `AC-AUD-01`, `AC-AUD-02` là DRAFT | [Audit cautious flow](03-product/user-flow.md) là DRAFT | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | `EVD-012`, `EVD-013`, `EVD-014`, `EVD-015`, `EVD-016`, `EVD-017`, `EVD-019`; `CAND-BR-002` |
| CAND-BR-002 | [`DRAFT-US-ADJ-001`](04-backlog/user-stories.md) — `AC-ADJ-001`, `AC-ADJ-002` là DRAFT | [Adjust cautious flow](03-product/user-flow.md) là DRAFT | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Trực tiếp: `EVD-012`, `EVD-017`; liên quan, không bắt buộc: `CAND-REQ-005`; `EVD-013` chỉ là current-state evidence |
| AI-DIR-001 | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Hướng được giảng viên xác nhận |
| AI-DIR-002 | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Hướng được giảng viên xác nhận |
| AI-DIR-003 | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Hướng được giảng viên xác nhận |

Deliverable môn học/báo cáo được theo dõi trong [`00-project-index.md`](00-project-index.md), không được gán ID yêu cầu sản phẩm tại đây.

## Putaway DRAFT trace

```text
REQ-002
  + EVD-006 / EVD-007 / EVD-008
  + EVD-010 / EVD-011 (Putaway/Transfer boundary remains OPEN)
  + EVD-019 (research limitation)
    -> DRAFT-US-PUT-001
    -> Acceptance Criteria: TBD
    -> Putaway cautious flow: DRAFT
    -> Taiga / Implementation / Test: Chưa bắt đầu
```

`CAND-REQ-003` vẫn là `DRAFT` và không được sử dụng tại đây như approval cho hành vi record/lookup location. Trigger, completion, partial Putaway, location cardinality (`OQ-034` chỉ là stable ID đề xuất, chưa canonical), Putaway/Transfer classification, role permission, Stock/Movement effect và device interaction tiếp tục là `TBD` / `OPEN QUESTION`.

## Audit DRAFT trace

```text
REQ-002 (Audit là khu vực quy trình bắt buộc)
  + REQ-004 (Audit thuộc core domain; hành vi chi tiết TBD)
  + CAND-REQ-005 (APPROVED — hỗ trợ đối chiếu số lượng đếm thực tế với dữ liệu tồn hệ thống)
  + CAND-BR-002 (APPROVED — re-check chênh lệch trước điều chỉnh tồn)
  + EVD-015 / EVD-016 / EVD-017 (kiểm kê, đối chiếu và discrepancy path)
  + EVD-012 / EVD-013 / EVD-014 (re-check, manager involvement và permission unknown)
  + EVD-019 (research limitation)
    -> DRAFT-US-AUD-001
    -> DRAFT AC-AUD-01 / AC-AUD-02
    -> Audit cautious flow: DRAFT
    -> Taiga / Implementation / Test: Chưa bắt đầu
```

Audit type, trigger, precondition, completion state, count scope, schedule, role permission, reason/evidence/approval, device interaction, relationship to Adjust và result after re-check tiếp tục là `TBD` / `OPEN QUESTION`. Trace này không xác nhận Audit tự động thay đổi Stock hoặc tự động tạo Adjust.

## Adjust DRAFT trace

```text
REQ-002 (Adjust là khu vực quy trình bắt buộc)
  + CAND-BR-002 (APPROVED — re-check chênh lệch trước điều chỉnh tồn)
  + EVD-012 / EVD-017 (evidence trực tiếp)
  + CAND-REQ-005 (liên quan đến Audit; không phải nguồn bắt buộc của Adjust)
  + EVD-013 (current-state evidence, không phải product role/permission/approval behavior)
    -> DRAFT-US-ADJ-001
    -> DRAFT AC-ADJ-001 / AC-ADJ-002
    -> Adjust cautious flow: DRAFT
    -> Taiga / Implementation / Test: Chưa bắt đầu
```

Nguồn/trigger chênh lệch, detailed recheck, completion state, exception handling, adjustment mechanism, reason/evidence/approval, role/permission, quantity definition, negative-stock handling và anomaly/discrepancy definition vẫn là `TBD` / `OPEN QUESTION`. Trace này không xác nhận Audit là trigger/dependency bắt buộc, automatic stock update, hoặc behavior ngoài `CAND-BR-002`.
