# Warehouse & Smart Inventory Management

Repository của Nhóm 10 cho môn MIS3032_1.

## Trạng thái hiện tại

- Giai đoạn: Khởi động, Discovery và Product Definition / Build Foundation
- Hạn Report Round 1: 04/09/2026
- Technology stack: **TBD — cần con người phê duyệt**
- Triển khai tính năng nghiệp vụ: **chưa bắt đầu**

## Bối cảnh dự án đã xác nhận

Dự án giải quyết bài toán kiểm soát nhập kho, xuất/lấy hàng, chuyển kho và tồn kho.

Quy trình đã được giảng viên xác nhận:

`Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`

Các role tối thiểu gồm Warehouse Staff, Manager, Purchasing và Admin. Các hướng AI hiện tại gồm Inventory Q&A, Explain inventory anomalies và Reorder recommendation.

## Bản đồ repository

- [`vault/`](vault/00-index.md): tri thức canonical của dự án và nguồn sự thật duy nhất.
- [`docs/`](docs/00-project-index.md): tài liệu phục vụ môn học/báo cáo và theo dõi artifact.
- [`apps/`](apps/README.md): code sản phẩm trong tương lai; chỉ bắt đầu sau khi stack được phê duyệt.
- [`PLANS.md`](PLANS.md): kế hoạch triển khai hiện tại và các cổng phê duyệt.
- [`AGENTS.md`](AGENTS.md): quy tắc làm việc bền vững cho phát triển có AI hỗ trợ.

Thông tin còn thiếu hoặc chưa có nguồn hỗ trợ phải được đánh dấu rõ là `TBD`, `ASSUMPTION` hoặc `OPEN QUESTION`.
