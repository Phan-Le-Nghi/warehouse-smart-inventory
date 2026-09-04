# User Story và Acceptance Criteria — Mục lục

## Trạng thái

- Mục tiêu môn học: tổng cộng 8–12 User Story.
- File User Story canonical: `vault/04-product/stories/` sau khi yêu cầu và story được phê duyệt.
- User Story BA CONFIRMED hiện tại: **1** (`US-REC-001`).
- User Story DRAFT hiện tại: **5** (`DRAFT-US-PUT-001`, `DRAFT-US-PICK-001`, `DRAFT-US-TRF-001`, `DRAFT-US-ADJ-001`, `DRAFT-US-AUD-001`).

Không tạo User Story giả để đạt mục tiêu. Mỗi User Story trong tương lai phải dẫn ID requirement/evidence đã xác nhận và có Acceptance Criteria kiểm thử được. Các story mang tiền tố `DRAFT-` không phải canonical hoặc implementation-ready.

## Ownership và trạng thái

| Flow | Người phụ trách | Story ID | Trạng thái review |
|---|---|---|---|
| Receive | Nghĩa | `US-REC-001` | BA CONFIRMED; `AC-01` đến `AC-03` |
| Putaway | Nghi | `DRAFT-US-PUT-001` | DRAFT; chưa canonical |
| Pick | Thảo Ngân | `DRAFT-US-PICK-001` | DRAFT / NEEDS HUMAN REVIEW |
| Transfer | Ly Na | `DRAFT-US-TRF-001` | DRAFT / NEEDS HUMAN REVIEW |
| Adjust | Thanh Ngân | `DRAFT-US-ADJ-001` | DRAFT; chưa canonical |
| Audit | Nghi sở hữu/hỗ trợ | `DRAFT-US-AUD-001` | DRAFT; chưa canonical |

User Story bổ sung và ownership phụ thuộc vào yêu cầu đã kiểm chứng (`OQ-023`).

## US-REC-001 — Ghi nhận Receive theo số lượng thực nhận

### Trạng thái

`BA CONFIRMED` — không có AC về tra cứu lại Receive vì evidence hiện có chưa support behavior này.

### Trace nguồn

- Requirements: `REQ-002`, `CAND-REQ-001`, `CAND-REQ-002`.
- Business Rule: `CAND-BR-001`.
- Evidence: `EVD-002`, `EVD-003`, `EVD-004`, `EVD-005`.
- Open Questions: `OQ-019`, `OQ-020`.
- Canonical story: `vault/04-product/stories/US-REC-001.md`.

### User Story

> Là người thực hiện Receive, tôi muốn kiểm tra mặt hàng, ghi nhận số lượng thực nhận và đối chiếu với số lượng kỳ vọng, để số lượng Receive phản ánh hàng thực tế và chênh lệch được ghi nhận.

Role/authority thực hiện Receive vẫn là `OPEN QUESTION` (`OQ-020`). Nguồn số lượng kỳ vọng vẫn là `OPEN QUESTION` (`OQ-019`).

### Acceptance Criteria

#### AC-01 — Ghi nhận và đối chiếu

Given một ngữ cảnh Receive có mặt hàng và số lượng kỳ vọng, when người thực hiện kiểm tra mặt hàng và nhập số lượng thực nhận, then hệ thống ghi nhận số lượng thực nhận và đối chiếu với số lượng kỳ vọng.

#### AC-02 — Nhận đủ

Given số lượng thực nhận bằng số lượng kỳ vọng, when Receive được ghi nhận, then số lượng Receive được ghi nhận bằng số lượng thực nhận.

#### AC-03 — Có chênh lệch

Given số lượng thực nhận khác số lượng kỳ vọng, when Receive được ghi nhận, then số lượng Receive được ghi nhận bằng số lượng thực nhận, không thay thế bằng số lượng kỳ vọng, và chênh lệch giữa hai số lượng được ghi nhận.

### Ngoài phạm vi hiện tại

- Không có Acceptance Criterion về tra cứu/xem lại Receive hoặc chênh lệch đã ghi nhận.
- Cách xử lý chênh lệch với bên giao, handoff sang Putaway, approval, lý do, attachment, damaged goods và over-receive vẫn là `TBD` / `OPEN QUESTION`.

## DRAFT-US-PUT-001 — Physical Putaway sau Receive

### Trace nguồn

- Requirement phạm vi: `REQ-002`.
- Evidence trực tiếp: `EVD-006`, `EVD-007`, `EVD-008`.
- Evidence về ranh giới Putaway/Transfer: `EVD-010`, `EVD-011`.
- Giới hạn khả năng khái quát: `EVD-019`.
- `CAND-REQ-003` vẫn là `DRAFT`; story không giả định record/lookup location là product behavior đã duyệt.

### DRAFT User Story

> Là người thực hiện Putaway *(role TBD)*, tôi muốn xử lý hàng sau Receive bằng cách bố trí hàng tại backroom hoặc sales shelf, để phản ánh hoạt động sắp xếp hàng vật lý đang diễn ra tại minimart.

Story mô tả workflow vật lý hiện tại, chưa xác định system capability. Story chưa sẵn sàng canonical hóa cho đến khi outcome hệ thống và completion state được xác nhận.

### Acceptance Criteria

`TBD` — chưa đủ evidence/requirement đã duyệt để tạo Acceptance Criteria sản phẩm có thể canonical hóa.

Các evidence checkpoint sau chỉ phục vụ discovery, không phải Acceptance Criteria:

1. Physical Putaway được quan sát sau Receive (`EVD-007`).
2. Hàng có thể được bố trí tại backroom hoặc sales shelf (`EVD-006`, `EVD-007`).

### Phạm vi chưa xác nhận

- Trigger, precondition, completion state và downstream handoff: `OQ-013`.
- Partial Putaway: `OQ-014`.
- Một SKU có thể tồn tại tại nhiều physical location: `OPEN QUESTION`; chưa có canonical ID.
- Ranh giới Putaway và Transfer: `OQ-016`.
- Role thực hiện/xem Putaway: `OQ-020`.
- Ảnh hưởng tới Stock/Movement: `TBD`.
- Barcode/QR/scanner/mobile/offline: `OQ-022`.

### Scope guard

Không giả định automatic location assignment, bin/capacity, multiple-location splitting, quantity update, Movement transaction, thiết bị hoặc permission behavior.

**Trạng thái:** DRAFT — chưa canonical.

## DRAFT-US-PICK-001 — Pick trong phạm vi workflow

### Trace nguồn

- Requirement phạm vi: `REQ-002`.
- Evidence current-state liên quan: `EVD-006`, `EVD-007`, `EVD-008`, `EVD-009`.
- `CAND-REQ-003` liên quan location support nhưng vẫn là `DRAFT`.
- Không có Business Rule đã duyệt trực tiếp xác định Pick behavior.
- Source artifact: `vault/04-product/pick-draft.md`.

### DRAFT User Story

> As a person performing Pick, I need Pick to be included in the required inventory workflow, so that Pick is within the defined process scope.

Wording này chỉ phản ánh `REQ-002`. Nó không xác nhận location support, system action, role permission, source-location rule, stock effect hoặc inventory outcome.

### DRAFT Acceptance Criteria

#### AC-PICK-001 — Workflow scope

- **Classification:** `CONFIRMED / scope-level / non-functional`.
- **Given** the required workflow areas are reviewed,
- **When** the workflow scope is checked,
- **Then** Pick is identified as a required area in `Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`.

Đây không phải functional Pick Acceptance Criterion.

### Functional Acceptance Criteria

`TBD / OPEN QUESTION` — chưa xác nhận SKU/quantity selection, location lookup, Pick confirmation, completion, stock deduction, Movement, exception, partial Pick, scanner hoặc role permission.

### Phạm vi chưa xác nhận

- Stock quantity definitions: `OQ-011`.
- Lot/batch, serial, expiry và UOM: `OQ-012`.
- Trigger, preconditions, outcome, exception và completion: `OQ-013`.
- Partial Pick: `OQ-014`.
- Negative stock: `OQ-015`.
- Pick/Transfer/Movement boundary: `OQ-016`.
- Role/permission: `OQ-020`.
- Barcode/QR/scanner/mobile/offline/integration: `OQ-022`.

### Scope guard

Không giả định barcode/scanner, FIFO/FEFO, reservation, stock reduction, Movement creation, Transfer behavior, một location cho mỗi SKU hoặc quyền của role.

**Trạng thái:** DRAFT / NEEDS HUMAN REVIEW.

## DRAFT-US-TRF-001 — Đánh giá hỗ trợ Transfer/Movement

### Trace nguồn

- Requirement phạm vi: `REQ-002`.
- Core domain: `REQ-004`.
- Candidate Requirement: `CAND-REQ-004` — vẫn `DRAFT`.
- Evidence: `EVD-010`, `EVD-011`.
- Giới hạn khả năng khái quát: `EVD-019`.
- Transfer scope: `OQ-016`.
- Source artifact: `vault/04-product/transfer-draft.md`.

### DRAFT User Story

> As a person involved in Transfer *(role/authority is still `OQ-020`)*, I want the product team to evaluate whether movement between the backroom storage area and the sales shelf area should be supported in the product, so that the team can decide whether any recording or query behavior belongs in the Transfer flow.

Story chỉ phản ánh nhu cầu đánh giá product scope. Nó không xác nhận system capability cụ thể.

### Acceptance Criteria

`AC-TRF-001` trong Transfer draft chỉ là scope-level confirmation rằng Transfer thuộc workflow bắt buộc theo `REQ-002`. Functional Acceptance Criteria vẫn là `TBD`.

Evidence checkpoints phục vụ discovery:

1. Có physical movement giữa backroom và sales shelf (`EVD-010`).
2. Chưa xác nhận movement là transaction riêng (`EVD-011`).

Các checkpoint trên không phải functional Acceptance Criteria.

### Phạm vi chưa xác nhận

- Trigger, precondition, success outcome, exception và completion: `OQ-013`.
- Partial Transfer: `OQ-014`.
- Negative stock: `OQ-015`.
- Transfer giữa location, Warehouse hay cả hai: `OQ-016`.
- Role có thể thực hiện/xem Transfer: `OQ-020`.
- Movement record, source/destination, query behavior và Stock/location effect: `TBD`.
- Barcode/QR, scanner, mobile/offline và integration: `OQ-022`.

### Scope guard

Không biến physical movement thành system transaction đã xác nhận. Không giả định Transfer tự động cập nhật Stock/location, hỗ trợ nhiều Warehouse hoặc cho phép một role cụ thể thực hiện.

**Trạng thái:** DRAFT / NEEDS HUMAN REVIEW.

## DRAFT-US-ADJ-001 — Kiểm tra lại chênh lệch trước điều chỉnh tồn

### Trace nguồn

- Requirement phạm vi: `REQ-002`.
- Business Rule đã duyệt: `CAND-BR-002`.
- Evidence trực tiếp: `EVD-012`, `EVD-017`.
- `CAND-REQ-005` liên quan Audit nhưng không phải nguồn bắt buộc của Adjust.
- `EVD-013` chỉ là current-state evidence, không xác nhận product role/permission/approval.

### DRAFT User Story

> As a person handling stock discrepancies, I want to recheck the discrepancy between physical stock and system stock before performing a stock adjustment.

Actor là nhãn trung tính. Role, authority và permission là `TBD` / `OQ-020`.

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

- Nguồn/trigger xác định discrepancy: `TBD`.
- Detailed recheck, completion, exception và adjustment mechanism: `OQ-013` / `TBD`.
- Reason, evidence và approval: `OQ-017`.
- Stock definitions và negative stock: `OQ-011`, `OQ-015`.
- Role/permission: `OQ-020`.
- Anomaly/discrepancy definition: `OQ-028`.
- Quan hệ Audit–Adjust: `TBD`.

### Scope guard

Không giả định Audit là trigger bắt buộc, role/permission, approval, reason, attachment, quantity validation, automatic Stock update hoặc Adjust outcome ngoài evidence hiện có.

**Trạng thái:** DRAFT — chưa canonical.

## DRAFT-US-AUD-001 — Đếm và đối chiếu tồn trong Audit

### Trace nguồn

- Requirement phạm vi: `REQ-002`.
- Core domain: `REQ-004`.
- Requirement đã duyệt: `CAND-REQ-005`.
- Business Rule đã duyệt: `CAND-BR-002`.
- Evidence trực tiếp: `EVD-015`, `EVD-016`, `EVD-017`.
- Evidence liên quan Adjust/role context: `EVD-012`, `EVD-013`, `EVD-014`.
- Giới hạn khả năng khái quát: `EVD-019`.

### DRAFT User Story

> Là người tham gia thực hiện Audit *(role và authority TBD)*, tôi muốn đối chiếu số lượng đếm thực tế với dữ liệu tồn trong hệ thống, để phát hiện chênh lệch cần được kiểm tra lại trước khi thực hiện bất kỳ điều chỉnh tồn nào.

Story không xác định loại Audit, phạm vi đếm, lịch thực hiện, quyền hạn, completion state hoặc cơ chế chuyển sang Adjust.

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

Hai AC là DRAFT ở mức outcome được evidence/rule hỗ trợ. Chúng không xác nhận Audit tự động tạo hoặc thực hiện Adjust.

### Phạm vi chưa xác nhận

- Trigger, precondition, success outcome, exception và completion: `OQ-013`.
- Reason, evidence và approval: `OQ-017`.
- Cycle count/full stocktake: `OQ-018`.
- Role/permission: `OQ-020`.
- Device/integration: `OQ-022`.
- Count scope, lịch/tần suất sản phẩm và Audit–Adjust relationship: `TBD`.
- Stock quantity dùng để đối chiếu: `OQ-011`.

### Scope guard

Không giả định Audit tự động thay đổi Stock, tự động tạo Adjust, yêu cầu approval cụ thể, hoặc áp dụng lịch hằng ngày cho mọi Warehouse.

**Trạng thái:** DRAFT — chưa canonical.
