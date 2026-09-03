# US-REC-001 — Ghi nhận Receive theo số lượng thực nhận

## Trạng thái

BA CONFIRMED — cập nhật theo feedback: không có AC về tra cứu lại Receive vì evidence hiện có chưa support behavior này.

## User Story

Là người thực hiện Receive, tôi muốn kiểm tra mặt hàng, ghi nhận số lượng thực nhận và đối chiếu với số lượng kỳ vọng, để số lượng Receive phản ánh hàng thực tế và chênh lệch được ghi nhận.

Role/authority thực hiện Receive vẫn là `OPEN QUESTION` (`OQ-020`). Nguồn của số lượng kỳ vọng vẫn là `OPEN QUESTION` (`OQ-019`).

## Traceability

- Requirements: `REQ-002`, `CAND-REQ-001`, `CAND-REQ-002`
- Business rule: `CAND-BR-001`
- Evidence: `EVD-002`, `EVD-003`, `EVD-004`, `EVD-005`
- Open questions: `OQ-019`, `OQ-020`

## Acceptance Criteria

### AC-01 — Ghi nhận và đối chiếu

Given một ngữ cảnh Receive có mặt hàng và số lượng kỳ vọng, when người thực hiện kiểm tra mặt hàng và nhập số lượng thực nhận, then hệ thống ghi nhận số lượng thực nhận và đối chiếu với số lượng kỳ vọng.

### AC-02 — Nhận đủ

Given số lượng thực nhận bằng số lượng kỳ vọng, when Receive được ghi nhận, then số lượng Receive được ghi nhận bằng số lượng thực nhận.

### AC-03 — Có chênh lệch

Given số lượng thực nhận khác số lượng kỳ vọng, when Receive được ghi nhận, then số lượng Receive được ghi nhận bằng số lượng thực nhận, không thay thế bằng số lượng kỳ vọng, và chênh lệch giữa hai số lượng được ghi nhận.

## Ngoài phạm vi hiện tại

- Không có Acceptance Criterion về tra cứu/xem lại Receive hoặc chênh lệch đã ghi nhận: chưa có evidence support behavior này.
- Cách xử lý chênh lệch với bên giao, handoff sang Putaway, approval, lý do, attachment, damaged goods và over-receive vẫn là `TBD` / `OPEN QUESTION`.
