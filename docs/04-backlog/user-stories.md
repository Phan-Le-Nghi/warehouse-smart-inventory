- Evidence giới hạn: `EVD-011` — chưa xác nhận movement có được ghi nhận thành transaction riêng trong KiotViet hay hệ thống mới có cần record Transfer/Movement riêng hay không.
- Giới hạn khả năng khái quát: `EVD-019`.
- Phạm vi Transfer: `OQ-016` — chưa xác định Transfer giữa location, Warehouse hay cả hai.

### DRAFT User Story

> Là người thực hiện xử lý hàng *(role TBD)*, tôi muốn theo dõi việc di chuyển hàng giữa các khu vực lưu trữ, để hỗ trợ kiểm soát movement hàng trong quá trình vận hành kho.

Story này phản ánh hoạt động movement đã được evidence hỗ trợ nhưng chưa xác định system capability cụ thể. Story chưa sẵn sàng canonical hóa cho đến khi phạm vi Transfer và outcome hệ thống được xác nhận.

### Acceptance Criteria

`TBD` — hiện chưa đủ requirement được phê duyệt để tạo Acceptance Criteria sản phẩm có thể canonical hóa.

Evidence checkpoint phục vụ discovery:

1. Có hoạt động di chuyển hàng giữa backroom và sales shelf (`EVD-010`).
2. Chưa xác nhận movement có phải transaction riêng hay không (`EVD-011`).

Các checkpoint trên **không phải Acceptance Criteria**.

### Phạm vi chưa xác nhận

- Trigger, precondition, success outcome, exception và completion state: `OPEN QUESTION` / `OQ-013`.
- Transfer giữa location, Warehouse hay cả hai: `OPEN QUESTION` / `OQ-016`.
- Partial Transfer: `OPEN QUESTION` / `OQ-014`.
- Role có thể thực hiện/xem Transfer: `OPEN QUESTION` / `OQ-020`.
- Movement có được ghi nhận thành transaction riêng hay không: `TBD` / `EVD-011`.
- Cách ghi nhận, lưu trữ và tra cứu movement: `TBD`.
- Quantity và ảnh hưởng của Transfer tới Stock: `TBD`.
- Barcode/QR, scanner, mobile/offline và tích hợp bên ngoài: `OPEN QUESTION` / `OQ-022`.

Không giả định Transfer phải tạo Movement transaction riêng, tự động cập nhật Stock, tự động thay đổi location, hỗ trợ nhiều Warehouse, hoặc cho phép một role cụ thể thực hiện Transfer.

### Scope guard

Story này chỉ ghi nhận nhu cầu theo dõi movement đã được evidence hỗ trợ.

Không biến hoạt động physical movement trong `EVD-010` thành một system transaction đã được xác nhận.

`EVD-011` vẫn giữ trạng thái chưa rõ và `CAND-REQ-004` vẫn là `DRAFT` cho đến khi Product/BA/Vault review.

**Trạng thái:** DRAFT — chờ Product/BA review.

**Nguồn chính:** `REQ-002`, `REQ-004`, `CAND-REQ-004`, `EVD-010`, `EVD-011`, `EVD-019`, `OQ-013`, `OQ-014`, `OQ-016`, `OQ-020`, `OQ-022`.