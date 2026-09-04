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

## Receive — `US-REC-001`, lifecycle partially open

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
- Reference mismatch là AC/scenario của `US-REC-001`, không phải story riêng.
- Receive final completion và exact Putaway handoff vẫn `OQ-013`.

## Putaway — `US-PUT-001`

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

## Pick — `US-PICK-001`

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

`PARTIAL / INSUFFICIENT` là AC/scenario trong `US-PICK-001`, không phải story riêng.

## Transfer — `US-TRF-001` execution và `US-TRF-002` history

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
- `US-TRF-001` kết thúc tại execution/confirmation và minimum system record; `US-TRF-002` cover Manager history lookup.

## Audit — `US-AUD-001` count/compare và `US-AUD-002` discrepancy review

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

`US-AUD-001` cover selected scope, count, compare và match completion. `US-AUD-002` cover Manager review, mandatory re-check và no-auto-adjust guard; không khẳng định mismatch closure.

## Adjust — `US-ADJ-001` request và `US-ADJ-002` decision/apply

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

`US-ADJ-001` cover Warehouse Staff request/re-check/reason. `US-ADJ-002` cover Manager approve/reject và approved apply; không khẳng định rejected-case final closure.

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
| `US-REC-001` | CANONICAL — HUMAN APPROVED |
| `US-PUT-001` | CANONICAL — HUMAN APPROVED |
| `US-PICK-001` | CANONICAL — HUMAN APPROVED |
| `US-TRF-001` | CANONICAL — HUMAN APPROVED |
| `US-TRF-002` | CANONICAL — HUMAN APPROVED |
| `US-AUD-001` | CANONICAL — HUMAN APPROVED |
| `US-AUD-002` | CANONICAL — HUMAN APPROVED |
| `US-ADJ-001` | CANONICAL — HUMAN APPROVED |
| `US-ADJ-002` | CANONICAL — HUMAN APPROVED |
