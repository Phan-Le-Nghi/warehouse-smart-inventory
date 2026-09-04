# US-AUD-001 — Thực hiện selected-scope Audit

## Trạng thái và ownership

`CANONICAL — HUMAN APPROVED`

Owner: Phan Lê Nghi.

## User Story

Là Warehouse Staff, tôi muốn thực hiện selected-scope Audit và so sánh physical count với `system stock quantity`, để ghi nhận kết quả match hoặc mismatch.

## Business value và scope

Story cover scope selection, physical count, comparison, result recording và approved match completion branch.

## Traceability

- Requirements: `REQ-002`, `REQ-004`, `CAND-REQ-003`, `CAND-REQ-005`, `CAND-REQ-010`.
- Business rules: `CAND-BR-003`, `CAND-BR-009`.
- Evidence: `EVD-015`, `EVD-016` hỗ trợ current-state count/compare.
- Human decisions: `DEC-010`, `DEC-014`, `DEC-017`.
- Open questions: `OQ-013`, `OQ-022`.
- Source classification: verified evidence + HUMAN PRODUCT DECISION.

## Acceptance Criteria

### AC-AUD1-001 — Select Audit scope

Given Audit session được bắt đầu, when Warehouse Staff chọn scope, then scope là nhóm SKU/location hoặc toàn Warehouse.

### AC-AUD1-002 — Count and compare

Given selected scope, when Warehouse Staff ghi physical count, then count được compare với `system stock quantity` tại scope/location tương ứng.

### AC-AUD1-003 — Record comparison result

Given comparison đã thực hiện, when result được ghi nhận, then Audit lưu kết quả match hoặc mismatch.

### AC-AUD1-004 — Match completion

Given result là match, when result được confirm, then Audit có thể complete.

## Remaining gaps và scope guards

- Audit mismatch completion và schedule vẫn `TBD / OQ-013`.
- Device/integration behavior vẫn `OQ-022`.
- Không canonicalize `cycle count`.
