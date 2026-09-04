# User Flow — Bản phục vụ báo cáo

## Tổng quan quy trình đã xác nhận

Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit

Đây là chuỗi các khu vực bắt buộc đã được giảng viên xác nhận, chưa phải interaction flow chi tiết.

## Người phụ trách User Story/flow

| Flow | Người phụ trách | Flow chi tiết |
|---|---|---|
| Receive | Nghĩa | DRAFT flow — US-REC-001 (BA CONFIRMED), AC-01 đến AC-03 |
| Putaway | Nghi | DRAFT cautious flow; system interaction và completion criteria TBD |
| Pick | Thảo Ngân | DRAFT — see Pick flow below |
| Transfer | Ly Na | DRAFT cautious flow; trigger, scope, system interaction và completion criteria TBD |
| Adjust | Thanh Ngân | DRAFT cautious flow; trigger và detailed behavior TBD |
| Audit | Nghi sở hữu/hỗ trợ | DRAFT cautious flow; trigger, scope, role và completion criteria TBD |

Flow chi tiết đã duyệt sẽ là canonical trong vault/04-product/user-flows/ và được liên kết tại đây.

---

## Receive — DRAFT flow

### Evidence boundary

- US-REC-001 — BA CONFIRMED; AC-01, AC-02, AC-03.
- CAND-REQ-001: ghi nhận số lượng thực nhận và đối chiếu với số lượng kỳ vọng.
- CAND-REQ-002: ghi nhận chênh lệch giữa số lượng thực nhận và số lượng kỳ vọng.
- CAND-BR-001: khi có chênh lệch, ghi nhận Receive dùng số lượng thực nhận, không thay bằng số lượng kỳ vọng.
- EVD-002 đến EVD-005: check item, đếm actual quantity, đối chiếu expected quantity và ghi nhận actual quantity khi chênh lệch.

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