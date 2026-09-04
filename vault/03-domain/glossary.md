# Bảng thuật ngữ domain

Các thuật ngữ domain sau đã được xác nhận là có liên quan. Định nghĩa chi tiết vẫn là `TBD` và không được suy diễn khi chưa có bằng chứng.

| Thuật ngữ | Hiểu biết đã xác nhận | Nội dung TBD |
|---|---|---|
| SKU | Khái niệm cốt lõi trong domain sản phẩm. | Định danh, thuộc tính, đơn vị, hành vi lot/serial |
| Warehouse | Khái niệm cốt lõi về địa điểm. Theo HUMAN PRODUCT DECISION `DEC-005`, MVP quản lý một Warehouse duy nhất; multi-Warehouse ngoài MVP. | Hành vi chi tiết trong Warehouse |
| Internal Location | Area-level placement context bên trong MVP Warehouse. Các location ban đầu là `Backroom` và `Sales Shelf`; aisle, rack, bin và detailed shelf ngoài MVP. Theo `DEC-006`, một SKU có thể liên kết với nhiều internal locations trong cùng Warehouse. | Quantity có được duy trì theo location hay không và aggregation |
| Stock | Khái niệm cốt lõi về tồn kho. Thuật ngữ MVP được human duyệt là `system stock quantity`; không canonicalize `on-hand`, `available`, `reserved`, `damaged` hoặc `in-transit`. | Granularity, aggregation, workflow effect và thời điểm thay đổi quantity (`OQ-011`) |
| Physical movement | Sự di chuyển hàng hóa ngoài thực tế. Physical movement không mặc định tạo system transaction hoặc Movement system record. | Classification/recording theo behavior được human duyệt |
| Movement system record | Bản ghi hệ thống về movement, chỉ tồn tại nếu Requirement/Business Rule tương ứng được human approve. | Loại, vòng đời, quy tắc tạo record và đảo giao dịch |
| Movement | Core domain concept liên quan đến biến động tồn kho; `DEC-009` yêu cầu phân biệt Physical movement với Movement system record. | Loại, vòng đời, Stock effect và quy tắc ghi nhận |
| Transfer | Trong MVP, subsequent relocation giữa tracked internal locations trong cùng một Warehouse. Cross-Warehouse Transfer ngoài MVP. | System Transfer transaction, Movement system record, Stock effect, automatic location update và vòng đời |
| Alert | Khái niệm domain cốt lõi. | Loại Alert, trigger, người nhận, cách xử lý |
| Audit | Khái niệm domain cốt lõi và khu vực quy trình bắt buộc. | Phạm vi cycle/full, bằng chứng, xử lý chênh lệch |
| Receive | Khu vực quy trình bắt buộc. | Trigger, đầu vào, trạng thái, ngoại lệ |
| Putaway | Khu vực quy trình bắt buộc; theo HUMAN PRODUCT MODELING, initial placement sau Receive tại một internal location. | Trigger chính xác, quantity/location effect, completion và ngoại lệ |
| Pick | Khu vực quy trình bắt buộc; theo HUMAN PRODUCT MODELING, lấy quantity từ source internal location để phục vụ downstream purpose. | Trigger, downstream purpose, Stock effect, completion và ngoại lệ |
| Adjust | Khu vực quy trình bắt buộc. | Lý do, phê duyệt, bằng chứng, ghi nhận |
