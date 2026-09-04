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

### AI-USE-004 — Taiga backlog synchronization

- **Task:** Taiga backlog synchronization.
- **Context/Input:** Project metadata, write plan đã được con người phê duyệt và các nguồn repository gồm Project Index, canonical backlog, Traceability, story ownership và external-tools metadata.
- **Tool:** Codex CLI dùng `fetch` tích hợp sẵn của Node.js với Taiga REST API, dưới sự phê duyệt rõ ràng của con người, để tạo và đọc lại các Taiga backlog items; credentials/tokens không được lưu trong repository.
- **Output:** Tạo 6 Epics, 9 canonical User Stories và 27 Tasks trong Taiga, đọc lại để kiểm tra mapping/status, rồi đồng bộ refs/statuses vào tài liệu repository.
- **Human verification:** Con người đã review/phê duyệt write plan và phải kiểm tra các Taiga refs/statuses cuối cùng trước khi tích hợp.
- **Human decision:** Product scope, canonical IDs, ownership, Acceptance Criteria và business behavior là đầu vào đã được con người phê duyệt; AI không độc lập quyết định hoặc mở rộng các nội dung này.
- **Artifact references:** [`00-project-index.md`](00-project-index.md), [`04-backlog/taiga-backlog.md`](04-backlog/taiga-backlog.md), [`04-backlog/user-stories.md`](04-backlog/user-stories.md), [`TRACEABILITY.md`](TRACEABILITY.md), [`../vault/04-product/external-tools.md`](../vault/04-product/external-tools.md).

### AI-USE-005 — Technical Foundation synthesis

- **Task:** Tổng hợp và ghi Technical Foundation documentation; chưa scaffold hoặc implement application.
- **Human-approved technical inputs:** React, TypeScript, Vite, npm; Python 3.13, FastAPI, uv, pytest; PostgreSQL 18, Docker; Playwright; SQLAlchemy 2, Alembic; modular monolith; authoritative stock theo SKU/location; derived Warehouse total; transactional/non-negative guards; Receive records actual quantity và Putaway performs initial posting.
- **AI/tool:** Codex đọc các canonical product/decision artifacts, soạn Markdown và chạy read-only/diff verification commands. AI không tự quyết architecture hoặc product behavior.
- **Output:** Canonical technical index, architecture, conceptual/vertical-slice data model, proposed API contract, 3 ADR, `US-PUT-001` technical Story Spec và report-facing/traceability updates.
- **Human verification:** Pending — con người cần review diff, xác nhận technical contract wording, route/payload/error proposal và ranh giới conceptual model trước integration.
- **Human decision:** Technical stack, persistence tooling, modular-monolith boundary và nội dung 3 ADR là human-approved inputs. `OQ-012`, `OQ-013`, `OQ-014`, production authentication, deployment, Adjust representation, attachment storage, advanced pagination/filtering và NFR vẫn OPEN/TBD.
- **Artifact references:** [`../vault/06-technical/README.md`](../vault/06-technical/README.md), [`../vault/08-decisions/decision-log.md`](../vault/08-decisions/decision-log.md), [`06-technical/architecture.md`](06-technical/architecture.md), [`06-technical/data-model.md`](06-technical/data-model.md), [`06-technical/API.md`](06-technical/API.md), [`06-technical/story-specs/putaway.md`](06-technical/story-specs/putaway.md), [`TRACEABILITY.md`](TRACEABILITY.md).
