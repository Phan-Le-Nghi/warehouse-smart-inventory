# Transfer — Product Artifact Draft

## Status

`DRAFT / NEEDS HUMAN CANONICAL REVIEW`

This artifact reflects approved HUMAN PRODUCT DECISIONS / MVP ASSUMPTIONS from Round 2. Those decisions are not verified research findings. The story remains DRAFT until explicit canonical story review.

## Approved scope and sources

- `REQ-002`, `REQ-004`: Transfer is a required workflow area and a core domain concept.
- `CAND-REQ-003`: `system stock quantity` is maintained by tracked internal location.
- `CAND-REQ-004`: functional Transfer recording and history/query are approved HUMAN PRODUCT DECISIONS.
- `CAND-BR-007`: confirmed Transfer reduces source quantity, increases the same quantity at destination and does not change Warehouse total.
- `CAND-BR-008`: confirmed Transfer has a minimum system record.
- `DEC-005`, `DEC-007`, `DEC-009`, `DEC-010`, `DEC-013`, `DEC-017`: one-Warehouse boundary, Transfer modeling, quantity behavior, recording/history and permissions.
- `EVD-010`, `EVD-011` remain current-state context only; they do not verify the approved system behavior.

## DRAFT User Story

### DRAFT-US-TRF-001

> Là Warehouse Staff, tôi muốn ghi nhận Transfer của một SKU từ source internal location sang destination internal location, để location quantities được cập nhật nhất quán và Transfer history có thể được dùng cho trace và discrepancy investigation.

## DRAFT Acceptance Criteria

### AC-TRF-001 — Confirm internal Transfer

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

These AC IDs remain part of this DRAFT artifact until explicit canonical story review.

## High-level Transfer flow

```text
Need for subsequent relocation between tracked internal locations
  ↓
Warehouse Staff identifies SKU, quantity, source and destination
  ↓
Physical relocation + Transfer confirmation
  ↓
Reduce source quantity + increase same destination quantity
  ↓
Warehouse total remains unchanged
  ↓
Create system Transfer record
  ↓
Transfer history supports trace/discrepancy investigation
```

## Minimum record and query boundary

- Stored minimum: SKU, quantity, source internal location, destination internal location, confirmation timestamp.
- Query/history output: source, destination, quantity, time.
- Manager may view Transfer history and review exceptions.

## Scope guards and remaining questions

- Cross-Warehouse Transfer is outside MVP.
- Partial Transfer remains `OQ-014`.
- Negative-stock behavior remains `OQ-015`.
- Transfer exception, cancellation/reversal and failed-confirmation behavior remain `TBD / OQ-013`.
- No API, data model, persistence technology or architecture is defined here.

## Readiness

`READY FOR HUMAN CANONICAL REVIEW`; not promoted and not implementation-ready until that review occurs.
