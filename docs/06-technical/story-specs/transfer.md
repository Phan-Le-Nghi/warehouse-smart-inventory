# Story Spec — Transfer / Movement Tracking

**Status:** DRAFT — product behavior approved; canonical story and technical contract review pending

**Story ID:** `DRAFT-US-TRF-001`

**Owner:** Ly Na

This spec records approved functional outcomes only. It does not choose architecture, data model, API, persistence technology, validation design or implementation. Round 2 decisions are HUMAN PRODUCT DECISIONS / MVP ASSUMPTIONS, not verified research findings.

## 1. Traceability

- Requirements: `REQ-002`, `REQ-004`, `CAND-REQ-003`, `CAND-REQ-004`.
- Business Rules: `CAND-BR-003`, `CAND-BR-007`, `CAND-BR-008`.
- Human decisions: `DEC-005`, `DEC-007`, `DEC-009`, `DEC-010`, `DEC-013`, `DEC-017`.
- Current-state evidence only: `EVD-010`, `EVD-011`, `EVD-019`.
- Open: `OQ-013` for Transfer exception/reversal, `OQ-014` for partial Transfer, `OQ-015` for negative stock, `OQ-022` for device/integration behavior.

`OQ-011`, `OQ-016` and `OQ-020` are resolved by HUMAN PRODUCT DECISIONS. Their resolution does not turn the supporting simulated input into verified research evidence.

## 2. Goal

Support subsequent relocation of a SKU between tracked internal locations in the same Warehouse, keep per-location quantities consistent and expose Transfer history for trace and discrepancy investigation.

Cross-Warehouse Transfer is outside MVP.

## 3. DRAFT User Story

> Là Warehouse Staff, tôi muốn ghi nhận Transfer của một SKU từ source internal location sang destination internal location, để location quantities được cập nhật nhất quán và Transfer history có thể được dùng cho trace và discrepancy investigation.

The story remains DRAFT until explicit human canonical review.

## 4. Approved functional inputs and outputs

### Minimum confirmed Transfer record

| Field | Approved meaning |
|---|---|
| SKU | SKU being relocated |
| quantity | Quantity transferred |
| source internal location | Tracked source within the MVP Warehouse |
| destination internal location | Tracked destination within the MVP Warehouse |
| confirmation timestamp | Time of Transfer confirmation |

This table defines product information requirements, not a database schema or API contract.

### History/query output

- source
- destination
- quantity
- time

Manager may view Transfer history. The approved purpose is trace and discrepancy investigation.

## 5. Approved happy path

1. A need exists for subsequent relocation between tracked internal locations.
2. Warehouse Staff identifies SKU, quantity, source and destination.
3. Physical relocation occurs and Warehouse Staff confirms Transfer.
4. Source `system stock quantity` decreases by Transfer quantity.
5. Destination `system stock quantity` increases by the same quantity.
6. Warehouse total quantity remains unchanged.
7. The system records SKU, quantity, source, destination and confirmation timestamp.
8. The record is available through Transfer history/query.

## 6. DRAFT Acceptance Criteria

### AC-TRF-001 — Quantity conservation

```gherkin
Given SKU, quantity, source internal location và destination internal location trong cùng Warehouse
When Warehouse Staff confirm Transfer
Then source quantity được giảm theo Transfer quantity
And destination quantity được tăng cùng quantity
And Warehouse total quantity không thay đổi
```

### AC-TRF-002 — Minimum Transfer record

```gherkin
Given một Transfer được confirm
When system Transfer record được ghi nhận
Then record chứa SKU, quantity, source internal location, destination internal location và confirmation timestamp
```

### AC-TRF-003 — Transfer history

```gherkin
Given confirmed Transfer records tồn tại
When Manager xem Transfer history
Then history cho phép xem source, destination, quantity và time
```

AC IDs remain DRAFT until canonical story review.

## 7. Unresolved behavior

- Transfer exception, cancellation, reversal and failed-confirmation behavior: `OQ-013`.
- Partial Transfer: `OQ-014`.
- Negative-stock behavior: `OQ-015`.
- Barcode/QR/scanner/mobile/offline/integration behavior: `OQ-022`.
- Validation details beyond the approved same-Warehouse/tracked-location boundary: TBD.

No unresolved behavior above may be inferred during implementation.

## 8. Technical boundary

- Architecture: TBD pending human approval.
- Data model: TBD pending human approval.
- API: TBD pending human approval.
- Authentication/authorization implementation: TBD; only the product permission outcome is approved.
- Implementation and tests: not started.

This spec is not implementation-ready until the story, AC and technical contract receive their required reviews.
