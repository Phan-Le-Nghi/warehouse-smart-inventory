# User Flow — Bản phục vụ báo cáo

## Tổng quan quy trình đã xác nhận

`Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`

Đây là chuỗi các khu vực bắt buộc đã được giảng viên xác nhận, chưa phải interaction flow chi tiết.

## Người phụ trách User Story/flow

| Flow | Người phụ trách | Flow chi tiết |
|---|---|---|
| Receive | Nghĩa | TBD |
| Putaway | Nghi | TBD |
| Pick | Thảo Ngân | DRAFT — see Pick flow below |
| Transfer | Ly Na | TBD |
| Adjust | Thanh Ngân | TBD |
| Audit | Nghi sở hữu/hỗ trợ | TBD |

Flow chi tiết đã duyệt sẽ là canonical trong `vault/04-product/user-flows/` và được liên kết tại đây.

## Pick — DRAFT User Flow

**Status:** `DRAFT / NEEDS HUMAN REVIEW`

**Owner:** Thảo Ngân
**Source:** `vault/04-product/pick-draft.md`

### Directed flow

```text
[TBD: Pick trigger — OQ-013]
        ↓
[Pick workflow area — CONFIRMED: REQ-002]
        ↓
[TBD: Identify item / quantity — OQ-011, OQ-013]
        ↓
[TBD: Select / confirm source location]
        ↓
[TBD: Complete / record Pick — OQ-013]
        ↓
[TBD: Downstream impact / boundary — OQ-011, OQ-016]
```

### Current-state context / evidence

- Backroom and sales shelf exist: `EVD-006`.
- Goods may be in the backroom or sales shelf after receiving: `EVD-007`.
- Current knowledge of goods location relies mainly on physical arrangement and staff experience: `EVD-008`, `EVD-009`.

This context is not a confirmed system step or Pick behavior. No barcode/scanner, FIFO/FEFO, reservation, stock reduction, Movement, Transfer, partial Pick, or role permission is assumed. `OQ-016` remains unresolved for the Pick/Transfer/Movement boundary; `OQ-020` remains unresolved for a specific Pick actor or permission.
