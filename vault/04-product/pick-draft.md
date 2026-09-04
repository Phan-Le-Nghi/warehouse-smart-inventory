# Pick — Product Artifact Draft

## Status

`DRAFT / NEEDS HUMAN CANONICAL REVIEW`

This artifact reflects approved HUMAN PRODUCT DECISIONS / MVP ASSUMPTIONS from Round 2. Those decisions are not verified research findings. The draft ID and proposed Acceptance Criteria remain non-canonical until explicit story review.

## Approved scope and sources

- `REQ-002`: Pick is a required workflow area.
- `CAND-REQ-003`: `system stock quantity` is maintained by tracked internal location.
- `CAND-REQ-006`: Warehouse Staff performs Pick from a Pick request with SKU/requested quantity and may use one or more tracked internal locations.
- `CAND-BR-005`: confirmed Pick reduces quantity at the corresponding source location(s).
- `CAND-BR-006`: only full requested quantity is fully completed; insufficient quantity is `PARTIAL / INSUFFICIENT` and not fully complete.
- `DEC-010`, `DEC-012`, `DEC-017`: approved quantity model, Pick behavior and permission model.
- `EVD-006` to `EVD-009` remain current-state context only and do not verify the approved product behavior.

## DRAFT User Story

### DRAFT-US-PICK-001

> Là Warehouse Staff, tôi muốn thực hiện Pick từ một Pick request có SKU và requested quantity, sử dụng một hoặc nhiều tracked internal locations khi cần, để cung cấp hàng cho downstream fulfilment/use và ghi nhận rõ trường hợp không đủ quantity.

Downstream fulfilment/use is the approved purpose boundary; a downstream module is outside MVP.

## DRAFT Acceptance Criteria

### AC-PICK-001 — Full Pick confirmation

```gherkin
Given một Pick request có SKU và requested quantity
And quantity được lấy từ một hoặc nhiều tracked source internal locations
When Warehouse Staff confirm full requested quantity
Then Pick được xem là fully completed
And confirmed quantity được giảm tại source internal location hoặc các source internal locations tương ứng
```

### AC-PICK-002 — Multi-location Pick

```gherkin
Given một source internal location không có đủ requested quantity
And tracked internal location khác có quantity cho cùng SKU
When Warehouse Staff thực hiện Pick
Then requested quantity có thể được lấy từ nhiều tracked internal locations
```

### AC-PICK-003 — Insufficient quantity

```gherkin
Given tổng quantity được lấy nhỏ hơn requested quantity
When Pick result được ghi nhận
Then Pick được ghi `PARTIAL / INSUFFICIENT`
And Pick không được xem là fully completed
And Manager có thể review exception
```

These AC IDs remain part of this DRAFT artifact until explicit canonical story review.

## High-level Pick flow

```text
Pick request: SKU + requested quantity
  ↓
Warehouse Staff selects one or more tracked source internal locations
  ↓
Warehouse Staff takes quantity and confirms result
  ├─ Full requested quantity
  │    ↓
  │  Reduce source location quantity/quantities
  │    ↓
  │  Fully completed → downstream fulfilment/use
  └─ Insufficient quantity
       ↓
     Record PARTIAL / INSUFFICIENT
       ↓
     Not fully completed → Manager may review exception
```

## Scope guards and remaining questions

- FIFO, FEFO, reservation and scanning are outside the current MVP (`DEC-012`).
- Negative-stock behavior remains `OQ-015`.
- Device/integration behavior outside the approved Pick exclusions remains `OQ-022`.
- No Transfer or generic Movement system record is inferred from Pick.
- Exact cancellation/retry behavior beyond `PARTIAL / INSUFFICIENT` remains `TBD / OQ-013`.

## Readiness

`READY FOR HUMAN CANONICAL REVIEW`; not promoted and not implementation-ready until that review occurs.
