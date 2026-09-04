# User Story và Acceptance Criteria — Mục lục

## Trạng thái

- Mục tiêu môn học: tổng cộng 8–12 User Story
- File User Story canonical: `vault/04-product/stories/` sau khi yêu cầu được phê duyệt
- User Story đã review hiện tại: **0**
- User Story DRAFT có plan được Product/BA duyệt: **3** (`DRAFT-US-PUT-001`, `DRAFT-US-ADJ-001`, `DRAFT-US-AUD-001`)

Không tạo User Story giả để đạt mục tiêu. Mỗi User Story trong tương lai phải dẫn ID yêu cầu/bằng chứng đã xác nhận và có Acceptance Criteria kiểm thử được.

## Điểm bắt đầu ownership đã xác nhận

| Flow | Người phụ trách | Story ID canonical | Trạng thái review |
|---|---|---|---|
| Receive | Nghĩa | TBD | Chưa soạn |
| Putaway | Nghi | `DRAFT-US-PUT-001` (ID tạm thời, chưa canonical) | DRAFT — plan đã được Product/BA duyệt; story chưa canonical hóa |
| Pick | Thảo Ngân | TBD | Chưa soạn |
| Transfer | Ly Na | TBD | Chưa soạn |
| Adjust | Thanh Ngân | `DRAFT-US-ADJ-001` (ID tạm thời, chưa canonical) | DRAFT — plan đã được Product/BA duyệt; story chưa canonical hóa |
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
- Một SKU có thể tồn tại tại nhiều physical location: `OPEN QUESTION`; `OQ-034` là stable ID được đề xuất để BA/Vault kiểm tra và phê duyệt, chưa canonical và chưa được resolve trong story này.
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

## DRAFT-US-ADJ-001 — Kiểm tra lại chênh lệch trước điều chỉnh tồn

### Trace nguồn

- Requirement phạm vi: `REQ-002` — Adjust thuộc chuỗi quy trình bắt buộc.
- Business Rule đã duyệt: `CAND-BR-002` — chênh lệch giữa tồn thực tế và tồn hệ thống phải được kiểm tra lại trước khi điều chỉnh tồn.
- Evidence trực tiếp: `EVD-012`, `EVD-017`.
- Liên quan nhưng không phải nguồn bắt buộc của Adjust: `CAND-REQ-005` — đối chiếu tồn trong Audit.
- `EVD-013` chỉ mô tả vận hành minimart hiện tại; không xác nhận role, permission, authority hoặc approval của sản phẩm.

### DRAFT User Story

> As a person handling stock discrepancies, I want to recheck the discrepancy between physical stock and system stock before performing a stock adjustment.

Actor là nhãn trung tính. Role, authority và permission chính thức là `TBD` / `OPEN QUESTION OQ-020`.

### DRAFT Acceptance Criteria

#### AC-ADJ-001 — Re-check trước điều chỉnh tồn

```gherkin
Given a discrepancy exists between physical stock and system stock,
when a stock adjustment is performed,
then the discrepancy must be rechecked before the adjustment.
```

Nguồn: `CAND-BR-002`, `EVD-012`, `EVD-017`.

#### AC-ADJ-002 — Không tiếp tục điều chỉnh khi chưa re-check

```gherkin
Given a discrepancy exists between physical stock and system stock,
when the discrepancy has not been rechecked,
then the stock adjustment must not continue.
```

Nguồn: `CAND-BR-002`, `EVD-012`, `EVD-017`.

Hai AC chỉ thể hiện thứ tự nghiệp vụ trong `CAND-BR-002`; không xác nhận cơ chế technical blocking.

### Phạm vi chưa xác nhận

- Nguồn hoặc trigger xác định chênh lệch: `TBD`.
- Detailed recheck steps, completion state, exception handling và adjustment mechanism: `TBD` / `OQ-013`.
- Reason, evidence và approval requirements: `OPEN QUESTION OQ-017`.
- Stock quantity definitions: `OPEN QUESTION OQ-011`; negative-stock handling: `OPEN QUESTION OQ-015`.
- Anomaly/discrepancy definition và proof: `OPEN QUESTION OQ-028`.
- Quan hệ Audit–Adjust: `TBD`; không giả định Audit là trigger hoặc dependency bắt buộc của Adjust.

Không giả định role/permission cụ thể, approval, reason, attachment, quantity validation, automatic stock update, hoặc edge case Adjust ngoài evidence hiện có.
