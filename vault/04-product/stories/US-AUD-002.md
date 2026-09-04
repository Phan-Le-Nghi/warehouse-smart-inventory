# US-AUD-002 — Review và re-check Audit discrepancy

## Trạng thái và ownership

`CANONICAL — HUMAN APPROVED`

Owner: Phan Lê Nghi.

## User Story

Là Manager, tôi muốn review Audit discrepancy và bảo đảm discrepancy được re-check, để Adjust không được áp dụng tự động từ một mismatch chưa kiểm tra lại.

## Business value và scope

Story cover discrepancy/review context, mandatory re-check và no-auto-adjust guard. Story không tuyên bố Audit mismatch được closed hoặc completed.

## Traceability

- Requirements: `REQ-002`, `REQ-004`, `CAND-REQ-005`, `CAND-REQ-010`.
- Business rules: `CAND-BR-002`, `CAND-BR-010`.
- Evidence: `EVD-012`, `EVD-017` hỗ trợ current-state re-check.
- Human decisions: `DEC-014`, `DEC-017`.
- Open question: `OQ-013`.
- Source classification: verified evidence + HUMAN PRODUCT DECISION.

## Acceptance Criteria

### AC-AUD2-001 — Create discrepancy context

Given Audit result là mismatch, when result được ghi nhận, then discrepancy/review context được tạo.

### AC-AUD2-002 — Mandatory re-check

Given discrepancy/review context tồn tại, when discrepancy được xử lý tiếp, then re-check là bắt buộc trước khi Adjust được cân nhắc.

### AC-AUD2-003 — No automatic Adjust

Given Audit mismatch được ghi nhận, when Audit result được xử lý, then Audit không tự động apply Adjust.

## Remaining gaps và scope guards

- Audit mismatch completion vẫn `TBD / OQ-013`.
- Exact handoff sang Adjust ngoài các approved guards chưa được suy diễn.
