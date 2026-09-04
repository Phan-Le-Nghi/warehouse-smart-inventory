# User Flow — Bản phục vụ báo cáo

## Tổng quan quy trình đã xác nhận

Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit

Đây là chuỗi các khu vực bắt buộc đã được giảng viên xác nhận, chưa phải interaction flow chi tiết.

## Người phụ trách User Story/flow

| Flow | Người phụ trách | Flow chi tiết |
|---|---|---|
| Receive | Nghĩa | TBD |
| Putaway | Nghi | DRAFT cautious flow; system interaction và completion criteria TBD |
| Pick | Thảo Ngân | TBD |
| Transfer | Ly Na | DRAFT cautious flow; trigger, scope, system interaction và completion criteria TBD |
| Adjust | Thanh Ngân | TBD |
| Audit | Nghi sở hữu/hỗ trợ | DRAFT cautious flow; trigger, scope, role và completion criteria TBD |

Flow chi tiết đã duyệt sẽ là canonical trong vault/04-product/user-flows/ và được liên kết tại đây.

---

## Putaway — DRAFT cautious flow

### Evidence boundary

- REQ-002: Putaway là khu vực quy trình bắt buộc.
- EVD-006, EVD-007: minimart có backroom và sales shelf; sau Receive, hàng có thể được bố trí tại một trong hai khu vực.
- EVD-008: kiến thức vị trí hiện phụ thuộc nhiều vào bố trí thực tế và kinh nghiệm nhân viên.
- EVD-010, EVD-011: movement giữa hai khu vực tồn tại, nhưng cách hệ thống phân loại hoặc ghi nhận chưa được xác nhận.
- EVD-019: evidence chỉ phản ánh vận hành của minimart được nghiên cứu.

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
Soạn
Viết cho Phan Lê Nghi
