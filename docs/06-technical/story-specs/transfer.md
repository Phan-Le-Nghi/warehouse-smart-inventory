# Story Spec — Transfer / Movement Tracking

**Status:** DRAFT — Pending Product/BA review
**Story ID:** `DRAFT-US-TRA-001`
**Owner:** Ly Na
**Process:** Transfer
**Related workflow:** `Receive → Putaway → Pick → Transfer → Adjust → Audit`

---

## 1. Requirement & Evidence Traceability

### Requirement IDs

* `REQ-001` — Business problem: kiểm soát nhập, xuất, chuyển kho và tồn kho.
* `REQ-002` — Required workflow: `Receive → Putaway → Pick → Transfer → Adjust → Audit`.
* `REQ-004` — Core domain gồm `SKU`, `Warehouse`, `Stock`, `Movement`, `Transfer`, `Alert`, `Audit`; quan hệ và hành vi chi tiết còn TBD.
* `CAND-REQ-004` — Đề xuất đánh giá việc hỗ trợ theo dõi movement giữa backroom và sales shelf; **DRAFT**.

### Evidence

* `EVD-010` — Có hoạt động di chuyển hàng giữa backroom và sales shelf trong vận hành hiện tại.
* `EVD-011` — Chưa xác nhận movement có được ghi nhận thành transaction riêng trong hệ thống hiện tại hay không.
* `EVD-019` — Evidence chỉ đến từ phạm vi nghiên cứu hiện tại và không nên khái quát cho mọi warehouse.

### Open Questions

* `OQ-013` — Trigger, precondition, success outcome, exception và completion state.
* `OQ-014` — Partial execution của các process.
* `OQ-016` — Transfer giữa location, warehouse hay cả hai.
* `OQ-020` — Quyền của Warehouse Staff / Manager / Purchasing / Admin.
* `OQ-022` — Barcode/QR/scanner/mobile/offline/external integration.

---

## 2. Goal

Hỗ trợ người thực hiện xử lý hàng **theo dõi việc di chuyển hàng giữa các khu vực lưu trữ**, dựa trên movement thực tế đã được quan sát trong evidence.

Story này **không xác nhận** rằng hệ thống bắt buộc phải tạo một Transfer transaction riêng, tự động cập nhật Stock hoặc tự động thay đổi Location.

---

## 3. User Story

> Là người thực hiện xử lý hàng *(role cụ thể TBD)*, tôi muốn theo dõi việc di chuyển hàng giữa các khu vực lưu trữ, để hỗ trợ kiểm soát movement hàng trong quá trình vận hành kho.

---

## 4. Preconditions

Các điều kiện dưới đây hiện chưa được chốt hoàn toàn:

* SKU cần theo dõi phải tồn tại trong phạm vi dữ liệu của hệ thống — **TBD**.
* Khu vực nguồn và khu vực đích phải được xác định — **TBD**.
* Actor thực hiện Transfer và quyền truy cập — **TBD / OQ-020**.
* Transfer giữa location hay warehouse — **TBD / OQ-016**.
* Điều kiện bắt đầu Transfer — **TBD / OQ-013**.

**Không giả định** rằng:

* một SKU chỉ có một location;
* movement luôn là một transaction riêng;
* Transfer luôn làm thay đổi Stock;
* Transfer luôn được thực hiện giữa hai warehouse.

---

## 5. Happy Path

### Proposed flow — DRAFT

1. Người thực hiện xác định hàng cần di chuyển.
2. Người thực hiện xác định khu vực nguồn và khu vực đích.
3. Hệ thống/giải pháp ghi nhận hoặc hiển thị thông tin movement phù hợp với scope được BA phê duyệt.
4. Movement được theo dõi với thông tin tối thiểu cần thiết.
5. Người thực hiện có thể xác định movement đã được xử lý/ghi nhận theo behavior được phê duyệt.

**Lưu ý:** Bước 3–5 hiện chỉ là behavior đề xuất ở mức outcome. Cách ghi nhận, trạng thái và completion state chưa được chốt.

---

## 6. Alternate / Error Paths

### 6.1 Không xác định được khu vực nguồn hoặc đích

* Không được tự suy đoán location.
* Hệ thống cần xử lý theo behavior được BA xác nhận.
* **Validation/error behavior: TBD — OQ-013/OQ-016.**

### 6.2 SKU không xác định được

* Không được tạo/ghi nhận movement với SKU không xác định.
* Cách validation và thông báo lỗi: **TBD**.

### 6.3 Movement không hợp lệ

Ví dụ: nguồn và đích không phù hợp với phạm vi Transfer được phê duyệt.

* Không tự động quyết định đây là lỗi location hay warehouse.
* Rule cụ thể: **TBD — OQ-016.**

### 6.4 Người dùng không có quyền

* Không xác nhận quyền cụ thể cho Warehouse Staff/Manager/Purchasing/Admin.
* Authorization behavior: **TBD — OQ-020.**

### 6.5 Partial Transfer

* Chưa xác nhận Transfer có hỗ trợ partial execution hay không.
* **TBD — OQ-014.**

---

## 7. Business Behavior

### Confirmed / Evidence-backed

* Trong vận hành hiện tại có movement hàng giữa **backroom và sales shelf** (`EVD-010`).
* Movement là một phần của chuỗi nghiệp vụ có `Transfer` (`REQ-002`).
* `Movement` và `Transfer` thuộc core domain (`REQ-004`).

### Proposed

* Sản phẩm nên hỗ trợ theo dõi movement để giảm sự phụ thuộc vào việc biết vị trí hàng thông qua bố trí thực tế và kinh nghiệm người vận hành.

### Chưa được xác nhận

* Movement có phải transaction riêng hay không.
* Transfer có tạo record hay không.
* Transfer có cập nhật Stock hay không.
* Transfer có cập nhật Location hay không.
* Transfer giữa location, warehouse hay cả hai.
* Transfer có trạng thái hay không.
* Có cho phép partial Transfer hay không.

`CAND-REQ-004` hiện vẫn là DRAFT và chỉ đề xuất đánh giá việc theo dõi movement; `EVD-011` cũng chưa xác nhận movement là transaction riêng.

---

## 8. Input

| Input                     | Status | Ghi chú                               |
| ------------------------- | ------ | ------------------------------------- |
| SKU                       | TBD    | Core domain                           |
| Source location/area      | TBD    | Evidence hiện có backroom/sales shelf |
| Destination location/area | TBD    | Evidence hiện có backroom/sales shelf |
| Quantity                  | TBD    | Chưa có requirement xác nhận behavior |
| Warehouse                 | TBD    | OQ-016                                |
| Actor/user                | TBD    | OQ-020                                |
| Movement time             | TBD    | Chưa có requirement                   |
| Reason                    | TBD    | Chưa có requirement                   |

**Không chốt field nào là mandatory cho đến khi BA/Product xác nhận.**

---

## 9. Output

Output dự kiến ở mức outcome:

* Thông tin movement được theo dõi/tra cứu theo behavior được phê duyệt.
* Có thể xác định hàng đã di chuyển từ khu vực nguồn sang khu vực đích nếu behavior này được BA xác nhận.

Các field cụ thể của output, status và transaction ID: **TBD**.

---

## 10. Data Read / Write

### Data có liên quan

* `SKU`
* `Warehouse`
* `Stock`
* `Movement`
* `Transfer`

Các entity trên thuộc core domain, nhưng quan hệ và behavior chi tiết vẫn TBD.

### Proposed data flow

**Read:**

* SKU
* khu vực/location hiện tại
* thông tin stock liên quan — nếu được xác nhận

**Write:**

* Movement/Transfer record — **TBD**
* Location change — **TBD**
* Stock quantity change — **TBD**

> Không được implement write operation dựa trên phần Proposed này trước khi API/Data Model được BA/Engineering chốt.

---

## 11. API Contract

**Status: TBD**

Chưa có API contract được phê duyệt cho Transfer.

Không tự tạo endpoint như:

`POST /api/transfers`

hoặc

`GET /api/transfers`

chỉ dựa trên tên User Story.

API cần được xác định sau khi:

1. BA chốt Transfer behavior.
2. Engineering chốt Data Model.
3. API contract được thống nhất.

API cần làm rõ khi được chốt:

* Endpoint
* HTTP method
* Authentication/authorization
* Request schema
* Response schema
* Validation errors
* Business errors
* Idempotency/concurrency nếu cần
* Audit/logging behavior

---

## 12. Authorization

**Status: TBD — OQ-020**

Các role tối thiểu của hệ thống gồm:

* Warehouse Staff
* Manager
* Purchasing
* Admin

Nhưng evidence hiện tại chưa đủ để xác nhận role nào được:

* tạo Transfer;
* xem Transfer;
* sửa/hủy Transfer;
* xác nhận Transfer.

Không được suy ra permission model từ việc Manager tham gia xử lý discrepancy trong research.

---

## 13. Validation

### Validation đã có căn cứ

Chưa có validation rule cụ thể nào được phê duyệt trực tiếp cho Transfer.

### Validation cần BA/Product xác nhận

* SKU có tồn tại không?
* Source location có tồn tại không?
* Destination location có tồn tại không?
* Source và destination có được phép khác nhau không?
* Quantity có bắt buộc không?
* Quantity có được vượt Stock không?
* Có cho phép partial Transfer không?
* Có cho phép negative stock không?
* Transfer giữa warehouse có được phép không?
* Actor có quyền thực hiện không?

Các vấn đề này liên quan đến `OQ-013`, `OQ-014`, `OQ-015`, `OQ-016` và `OQ-020`.

---

## 14. Observability / Audit Logging

**TBD**

Chưa có requirement xác nhận:

* Transfer/Movement có tạo audit log hay không;
* log gồm actor/time/source/destination/quantity hay không;
* có cần correlation ID hay transaction ID hay không.

Nếu sau này Transfer được xác nhận là transaction nghiệp vụ, các yêu cầu audit/logging cần được chốt trong Technical Design.

---

## 15. Test Plan

### Test Case 01 — Theo dõi movement giữa hai khu vực

**Given:** Có movement hàng giữa hai khu vực được phép.
**When:** Người dùng thực hiện/tra cứu movement theo behavior đã được phê duyệt.
**Then:** Movement được hiển thị/ghi nhận đúng theo scope.

**Status:** DRAFT — phụ thuộc behavior được BA xác nhận.

### Test Case 02 — Không xác định được source/destination

**Given:** Source hoặc destination không hợp lệ/không xác định.
**When:** Người dùng thực hiện Transfer.
**Then:** Hệ thống không xử lý movement như một movement hợp lệ.

**Expected validation message:** TBD.

### Test Case 03 — User không có quyền

**Given:** User không có permission Transfer.
**When:** User cố thực hiện operation yêu cầu quyền.
**Then:** Operation bị từ chối.

**Expected authorization behavior:** TBD.

### Test Case 04 — Partial Transfer

**Given:** User yêu cầu chuyển một phần quantity.
**When:** Thực hiện Transfer.
**Then:** Kết quả phụ thuộc vào việc partial Transfer có được hỗ trợ hay không.

**Status:** OPEN — `OQ-014`.

### Test Case 05 — Transfer giữa warehouse

**Given:** Source và destination thuộc hai warehouse khác nhau.
**When:** User thực hiện Transfer.
**Then:** Kết quả phụ thuộc scope Transfer được xác nhận.

**Status:** OPEN — `OQ-016`.

### Test Case 06 — Stock effect

**Given:** Có movement từ source sang destination.
**When:** Movement được xử lý.
**Then:** Việc Stock có thay đổi hay không phải khớp Data Model/API contract đã được phê duyệt.

**Status:** OPEN.

---

## 16. Traceability

```text
REQ-001
  └── Business problem:
      Kiểm soát nhập/xuất/chuyển kho và tồn kho

REQ-002
  └── Required workflow:
      Receive → Putaway → Pick → Transfer → Adjust → Audit
          └── DRAFT-US-TRA-001

REQ-004
  └── Core domain:
      SKU / Warehouse / Stock / Movement / Transfer
          └── DRAFT-US-TRA-001

CAND-REQ-004 [DRAFT]
  └── Đề xuất đánh giá hỗ trợ theo dõi movement
      giữa backroom và sales shelf
          └── DRAFT-US-TRA-001

EVD-010
  └── Physical movement giữa backroom và sales shelf
      └── DRAFT-US-TRA-001

EVD-011
  └── Chưa xác nhận movement là transaction riêng
      └── Scope guard / TBD

EVD-019
  └── Research limitation
      └── Không generalize ngoài evidence hiện có

OQ-013
  └── Trigger / precondition / outcome / exception / completion

OQ-014
  └── Partial execution

OQ-016
  └── Location vs Warehouse scope

OQ-020
  └── Role / permission

OQ-022
  └── Barcode / QR / scanner / mobile / offline
```

Traceability hiện tại cũng đã nối `REQ-002 + REQ-004 + CAND-REQ-004 + EVD-010 + EVD-011 + EVD-019` tới `DRAFT-US-TRA-001`.

---

## 17. Definition of Done

Story Spec này chỉ được xem là **Ready for Implementation** khi:

* [ ] Product/BA review `DRAFT-US-TRA-001`.
* [ ] `CAND-REQ-004` được human review.
* [ ] Trigger/precondition/outcome/exception/completion được chốt.
* [ ] Transfer scope được chốt: location / warehouse / both.
* [ ] Role & permission được chốt.
* [ ] Partial Transfer được chốt.
* [ ] Stock effect được chốt.
* [ ] Data Model liên quan được chốt.
* [ ] API contract được chốt.
* [ ] Acceptance Criteria được chuyển từ TBD sang testable criteria.
* [ ] Test cases được cập nhật theo behavior đã approved.
* [ ] Traceability `REQ → Story → Spec → Design/API/Data → Task/Test` hoàn chỉnh.
* [ ] Story đạt Definition of Ready trước khi bắt đầu code.

---

## 18. Scope Guard

Story Spec này **không xác nhận** các behavior sau:

* ❌ Tạo Transfer transaction riêng.
* ❌ Tự động cập nhật Stock.
* ❌ Tự động thay đổi Location.
* ❌ Transfer bắt buộc giữa hai Warehouse.
* ❌ Một SKU chỉ có một Location.
* ❌ User/role cụ thể được quyền Transfer.
* ❌ Barcode/QR/scanner/mobile/offline.
* ❌ Partial Transfer.
* ❌ Negative stock handling.
## Acceptance Criteria

> Status: DRAFT — Pending Product/BA review

### AC-01 — Track movement between areas
**Given** có movement hàng giữa source và destination thuộc phạm vi được phê duyệt  
**When** người dùng thực hiện hoặc tra cứu movement  
**Then** hệ thống/giải pháp phải cung cấp thông tin movement theo behavior được BA/Product phê duyệt.

### AC-02 — Invalid source/destination
**Given** source hoặc destination không hợp lệ hoặc không xác định  
**When** người dùng thực hiện Transfer  
**Then** hệ thống không xử lý movement như một movement hợp lệ.

### AC-03 — Authorization
**Given** user không có quyền thực hiện operation Transfer  
**When** user cố thực hiện operation  
**Then** operation phải bị từ chối theo authorization rule được phê duyệt.

### AC-04 — Partial Transfer
**Given** user yêu cầu chuyển một phần quantity  
**When** thực hiện Transfer  
**Then** behavior phải tuân theo quyết định về partial Transfer được Product/BA xác nhận.

### AC-05 — Stock effect
**Given** movement được xử lý  
**When** Transfer hoàn tất theo behavior được phê duyệt  
**Then** bất kỳ thay đổi nào đối với Stock phải phù hợp với Data Model/API contract đã được phê duyệt.
Các điểm trên phải được giải quyết bằng requirement/business decision tương ứng trước khi implementation.
