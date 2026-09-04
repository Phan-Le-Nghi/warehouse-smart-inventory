# US-PUT-001 — Phân bổ Putaway vào initial location

## Trạng thái và ownership

`CANONICAL — HUMAN APPROVED`

Owner: Phan Lê Nghi.

## User Story

Là Warehouse Staff, tôi muốn xác nhận SKU, quantity và destination internal location cho initial placement sau Receive, để quantity được phân bổ vào `Backroom` hoặc `Sales Shelf`.

## Business value và scope

Story cover approved Putaway happy path: initial placement sau Receive vào một tracked internal location. Putaway không tự tạo Transfer hoặc Movement system record.

## Traceability

- Requirements: `REQ-002`, `REQ-003`, `REQ-004`, `CAND-REQ-003`, `CAND-REQ-007`, `CAND-REQ-010`.
- Business rules: `CAND-BR-003`, `CAND-BR-004`.
- Human decisions: `DEC-006`, `DEC-010`, `DEC-011`, `DEC-017`.
- Open questions: `OQ-013`, `OQ-014`, `OQ-022`.
- Source classification: HUMAN PRODUCT DECISION / MVP ASSUMPTION. `EVD-006`, `EVD-007` chỉ là current-state context và không verify product behavior này.

## Acceptance Criteria

### AC-PUT-001 — Confirm destination allocation

Given SKU và quantity cần initial placement sau Receive, when Warehouse Staff confirm destination là `Backroom` hoặc `Sales Shelf`, then quantity được phân bổ vào destination đã confirm.

### AC-PUT-002 — Tracked internal location

Given một MVP Putaway destination được chọn, when Putaway được confirm, then destination được ghi nhận ở mức tracked internal location `Backroom` hoặc `Sales Shelf`.

### AC-PUT-003 — Không tự tạo movement record

Given Putaway được confirm, when quantity được phân bổ, then Putaway không tự tạo Transfer hoặc Movement system record.

## Remaining gaps và scope guards

- Putaway exception và downstream handoff vẫn `TBD / OQ-013`.
- Partial Putaway vẫn `OQ-014`; device/integration behavior vẫn `OQ-022`.
- Không có AC về automatic Putaway handoff hoặc exception chưa được duyệt.
