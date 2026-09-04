# Tổng quan quy trình

## Chuỗi đã xác nhận

`Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`

Chuỗi này xác định các khu vực quy trình bắt buộc. Chuỗi chưa khẳng định mọi mặt hàng tồn kho hoặc giao dịch luôn đi qua cả sáu khu vực trong một quy trình liên tục.

## Boundary được human phê duyệt cho MVP

- MVP quản lý một Warehouse duy nhất; multi-Warehouse và cross-Warehouse operation ngoài MVP (`DEC-005`).
- Internal location ở mức area-level gồm `Backroom` và `Sales Shelf`; một SKU có thể liên kết với nhiều internal locations trong cùng Warehouse (`DEC-006`).
- Putaway là initial placement sau Receive tại một internal location (`DEC-009`).
- Transfer là subsequent relocation giữa tracked internal locations trong cùng một Warehouse; cross-Warehouse Transfer ngoài MVP (`DEC-007`, `DEC-009`).
- Pick là lấy quantity từ source internal location để phục vụ downstream purpose (`DEC-009`). Pick trigger, downstream purpose, Stock effect, completion và exceptions vẫn `TBD` / `OPEN QUESTION`.
- Physical movement không mặc định tạo system Transfer transaction hoặc Movement system record. Stock effect và automatic location update chưa được duyệt.

Các mục trên là HUMAN PRODUCT DECISIONS / PRODUCT MODELING, không phải research findings.

## Trạng thái chi tiết

| Khu vực | Người phụ trách | Chi tiết nghiệp vụ |
|---|---|---|
| Receive | Nghĩa | TBD thông qua yêu cầu/nghiên cứu đã kiểm chứng |
| Putaway | Nghi | TBD thông qua yêu cầu/nghiên cứu đã kiểm chứng |
| Pick | Thảo Ngân | TBD thông qua yêu cầu/nghiên cứu đã kiểm chứng |
| Transfer | Ly Na | TBD thông qua yêu cầu/nghiên cứu đã kiểm chứng |
| Adjust | Thanh Ngân | TBD thông qua yêu cầu/nghiên cứu đã kiểm chứng |
| Audit | Nghi sở hữu/hỗ trợ ngoài Putaway | TBD thông qua yêu cầu/nghiên cứu đã kiểm chứng |

Trigger, điều kiện trước, trạng thái, ngoại lệ và quan hệ giữa các flow vẫn còn mở tại `OQ-013`.
