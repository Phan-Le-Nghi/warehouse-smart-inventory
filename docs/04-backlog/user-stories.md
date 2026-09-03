# User Story và Acceptance Criteria — Mục lục

## Trạng thái

- Mục tiêu môn học: tổng cộng 8–12 User Story
- File User Story canonical: `vault/04-product/stories/` sau khi yêu cầu được phê duyệt
- User Story đã review hiện tại: **0**
- User Story DRAFT có plan được Product/BA duyệt: **2** (`DRAFT-US-PUT-001`, `DRAFT-US-AUD-001`)

Không tạo User Story giả để đạt mục tiêu. Mỗi User Story trong tương lai phải dẫn ID yêu cầu/bằng chứng đã xác nhận và có Acceptance Criteria kiểm thử được.

## Điểm bắt đầu ownership đã xác nhận

| Flow | Người phụ trách | Story ID canonical | Trạng thái review |
|---|---|---|---|
| Receive | Nghĩa | TBD | Chưa soạn |
| Putaway | Nghi | `DRAFT-US-PUT-001` (ID tạm thời, chưa canonical) | DRAFT — plan đã được Product/BA duyệt; story chưa canonical hóa |
| Pick | Thảo Ngân | TBD | Chưa soạn |
| Transfer | Ly Na | `DRAFT-US-TRA-001` | DRAFT — chờ Product/BA review |
| Adjust | Thanh Ngân | TBD | Chưa soạn |
| Audit | Nghi sở hữu/hỗ trợ | `DRAFT-US-AUD-001` (ID tạm thời, chưa canonical) | DRAFT — plan đã được Product/BA duyệt; story chưa canonical hóa |

User Story bổ sung và ownership phụ thuộc vào yêu cầu đã kiểm chứng (`OQ-023`).

## DRAFT-US-PUT-001 — Physical Putaway sau Receive

### Trace nguồn

- Requirement phạm vi: `REQ-002` — Putaway thuộc chuỗi quy trình bắt buộc.
- Evidence trực tiếp: `EVD-006`, `EVD-007`, `EVD-008`.
- Evidence về ranh giới Putaway/Transfer: `EVD-010`, `EVD-011`.
- Giới hạn khả năng khái quát: `EVD-019`.
- `CAND-REQ-003` vẫn là `DRAFT`; story này không giả định record/lookup location là product behavior đã duyệt.

### DRAFT User Story

> Là người thực hiện Putaway *(role TBD)*, tôi muốn xử lý hàng sau Receive bằng cách bố trí hàng tại backroom hoặc sales shelf, để phản ánh hoạt động sắp xếp hàng vật lý đang diễn ra tại minimart.

Story này mô tả workflow vật lý hiện tại, chưa xác định system capability. Story chưa sẵn sàng canonical hóa cho đến khi outcome hệ thống và completion state được xác nhận.

### Acceptance Criteria

`TBD` — hiện chưa đủ evidence/requirement đã duyệt để tạo Acceptance Criteria sản phẩm có thể canonical hóa.

Hai evidence checkpoint sau chỉ phục vụ discovery và kiểm tra phạm vi; **không phải Acceptance Criteria**:

1. Physical Putaway được quan sát sau Receive (`EVD-007`).
2. Hàng có thể được bố trí tại backroom hoặc sales shelf (`EVD-006`, `EVD-007`).

Các AC về ghi nhận, lưu, tra cứu, trả về location hoặc theo dõi movement vẫn là `PROPOSED` / `TBD` cho đến khi có requirement được phê duyệt.

### Phạm vi chưa xác nhận

- Trigger, precondition, completion state và downstream handoff: `TBD` / `OQ-013`.
- Partial Putaway: `OPEN QUESTION` / `OQ-014`.
- Một SKU có thể tồn tại tại nhiều physical location: `OPEN QUESTION`; chưa có canonical Open Question ID được xác nhận.
- Ranh giới Putaway và Transfer: `OPEN QUESTION` / `OQ-016`.
- Role thực hiện/xem Putaway: `OPEN QUESTION` / `OQ-020`.
- Ảnh hưởng tới Stock/Movement: `TBD`.
- Barcode/QR/scanner/mobile/offline: `OPEN QUESTION` / `OQ-022`.

Không giả định automatic location assignment, bin/capacity, multiple-location splitting, quantity update, Movement transaction, thiết bị hay permission behavior.

## DRAFT-US-AUD-001 — Đếm và đối chiếu tồn trong Audit

### Trace nguồn

- Requirement phạm vi: `REQ-002` — Audit thuộc chuỗi quy trình bắt buộc.
- Core domain liên quan: `REQ-004` — Audit thuộc phạm vi core domain; định nghĩa và hành vi chi tiết vẫn TBD.
- Requirement đã duyệt: `CAND-REQ-005` — sản phẩm nên hỗ trợ đối chiếu số lượng đếm thực tế với dữ liệu tồn trong hệ thống trong khu vực Audit.
- Business Rule đã duyệt: `CAND-BR-002` — chênh lệch giữa tồn thực tế và tồn hệ thống phải được kiểm tra lại trước khi thực hiện điều chỉnh tồn.
- Evidence trực tiếp: `EVD-015`, `EVD-016`, `EVD-017`.
- Evidence liên quan Adjust và vai trò trong vận hành hiện tại: `EVD-012`, `EVD-013`, `EVD-014`.
- Giới hạn khả năng khái quát: `EVD-019`.

### DRAFT User Story

> Là người tham gia thực hiện Audit *(role và authority TBD)*, tôi muốn đối chiếu số lượng đếm thực tế với dữ liệu tồn trong hệ thống, để phát hiện chênh lệch cần được kiểm tra lại trước khi thực hiện bất kỳ điều chỉnh tồn nào.

Story này chỉ mô tả khả năng đếm/đối chiếu đã có requirement được duyệt và nghĩa vụ re-check trước Adjust. Story không xác định loại Audit, phạm vi đếm, lịch thực hiện, quyền hạn, completion state hoặc cơ chế chuyển sang Adjust.

### DRAFT Acceptance Criteria

#### AC-AUD-01 — Đối chiếu số lượng

```gherkin
Given số lượng thực tế trong phạm vi Audit đã được đếm
And dữ liệu tồn tương ứng trong hệ thống có sẵn để đối chiếu
When thực hiện đối chiếu trong Audit
Then kết quả đối chiếu xác định số lượng thực tế và dữ liệu tồn hệ thống khớp hay có chênh lệch
```

Nguồn: `CAND-REQ-005`, `EVD-016`, `EVD-017`.

#### AC-AUD-02 — Re-check trước điều chỉnh tồn

```gherkin
Given kết quả đối chiếu phát hiện chênh lệch giữa tồn thực tế và tồn hệ thống
When việc điều chỉnh tồn được thực hiện
Then chênh lệch đã được kiểm tra lại trước khi điều chỉnh tồn
```

Nguồn: `CAND-BR-002`, `EVD-012`, `EVD-017`.

Hai AC này là DRAFT ở mức outcome được evidence/rule hỗ trợ. Cách nhập số đếm, cách biểu diễn kết quả, cách ghi nhận hoặc chứng minh re-check và cơ chế kiểm soát trước Adjust vẫn là `TBD` / `OPEN QUESTION`; AC không xác nhận Audit tự động tạo hoặc thực hiện Adjust.

### Phạm vi chưa xác nhận

- Trigger, precondition, success outcome, exception và completion state: `OPEN QUESTION` / `OQ-013`.
- Lý do, bằng chứng và phê duyệt cho Audit/Adjust: `OPEN QUESTION` / `OQ-017`.
- Audit là cycle count, full stocktake hay cả hai: `OPEN QUESTION` / `OQ-018`.
- Role có thể bắt đầu, xem, thực hiện hoặc hoàn tất Audit: `OPEN QUESTION` / `OQ-020`.
- Barcode/QR, scanner, mobile/offline và tích hợp bên ngoài: `OPEN QUESTION` / `OQ-022`.
- Phạm vi đếm theo SKU, location, category hoặc toàn bộ tồn: `TBD`; chưa có canonical Open Question riêng.
- Lịch và tần suất Audit trong sản phẩm mới: `TBD`; evidence hằng ngày chỉ mô tả minimart được nghiên cứu (`EVD-015`, `EVD-019`).
- Quan hệ giữa Audit và Adjust, gồm việc có tạo Adjust hay không: `TBD`; không giả định tự động.
- Kết quả và bước xử lý sau re-check: `TBD`.
- Định nghĩa dữ liệu tồn được dùng để đối chiếu: `OPEN QUESTION` / `OQ-011`.

Không giả định Audit tự động thay đổi Stock, tự động tạo Adjust, yêu cầu lý do/evidence/approval cụ thể, áp dụng lịch hằng ngày cho mọi Warehouse, hay có device/permission behavior cụ thể.

**## DRAFT-US-TRA-001 — Theo dõi movement hàng giữa các khu vực**

**### Trace nguồn**

* Requirement phạm vi: `REQ-002` — Transfer thuộc chuỗi quy trình bắt buộc.
* Core domain liên quan: `REQ-004` — Movement và Transfer thuộc core domain; định nghĩa, quan hệ và hành vi chi tiết vẫn `TBD`.
* Candidate Requirement: `CAND-REQ-004` — nhóm nên đánh giá việc hỗ trợ theo dõi movement giữa backroom và sales shelf; hiện vẫn `DRAFT`.
* Evidence trực tiếp: `EVD-010` — có hoạt động di chuyển hàng giữa backroom và sales shelf.
* Evidence giới hạn: `EVD-011` — chưa xác nhận movement có được ghi nhận thành transaction riêng trong KiotViet hay hệ thống mới có cần record Transfer/Movement riêng hay không.
* Giới hạn khả năng khái quát: `EVD-019`.
* Phạm vi Transfer: `OQ-016` — chưa xác định Transfer giữa location, Warehouse hay cả hai.

**### DRAFT User Story**

> Là người thực hiện xử lý hàng *(role TBD)*, tôi muốn theo dõi việc di chuyển hàng giữa các khu vực lưu trữ, để hỗ trợ kiểm soát movement hàng trong quá trình vận hành kho.

Story này phản ánh hoạt động movement đã được evidence hỗ trợ nhưng chưa xác định system capability cụ thể. Story chưa sẵn sàng canonical hóa cho đến khi phạm vi Transfer và outcome hệ thống được xác nhận.

**### Acceptance Criteria**

`TBD` — hiện chưa đủ requirement được phê duyệt để tạo Acceptance Criteria sản phẩm có thể canonical hóa.

Evidence checkpoint phục vụ discovery:

1. Có hoạt động di chuyển hàng giữa backroom và sales shelf (`EVD-010`).
2. Chưa xác nhận movement có phải transaction riêng hay không (`EVD-011`).

Các checkpoint trên **không phải Acceptance Criteria**.

**### Phạm vi chưa xác nhận**

* Trigger, precondition, success outcome, exception và completion state: `OPEN QUESTION` / `OQ-013`.
* Transfer giữa location, Warehouse hay cả hai: `OPEN QUESTION` / `OQ-016`.
* Partial Transfer: `OPEN QUESTION` / `OQ-014`.
* Role có thể thực hiện/xem Transfer: `OPEN QUESTION` / `OQ-020`.
* Movement có được ghi nhận thành transaction riêng hay không: `TBD` / `EVD-011`.
* Cách ghi nhận, lưu trữ và tra cứu movement: `TBD`.
* Quantity và ảnh hưởng của Transfer tới Stock: `TBD`.
* Barcode/QR, scanner, mobile/offline và tích hợp bên ngoài: `OPEN QUESTION` / `OQ-022`.

Không giả định Transfer phải tạo Movement transaction riêng, tự động cập nhật Stock, tự động thay đổi location, hỗ trợ nhiều Warehouse, hoặc cho phép một role cụ thể thực hiện Transfer.

**### Scope guard**

Story này chỉ ghi nhận nhu cầu theo dõi movement đã được evidence hỗ trợ. Không biến hoạt động physical movement trong `EVD-010` thành một system transaction đã được xác nhận. `EVD-011` vẫn giữ trạng thái chưa rõ và `CAND-REQ-004` vẫn là `DRAFT` cho đến khi Product/BA/Vault review.

**Trạng thái:** DRAFT — chờ Product/BA review.

**Nguồn chính:** `REQ-002`, `REQ-004`, `CAND-REQ-004`, `EVD-010`, `EVD-011`, `EVD-019`, `OQ-013`, `OQ-014`, `OQ-016`, `OQ-020`, `OQ-022`.
