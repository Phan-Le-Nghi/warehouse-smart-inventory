# User Story và Acceptance Criteria — Mục lục

## Trạng thái

- Mục tiêu môn học: tổng cộng 8–12 User Story.
- User Story BA CONFIRMED hiện tại: **1** (`US-REC-001`).
- User Story DRAFT hiện tại: **5** (`DRAFT-US-PUT-001`, `DRAFT-US-PICK-001`, `DRAFT-US-TRF-001`, `DRAFT-US-ADJ-001`, `DRAFT-US-AUD-001`).
- Năm draft story đã được cập nhật theo HUMAN PRODUCT DECISIONS / MVP ASSUMPTIONS Round 2 và ở trạng thái `READY FOR HUMAN CANONICAL REVIEW`; chúng chưa canonical hoặc implementation-ready.

Không tạo User Story chỉ để đạt mục tiêu. Mỗi story mới phải trace tới Requirement/Business Rule đã duyệt và có Acceptance Criteria kiểm thử được.

## Ownership và trạng thái review

| Flow | Người phụ trách | Story ID | Trạng thái review |
|---|---|---|---|
| Receive | Nghĩa | `US-REC-001` | BA CONFIRMED; giữ canonical; proposed Round 2 additions chờ story review |
| Putaway | Nghi | `DRAFT-US-PUT-001` | DRAFT / READY FOR HUMAN CANONICAL REVIEW |
| Pick | Thảo Ngân | `DRAFT-US-PICK-001` | DRAFT / READY FOR HUMAN CANONICAL REVIEW |
| Transfer | Ly Na | `DRAFT-US-TRF-001` | DRAFT / READY FOR HUMAN CANONICAL REVIEW |
| Adjust | Thanh Ngân | `DRAFT-US-ADJ-001` | DRAFT / READY FOR HUMAN CANONICAL REVIEW |
| Audit | Nghi sở hữu/hỗ trợ | `DRAFT-US-AUD-001` | DRAFT / READY FOR HUMAN CANONICAL REVIEW |

## US-REC-001 — Ghi nhận Receive theo số lượng thực nhận

**Trạng thái:** `BA CONFIRMED`. `AC-01` đến `AC-03` được bảo tồn.

### User Story canonical hiện tại

> Là người thực hiện Receive, tôi muốn kiểm tra mặt hàng, ghi nhận số lượng thực nhận và đối chiếu với số lượng kỳ vọng, để số lượng Receive phản ánh hàng thực tế và chênh lệch được ghi nhận.

### Acceptance Criteria đã BA CONFIRMED

#### AC-01 — Ghi nhận và đối chiếu

Given một ngữ cảnh Receive có mặt hàng và số lượng kỳ vọng, when người thực hiện kiểm tra mặt hàng và nhập số lượng thực nhận, then hệ thống ghi nhận số lượng thực nhận và đối chiếu với số lượng kỳ vọng.

#### AC-02 — Nhận đủ

Given số lượng thực nhận bằng số lượng kỳ vọng, when Receive được ghi nhận, then số lượng Receive được ghi nhận bằng số lượng thực nhận.

#### AC-03 — Có chênh lệch

Given số lượng thực nhận khác số lượng kỳ vọng, when Receive được ghi nhận, then số lượng Receive được ghi nhận bằng số lượng thực nhận, không thay thế bằng số lượng kỳ vọng, và chênh lệch giữa hai số lượng được ghi nhận.

### Round 2 additions — proposed, chưa thay đổi canonical story

- Warehouse Staff thực hiện Receive (`DEC-017`).
- Expected quantity đến từ external/manual order or delivery reference do Purchasing cung cấp/chuẩn bị; full Purchase Order lifecycle ngoài MVP (`CAND-REQ-009`, `DEC-016`).
- Nếu system reference và document reference khác nhau, user phải review mismatch trước completion; system không tự chọn authoritative source (`CAND-BR-014`).
- Receive completion/handoff wording cuối vẫn `OQ-013 — PARTIALLY DECIDED / OPEN`.

## DRAFT-US-PUT-001 — Initial placement sau Receive

### DRAFT User Story

> Là Warehouse Staff, tôi muốn xác nhận SKU, quantity và destination internal location cho initial placement sau Receive, để quantity được phân bổ vào `Backroom` hoặc `Sales Shelf`.

### DRAFT Acceptance Criteria

#### AC-PUT-001 — Confirm destination allocation

```gherkin
Given SKU và quantity cần initial placement sau Receive
And destination là Backroom hoặc Sales Shelf
When Warehouse Staff confirm quantity và destination internal location
Then quantity được phân bổ vào destination internal location
```

#### AC-PUT-002 — Không tự tạo Transfer/Movement record

```gherkin
Given Putaway được confirm
When quantity được phân bổ vào destination internal location
Then Putaway không tự tạo Transfer hoặc Movement system record
```

Trace: `CAND-REQ-003`, `CAND-REQ-007`, `CAND-BR-003`, `CAND-BR-004`, `DEC-010`, `DEC-011`, `DEC-017`.

Remaining: exception/downstream handoff `OQ-013`; partial Putaway `OQ-014`; device behavior `OQ-022`.

**Trạng thái:** DRAFT / READY FOR HUMAN CANONICAL REVIEW.

## DRAFT-US-PICK-001 — Pick từ tracked internal locations

### DRAFT User Story

> Là Warehouse Staff, tôi muốn thực hiện Pick từ một Pick request có SKU và requested quantity, sử dụng một hoặc nhiều tracked internal locations khi cần, để cung cấp hàng cho downstream fulfilment/use và ghi nhận rõ trường hợp không đủ quantity.

### DRAFT Acceptance Criteria

#### AC-PICK-001 — Full Pick confirmation

```gherkin
Given một Pick request có SKU và requested quantity
And quantity được lấy từ một hoặc nhiều tracked source internal locations
When Warehouse Staff confirm full requested quantity
Then Pick được xem là fully completed
And confirmed quantity được giảm tại source internal location hoặc các source internal locations tương ứng
```

#### AC-PICK-002 — Multi-location Pick

```gherkin
Given một source internal location không có đủ requested quantity
And tracked internal location khác có quantity cho cùng SKU
When Warehouse Staff thực hiện Pick
Then requested quantity có thể được lấy từ nhiều tracked internal locations
```

#### AC-PICK-003 — Insufficient quantity

```gherkin
Given tổng quantity được lấy nhỏ hơn requested quantity
When Pick result được ghi nhận
Then Pick được ghi PARTIAL / INSUFFICIENT
And Pick không được xem là fully completed
And Manager có thể review exception
```

Trace: `CAND-REQ-003`, `CAND-REQ-006`, `CAND-BR-003`, `CAND-BR-005`, `CAND-BR-006`, `DEC-010`, `DEC-012`, `DEC-017`.

FIFO/FEFO/reservation/scanning ngoài MVP hiện tại. Negative-stock behavior vẫn `OQ-015`; cancellation/retry ngoài approved exception vẫn `OQ-013`.

**Trạng thái:** DRAFT / READY FOR HUMAN CANONICAL REVIEW.

## DRAFT-US-TRF-001 — Internal Transfer recording

### DRAFT User Story

> Là Warehouse Staff, tôi muốn ghi nhận Transfer của một SKU từ source internal location sang destination internal location, để location quantities được cập nhật nhất quán và Transfer history có thể được dùng cho trace và discrepancy investigation.

### DRAFT Acceptance Criteria

#### AC-TRF-001 — Confirm internal Transfer

```gherkin
Given SKU, quantity, source internal location và destination internal location trong cùng Warehouse
When Warehouse Staff confirm Transfer
Then source quantity được giảm theo Transfer quantity
And destination quantity được tăng cùng quantity
And Warehouse total quantity không thay đổi
```

#### AC-TRF-002 — Minimum Transfer record

```gherkin
Given một Transfer được confirm
When system Transfer record được ghi nhận
Then record chứa SKU, quantity, source internal location, destination internal location và confirmation timestamp
```

#### AC-TRF-003 — Transfer history

```gherkin
Given confirmed Transfer records tồn tại
When Manager xem Transfer history
Then history cho phép xem source, destination, quantity và time
```

Trace: `CAND-REQ-003`, `CAND-REQ-004`, `CAND-BR-003`, `CAND-BR-007`, `CAND-BR-008`, `DEC-007`, `DEC-013`, `DEC-017`.

Cross-Warehouse Transfer ngoài MVP. Partial Transfer `OQ-014`; negative stock `OQ-015`; exception/reversal `OQ-013`.

**Trạng thái:** DRAFT / READY FOR HUMAN CANONICAL REVIEW.

## DRAFT-US-ADJ-001 — Adjust request và approval

### DRAFT User Story

> Là Warehouse Staff, tôi muốn tạo Adjust request cho discrepancy đã được re-check và cung cấp reason, để Manager có thể approve hoặc reject trước khi bất kỳ thay đổi quantity nào được apply.

### DRAFT Acceptance Criteria

#### AC-ADJ-001 — Re-check và reason

```gherkin
Given một discrepancy/Adjust request
When Adjust được cân nhắc
Then discrepancy phải được re-check
And Adjust reason phải được ghi
```

#### AC-ADJ-002 — Approved Adjust

```gherkin
Given discrepancy đã được re-check
And Manager approve Adjust request
When Adjust được apply
Then system stock quantity tại affected internal location được cập nhật
```

#### AC-ADJ-003 — Không còn discrepancy

```gherkin
Given re-check không còn discrepancy
When case được xử lý
Then Adjust không được apply
And discrepancy case có thể close
```

#### AC-ADJ-004 — Manager reject

```gherkin
Given Manager reject Adjust request
When rejection được ghi nhận
Then system stock quantity không thay đổi
```

Attachment/evidence là optional trong MVP. Purchasing không có warehouse adjustment permission.

Trace: `CAND-REQ-008`, `CAND-REQ-010`, `CAND-BR-002`, `CAND-BR-011`, `CAND-BR-012`, `CAND-BR-013`, `DEC-015`, `DEC-017`.

Rejected-case closure vẫn `OQ-013`; negative-stock behavior vẫn `OQ-015`.

**Trạng thái:** DRAFT / READY FOR HUMAN CANONICAL REVIEW.

## DRAFT-US-AUD-001 — Selected-scope Audit

### DRAFT User Story

> Là Warehouse Staff, tôi muốn thực hiện selected-scope Audit bằng cách ghi physical count và so sánh với `system stock quantity`, để xác định kết quả match hoặc tạo discrepancy/review context khi mismatch.

### DRAFT Acceptance Criteria

#### AC-AUD-001 — Count và compare

```gherkin
Given selected Audit scope là một nhóm SKU/location hoặc toàn Warehouse
When Warehouse Staff ghi physical count
Then physical count được so sánh với system stock quantity tại scope/location tương ứng
And comparison result được ghi nhận
```

#### AC-AUD-002 — Match completion

```gherkin
Given Audit comparison result là match
When result được confirm
Then Audit có thể complete
```

#### AC-AUD-003 — Mismatch handling

```gherkin
Given Audit comparison result là mismatch
When result được ghi nhận
Then discrepancy/review context được tạo
And discrepancy phải được re-check
And Audit không tự động apply Adjust
```

Trace: `CAND-REQ-005`, `CAND-BR-002`, `CAND-BR-009`, `CAND-BR-010`, `DEC-010`, `DEC-014`, `DEC-017`.

Không canonicalize `cycle count`. Mismatch completion/schedule vẫn `OQ-013`; device behavior vẫn `OQ-022`.

**Trạng thái:** DRAFT / READY FOR HUMAN CANONICAL REVIEW.

## Candidate decomposition để đạt 8–12 stories

Các candidate sau chưa phải canonical backlog và cần review independent user value/testability:

1. Receive actual quantity và comparison.
2. Receive reference mismatch review.
3. Putaway initial location allocation.
4. Full Pick execution.
5. `PARTIAL / INSUFFICIENT` Pick review.
6. Internal Transfer execution/confirmation.
7. Transfer history lookup.
8. Selected-scope Audit count/compare.
9. Audit discrepancy/re-check context.
10. Adjust request, approval/rejection và apply.
