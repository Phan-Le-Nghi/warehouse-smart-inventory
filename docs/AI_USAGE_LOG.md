# AI Usage Log v1

## Trạng thái hiện tại

Log đã có các mục sử dụng AI; mỗi output vẫn cần human verification trước khi được tích hợp hoặc canonical hóa.

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
  2. Một ID Open Question không canonical về location cardinality được tham chiếu trong downstream artifacts nhưng không tồn tại trong canonical `open-questions.md`.
- Cách kiểm chứng:
  - Kiểm tra trực tiếp các artifact trong repository và đối chiếu ID/status giữa các file.
  - Không sử dụng output của AI làm nguồn có thẩm quyền.
- Quyết định xử lý:
  - Không tự ý thay đổi trạng thái `CAND-REQ-003`.
  - Không tự tạo stable Open Question ID cho location cardinality.
  - Đánh dấu hai vấn đề để BA/team xác nhận trước khi cập nhật artifact.

  ## AI-USE-002 — Draft Transfer Story và Traceability consistency review

* **Member:** Ly Na
* **Date:** 2026-09-03
* **Affected artifacts:** `docs/04-backlog/user-stories.md`, `docs/TRACEABILITY.md`
* **AI purpose:** Hỗ trợ kiểm tra consistency và draft User Story Transfer từ các requirement, evidence và open questions đã có trong Vault.
* **Scope:** `REQ-002`, `REQ-004`, `CAND-REQ-004`, `EVD-010`, `EVD-011`, `EVD-019`, `OQ-013`, `OQ-014`, `OQ-016`, `OQ-020`, `OQ-022`.
* **AI output:** Đề xuất Transfer draft story ID (hiện đã được chuẩn hóa thành `DRAFT-US-TRF-001`) và downstream trace tương ứng, đồng thời giữ các behavior chưa được xác nhận ở trạng thái `TBD` / `OPEN QUESTION`.
* **Human verification:** Đã đối chiếu lại với `requirements.md`, `research-evidence.md`, `open-questions.md`, `user-stories.md` và `TRACEABILITY.md`.
* **Consistency decision:** Giữ `CAND-REQ-004` ở trạng thái `DRAFT`; không biến `EVD-010` thành bằng chứng cho việc hệ thống bắt buộc có Transfer/Movement transaction riêng.
* **Scope guard:** Không xác nhận automatic Stock update, Movement transaction, location change, warehouse scope hoặc role permission khi chưa có requirement được phê duyệt.
* **Verification status:** AI output không phải nguồn authoritative; Product/BA review vẫn cần thiết trước khi canonical hóa Story.

### AI-USE-003 — Prototype / usability artifact synthesis

- **Task:** Tổng hợp prototype/usability artifacts cho 3 critical flows.
- **Context/Input:** PRD, MVP Scope, consolidated User Flow, canonical User Stories, Traceability, Decision Log, Figma URL và 3 bộ human-reviewed findings cho `P1`/`P2`/`P3`.
- **AI/tool:** Codex hỗ trợ đọc repository, soạn/cập nhật Markdown và kiểm tra diff; không đóng vai participant và không thực hiện usability session.
- **Output:** Usability Test Script, Usability Findings, Screen Inventory; cập nhật Project Index, Traceability và các landing/status links liên quan.
- **Human verification:** Pending — con người cần review diff, đối chiếu 10 logical base screens với exact Figma frames và xác nhận wording/state visibility trong prototype.
- **Human decision:** Findings và ba UX clarity decisions đầu vào đã được xác nhận là human-reviewed; không tạo Requirement/Business Rule mới và không tạo decision-log entry trùng các `DEC-012/014/015/018/019`.
- **Artifact link:** [`05-design/usability-test-script.md`](05-design/usability-test-script.md), [`05-design/usability-findings.md`](05-design/usability-findings.md), [`05-design/screen-inventory.md`](05-design/screen-inventory.md), [`TRACEABILITY.md`](TRACEABILITY.md).
