# User Flow — Bản phục vụ báo cáo

## Tổng quan quy trình đã xác nhận

`Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`

Đây là chuỗi các khu vực bắt buộc đã được giảng viên xác nhận, chưa phải interaction flow chi tiết.

## Người phụ trách User Story/flow

| Flow | Người phụ trách | Flow chi tiết |
|---|---|---|
| Receive | Nghĩa | DRAFT flow — `US-REC-001` (BA CONFIRMED), AC-01 đến AC-03 |
| Putaway | Nghi | DRAFT cautious flow; system interaction và completion criteria TBD |
| Pick | Thảo Ngân | TBD |
| Transfer | Ly Na | DRAFT cautious flow; trigger, scope, system interaction và completion criteria TBD |
| Adjust | Thanh Ngân | DRAFT cautious flow; trigger, role, re-check detail và completion criteria TBD |
| Audit | Nghi sở hữu/hỗ trợ | DRAFT cautious flow; trigger, scope, role và completion criteria TBD |

Flow chi tiết đã duyệt sẽ là canonical trong `vault/04-product/user-flows/` và được liên kết tại đây.

## Receive — DRAFT flow

### Evidence boundary

- `US-REC-001` — BA CONFIRMED; AC-01, AC-02, AC-03.
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
Exact system interaction: TBD
  ↓
Putaway completion criteria: TBD / OQ-013
  ↓
Downstream handoff: TBD / OQ-013
```

### Putaway/Transfer boundary

```text
Physical movement between backroom and sales shelf exists
  ↓
Classification as Putaway or Transfer: OPEN QUESTION / OQ-016
  ↓
System recording/tracking behavior: TBD
```

Flow này không xác nhận record/lookup location, automatic assignment, quantity update, Movement transaction, partial/multiple-location behavior, barcode/scanner/mobile interaction hoặc permission behavior.

### Open Questions được bảo tồn

- Putaway trigger, precondition, completion state và downstream handoff: `OQ-013`.
- Partial Putaway: `OQ-014`.
- Một SKU có thể tồn tại tại nhiều physical location: `OPEN QUESTION`; chưa có canonical Open Question ID được xác nhận.
- Putaway hay Transfer đối với movement giữa backroom và sales shelf: `OQ-016`.
- Role có thể thực hiện/xem Putaway: `OQ-020`.
- Putaway có ảnh hưởng Stock/Movement hay không: `TBD`.
- Barcode/QR/scanner/mobile/offline có thuộc phạm vi không: `OQ-022`.
## Transfer — DRAFT cautious flow

### Evidence boundary

* `REQ-002`: Transfer là một khu vực trong chuỗi quy trình bắt buộc `Receive → Putaway → Pick → Transfer → Adjust → Audit`.
* `REQ-004`: `Movement` và `Transfer` thuộc core domain; định nghĩa, quan hệ và behavior chi tiết vẫn TBD.
* `CAND-REQ-004`: đề xuất đánh giá việc hỗ trợ theo dõi movement giữa các khu vực lưu trữ; **DRAFT**.
* `EVD-010`: có hoạt động di chuyển hàng giữa backroom và sales shelf trong vận hành hiện tại.
* `EVD-011`: chưa xác nhận movement có được ghi nhận thành transaction riêng trong hệ thống hiện tại hay không.
* `EVD-019`: evidence chỉ phản ánh phạm vi nghiên cứu hiện tại và không nên khái quát cho mọi Warehouse.

### High-level flow

```text
Transfer context

(trigger, precondition và actor: TBD / OQ-013, OQ-020)

 ↓

Item/SKU cần di chuyển được xác định

(SKU validation: TBD)

 ↓

Source và destination được xác định

(location / warehouse scope: TBD / OQ-016)

 ↓

Physical movement occurs

 ↓

System interaction / movement recording: TBD

 ↓

Movement outcome / completion state: TBD / OQ-013

 ↓

Downstream inventory effect: TBD
```

Flow này chỉ phản ánh movement ở mức high-level. Không xác nhận movement bắt buộc phải được tạo thành Transfer transaction riêng, tự động cập nhật Stock hoặc tự động thay đổi Location.

### Putaway/Transfer boundary

```text
Physical movement between backroom and sales shelf exists

 ↓

Classification as Putaway or Transfer: OPEN QUESTION / OQ-016

 ↓

Transfer system recording/tracking behavior: TBD
```

Physical movement giữa backroom và sales shelf đã được evidence xác nhận, nhưng chưa đủ căn cứ để xác định mọi movement như vậy thuộc Transfer thay vì Putaway.

Flow không xác nhận Transfer bắt buộc giữa hai Warehouse, một SKU chỉ có một Location, hoặc Transfer luôn tạo Movement/Transfer record.

### Open Questions được bảo tồn

* Transfer trigger, precondition, success outcome, exception và completion state: `OQ-013`.
* Partial Transfer: `OQ-014`.
* Negative stock handling: `OQ-015`.
* Transfer giữa location, warehouse hay cả hai: `OQ-016`.
* Role có thể thực hiện/xem/sửa/xác nhận Transfer: `OQ-020`.
* Barcode/QR, scanner, mobile/offline và tích hợp bên ngoài: `OQ-022`.
* Transfer có tạo Movement/Transfer record hay không: `TBD`.
* Transfer có ảnh hưởng Stock/Location hay không: `TBD`.
* Quan hệ giữa Transfer và Putaway đối với movement giữa backroom và sales shelf: `OQ-016`.


## Audit — DRAFT cautious flow

### Evidence boundary

- `REQ-002`: Audit là khu vực quy trình bắt buộc; ý nghĩa trình tự và quan hệ với các flow khác vẫn TBD.
- `REQ-004`: Audit thuộc core domain; định nghĩa, quan hệ, thuộc tính và hành vi vẫn TBD.
- `CAND-REQ-005`: sản phẩm nên hỗ trợ đối chiếu số lượng đếm thực tế với dữ liệu tồn trong hệ thống trong khu vực Audit.
- `EVD-015`, `EVD-016`: minimart được nghiên cứu kiểm kê hằng ngày bằng cách đếm/kiểm tra hàng thực tế và đối chiếu với dữ liệu tồn trong KiotViet.
- `CAND-BR-002`, `EVD-012`, `EVD-017`: chênh lệch phải được kiểm tra lại trước khi thực hiện điều chỉnh tồn.
- `EVD-013`, `EVD-014`: manager tham gia và staff report/escalate trong vận hành hiện tại, nhưng đây không phải permission model của sản phẩm mới.
- `EVD-019`: evidence chỉ phản ánh vận hành của minimart được nghiên cứu và không tạo quy tắc Audit hằng ngày cho mọi Warehouse.

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

Nhánh “Quantities match” chỉ là nhánh logic tối thiểu của phép đối chiếu, không xác nhận completion state. Flow không xác nhận Audit tự động thay đổi Stock, tự động tạo Adjust, hoặc tự động chuyển sang Adjust.

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

Trong minimart được nghiên cứu, staff report/escalate chênh lệch và manager tham gia xử lý (`EVD-013`). Chi tiết này được giữ làm evidence context, không được dùng để gán quyền hệ thống khi `OQ-020` còn mở.

### Open Questions được bảo tồn

- Trigger, precondition, success outcome, exception và completion state của Audit: `OQ-013`.
- Lý do, bằng chứng và phê duyệt cho Adjust/Audit: `OQ-017`.
- Audit là cycle count, full stocktake hay cả hai: `OQ-018`.
- Quyền của Warehouse Staff, Manager, Purchasing và Admin: `OQ-020`.
- Barcode/QR, scanner, mobile/offline và tích hợp bên ngoài: `OQ-022`.
- Định nghĩa các loại dữ liệu tồn được dùng để đối chiếu: `OQ-011`.
- Phạm vi đếm, lịch/tần suất trong sản phẩm mới, quan hệ Audit–Adjust và kết quả sau re-check: `TBD`; không được resolve trong flow này.

## Adjust — DRAFT cautious flow

### Evidence boundary

- `REQ-002`: Adjust là khu vực quy trình bắt buộc; trigger, trạng thái và hành vi chi tiết vẫn TBD.
- `CAND-BR-002`: chênh lệch giữa tồn thực tế và tồn hệ thống phải được kiểm tra lại trước khi thực hiện điều chỉnh tồn.
- `EVD-012`, `EVD-017`: evidence trực tiếp cho nghĩa vụ re-check trước Adjust.
- `CAND-REQ-005` có liên quan đến đối chiếu tồn trong Audit, nhưng không xác nhận Audit là trigger hoặc dependency bắt buộc của Adjust.
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

### Open Questions được bảo tồn

- Nguồn/trigger xác định chênh lệch: `TBD`.
- Detailed recheck steps, completion state, exception handling và adjustment mechanism: `TBD` / `OQ-013`.
- Reason, evidence và approval requirements: `OPEN QUESTION` / `OQ-017`.
- Official role, authority và permission: `OPEN QUESTION` / `OQ-020`.
- Stock quantity definitions: `OPEN QUESTION` / `OQ-011`.
- Negative-stock handling: `OPEN QUESTION` / `OQ-015`.
- Anomaly/discrepancy definition và proof: `OPEN QUESTION` / `OQ-028`.

Flow này không xác nhận Audit tự động tạo Adjust, system behavior sau re-check, role/permission cụ thể, approval, reason, attachment/evidence, quantity validation, negative-stock handling, automatic stock update hoặc edge case Adjust.
