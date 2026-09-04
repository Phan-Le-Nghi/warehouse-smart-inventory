# User Story và Acceptance Criteria — Mục lục

## Trạng thái

- Mục tiêu môn học: tổng cộng 8–12 User Story
- File User Story canonical: vault/04-product/stories/ sau khi yêu cầu được phê duyệt
- User Story đã review hiện tại: *1* (US-REC-001)
- User Story DRAFT có plan được Product/BA duyệt: *2* (DRAFT-US-PUT-001, DRAFT-US-AUD-001)
- User Story DRAFT chờ Product/BA review: *1* (DRAFT-US-TRA-001)

Không tạo User Story giả để đạt mục tiêu. Mỗi User Story trong tương lai phải dẫn ID yêu cầu/bằng chứng đã xác nhận và có Acceptance Criteria kiểm thử được.

## Điểm bắt đầu ownership đã xác nhận

| Flow | Người phụ trách | Story ID canonical | Trạng thái review |
|---|---|---|---|
| Receive | Nghĩa | US-REC-001 | BA CONFIRMED |
| Putaway | Nghi | DRAFT-US-PUT-001 (ID tạm thời, chưa canonical) | DRAFT — plan đã được Product/BA duyệt; story chưa canonical hóa |
| Pick | Thảo Ngân | TBD | Chưa soạn |
| Transfer | Ly Na | DRAFT-US-TRA-001 | DRAFT — chờ Product/BA review |
| Adjust | Thanh Ngân | TBD | Chưa soạn |
| Audit | Nghi sở hữu/hỗ trợ | DRAFT-US-AUD-001 (ID tạm thời, chưa canonical) | DRAFT — plan đã được Product/BA duyệt; story chưa canonical hóa |

User Story bổ sung và ownership phụ thuộc vào yêu cầu đã kiểm chứng (OQ-023).

## DRAFT-US-PUT-001 — Physical Putaway sau Receive

### Trace nguồn

- Requirement phạm vi: REQ-002 — Putaway thuộc chuỗi quy trình bắt buộc.
- Evidence trực tiếp: EVD-006, EVD-007, EVD-008.
- Evidence về ranh giới Putaway/Transfer: EVD-010, EVD-011.
- Giới hạn khả năng khái quát: EVD-019.
- CAND-REQ-003 vẫn là DRAFT; story này không giả định record/lookup location là product behavior đã duyệt.

### DRAFT User Story

Là người thực hiện Putaway *(role TBD)*, tôi muốn xử lý hàng sau Receive bằng cách bố trí hàng tại backroom hoặc sales shelf, để phản ánh hoạt động sắp xếp hàng vật lý đang diễn ra tại minimart.


Story này mô tả workflow vật lý hiện tại, chưa xác định system capability. Story chưa sẵn sàng canonical hóa cho đến khi outcome hệ thống và completion state được xác nhận.

### Acceptance Criteria

TBD — hiện chưa đủ evidence/requirement đã duyệt để tạo Acceptance Criteria sản phẩm có thể canonical hóa.

Hai evidence checkpoint sau chỉ phục vụ discovery và kiểm tra phạm vi; *không phải Acceptance Criteria*:

1. Physical Putaway được quan sát sau Receive (EVD-007).
2. Hàng có thể được bố trí tại backroom hoặc sales shelf (EVD-006, EVD-007).

Các AC về ghi nhận, lưu, tra cứu, trả về location hoặc theo dõi movement vẫn là PROPOSED / TBD cho đến khi có requirement được phê duyệt.

### Phạm vi chưa xác nhận

- Trigger, precondition, completion state và downstream handoff: TBD / OQ-013.
- Partial Putaway: OPEN QUESTION / OQ-014.
- Một SKU có thể tồn tại tại nhiều physical location: OPEN QUESTION; chưa có canonical Open Question ID được xác nhận.
- Ranh giới Putaway và Transfer: OPEN QUESTION / OQ-016.
- Role thực hiện/xem Putaway: OPEN QUESTION / OQ-020.
- Ảnh hưởng tới Stock/Movement: TBD.
- Barcode/QR/scanner/mobile/offline: OPEN QUESTION / OQ-022.

Không giả định automatic location assignment, bin/capacity, multiple-location splitting, quantity update, Movement transaction, thiết bị hay permission behavior.

## DRAFT-US-AUD-001 — Đếm và đối chiếu tồn trong Audit

### Trace nguồn

- Requirement phạm vi: REQ-002 — Audit thuộc chuỗi quy trình bắt buộc.
- Core domain liên quan: REQ-004 — Audit thuộc phạm vi core domain; định nghĩa và hành vi chi tiết vẫn TBD.
- Requirement đã duyệt: CAND-REQ-005 — sản phẩm nên hỗ trợ đối chiếu số lượng đếm thực tế với dữ liệu tồn trong hệ thống trong khu vực Audit.
- Business Rule đã duyệt: CAND-BR-002 — chênh lệch giữa tồn thực tế và tồn hệ thống phải được kiểm tra lại trước khi thực hiện điều chỉnh tồn.
- Evidence trực tiếp: EVD-015, EVD-016, EVD-017.
- Evidence liên quan Adjust và vai trò trong vận hành hiện tại: EVD-012, EVD-013, EVD-014.
- Giới hạn khả năng khái quát: EVD-019.

### DRAFT User Story

Là người tham gia thực hiện Audit *(role và authority TBD)*, tôi muốn đối chiếu số lượng đếm thực tế với dữ liệu tồn trong hệ thống, để phát hiện chênh lệch cần được kiểm tra lại trước khi thực hiện bất kỳ điều chỉnh tồn nào.


Story này chỉ mô tả khả năng đếm/đối chiếu đã có requirement được duyệt và nghĩa vụ re-check trước Adjust. Story không xác định loại Audit, phạm vi đếm, lịch thực hiện, quyền hạn, completion state hoặc cơ chế chuyển sang Adjust.

### DRAFT Acceptance Criteria

#### AC-AUD-01 — Đối chiếu số lượng

```gherkin
Given số lượng thực tế trong phạm vi Audit đã được đếm
And dữ liệu tồn tương ứng trong hệ thống có sẵn để đối chiếu
When thực hiện đối chiếu trong Audit
Then kết quả đối chiếu xác định số lượng thực tế và dữ liệu tồn hệ thống khớp hay có chênh lệch
Soạn
Viết cho Phan Lê Nghi
