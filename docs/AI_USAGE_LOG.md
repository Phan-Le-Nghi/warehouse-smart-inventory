# AI Usage Log v1

## Trạng thái hiện tại

`TBD`: Chưa ghi mục sử dụng AI cá nhân nào trong scaffold này.

Mỗi sinh viên phải cung cấp ít nhất một mục có ý nghĩa và đã được kiểm chứng cho Report Round 1. Mục ghi nhận việc AI hỗ trợ và cách kiểm chứng; mục này không làm cho output AI trở thành nguồn có thẩm quyền.

## Template cho mỗi mục

### AI-USE-### — Kết quả ngắn gọn

- Thành viên: TBD
- Ngày/giờ: TBD
- Mục tiêu: TBD
- Ngữ cảnh có giới hạn đã cung cấp: TBD
- Tham chiếu prompt hoặc tương tác: TBD
- Tóm tắt output: TBD
- Cách con người kiểm chứng: TBD
- Thay đổi được chấp nhận: TBD
- Đề xuất bị từ chối/điều chỉnh: TBD
- ID/link artifact bị ảnh hưởng: TBD
- Người review: TBD

Không đưa secret, dữ liệu cá nhân, Context Pack tạm thời hoặc bước kiểm chứng giả vào đây.

### AI-USE-001 — Consistency review giữa Requirements và downstream artifacts

- Thành viên: Ly Na
- Ngày/giờ: 2026-09-03
- ID/link artifact bị ảnh hưởng:
  - `vault/02-requirements/requirements.md`
  - `vault/02-requirements/open-questions.md`
  - `docs/04-backlog/user-stories.md`
  - `docs/TRACEABILITY.md`
- Mục đích sử dụng AI:
  - Hỗ trợ kiểm tra tính nhất quán giữa requirement status, User Story, traceability và Open Questions.
- Kết quả AI hỗ trợ phát hiện:
  1. `CAND-REQ-003` có trạng thái không nhất quán: `APPROVED` trong Requirements nhưng `DRAFT` trong User Stories và TRACEABILITY.
  2. `OQ-034` được tham chiếu trong downstream artifacts nhưng không tồn tại trong canonical `open-questions.md`.
- Cách kiểm chứng:
  - Kiểm tra trực tiếp các artifact trong repository và đối chiếu ID/status giữa các file.
  - Không sử dụng output của AI làm nguồn có thẩm quyền.
- Quyết định xử lý:
  - Không tự ý thay đổi trạng thái `CAND-REQ-003`.
  - Không tự tạo `OQ-034`.
  - Đánh dấu hai vấn đề để BA/team xác nhận trước khi cập nhật artifact.