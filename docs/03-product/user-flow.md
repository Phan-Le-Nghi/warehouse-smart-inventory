# Consolidated User Flow — Warehouse & Smart Inventory Management

## Status and interpretation

`BASELINE FOR REPORT ROUND 1 — HUMAN APPROVED PRODUCT DEFINITION`

`Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit` tại `REQ-002` là danh sách sáu workflow/capability bắt buộc, không phải một transaction bắt buộc tuần tự qua cả sáu bước. Consolidated flow tuân theo `DEC-018`:

- Receive có thể dẫn tới Putaway.
- Sau Putaway, Pick và Transfer là các operational path độc lập.
- Audit chạy trên inventory theo selected scope và không bắt buộc xảy ra sau Pick hoặc Transfer.
- Audit mismatch tạo discrepancy context, bắt buộc re-check và chỉ khi discrepancy vẫn còn thì Adjust mới có thể được cân nhắc.
- Audit không auto Adjust.

## MVP boundary

- Một Warehouse; tracked locations là `Backroom` và `Sales Shelf`.
- `system stock quantity` duy trì theo location; Warehouse total bằng tổng location quantities.
- Quantity tại internal location không được âm.
- Full Purchase Order lifecycle, multi-Warehouse và cross-Warehouse operations ngoài MVP.
- FIFO/FEFO/reservation và Pick scanning ngoài Pick MVP hiện tại.
- Lifecycle chưa quyết định vẫn mang marker `OPEN`.

## Consolidated flow

```text
PURCHASING — supporting role
Provide/view external or manual expected quantity/reference
  │
  ▼
RECEIVE — Warehouse Staff — US-REC-001
Check item + record actual quantity + compare expected quantity/reference
  ├─ Quantity match
  │    └─ Record actual Receive quantity
  ├─ Quantity discrepancy
  │    └─ Record actual quantity + discrepancy
  └─ System/document reference mismatch
       └─ User review required before completion
          System does not choose authoritative source
  │
  ▼
[Receive final completion / exact Putaway handoff: OPEN — OQ-013]
  │
  ▼
PUTAWAY — Warehouse Staff — US-PUT-001
Confirm SKU + quantity + initial destination
  ├─ Backroom
  └─ Sales Shelf
  │
  └─ Allocate quantity to confirmed destination
     No automatic Transfer/Movement system record
  │
  ▼
[Putaway exception/downstream handoff: OPEN — OQ-013]

After Putaway, inventory may support independent operational paths:

PICK OPERATIONAL PATH — Warehouse Staff — US-PICK-001
Pick request: SKU + requested quantity
  ↓
Select one or more source locations
  ↓
Validate confirmed quantity against total quantity at selected sources
  ├─ Would create negative source quantity
  │    └─ Do not confirm; do not apply quantity change
  │       Report operation invalid / unable to confirm
  │       [Retry/cancel lifecycle: OPEN]
  └─ Validation passes
       ↓
     Confirm picked quantity and reduce selected-source quantities
       ├─ Full requested quantity
       │    └─ Fully completed
       │       Downstream fulfilment/use is outside MVP
       └─ Less than requested quantity
            └─ Record PARTIAL / INSUFFICIENT
               Not fully completed; Manager may review

TRANSFER OPERATIONAL PATH — Warehouse Staff — US-TRF-001
Need subsequent relocation within the same Warehouse
  ↓
Input SKU + quantity + source + destination
  ↓
Validate Transfer quantity against source location quantity
  ├─ Would create negative source quantity
  │    └─ Do not confirm; do not apply quantity change
  │       Report operation invalid / unable to confirm
  │       [Retry/cancel lifecycle: OPEN]
  └─ Validation passes
       ↓
     Confirm Transfer
       ├─ Reduce source quantity
       ├─ Increase same destination quantity
       ├─ Warehouse total remains unchanged
       └─ Create record: SKU + quantity + source + destination
          + confirmation timestamp
              │
              ▼
        TRANSFER HISTORY — Manager — US-TRF-002
        View source + destination + quantity + confirmation time
        for trace/discrepancy investigation

AUDIT — Warehouse Staff — US-AUD-001
May start on inventory independently of Pick/Transfer order
  ↓
Select group of SKU/location or whole Warehouse
  ↓
Record physical count
  ↓
Compare with system stock quantity at selected scope/location
  ↓
Record result
  ├─ Match
  │    └─ Confirm result → Audit may complete
  └─ Mismatch
       └─ Create discrepancy/review context
          │
          ▼
AUDIT REVIEW — Manager — US-AUD-002
Mandatory re-check
No automatic Adjust
  ├─ Re-check finds no discrepancy
  │    └─ Do not Adjust; quantity unchanged; case may close
  └─ Discrepancy remains
       └─ Adjust may be considered
          │
          ▼
ADJUST REQUEST — Warehouse Staff — US-ADJ-001
Record required reason
Attachment/evidence optional
Quantity remains unchanged while awaiting Manager decision
          │
          ▼
MANAGER DECISION — US-ADJ-002
  ├─ Reject
  │    └─ Quantity unchanged
  │       [Rejected-case final closure: OPEN — OQ-013]
  └─ Approve
       ↓
     Validate resulting affected-location quantity
       ├─ Result would be negative
       │    └─ Do not apply Adjust; quantity unchanged
       │       Report operation invalid / unable to confirm
       │       [Retry/cancel lifecycle: OPEN]
       └─ Result is not negative
            └─ Apply Adjust
               Update affected-location system stock quantity
```

## Story-to-flow mapping

| Flow step / branch | Story | Acceptance Criteria |
|---|---|---|
| Receive input/compare | `US-REC-001` | `AC-01` |
| Receive quantity match | `US-REC-001` | `AC-02` |
| Receive quantity discrepancy | `US-REC-001` | `AC-03` |
| Receive reference mismatch | `US-REC-001` | `AC-04` |
| Putaway allocation/tracked destination | `US-PUT-001` | `AC-PUT-001/002` |
| Putaway no automatic Movement record | `US-PUT-001` | `AC-PUT-003` |
| Full/multi-location Pick | `US-PICK-001` | `AC-PICK-001/002` |
| `PARTIAL / INSUFFICIENT` Pick | `US-PICK-001` | `AC-PICK-003` |
| Pick negative-stock guard | `US-PICK-001` | `AC-PICK-004` |
| Transfer effects/total/record | `US-TRF-001` | `AC-TRF1-001/002/003` |
| Transfer negative-stock guard | `US-TRF-001` | `AC-TRF1-004` |
| Transfer history | `US-TRF-002` | `AC-TRF2-001/002/003` |
| Audit scope/count/compare/result | `US-AUD-001` | `AC-AUD1-001/002/003` |
| Audit match completion | `US-AUD-001` | `AC-AUD1-004` |
| Audit mismatch/re-check/no-auto-Adjust | `US-AUD-002` | `AC-AUD2-001/002/003` |
| Adjust request/reason/re-check/attachment/no pre-decision change | `US-ADJ-001` | `AC-ADJ1-001/002/003/004` |
| Approve/reject/no-discrepancy outcomes | `US-ADJ-002` | `AC-ADJ2-001/002/003` |
| Adjust negative-stock guard | `US-ADJ-002` | `AC-ADJ2-004` |

## Permission coverage

| Role | Flow participation |
|---|---|
| Warehouse Staff | Receive, Putaway, Pick, Transfer, Audit count, Adjust request |
| Manager | Operational record/exception review, Transfer history, Audit discrepancy review, Adjust decision |
| Purchasing | Supporting role: provide/view Receive expected quantity/reference; no warehouse adjustment permission |
| Admin | Manage users, role assignments, basic system configuration; no mandatory daily operational path |

## Preserved open boundaries

- `OQ-013`: Receive completion/handoff, Putaway exception/handoff, Transfer exception/reversal, Audit mismatch completion, Adjust rejected-case closure và other unapproved lifecycle gaps.
- `OQ-014`: partial Receive, Putaway và Transfer.
- `OQ-021`: Alert behavior; no Alert story.
- `OQ-022`: device/integration behavior.
- Retry/cancel lifecycle sau negative-stock validation không được quyết định bởi `DEC-019`.
- AI directions remain open/future and have no canonical MVP story.
