# US-TRF-002 — Xem Transfer history

## Trạng thái và ownership

`CANONICAL — HUMAN APPROVED`

Owner: Nguyễn Thị Ly Na.

## User Story

Là Manager, tôi muốn xem Transfer history, để trace relocation và hỗ trợ discrepancy investigation.

## Business value và scope

Story chỉ cover việc xem confirmed Transfer history và các thông tin output đã được duyệt; không định nghĩa filter, search algorithm hoặc technical query contract.

## Traceability

- Requirements: `REQ-002`, `REQ-003`, `REQ-004`, `FR-013`, `CAND-REQ-010`. Historical `CAND-REQ-004` was decomposed and superseded by `FR-012`/`FR-013`; it is not an active trace target.
- Business rule: `CAND-BR-008`.
- Human decisions: `DEC-013`, `DEC-017`, `DEC-024`.
- Open questions: `OQ-013`, `OQ-022`.
- Source classification: HUMAN PRODUCT DECISION / MVP ASSUMPTION. `EVD-010`, `EVD-011` chỉ là current-state context.

## Acceptance Criteria

### AC-TRF2-001 — View confirmed history

Given confirmed Transfer records tồn tại, when Manager mở Transfer history, then Manager có thể xem history.

### AC-TRF2-002 — History fields

Given một confirmed Transfer xuất hiện trong history, when Manager xem record, then source, destination, quantity và time được hiển thị.

### AC-TRF2-003 — Confirmation time

Given một Transfer có confirmation timestamp, when record được xem trong history, then displayed time phản ánh confirmation time của record.

## Remaining gaps và scope guards

- Transfer exception/reversal behavior vẫn `TBD / OQ-013`.
- Filter, sorting, export và device/integration behavior chưa được duyệt.
