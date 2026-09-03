# Traceability v1

Traceability sử dụng stable ID canonical. Artifact downstream còn thiếu phải hiển thị rõ `TBD` hoặc `Chưa bắt đầu`; không được tạo link giả.

## Nền tảng sản phẩm đã xác nhận

| Requirement/Hướng | User Story/AC | Flow/Design/Spec | Taiga | Implementation | Test | Bằng chứng |
|---|---|---|---|---|---|---|
| REQ-001 | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận |
| REQ-002 | [`DRAFT-US-PUT-001`](04-backlog/user-stories.md) — AC sản phẩm: TBD | Chuỗi cấp cao đã xác nhận; [Putaway cautious flow](03-product/user-flow.md) là DRAFT | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận; `EVD-006`, `EVD-007`, `EVD-008`, `EVD-010`, `EVD-011`, `EVD-019` |
| REQ-003 | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận |
| REQ-004 | TBD | Bảng thuật ngữ domain mới có một phần | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận |
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
