# US-PICK-001 — Thực hiện Pick từ tracked locations

## Trạng thái và ownership

`CANONICAL — HUMAN APPROVED`

Owner: Trương Huỳnh Thảo Ngân.

## User Story

Là Warehouse Staff, tôi muốn thực hiện Pick từ một Pick request bằng một hoặc nhiều tracked internal locations, để cung cấp confirmed quantity cho downstream use và ghi nhận trung thực trường hợp không đủ.

## Business value và scope

Story cover full Pick và `PARTIAL / INSUFFICIENT` như một exception scenario của cùng Pick request. Downstream fulfilment/use nằm ngoài MVP.

## Traceability

- Requirements: `REQ-002`, `REQ-003`, `CAND-REQ-003`, `CAND-REQ-006`, `CAND-REQ-010`, `CAND-REQ-011`.
- Business rules: `CAND-BR-003`, `CAND-BR-005`, `CAND-BR-006`, `CAND-BR-015`.
- Human decisions: `DEC-010`, `DEC-012`, `DEC-017`, `DEC-019`.
- Open questions: `OQ-013`, `OQ-022`.
- Source classification: HUMAN PRODUCT DECISION / MVP ASSUMPTION. `EVD-006` đến `EVD-009` chỉ là current-state context.

## Acceptance Criteria

### AC-PICK-001 — Full Pick confirmation

Given Pick request có SKU/requested quantity, when Warehouse Staff confirm full requested quantity từ một hoặc nhiều source locations, then Pick là fully completed và confirmed quantity được giảm tại các source tương ứng.

### AC-PICK-002 — Multi-location Pick

Given một location không đủ nhưng location khác có quantity cho cùng SKU, when Pick được thực hiện, then requested quantity có thể được lấy từ nhiều tracked internal locations.

### AC-PICK-003 — Insufficient quantity

Given tổng quantity được lấy nhỏ hơn requested quantity, when result được ghi nhận, then Pick là `PARTIAL / INSUFFICIENT` và không fully completed.

### AC-PICK-004 — Prevent negative stock

Given confirmed quantity lớn hơn tổng `system stock quantity` tại các selected source locations, when Warehouse Staff cố confirm Pick, then Pick không được confirm, quantity change không được apply và operation được báo không hợp lệ/không thể confirm.

## Remaining gaps và scope guards

- Cancellation/retry ngoài approved insufficient branch vẫn `TBD / OQ-013`.
- Retry/cancel lifecycle sau failed validation chưa được quyết định; device/integration behavior vẫn `OQ-022`.
- FIFO, FEFO, reservation và scanning ngoài Pick MVP hiện tại.
