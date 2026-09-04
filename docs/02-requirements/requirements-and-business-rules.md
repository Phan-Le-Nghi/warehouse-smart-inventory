# Requirements và Business Rules — Bản phục vụ báo cáo

Tài liệu này là bản phục vụ báo cáo, không phải bản canonical thứ hai.

## Yêu cầu sản phẩm

Yêu cầu canonical và bằng chứng được duy trì trong [`../../vault/02-requirements/requirements.md`](../../vault/02-requirements/requirements.md).

Hiện đã xác nhận ở cấp cao:

- `REQ-001`: kiểm soát nhập, xuất/lấy hàng, chuyển kho và tồn kho;
- `REQ-002`: phạm vi vận hành gồm Receive, Putaway, Pick, Transfer, Adjust và Audit;
- `REQ-003`: các role Warehouse Staff, Manager, Purchasing và Admin;
- `REQ-004`: các khái niệm SKU, Warehouse, Stock, Movement, Transfer, Alert và Audit.

Round 2 đã bổ sung HUMAN PRODUCT DECISIONS / MVP ASSUMPTIONS cho per-location quantity, Putaway, Pick, Transfer, Audit, Adjust, Receive/Purchasing và permissions. Các quyết định này không phải verified research findings. Danh sách canonical và stable IDs nằm trong Vault.

## Quy tắc nghiệp vụ

Các rule canonical đã human review gồm `CAND-BR-001` đến `CAND-BR-015`. Chúng bao phủ actual Receive quantity, re-check trước Adjust, location aggregation, Putaway/Pick/Transfer effects, Transfer recording, Audit comparison/no-auto-Adjust, Adjust control/outcome, Receive reference mismatch và negative-stock guard. Xem [`../../vault/02-requirements/business-rules.md`](../../vault/02-requirements/business-rules.md) để có wording và classification chính xác.

## Khoảng trống

`OQ-015` đã được resolve bởi `DEC-019`. `OQ-013` vẫn `PARTIALLY DECIDED / OPEN`; `OQ-014`, `OQ-022` và các OQ AI chưa có quyết định vẫn mở. Xem [`../../vault/02-requirements/open-questions.md`](../../vault/02-requirements/open-questions.md).
