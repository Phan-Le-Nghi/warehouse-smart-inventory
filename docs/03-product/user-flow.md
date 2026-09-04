# User Flow — Bản phục vụ báo cáo

## Tổng quan quy trình đã xác nhận

`Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`

Đây là chuỗi các khu vực bắt buộc đã được giảng viên xác nhận, chưa phải interaction flow chi tiết và không xác nhận mọi mặt hàng hoặc giao dịch phải đi qua cả sáu khu vực trong một quy trình liên tục.

## Human-approved MVP context

- MVP quản lý một Warehouse duy nhất; multi-Warehouse và cross-Warehouse operation ngoài MVP (`DEC-005`).
- Internal location ở mức area-level gồm `Backroom` và `Sales Shelf`; một SKU có thể được ghi nhận tại nhiều internal locations trong cùng Warehouse (`CAND-REQ-003`, `DEC-006`).
- Putaway là initial placement sau Receive; Transfer là subsequent relocation giữa tracked internal locations trong cùng Warehouse; Pick là lấy quantity từ source internal location cho downstream purpose (`DEC-007`, `DEC-009`).
- Physical movement và Movement system record là hai khái niệm khác nhau. Không mặc định physical movement tạo system transaction/record, thay đổi Stock hoặc tự động cập nhật location.

Các mục trên là HUMAN PRODUCT DECISIONS / PRODUCT MODELING, không phải research findings.

## Người phụ trách và trạng thái User Story/flow

| Flow | Người phụ trách | Story/flow hiện tại |
|---|---|---|
| Receive | Nghĩa | `US-REC-001` — BA CONFIRMED; `AC-01` đến `AC-03`; flow DRAFT |
| Putaway | Nghi | `DRAFT-US-PUT-001`; cautious flow DRAFT |
| Pick | Thảo Ngân | `DRAFT-US-PICK-001`; flow DRAFT |
| Transfer | Ly Na | `DRAFT-US-TRF-001`; cautious flow DRAFT |
| Adjust | Thanh Ngân | `DRAFT-US-ADJ-001`; cautious flow DRAFT |
| Audit | Nghi sở hữu/hỗ trợ | `DRAFT-US-AUD-001`; cautious flow DRAFT |

Flow chi tiết đã duyệt trong tương lai sẽ là canonical trong `vault/04-product/user-flows/` và được liên kết tại đây. Các mục `DRAFT`, `TBD` và `OPEN QUESTION` bên dưới không phải hành vi sản phẩm đã được xác nhận.

---

## Receive — DRAFT flow

### Evidence boundary

- `US-REC-001` — BA CONFIRMED; `AC-01`, `AC-02`, `AC-03`.
- `CAND-REQ-001`: ghi nhận số lượng thực nhận và đối chiếu với số lượng kỳ vọng.
- `CAND-REQ-002`: ghi nhận chênh lệch giữa số lượng thực nhận và số lượng kỳ vọng.
- `CAND-BR-001`: khi có chênh lệch, ghi nhận Receive dùng số lượng thực nhận, không thay bằng số lượng kỳ vọng.
- `EVD-002` đến `EVD-005`: check item, đếm actual quantity, đối chiếu expected quantity và ghi nhận actual quantity khi chênh lệch.

### High-level flow

```text
Receive context
(trigger, precondition và actor: TBD / OQ-013, OQ-020)
  ↓
Check received item and count actual received quantity
  ↓
Compare actual quantity with expected quantity
(expected quantity source: TBD / OQ-019)
  ├─ Quantities equal
  │    ↓
  │  Record Receive using actual quantity
  └─ Quantities differ
       ↓
     Record Receive using actual quantity
     and record discrepancy
  ↓
Completion state and downstream handoff: TBD / OQ-013
```

### Scope guard

Flow này không xác nhận tra cứu lại Receive, approval, discrepancy reason, attachment, delivery-party handling UI, damaged goods, over-receive, cancellation, automatic stock update, barcode/scanner/mobile/offline, role permission hoặc auto-handoff sang Putaway.

### Open Questions được bảo tồn

- Receive trigger, precondition, success outcome, exception, completion state và downstream handoff: `OQ-013`.
- Nguồn số lượng kỳ vọng và vai trò Purchasing/Purchase Order: `OQ-019`.
- Role/authority có thể thực hiện hoặc ghi nhận Receive: `OQ-020`.

## Putaway — DRAFT cautious flow

### Evidence boundary

- `REQ-002`: Putaway là khu vực quy trình bắt buộc.
- `EVD-006`, `EVD-007`: minimart có backroom và sales shelf; sau Receive, hàng có thể được bố trí tại một trong hai khu vực.
- `EVD-008`: kiến thức vị trí hiện phụ thuộc nhiều vào bố trí thực tế và kinh nghiệm nhân viên.
- `EVD-010`, `EVD-011`: movement giữa hai khu vực tồn tại, nhưng cách hệ thống phân loại hoặc ghi nhận chưa được xác nhận.
- `EVD-019`: evidence chỉ phản ánh vận hành của minimart được nghiên cứu.
- `CAND-REQ-003` là `APPROVED — HUMAN PRODUCT DECISION` cho record/lookup area-level internal-location information; không quyết định quantity per location, Stock effect hoặc automatic location update.

### High-level flow

```text
Receive
  ↓
Putaway context
(trigger/precondition chính xác: TBD / OQ-013)
  ↓
Physical placement occurs
  ├─ Backroom
  └─ Sales shelf
  ↓
Record area-level location-related inventory information
(exact interaction and quantity semantics: TBD)
  ↓
Putaway completion criteria: TBD / OQ-013
  ↓
Downstream handoff: TBD / OQ-013
```

### Putaway/Transfer boundary

```text
Physical movement between backroom and sales shelf exists
  ↓
Initial placement = Putaway; subsequent relocation = Transfer
(HUMAN PRODUCT MODELING: DEC-007 / DEC-009)
  ↓
Transfer transaction / Movement system record / Stock effect: TBD
```

### Scope guard

Flow này xác nhận capability record/lookup area-level location information nhưng không xác nhận automatic assignment/update, quantity per location, quantity update, Movement system record, partial behavior, barcode/scanner/mobile interaction hoặc permission behavior. Multiple internal locations per SKU là product modeling đã duyệt; behavior chi tiết vẫn TBD.

### Open Questions được bảo tồn

- Putaway trigger, precondition, completion state và downstream handoff: `OQ-013`.
- Partial Putaway: `OQ-014`.
- Quantity có được duy trì theo internal location và aggregation: `OQ-011`.
- `OQ-016` đã được resolve bởi `DEC-007`; Transfer system behavior vẫn TBD.
- Role có thể thực hiện/xem Putaway: `OQ-020`.
- Putaway có ảnh hưởng Stock/Movement hay không: `TBD`.
- Barcode/QR/scanner/mobile/offline có thuộc phạm vi không: `OQ-022`.

## Pick — DRAFT flow

**Status:** `DRAFT / NEEDS HUMAN REVIEW`

**Owner:** Thảo Ngân

**Story:** `DRAFT-US-PICK-001`

**Source:** `vault/04-product/pick-draft.md`

### Evidence boundary

- `REQ-002`: Pick là khu vực quy trình bắt buộc.
- `EVD-006` đến `EVD-009`: backroom/sales shelf và kiến thức vị trí phụ thuộc bố trí thực tế/kinh nghiệm là current-state context, không phải Pick system behavior.
- Không có Business Rule đã duyệt trực tiếp xác định hành vi Pick.
- `CAND-REQ-003` là `APPROVED — HUMAN PRODUCT DECISION`; Pick boundary là lấy quantity từ source internal location theo `DEC-009`.

### Directed flow

```text
[TBD: Pick trigger — OQ-013]
        ↓
[Pick workflow area — CONFIRMED: REQ-002]
        ↓
[TBD: Identify item / quantity — OQ-011, OQ-013]
        ↓
[Pick boundary: take quantity from a source internal location — DEC-009]
        ↓
[TBD: Complete / record Pick — OQ-013]
        ↓
[TBD: Downstream purpose and impact — OQ-011, OQ-013]
```

### Scope guard

Flow không giả định barcode/scanner, FIFO/FEFO, reservation, stock reduction, Movement system record creation, Transfer system behavior, partial Pick hoặc quyền của role. Một SKU có thể được ghi nhận tại nhiều internal locations theo `DEC-006`; source-selection behavior vẫn TBD. `AC-PICK-001` trong Pick draft chỉ là scope-level và không phải functional Pick Acceptance Criterion.

### Open Questions được bảo tồn

- `system stock quantity` granularity, aggregation, workflow effect và change timing: `OQ-011`.
- Lot/batch, serial, expiry, UOM/conversion: `OQ-012`.
- Trigger, preconditions, outcome, exception và completion: `OQ-013`.
- Partial Pick: `OQ-014`.
- Negative stock: `OQ-015`.
- `OQ-016` đã resolved cho Transfer scope; Pick trigger, downstream purpose và system effects vẫn OPEN/TBD.
- Role/permission: `OQ-020`.
- Barcode/QR/scanner/mobile/offline/integration: `OQ-022`.

## Transfer — DRAFT cautious flow

**Status:** `DRAFT / NEEDS HUMAN REVIEW`

**Owner:** Ly Na

**Story:** `DRAFT-US-TRF-001`

**Source:** `vault/04-product/transfer-draft.md`

### Evidence boundary

- `REQ-002`: Transfer là khu vực quy trình bắt buộc.
- `REQ-004`: Movement và Transfer thuộc core domain; định nghĩa, quan hệ và behavior chi tiết vẫn TBD.
- `CAND-REQ-003`: area-level internal-location capability — `APPROVED — HUMAN PRODUCT DECISION`.
- `CAND-REQ-004`: đề xuất đánh giá hỗ trợ theo dõi movement giữa backroom và sales shelf; trạng thái vẫn `DRAFT`.
- `EVD-010`: có physical movement giữa backroom và sales shelf trong vận hành hiện tại.
- `EVD-011`: chưa xác nhận movement có được ghi nhận thành transaction riêng hay không.
- `EVD-019`: evidence chỉ phản ánh minimart được nghiên cứu.

### High-level flow

```text
[TBD: Transfer trigger and actor — OQ-013, OQ-020]
        ↓
[Transfer workflow area — CONFIRMED: REQ-002]
        ↓
[Evidence context: physical movement exists — EVD-010]
        ↓
[APPROVED MODELING BOUNDARY: subsequent relocation between tracked internal locations in one Warehouse — DEC-007 / DEC-009]
        ↓
[PROPOSED / TBD: system interaction or movement recording]
        ↓
[TBD: completion state, Stock effect, Movement behavior and handoff]
```

### Putaway/Transfer boundary

Theo HUMAN PRODUCT MODELING, initial placement sau Receive là Putaway và subsequent relocation giữa tracked internal locations là Transfer. Evidence chỉ xác nhận physical movement tồn tại; không xác nhận system Transfer transaction.

### Scope guard

Flow không xác nhận source/destination fields, Transfer/Movement transaction riêng, automatic Stock update, automatic location change, approval, rollback, partial Transfer, negative-stock behavior, device interaction hoặc permission.

### Open Questions được bảo tồn

- Transfer trigger, precondition, success outcome, exception và completion state: `OQ-013`.
- Partial Transfer: `OQ-014`.
- Negative stock handling: `OQ-015`.
- `OQ-016` đã `RESOLVED — HUMAN PRODUCT DECISION`; system Transfer transaction và behavior vẫn chưa được duyệt.
- Role có thể thực hiện/xem/sửa/xác nhận Transfer: `OQ-020`.
- Barcode/QR, scanner, mobile/offline và tích hợp bên ngoài: `OQ-022`.
- Transfer có tạo record hoặc ảnh hưởng Stock/location hay không: `TBD`.

## Adjust — DRAFT cautious flow

### Evidence boundary

- `REQ-002`: Adjust là khu vực quy trình bắt buộc; trigger, trạng thái và hành vi chi tiết vẫn TBD.
- `CAND-BR-002`: chênh lệch giữa tồn thực tế và tồn hệ thống phải được kiểm tra lại trước khi thực hiện điều chỉnh tồn.
- `EVD-012`, `EVD-017`: evidence trực tiếp cho nghĩa vụ re-check trước Adjust.
- `CAND-REQ-005` liên quan đến đối chiếu tồn trong Audit nhưng không xác nhận Audit là trigger hoặc dependency bắt buộc của Adjust.
- `EVD-013` là current-state evidence; không xác nhận role, permission, authority hoặc approval behavior của sản phẩm.

### High-level flow

```text
[TBD: source/trigger that identifies the discrepancy]
  ↓
Discrepancy between physical stock and system stock is identified
  ↓
Recheck discrepancy
  ↓
Perform stock adjustment
```

### Scope guard

Flow không xác nhận Audit tự động tạo Adjust, system behavior sau re-check, role/permission cụ thể, approval, reason, attachment/evidence, quantity validation, negative-stock handling, automatic Stock update hoặc edge case ngoài evidence hiện có.

### Open Questions được bảo tồn

- Nguồn/trigger xác định chênh lệch: `TBD`.
- Detailed recheck, completion, exception và adjustment mechanism: `OQ-013` / `TBD`.
- Reason, evidence và approval: `OQ-017`.
- Role/authority/permission: `OQ-020`.
- `system stock quantity` granularity, aggregation, workflow effect và change timing: `OQ-011`.
- Negative-stock handling: `OQ-015`.
- Anomaly/discrepancy definition và proof: `OQ-028`.

## Audit — DRAFT cautious flow

### Evidence boundary

- `REQ-002`: Audit là khu vực quy trình bắt buộc; ý nghĩa trình tự và quan hệ với các flow khác vẫn TBD.
- `REQ-004`: Audit thuộc core domain; định nghĩa, quan hệ, thuộc tính và hành vi vẫn TBD.
- `CAND-REQ-005`: sản phẩm nên hỗ trợ đối chiếu số lượng đếm thực tế với dữ liệu tồn trong hệ thống trong khu vực Audit; đã human reviewed.
- `EVD-015`, `EVD-016`: minimart được nghiên cứu kiểm kê hằng ngày bằng cách đếm/kiểm tra hàng thực tế và đối chiếu dữ liệu tồn.
- `CAND-BR-002`, `EVD-012`, `EVD-017`: chênh lệch phải được kiểm tra lại trước khi thực hiện điều chỉnh tồn.
- `EVD-013`, `EVD-014`: manager involvement/staff escalation là current-state evidence, không phải permission model.
- `EVD-019`: evidence không tạo quy tắc Audit hằng ngày cho mọi Warehouse.

### High-level flow

```text
Audit context begins
(trigger, actor, schedule và precondition: TBD / OQ-013, OQ-020)
  ↓
Physical inventory is checked/counted
(count scope và interaction: TBD)
  ↓
Physical count is compared with system inventory data
  ├─ Quantities match
  │    └─ Audit completion / next step: TBD / OQ-013
  └─ Discrepancy detected
       ↓
     Discrepancy must be re-checked before any inventory adjustment
       ↓
     Result after re-check / further handling / relationship to Adjust: TBD
```

### Evidence-supported discrepancy path

```text
Physical count differs from system inventory data
  ↓
Re-check is required
  ↓
Any later inventory adjustment may occur only after that re-check
  ↓
Exact handling, reason, evidence, approval, actor and outcome: TBD / OPEN QUESTION
```

### Scope guard

Flow không xác nhận Audit tự động thay đổi Stock, tự động tạo Adjust, tự động chuyển sang Adjust, hoặc áp dụng lịch hằng ngày cho mọi Warehouse.

### Open Questions được bảo tồn

- Trigger, precondition, success outcome, exception và completion state: `OQ-013`.
- Reason, evidence và approval cho Adjust/Audit: `OQ-017`.
- Audit là cycle count, full stocktake hay cả hai: `OQ-018`.
- Role permissions: `OQ-020`.
- Barcode/QR, scanner, mobile/offline và integration: `OQ-022`.
- Granularity/aggregation của `system stock quantity` dùng để đối chiếu: `OQ-011`.
- Count scope, lịch/tần suất sản phẩm, quan hệ Audit–Adjust và kết quả sau re-check: `TBD`.
