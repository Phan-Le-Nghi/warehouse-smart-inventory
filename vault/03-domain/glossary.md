# Bảng thuật ngữ domain

Các thuật ngữ domain sau đã được xác nhận là có liên quan. Định nghĩa chi tiết vẫn là `TBD` và không được suy diễn khi chưa có bằng chứng.

| Thuật ngữ | Hiểu biết đã xác nhận | Nội dung TBD |
|---|---|---|
| SKU | Khái niệm cốt lõi trong domain sản phẩm. | Định danh, thuộc tính, đơn vị, hành vi lot/serial |
| Warehouse | Khái niệm cốt lõi về địa điểm. Theo HUMAN PRODUCT DECISION `DEC-005`, MVP quản lý một Warehouse duy nhất; multi-Warehouse ngoài MVP. | Hành vi chi tiết trong Warehouse |
| Internal Location | Area-level placement context bên trong MVP Warehouse. Các tracked internal locations là `Backroom` và `Sales Shelf`; aisle, rack, bin và detailed shelf ngoài MVP. Một SKU có thể có `system stock quantity` tại nhiều internal locations. | Capacity, detailed sub-location và behavior ngoài các workflow effects đã duyệt vẫn TBD. |
| Stock | Khái niệm cốt lõi về tồn kho. MVP duy trì `system stock quantity` theo internal location; Warehouse total quantity của SKU bằng tổng quantity tại các internal locations. Không canonicalize `on-hand`, `available`, `reserved`, `damaged` hoặc `in-transit`. | Negative-stock behavior và semantics ngoài các quantity effects đã duyệt vẫn OPEN. |
| Physical movement | Sự di chuyển hàng hóa ngoài thực tế. Physical movement không mặc định tạo system transaction hoặc Movement system record. | Classification/recording theo behavior được human duyệt |
| Movement system record | Bản ghi hệ thống về movement khi Requirement/Business Rule tương ứng được human approve. Round 2 chỉ approve system Transfer record; Putaway không tự tạo Transfer hoặc Movement system record. | Các loại Movement record khác, vòng đời và reversal vẫn TBD. |
| Movement | Core domain concept liên quan đến biến động tồn kho; `DEC-009` phân biệt Physical movement với Movement system record. | Các loại ngoài Transfer, vòng đời và reversal vẫn TBD. |
| Transfer | Subsequent relocation giữa tracked internal locations trong cùng một Warehouse. Confirmed Transfer có system record, giảm source quantity, tăng cùng quantity tại destination và không đổi Warehouse total. Cross-Warehouse Transfer ngoài MVP. | Exception, partial Transfer, negative-stock và reversal behavior vẫn OPEN/TBD. |
| Alert | Khái niệm domain cốt lõi. | Loại Alert, trigger, người nhận, cách xử lý |
| Audit | Selected-scope Audit session cho nhóm SKU/location hoặc toàn Warehouse; gồm physical count, compare với `system stock quantity` và record result. Không canonicalize `cycle count`; mismatch không auto Adjust. | Audit mismatch completion, schedule và exception ngoài discrepancy vẫn TBD. |
| Receive | Khu vực quy trình bắt buộc; expected quantity dùng external/manual order or delivery reference do Purchasing cung cấp/chuẩn bị. Full Purchase Order lifecycle ngoài MVP. | Trigger/completion wording cuối và lifecycle gaps tại `OQ-013`. |
| Putaway | Initial placement sau Receive với SKU, quantity và destination `Backroom` hoặc `Sales Shelf`. Confirmed Putaway phân bổ quantity vào destination và không tự tạo Transfer/Movement record. | Exception và downstream handoff tại `OQ-013`; partial Putaway tại `OQ-014`. |
| Pick | Lấy quantity từ một hoặc nhiều tracked source internal locations theo Pick request có SKU/requested quantity. Confirmed Pick giảm source quantity; chỉ full quantity mới fully completed; thiếu quantity là `PARTIAL / INSUFFICIENT`. | Negative-stock behavior và lifecycle ngoài approved exception vẫn OPEN/TBD. |
| Adjust | Action riêng sau discrepancy/re-check. Warehouse Staff tạo request; Manager approve/reject; reason bắt buộc, evidence optional; approved Adjust cập nhật affected location quantity. | Rejected-case closure và negative-stock behavior vẫn OPEN/TBD. |
