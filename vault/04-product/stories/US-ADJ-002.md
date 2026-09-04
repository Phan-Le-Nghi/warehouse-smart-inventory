# US-ADJ-002 — Quyết định và apply Adjust

## Trạng thái và ownership

`CANONICAL — HUMAN APPROVED`

Owner: Đặng Thị Thanh Ngân.

## User Story

Là Manager, tôi muốn approve hoặc reject Adjust request, để chỉ approved Adjust mới cập nhật `system stock quantity` tại affected location.

## Business value và scope

Story cover Manager decision, approved apply effect và no-change branches. Story không xác định rejected-case final closure.

## Traceability

- Requirements: `REQ-001`, `REQ-002`, `REQ-003`, `CAND-REQ-003`, `CAND-REQ-008`, `CAND-REQ-010`.
- Business rules: `CAND-BR-002`, `CAND-BR-011`, `CAND-BR-013`.
- Evidence: `EVD-012`, `EVD-013`, `EVD-017` hỗ trợ current-state re-check/Manager involvement.
- Human decisions: `DEC-010`, `DEC-015`, `DEC-017`.
- Open questions: `OQ-013`, `OQ-015`.
- Source classification: verified evidence + HUMAN PRODUCT DECISION.

## Acceptance Criteria

### AC-ADJ2-001 — Approve and apply

Given discrepancy đã re-check, reason đã ghi và Manager approves request, when Adjust được apply, then `system stock quantity` tại affected internal location được cập nhật.

### AC-ADJ2-002 — Reject without quantity change

Given Manager rejects request, when rejection được ghi nhận, then `system stock quantity` không thay đổi.

### AC-ADJ2-003 — No discrepancy after re-check

Given re-check không còn discrepancy, when case được xử lý, then Adjust không được apply và quantity không thay đổi.

## Remaining gaps và scope guards

- Rejected-case final closure vẫn `TBD / OQ-013`.
- Negative-stock behavior vẫn `OQ-015`.
