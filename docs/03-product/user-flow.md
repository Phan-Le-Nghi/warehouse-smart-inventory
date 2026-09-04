# User Flow — Bản phục vụ báo cáo

## Tổng quan

`Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`

Đây là chuỗi các khu vực workflow bắt buộc, không khẳng định mọi item hoặc transaction luôn đi qua sáu khu vực như một flow liên tục. Chi tiết Round 2 dưới đây là HUMAN PRODUCT DECISIONS / MVP ASSUMPTIONS, không phải verified research findings.

## MVP boundary

- Một Warehouse; cross-Warehouse operation ngoài MVP.
- Tracked internal locations: `Backroom`, `Sales Shelf`.
- `system stock quantity` duy trì theo internal location; Warehouse total bằng tổng location quantities.
- Full Purchase Order lifecycle ngoài MVP.
- FIFO/FEFO/reservation/scanning ngoài Pick MVP hiện tại.
- `OQ-013` giữ `PARTIALLY DECIDED / OPEN`; không suy diễn lifecycle gap.

## Receive — BA CONFIRMED story, lifecycle partially open

```text
Receive context
  ↓
Warehouse Staff checks item and counts actual quantity
  ↓
Compare actual quantity with external/manual expected quantity/reference
  ├─ Quantity discrepancy
  │    ↓
  │  Record actual quantity and discrepancy
  ├─ System/document reference mismatch
  │    ↓
  │  User reviews mismatch before completion
  │  System does not select an authoritative source
  └─ Match
       ↓
     Record actual quantity
  ↓
[Completion wording / exact Putaway handoff: PARTIALLY OPEN — OQ-013]
```

- Purchasing provides/views expected quantity/reference.
- Full Purchase Order lifecycle is outside MVP.
- `US-REC-001` remains BA CONFIRMED with `AC-01` to `AC-03`; Round 2 additions await explicit story review.

## Putaway — DRAFT

```text
Initial placement after Receive
  ↓
Input: SKU + quantity + destination internal location
  ↓
Warehouse Staff selects Backroom or Sales Shelf
  ↓
Confirm quantity and destination
  ↓
Allocate quantity to destination internal location
  ↓
Putaway complete for approved happy path
```

- Putaway does not automatically create Transfer or Movement system record.
- Exception/downstream handoff remains `OQ-013`; partial Putaway remains `OQ-014`.

## Pick — DRAFT

```text
Pick request: SKU + requested quantity
  ↓
Warehouse Staff selects one or more tracked source internal locations
  ↓
Take quantity and confirm result
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

Downstream module, FIFO/FEFO/reservation/scanning are outside the current Pick MVP. Negative-stock behavior remains `OQ-015`.

## Transfer — DRAFT

```text
Need for subsequent relocation between tracked internal locations
  ↓
Input: SKU + quantity + source + destination
  ↓
Warehouse Staff performs physical relocation and confirms Transfer
  ↓
Reduce source quantity + increase same destination quantity
  ↓
Warehouse total remains unchanged
  ↓
Create system Transfer record:
SKU + quantity + source + destination + confirmation timestamp
  ↓
Transfer history exposes source + destination + quantity + time
for trace/discrepancy investigation
```

- Manager may view Transfer history and review exception.
- Cross-Warehouse Transfer ngoài MVP.
- Partial Transfer `OQ-014`; negative stock `OQ-015`; exception/reversal `OQ-013`.

## Audit — DRAFT

```text
Start selected-scope Audit session
  ↓
Select group of SKU/location or whole Warehouse
  ↓
Warehouse Staff records physical count
  ↓
Compare with system stock quantity at selected scope/location
  ↓
Record comparison result
  ├─ Match
  │    ↓
  │  Confirm result → Audit may complete
  └─ Mismatch
       ↓
     Create discrepancy/review context
       ↓
     Mandatory re-check
       ↓
     No automatic Adjust
```

Không canonicalize `cycle count`. Mismatch completion và schedule vẫn `OQ-013`.

## Adjust — DRAFT

```text
Warehouse Staff creates discrepancy / Adjust request
  ↓
Mandatory re-check + required Adjust reason
(attachment/evidence optional)
  ├─ Re-check finds no discrepancy
  │    ↓
  │  Do not Adjust → case may close
  └─ Discrepancy remains
       ↓
     Manager reviews request
       ├─ Reject
       │    ↓
       │  Quantity does not change
       └─ Approve
            ↓
          Apply Adjust
            ↓
          Update system stock quantity at affected internal location
```

Rejected-case closure remains `OQ-013`. Purchasing has no warehouse adjustment permission.

## Permission summary

| Role | Approved MVP participation |
|---|---|
| Warehouse Staff | Receive, Putaway, Pick, Transfer, Audit count, create discrepancy/Adjust request |
| Manager | View operational records, review exceptions/discrepancy, approve/reject Adjust, view Transfer history, confirm/close sensitive exception flows |
| Purchasing | Provide/view Receive expected quantity/reference; no warehouse adjustment permission |
| Admin | Manage users, role assignments, basic system configuration; not required in daily warehouse operations |

## Story status

| Story | Status |
|---|---|
| `US-REC-001` | BA CONFIRMED; canonical wording preserved |
| `DRAFT-US-PUT-001` | DRAFT / READY FOR HUMAN CANONICAL REVIEW |
| `DRAFT-US-PICK-001` | DRAFT / READY FOR HUMAN CANONICAL REVIEW |
| `DRAFT-US-TRF-001` | DRAFT / READY FOR HUMAN CANONICAL REVIEW |
| `DRAFT-US-ADJ-001` | DRAFT / READY FOR HUMAN CANONICAL REVIEW |
| `DRAFT-US-AUD-001` | DRAFT / READY FOR HUMAN CANONICAL REVIEW |
