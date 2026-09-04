# US-ADJ-001 — Tạo Adjust request

## Trạng thái và ownership

`CANONICAL — HUMAN APPROVED`

Owner: Đặng Thị Thanh Ngân.

## User Story

Là Warehouse Staff, tôi muốn tạo Adjust request cho discrepancy đã re-check và ghi reason, để Manager có đủ context quyết định trước khi quantity thay đổi.

## Business value và scope

Story cover request preparation, mandatory re-check/reason, optional attachment và guard không apply quantity trước Manager decision.

## Traceability

- Requirements: `REQ-001`, `REQ-002`, `REQ-003`, `CAND-REQ-008`, `CAND-REQ-010`.
- Business rules: `CAND-BR-002`, `CAND-BR-011`, `CAND-BR-012`.
- Evidence: `EVD-012`, `EVD-013`, `EVD-017` hỗ trợ current-state re-check/handling context.
- Human decisions: `DEC-015`, `DEC-017`.
- Open questions: `OQ-013`, `OQ-015`.
- Source classification: verified evidence + HUMAN PRODUCT DECISION.

## Acceptance Criteria

### AC-ADJ1-001 — Create request with reason

Given discrepancy tại affected SKU/location đã được re-check và vẫn còn, when Warehouse Staff tạo Adjust request, then Adjust reason được ghi nhận.

### AC-ADJ1-002 — Require re-check

Given discrepancy chưa được re-check, when Adjust được cân nhắc, then điều kiện bắt buộc về re-check chưa được đáp ứng.

### AC-ADJ1-003 — Optional attachment

Given re-check và reason đã có nhưng không có attachment, when request được tạo, then attachment không phải điều kiện bắt buộc trong MVP.

### AC-ADJ1-004 — No change before decision

Given Adjust request đang chờ Manager decision, when request được ghi nhận, then `system stock quantity` chưa được thay đổi bởi Adjust đó.

## Remaining gaps và scope guards

- Negative-stock behavior vẫn `OQ-015`.
- Story không định nghĩa approval implementation hoặc technical workflow.
