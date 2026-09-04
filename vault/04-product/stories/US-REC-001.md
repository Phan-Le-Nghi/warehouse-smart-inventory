# US-REC-001 — Ghi nhận Receive theo số lượng thực nhận

## Trạng thái và ownership

`CANONICAL — HUMAN APPROVED`

Owner: Nguyễn Thị Nghĩa.

## User Story

Là Warehouse Staff, tôi muốn kiểm tra item, ghi nhận actual quantity và đối chiếu với expected quantity/reference, để Receive phản ánh hàng thực tế và các mismatch được nhận biết trước khi completion được cân nhắc.

Purchasing cung cấp/xem expected quantity/reference. Expected quantity đến từ external/manual order or delivery reference; full Purchase Order lifecycle ngoài MVP (`DEC-016`, `DEC-017`).

## Traceability

- Requirements: `REQ-002`, `CAND-REQ-001`, `CAND-REQ-002`; Round 2 context: `CAND-REQ-009`, `CAND-REQ-010`
- Business rules: `CAND-BR-001`, `CAND-BR-014`
- Evidence: `EVD-002`, `EVD-003`, `EVD-004`, `EVD-005`
- Human decisions: `DEC-016`, `DEC-017`; remaining lifecycle gap: `OQ-013`
- Source classification: verified evidence + HUMAN PRODUCT DECISION.

## Acceptance Criteria

### AC-01 — Ghi nhận và đối chiếu

Given một ngữ cảnh Receive có mặt hàng và số lượng kỳ vọng, when người thực hiện kiểm tra mặt hàng và nhập số lượng thực nhận, then hệ thống ghi nhận số lượng thực nhận và đối chiếu với số lượng kỳ vọng.

### AC-02 — Nhận đủ

Given số lượng thực nhận bằng số lượng kỳ vọng, when Receive được ghi nhận, then số lượng Receive được ghi nhận bằng số lượng thực nhận.

### AC-03 — Có chênh lệch

Given số lượng thực nhận khác số lượng kỳ vọng, when Receive được ghi nhận, then số lượng Receive được ghi nhận bằng số lượng thực nhận, không thay thế bằng số lượng kỳ vọng, và chênh lệch giữa hai số lượng được ghi nhận.

### AC-04 — Review reference mismatch

Given system reference khác document reference, when Receive được xử lý, then mismatch phải được user review trước completion và system không tự chọn authoritative reference.

## Ngoài phạm vi hiện tại

- Không có Acceptance Criterion về tra cứu/xem lại Receive hoặc chênh lệch đã ghi nhận: chưa có evidence support behavior này.
- Receive trigger/completion wording cuối, exact handoff sang Putaway, damaged goods, over-receive và behavior ngoài approved reference mismatch vẫn là `TBD` / `OQ-013` hoặc OQ liên quan.
- Partial Receive vẫn thuộc `OQ-014`; device/integration behavior vẫn thuộc `OQ-022`.
