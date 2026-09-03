# User Flow — Bản phục vụ báo cáo

## Tổng quan quy trình đã xác nhận

`Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`

Đây là chuỗi các khu vực bắt buộc đã được giảng viên xác nhận, chưa phải interaction flow chi tiết.

## Người phụ trách User Story/flow

| Flow | Người phụ trách | Flow chi tiết |
|---|---|---|
| Receive | Nghĩa | TBD |
| Putaway | Nghi | DRAFT cautious flow; system interaction và completion criteria TBD |
| Pick | Thảo Ngân | TBD |
| Transfer | Ly Na | TBD |
| Adjust | Thanh Ngân | TBD |
| Audit | Nghi sở hữu/hỗ trợ | TBD |

Flow chi tiết đã duyệt sẽ là canonical trong `vault/04-product/user-flows/` và được liên kết tại đây.

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
- Một SKU có thể tồn tại tại nhiều physical location: `OPEN QUESTION`; `OQ-034` là stable ID được đề xuất để BA/Vault kiểm tra và phê duyệt, chưa canonical và task này không resolve.
- Putaway hay Transfer đối với movement giữa backroom và sales shelf: `OQ-016`.
- Role có thể thực hiện/xem Putaway: `OQ-020`.
- Putaway có ảnh hưởng Stock/Movement hay không: `TBD`.
- Barcode/QR/scanner/mobile/offline có thuộc phạm vi không: `OQ-022`.
