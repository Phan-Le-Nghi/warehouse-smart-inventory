# US-REC-001 — Ghi nhận Receive theo số lượng thực nhận

## Trạng thái

BA CONFIRMED — cập nhật theo feedback: không có AC về tra cứu lại Receive vì evidence hiện có chưa support behavior này.

## User Story

Là người thực hiện Receive, tôi muốn kiểm tra mặt hàng, ghi nhận số lượng thực nhận và đối chiếu với số lượng kỳ vọng, để số lượng Receive phản ánh hàng thực tế và chênh lệch được ghi nhận.

Theo HUMAN PRODUCT DECISIONS Round 2, Warehouse Staff thực hiện Receive; Purchasing cung cấp/xem expected quantity/reference. Expected quantity đến từ external/manual order or delivery reference; full Purchase Order lifecycle ngoài MVP (`DEC-016`, `DEC-017`). Canonical story wording và `AC-01` đến `AC-03` được bảo tồn; reference-mismatch AC cần explicit canonical story review trước khi bổ sung.

## Traceability

- Requirements: `REQ-002`, `CAND-REQ-001`, `CAND-REQ-002`; Round 2 context: `CAND-REQ-009`, `CAND-REQ-010`
- Business rule: `CAND-BR-001`; proposed story addition context: `CAND-BR-014`
- Evidence: `EVD-002`, `EVD-003`, `EVD-004`, `EVD-005`
- Human decisions: `DEC-016`, `DEC-017`; remaining lifecycle gap: `OQ-013`

## Acceptance Criteria

### AC-01 — Ghi nhận và đối chiếu

Given một ngữ cảnh Receive có mặt hàng và số lượng kỳ vọng, when người thực hiện kiểm tra mặt hàng và nhập số lượng thực nhận, then hệ thống ghi nhận số lượng thực nhận và đối chiếu với số lượng kỳ vọng.

### AC-02 — Nhận đủ

Given số lượng thực nhận bằng số lượng kỳ vọng, when Receive được ghi nhận, then số lượng Receive được ghi nhận bằng số lượng thực nhận.

### AC-03 — Có chênh lệch

Given số lượng thực nhận khác số lượng kỳ vọng, when Receive được ghi nhận, then số lượng Receive được ghi nhận bằng số lượng thực nhận, không thay thế bằng số lượng kỳ vọng, và chênh lệch giữa hai số lượng được ghi nhận.

## Ngoài phạm vi hiện tại

- Không có Acceptance Criterion về tra cứu/xem lại Receive hoặc chênh lệch đã ghi nhận: chưa có evidence support behavior này.
- Receive completion/exact handoff sang Putaway, damaged goods, over-receive và behavior ngoài approved reference mismatch vẫn là `TBD` / `OQ-013` hoặc OQ liên quan.
