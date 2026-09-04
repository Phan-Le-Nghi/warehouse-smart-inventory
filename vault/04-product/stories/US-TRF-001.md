# US-TRF-001 — Xác nhận Internal Transfer

## Trạng thái và ownership

`CANONICAL — HUMAN APPROVED`

Owner: Nguyễn Thị Ly Na.

## User Story

Là Warehouse Staff, tôi muốn xác nhận Internal Transfer giữa tracked internal locations, để source và destination quantities được cập nhật nhất quán mà không đổi Warehouse total.

## Business value và scope

Story cover execution/confirmation của subsequent relocation trong cùng một Warehouse và minimum confirmed Transfer record.

## Traceability

- Requirements: `REQ-001`, `REQ-002`, `REQ-004`, `CAND-REQ-003`, `CAND-REQ-004`, `CAND-REQ-010`, `CAND-REQ-011`.
- Business rules: `CAND-BR-003`, `CAND-BR-007`, `CAND-BR-008`, `CAND-BR-015`.
- Human decisions: `DEC-005`, `DEC-007`, `DEC-009`, `DEC-010`, `DEC-013`, `DEC-017`, `DEC-019`.
- Open questions: `OQ-013`, `OQ-014`, `OQ-022`.
- Source classification: HUMAN PRODUCT DECISION / MVP ASSUMPTION. `EVD-010`, `EVD-011` chỉ là current-state context.

## Acceptance Criteria

### AC-TRF1-001 — Confirm quantity effects

Given SKU, quantity, source và destination tracked locations trong cùng Warehouse, when Warehouse Staff confirm Transfer, then source giảm Transfer quantity và destination tăng cùng quantity.

### AC-TRF1-002 — Preserve Warehouse total

Given Internal Transfer được confirm, when quantity effects được ghi nhận, then Warehouse total quantity không thay đổi.

### AC-TRF1-003 — Minimum Transfer record

Given Transfer được confirm, when system record được tạo, then record chứa SKU, quantity, source, destination và confirmation timestamp.

### AC-TRF1-004 — Prevent negative source quantity

Given Transfer quantity lớn hơn `system stock quantity` tại source location, when Warehouse Staff cố confirm Transfer, then Transfer không được confirm, quantity change không được apply và operation được báo không hợp lệ/không thể confirm.

## Remaining gaps và scope guards

- Transfer exception, failed confirmation, cancellation và reversal vẫn `TBD / OQ-013`.
- Partial Transfer vẫn `OQ-014`; retry/cancel lifecycle sau failed validation chưa được quyết định; device/integration behavior vẫn `OQ-022`.
- Cross-Warehouse Transfer ngoài MVP.
