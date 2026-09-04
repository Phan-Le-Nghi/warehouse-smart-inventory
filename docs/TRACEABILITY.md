# Traceability v1

Traceability sử dụng stable ID canonical. Artifact downstream còn thiếu phải hiển thị rõ TBD hoặc Chưa bắt đầu; không được tạo link giả.

## Nền tảng sản phẩm đã xác nhận

| Requirement/Hướng | User Story/AC | Flow/Design/Spec | Taiga | Implementation | Test | Bằng chứng |
|---|---|---|---|---|---|---|
| REQ-001 | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận |
| REQ-002 | [`DRAFT-US-PUT-001`](04-backlog/user-stories.md) — AC sản phẩm: TBD | Chuỗi cấp cao đã xác nhận; [Putaway cautious flow](03-product/user-flow.md) là DRAFT | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận; EVD-006, EVD-007, EVD-008, EVD-010, EVD-011, EVD-019 |
| REQ-003 | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận |
| REQ-004 | TBD | Bảng thuật ngữ domain mới có một phần | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Bối cảnh được giảng viên xác nhận |
| CAND-REQ-005 | [`DRAFT-US-AUD-001`](04-backlog/user-stories.md) — AC-AUD-01, AC-AUD-02 là DRAFT | [Audit cautious flow](03-product/user-flow.md) là DRAFT | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | EVD-012, EVD-013, EVD-014, EVD-015, EVD-016, EVD-017, EVD-019; CAND-BR-002 |
| AI-DIR-001 | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Hướng được giảng viên xác nhận |
| AI-DIR-002 | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Hướng được giảng viên xác nhận |
| AI-DIR-003 | TBD | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | Hướng được giảng viên xác nhận |

## Receive — BA confirmed

| Requirement/Hướng | User Story/AC | Flow/Design/Spec | Taiga | Implementation | Test | Bằng chứng |
|---|---|---|---|---|---|---|
| CAND-REQ-001 | US-REC-001: AC-01, AC-02 | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | EVD-002, EVD-003 |
| CAND-REQ-002 | US-REC-001: AC-03 | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | EVD-004, EVD-005 |
| CAND-BR-001 | US-REC-001: AC-03 | TBD | Chưa tạo | Chưa bắt đầu | Chưa bắt đầu | EVD-002, EVD-003, EVD-004 |

OQ-019 (nguồn số lượng kỳ vọng) và OQ-020 (role/authority Receive) vẫn mở.

Không có AC-04 vì evidence hiện có chưa xác nhận hành vi tra cứu/xem lại Receive.

Deliverable môn học/báo cáo được theo dõi trong [`00-project-index.md`](00-project-index.md), không được gán ID yêu cầu sản phẩm tại đây.

## Putaway DRAFT trace

```text
REQ-002
  + EVD-006 / EVD-007 / EVD-008
  + EVD-010 / EVD-011
    (Putaway/Transfer boundary remains OPEN)
  + EVD-019
    (research limitation)
    -> DRAFT-US-PUT-001
    -> Acceptance Criteria: TBD
    -> Putaway cautious flow: DRAFT
    -> Taiga / Implementation / Test: Chưa bắt đầu