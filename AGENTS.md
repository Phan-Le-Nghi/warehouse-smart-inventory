# Quy tắc làm việc bền vững

Các quy tắc này áp dụng cho toàn bộ repository.

1. Project Vault là nguồn sự thật duy nhất cho tri thức dự án, yêu cầu, quyết định, định nghĩa sản phẩm và technical contract.
2. Tuân theo vòng lặp: `inspect -> plan -> implement -> verify -> review`.
3. Mỗi cuộc trò chuyện với Codex chỉ nên hướng tới một kết quả mạch lạc, có thể review.
4. Không tự tạo hành vi nghiệp vụ, bằng chứng nghiên cứu, quy tắc nghiệp vụ, quyền hạn hoặc Acceptance Criteria còn thiếu.
5. Không thay đổi yêu cầu nghiệp vụ hoặc xem giả định là thông tin đã xác nhận khi chưa có con người phê duyệt và bằng chứng nguồn.
6. Không chọn technology stack, database, thư viện authentication hoặc nền tảng deployment khi chưa có con người phê duyệt.
7. Chỉ dùng phần ngữ cảnh Vault có giới hạn và liên quan đến User Story hoặc tác vụ hiện tại. Không đưa toàn bộ Vault vào mọi prompt.
8. Phải có output mới từ command trước khi khẳng định build, test, lint hoặc bước kiểm tra đã thành công.
9. Con người phải review diff trước khi tích hợp hoặc commit.
10. Cập nhật Traceability khi hành vi, contract, implementation hoặc test đã duyệt thay đổi.
11. Không bao giờ commit secret, giá trị `.env`, thông tin đăng nhập cục bộ hoặc Context Pack tạm thời.
12. Công cụ bên ngoài không được âm thầm ghi đè nội dung canonical trong Vault.

Không đưa yêu cầu nghiệp vụ Warehouse chi tiết vào file này.
