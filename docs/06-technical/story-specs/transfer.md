# Story Spec — Transfer / Movement Tracking

**Status:** DRAFT — Pending Product/BA review

**Story ID:** `DRAFT-US-TRF-001`

**Owner:** Ly Na

**Process:** Transfer

**Related workflow:** `Receive → Putaway → Pick → Transfer → Adjust → Audit`

---

## 1. Requirement & Evidence Traceability

### Requirement IDs

* `REQ-001` — Business problem: kiểm soát nhập, xuất, chuyển kho và tồn kho.
* `REQ-002` — Required workflow: `Receive → Putaway → Pick → Transfer → Adjust → Audit`.
* `REQ-004` — Core domain gồm `SKU`, `Warehouse`, `Stock`, `Movement`, `Transfer`, `Alert`, `Audit`; quan hệ và hành vi chi tiết còn TBD.
* `CAND-REQ-003` — Area-level internal-location recording/lookup với `Backroom` và `Sales Shelf`; một SKU có thể được ghi nhận tại nhiều internal locations trong cùng Warehouse; **APPROVED — HUMAN PRODUCT DECISION**.
* `CAND-REQ-004` — Đề xuất đánh giá việc hỗ trợ theo dõi movement giữa backroom và sales shelf; **DRAFT**.

### Human Product Decisions

* `DEC-005` — MVP quản lý một Warehouse duy nhất; multi-Warehouse ngoài MVP.
* `DEC-006` — MVP dùng area-level internal locations `Backroom` và `Sales Shelf`; một SKU có thể liên kết với nhiều internal locations.
* `DEC-007` — Transfer trong MVP chỉ nằm trong boundary subsequent relocation giữa tracked internal locations trong cùng Warehouse; cross-Warehouse Transfer ngoài MVP.
* `DEC-008` — Thuật ngữ Stock tối thiểu là `system stock quantity`; granularity, aggregation và effects vẫn OPEN.
* `DEC-009` — Phân biệt Physical movement với Movement system record; Transfer là subsequent internal relocation.

Các quyết định trên là product scope/modeling, không phải research findings. Chúng không duyệt functional Transfer transaction, Movement system record, Stock effect hoặc automatic location update.

### Evidence

* `EVD-010` — Có hoạt động di chuyển hàng giữa backroom và sales shelf trong vận hành hiện tại.
* `EVD-011` — Chưa xác nhận movement có được ghi nhận thành transaction riêng trong hệ thống hiện tại hay không.
* `EVD-019` — Evidence chỉ đến từ phạm vi nghiên cứu hiện tại và không nên khái quát cho mọi warehouse.

### Open Questions

* `OQ-013` — Trigger, precondition, success outcome, exception và completion state.
* `OQ-014` — Partial execution của các process.
* `OQ-015` — Negative stock.
* `OQ-020` — Quyền của Warehouse Staff / Manager / Purchasing / Admin.
* `OQ-022` — Barcode/QR/scanner/mobile/offline/external integration.

`OQ-011` là `PARTIALLY DECIDED / OPEN`. `OQ-016` là `RESOLVED — HUMAN PRODUCT DECISION`; system behavior vẫn chưa được duyệt.

---

## 2. Goal

Đánh giá system behavior, nếu có, để hỗ trợ subsequent relocation giữa tracked internal locations trong one-Warehouse MVP. Physical movement được quan sát trong evidence chỉ là current-state context.

Story này **không xác nhận** rằng hệ thống bắt buộc phải tạo một Transfer transaction riêng, tự động cập nhật Stock hoặc tự động thay đổi Location.

---

## 3. User Story

> Là người thực hiện xử lý hàng *(role cụ thể TBD)*, tôi muốn Product/BA đánh giá system behavior cho subsequent relocation giữa tracked internal locations, để quyết định recording hoặc query behavior nào thuộc Transfer flow.

---

## 4. Preconditions

Các điều kiện dưới đây hiện chưa được chốt hoàn toàn:

* SKU cần theo dõi phải tồn tại trong phạm vi dữ liệu của hệ thống — **TBD**.
* Khu vực nguồn và khu vực đích phải được xác định — **TBD**.
* Actor thực hiện Transfer và quyền truy cập — **TBD / OQ-020**.
* Boundary Transfer là subsequent relocation giữa tracked internal locations trong cùng một Warehouse — **HUMAN PRODUCT DECISION / DEC-007**; system fields và validation vẫn **TBD**.
* Điều kiện bắt đầu Transfer — **TBD / OQ-013**.

**Không giả định** rằng:

* `system stock quantity` được duy trì theo location;
* movement luôn là một transaction riêng;
* Transfer luôn làm thay đổi Stock;
* Transfer tự động thay đổi location information.

---

## 5. Happy Path

### Proposed flow — DRAFT

1. Người thực hiện xác định hàng cần di chuyển.
2. Người thực hiện xác định khu vực nguồn và khu vực đích.
3. Hệ thống/giải pháp ghi nhận hoặc hiển thị thông tin movement phù hợp với scope được BA/Product phê duyệt.
4. Người thực hiện theo dõi movement theo thông tin được Product/BA phê duyệt.
5. Người thực hiện có thể xác định movement đã được xử lý/ghi nhận theo behavior và completion state được phê duyệt.

**Lưu ý:** Bước 3–5 hiện chỉ là behavior đề xuất ở mức outcome. Cách ghi nhận, thông tin hiển thị, trạng thái và completion state chưa được chốt.

---

## 6. Alternate / Error Paths

### 6.1 Không xác định được khu vực nguồn hoặc đích

* Không được tự suy đoán location.
* Hệ thống cần xử lý theo behavior được BA xác nhận.
* **Validation/error behavior: TBD — OQ-013.**

### 6.2 SKU không xác định được

* Không được tạo/ghi nhận movement với SKU không xác định.
* Cách validation và thông báo lỗi: **TBD**.

### 6.3 Movement không hợp lệ

Ví dụ: nguồn và đích không phù hợp với phạm vi Transfer được phê duyệt.

* Không tự động quyết định validation/error behavior.
* Rule cụ thể: **TBD — OQ-013.**

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

### Human-approved product scope/modeling

* MVP có một Warehouse và area-level internal locations `Backroom` / `Sales Shelf` (`DEC-005`, `DEC-006`).
* Một SKU có thể liên kết với nhiều internal locations trong cùng Warehouse (`DEC-006`).
* Transfer là subsequent relocation giữa tracked internal locations trong cùng Warehouse; cross-Warehouse Transfer ngoài MVP (`DEC-007`, `DEC-009`).
* Physical movement không mặc định tạo Movement system record (`DEC-009`).

### Proposed

* Sản phẩm nên hỗ trợ theo dõi movement để giảm sự phụ thuộc vào việc biết vị trí hàng thông qua bố trí thực tế và kinh nghiệm người vận hành.

### Chưa được xác nhận

* Movement có phải transaction riêng hay không.
* Transfer có tạo record hay không.
* Transfer có cập nhật Stock hay không.
* Transfer có cập nhật Location hay không.
* Transfer có trạng thái hay không.
* Có cho phép partial Transfer hay không.
* Quy tắc xử lý negative stock khi Transfer được thực hiện.

`CAND-REQ-004` hiện vẫn là **DRAFT** và chỉ đề xuất đánh giá việc theo dõi movement; `EVD-011` cũng chưa xác nhận movement là transaction riêng.

---

## 8. Input

| Input                     | Status | Ghi chú                               |
| ------------------------- | ------ | ------------------------------------- |
| SKU                       | TBD    | Core domain                           |
| Source location/area      | TBD    | Boundary dùng tracked `Backroom`/`Sales Shelf`; system field/validation TBD |
| Destination location/area | TBD    | Boundary dùng tracked `Backroom`/`Sales Shelf`; system field/validation TBD |
| Quantity                  | TBD    | Chưa có requirement xác nhận behavior |
| Warehouse                 | Scope decided | Một Warehouse trong MVP (`DEC-005`); system field TBD |
| Actor/user                | TBD    | `OQ-020`                              |
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
* Khu vực/location hiện tại
* Thông tin stock liên quan — nếu được xác nhận

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
* System xử lý input ngoài one-Warehouse/internal-location scope như thế nào?
* Actor có quyền thực hiện không?

Các vấn đề này liên quan đến:

* `OQ-013` — Trigger/precondition/outcome/exception/completion.
* `OQ-014` — Partial execution.
* `OQ-015` — Negative stock.
* `DEC-005`, `DEC-007` — One-Warehouse và internal-location Transfer scope; validation behavior vẫn cần duyệt.
* `OQ-020` — Role/permission.

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

**Related OQ:** `OQ-013`.

### Test Case 03 — User không có quyền

**Given:** User không có permission Transfer.

**When:** User cố thực hiện operation yêu cầu quyền.

**Then:** Operation bị từ chối theo authorization rule được phê duyệt.

**Expected authorization behavior:** TBD.

**Related OQ:** `OQ-020`.

### Test Case 04 — Partial Transfer

**Given:** User yêu cầu chuyển một phần quantity.

**When:** Thực hiện Transfer.

**Then:** Kết quả phụ thuộc vào việc partial Transfer có được hỗ trợ hay không.

**Status:** OPEN — `OQ-014`.

### Test Case 05 — Cross-Warehouse request ngoài MVP

**Given:** Source và destination thuộc hai warehouse khác nhau.

**When:** User thực hiện Transfer.

**Then:** Không có functional behavior được quy định trong Story Spec này vì cross-Warehouse Transfer ngoài MVP; handling/validation vẫn TBD.

**Status:** SCOPE EXCLUDED by `DEC-005`, `DEC-007`; handling chưa được duyệt.

### Test Case 06 — Stock effect

**Given:** Có movement từ source sang destination.

**When:** Movement được xử lý.

**Then:** Việc Stock có thay đổi hay không phải khớp Data Model/API contract đã được phê duyệt.

**Status:** OPEN — phụ thuộc quyết định về Transfer behavior và Stock/negative-stock rules.

**Related OQ:** `OQ-015`.

---

## 16. Traceability

```text
REQ-001

 └── Business problem:
     Kiểm soát nhập/xuất/chuyển kho và tồn kho

REQ-002

 └── Required workflow:
     Receive → Putaway → Pick → Transfer → Adjust → Audit

         └── DRAFT-US-TRF-001

REQ-004

 └── Core domain:
     SKU / Warehouse / Stock / Movement / Transfer

         └── DRAFT-US-TRF-001

CAND-REQ-003 [APPROVED — HUMAN PRODUCT DECISION]

 └── Area-level internal-location capability
     + multiple internal locations per SKU

         └── Scope context for DRAFT-US-TRF-001

CAND-REQ-004 [DRAFT]

 └── Đề xuất đánh giá hỗ trợ theo dõi movement
     giữa backroom và sales shelf

         └── DRAFT-US-TRF-001

EVD-010

 └── Physical movement giữa backroom và sales shelf

         └── DRAFT-US-TRF-001

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

OQ-015

 └── Negative stock handling

DEC-005 / DEC-006 / DEC-007 / DEC-008 / DEC-009

 └── One Warehouse / area-level locations / internal Transfer boundary
     / system stock quantity terminology / Physical movement distinction

OQ-020

 └── Role / permission

OQ-022

 └── Barcode / QR / scanner / mobile / offline

```

Traceability hiện tại nối:

`REQ-002 + REQ-004 + CAND-REQ-003 + CAND-REQ-004 + DEC-005 + DEC-006 + DEC-007 + DEC-008 + DEC-009 + EVD-010 + EVD-011 + EVD-019`

tới `DRAFT-US-TRF-001`.

Các `OQ` được dùng trong validation/test cũng được trace tại đây để tránh tạo hoặc sử dụng Open Question ID không canonical.

---

## 17. Definition of Done

Story Spec này chỉ được xem là **Ready for Implementation** khi:

* [ ] Product/BA review `DRAFT-US-TRF-001`.
* [x] `CAND-REQ-004` được human review và giữ `DRAFT`; functional behavior chưa được duyệt.
* [ ] Trigger/precondition/outcome/exception/completion được chốt.
* [x] Transfer scope được chốt: subsequent relocation giữa tracked internal locations trong cùng Warehouse; cross-Warehouse ngoài MVP.
* [ ] Role & permission được chốt.
* [ ] Partial Transfer được chốt.
* [ ] Stock effect được chốt.
* [ ] Negative stock handling được chốt.
* [ ] Data Model liên quan được chốt.
* [ ] API contract được chốt.
* [ ] Acceptance Criteria được chuyển từ TBD/DRAFT sang testable criteria đã approved.
* [ ] Test cases được cập nhật theo behavior đã approved.
* [ ] Traceability `REQ → Story → Spec → Design/API/Data → Task/Test` hoàn chỉnh.
* [ ] Story đạt Definition of Ready trước khi bắt đầu code.

---

## 18. Scope Guard

Story Spec này **không xác nhận** các behavior sau:

* ❌ Tạo Transfer transaction riêng.
* ❌ Tự động cập nhật Stock.
* ❌ Tự động thay đổi Location.
* ❌ Cross-Warehouse Transfer trong MVP.
* ❌ User/role cụ thể được quyền Transfer.
* ❌ Barcode/QR/scanner/mobile/offline.
* ❌ Partial Transfer.
* ❌ Negative stock handling.

---

## 19. Acceptance Criteria — DRAFT

> **Status: DRAFT — Pending Product/BA review.**
>
> Các AC dưới đây là **candidate acceptance criteria** để Product/BA review, chưa phải acceptance criteria đã được approved.

### AC-01 — Track movement between areas

**Given** có movement hàng giữa source và destination thuộc phạm vi được phê duyệt.

**When** người dùng thực hiện hoặc tra cứu movement.

**Then** hệ thống/giải pháp phải cung cấp thông tin movement theo behavior được BA/Product phê duyệt.

**Status:** DRAFT.

### AC-02 — Invalid source/destination

**Given** source hoặc destination không hợp lệ hoặc không xác định.

**When** người dùng thực hiện Transfer.

**Then** hệ thống không xử lý movement như một movement hợp lệ.

**Status:** DRAFT — phụ thuộc `OQ-013` và validation behavior chưa được duyệt.

### AC-03 — Authorization

**Given** user không có quyền thực hiện operation Transfer.

**When** user cố thực hiện operation.

**Then** operation phải bị từ chối theo authorization rule được phê duyệt.

**Status:** DRAFT — phụ thuộc `OQ-020`.

### AC-04 — Partial Transfer

**Given** user yêu cầu chuyển một phần quantity.

**When** thực hiện Transfer.

**Then** behavior phải tuân theo quyết định về partial Transfer được Product/BA xác nhận.

**Status:** DRAFT — phụ thuộc `OQ-014`.

### AC-05 — Stock effect

**Given** movement được xử lý.

**When** Transfer hoàn tất theo behavior được phê duyệt.

**Then** bất kỳ thay đổi nào đối với Stock phải phù hợp với Data Model/API contract đã được phê duyệt.

**Status:** DRAFT — phụ thuộc quyết định về Stock effect và `OQ-015`.

---

## 20. Implementation Guard

Trước khi implementation:

* Không implement endpoint/API chưa được chốt.
* Không tự tạo Transfer/Movement entity hoặc transaction chỉ dựa trên tên story.
* Không tự động cập nhật Stock hoặc Location khi chưa có approved business rule.
* Không tự suy ra permission từ role name.
* Không biến `TBD`, `DRAFT`, `Proposed` hoặc `OPEN QUESTION` thành confirmed behavior.
* Mọi thay đổi behavior phải được trace ngược về Requirement/Evidence/Decision tương ứng.
