# Hướng dẫn sử dụng AI

## Cách sử dụng được phép

- Tóm tắt hoặc sắp xếp nguồn được cung cấp nhưng vẫn giữ provenance.
- Xác định khoảng trống, mâu thuẫn, rủi ro và câu hỏi mở.
- Soạn kế hoạch hoặc artifact từ ngữ cảnh có giới hạn, liên quan để con người review.
- Hỗ trợ implementation và verification sau khi yêu cầu chi phối cùng kế hoạch được phê duyệt.

## Hành vi bắt buộc

- Phân biệt `CONFIRMED`, `ASSUMPTION`, `TBD` và `OPEN QUESTION`.
- Dẫn artifact Vault hoặc stable ID hỗ trợ cho câu trả lời về sự thật hay quy tắc.
- Trả lời `KHÔNG ĐỦ DỮ LIỆU` khi Vault không hỗ trợ câu trả lời.
- Không bao giờ tự tạo bằng chứng nghiên cứu, quy tắc Warehouse, quyền hạn, User Story, kết quả test, Taiga item hoặc phát hiện thiết kế.
- Dùng ngữ cảnh liên quan đến User Story hiện tại thay vì sao chép toàn bộ Vault.
- Ghi lại việc sử dụng có ý nghĩa và bước kiểm chứng của con người trong [`../../docs/AI_USAGE_LOG.md`](../../docs/AI_USAGE_LOG.md).

## Nội dung bị cấm trong repository

- Secret và giá trị `.env`
- Context Pack tạm thời
- Output AI chưa được review nhưng được trình bày như tri thức có thẩm quyền
