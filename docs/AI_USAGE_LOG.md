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

### AI-USE-006 — Repo Scaffold + CI baseline

- **Task:** Dựng application repository scaffold và CI baseline; không implement business feature.
- **Human-approved stack:** React + TypeScript + Vite/npm; Python 3.13 + FastAPI/uv/pytest/Ruff; PostgreSQL 18/Docker Compose; SQLAlchemy 2 + Alembic; Playwright; GitHub Actions.
- **AI/tool:** Codex đọc các technical source/decision liên quan, tạo scaffold/config/lockfile/test/workflow, chạy dependency tooling và local verification commands. AI không tự tạo business behavior, schema, migration hoặc API Putaway.
- **Output:** Frontend placeholder với unit/E2E smoke tests; FastAPI với technical `GET /health`; lazy SQLAlchemy engine/session infrastructure; PostgreSQL 18 Compose; `.env.example`; README; Git ignore rules; hai CI jobs frontend/backend.
- **Human verification:** Pending — con người cần review toàn bộ diff. Evidence local: `npm ci`, lint, typecheck, 1 unit test, build và 1 Playwright smoke test pass; `uv sync --locked`, Ruff lint/format check và 1 pytest pass. `docker compose config` không chạy được vì Docker CLI không có trên máy; không claim PostgreSQL runtime.
- **Human decision:** Stack là input đã được duyệt tại `DEC-020`; production authentication/deployment vẫn `TBD`. `US-PUT-001` và mọi business feature/schema/API vẫn Not started.
- **Artifact references:** [`../apps/README.md`](../apps/README.md), [`../apps/frontend/`](../apps/frontend/), [`../apps/backend/`](../apps/backend/), [`../apps/docker/compose.yml`](../apps/docker/compose.yml), [`../.github/workflows/ci.yml`](../.github/workflows/ci.yml), [`../vault/06-technical/README.md`](../vault/06-technical/README.md), [`../vault/06-technical/architecture.md`](../vault/06-technical/architecture.md), [`06-technical/architecture.md`](06-technical/architecture.md), [`00-project-index.md`](00-project-index.md), [`TRACEABILITY.md`](TRACEABILITY.md).

### AI-USE-007 — US-PUT-001 Vertical Slice implementation

- **Task:** Triển khai first vertical slice end-to-end cho `US-PUT-001`; không commit, push hoặc đổi trạng thái Taiga.
- **Context/Input:** Canonical Story/AC `US-PUT-001`, Technical Architecture, Data Model, API Contract, `ADR-001/002/003`, Technical Story Spec, Putaway report spec, Traceability, Taiga mapping và scaffold hiện có.
- **AI/tool:** Codex đọc context giới hạn, sửa source/config/docs bằng patch, dùng Ruff/pytest/npm/Vitest/Vite/Alembic cho verification. Không tạo product rule mới và không dùng AI output làm nguồn canonical.
- **Output:** Schema/migration tối thiểu; actor dependency boundary; context read và `POST /api/v1/putaways`; transactional allocation + location balance upsert; idempotency guard; structured errors; test-only fixture; React UI; API/component tests; Playwright thật; PostgreSQL 18 CI jobs.
- **Human verification:** Con người đã review Git diff và thực hiện local frontend/backend checks. GitHub Actions sau đó xác minh `backend-checks` trên PostgreSQL 18, `frontend-checks`, và `putaway-e2e` qua React → FastAPI → PostgreSQL 18. Backend CI ban đầu fail do thứ tự flush fixture vi phạm FK; nguyên nhân đã được điều tra, fixture ordering đã được sửa và cả push lẫn pull-request reruns đều pass.
- **Human decision:** Chấp nhận vertical slice sau khi review diff và CI evidence. Stack, technical contracts và fixture 16 units là input đã duyệt; AI không tự quyết business behavior. Full placement chỉ là test scope; `OQ-012`, `OQ-013`, `OQ-014`, production authentication và deployment vẫn OPEN/TBD.
- **Actual verification commands/results (2026-09-05):** `$env:NODE_OPTIONS='--use-system-ca'; npm.cmd ci --cache .npm-cache --no-audit --no-fund` pass (`259 packages`); frontend lint/typecheck pass; Vitest `3 passed`; Vite build pass; Ruff lint/format-check pass; pytest `8 passed` trên SQLite component database; Alembic upgrade và downgrade smoke pass trên SQLite tạm. `uv sync --locked` không chạy vì `uv` không có trong PATH, nhưng checked-in `.venv` executables chạy được. Docker CLI không có, vì vậy PostgreSQL integration và `TEST-PUT-E2E-001` không chạy local và không được claim Pass.
- **Artifact references:** [`../apps/backend/alembic/`](../apps/backend/alembic/), [`../apps/backend/src/warehouse_api/`](../apps/backend/src/warehouse_api/), [`../apps/backend/tests/test_putaway.py`](../apps/backend/tests/test_putaway.py), [`../apps/frontend/src/App.tsx`](../apps/frontend/src/App.tsx), [`../apps/frontend/e2e/putaway.spec.ts`](../apps/frontend/e2e/putaway.spec.ts), [`../.github/workflows/ci.yml`](../.github/workflows/ci.yml), [`TRACEABILITY.md`](TRACEABILITY.md).

### AI-USE-008 — CI failure diagnosis and verification

- **Task:** Diagnose the initial `US-PUT-001` backend CI failure and verify the corrected vertical slice.
- **Input/context:** Failed PostgreSQL 18 backend check, Putaway test fixture, SQLAlchemy model relationships, CI workflow, and the already-approved `US-PUT-001` behavior/contracts.
- **Tool:** Codex supported repository inspection and failure diagnosis; GitHub Actions executed the authoritative CI checks.
- **Output:** Identified fixture foreign-key ordering as the cause: `Warehouse` and `InternalLocation` were not flushed in dependency order under PostgreSQL FK enforcement, while the earlier local SQLite path did not enforce the same FK behavior by default. The fixture was ordered as Warehouse → flush → InternalLocation → flush → SKU → Receive → ReceiveLine → StockBalance.
- **Human verification:** Human reviewed the Git diff and local checks, inspected the failure/fix, and confirmed successful GitHub Actions reruns for both push and pull-request events: `backend-checks`, `frontend-checks`, and `putaway-e2e` all passed.
- **Decision:** Accept the fixture-ordering correction and the vertical slice based on the resulting evidence. No business behavior, canonical Acceptance Criterion, production authentication, or deployment decision was changed.
- **Evidence:** [`../apps/backend/tests/test_putaway.py`](../apps/backend/tests/test_putaway.py), [`../apps/frontend/e2e/putaway.spec.ts`](../apps/frontend/e2e/putaway.spec.ts), [`../.github/workflows/ci.yml`](../.github/workflows/ci.yml), [`TRACEABILITY.md`](TRACEABILITY.md).
- **Time impact:** Not measured; the diagnosis isolated the PostgreSQL-specific fixture issue and supported a focused rerun.

### AI-USE-009 — Human-confirmed Taiga status documentation sync

- **Task:** Đồng bộ tài liệu repository với trạng thái Taiga của `US-PUT-001` sau khi evidence đã pass.
- **Input/context:** Human xác nhận Taiga Story [#8](https://tree.taiga.io/project/lenghi-group-07-project/us/8) và Tasks [#19](https://tree.taiga.io/project/lenghi-group-07-project/task/19), [#20](https://tree.taiga.io/project/lenghi-group-07-project/task/20), [#21](https://tree.taiga.io/project/lenghi-group-07-project/task/21) đã được cập nhật thủ công thành `Done`.
- **AI/tool:** Codex chỉ đồng bộ các trạng thái đã được human xác nhận vào tài liệu và kiểm tra Git diff; AI không thao tác Taiga, không sửa application code, business rule hoặc canonical Acceptance Criteria.
- **Human decision:** Human cập nhật trạng thái Taiga sau khi Technical Story Spec, implementation merge, frontend checks, backend PostgreSQL 18 checks, Playwright E2E và Traceability evidence đã pass.
- **Scope guard:** First vertical slice được ghi nhận `Completed / Verified`; không claim toàn bộ MVP Done. `OQ-012`, `OQ-013`, `OQ-014`, production authentication và deployment giữ nguyên trạng thái.
- **Human verification:** Chờ human review documentation diff trước khi tích hợp; không commit hoặc push trong lần đồng bộ này.

### AI-USE-010 — Q&A Benchmark Round 1 human-review finalization

- **Task:** Finalize trạng thái human review cho Q&A Benchmark Round 1 gồm 20 câu.
- **AI support:** AI đọc Vault, tạo Actual answer draft, so khớp Expected answer với Actual answer và tính score draft.
- **AI authority guard:** AI không tự xác nhận benchmark, không tự approve/reject score và không dùng output AI làm evidence có thẩm quyền.
- **Human verification:** Human đã kiểm tra Expected answer, Actual answer, supporting source và score của 20 câu.
- **Human responsibility and decision:** Human chịu trách nhiệm verify source, approve/reject score và đã chấp nhận benchmark cuối cùng với Total 20, Correct 20, Partial 0, Wrong 0, Unsupported 0, Accuracy 100%.
- **Scope guard:** Không thay đổi Question, Expected answer, Actual answer, Result hoặc supporting source; không đóng `OQ-013`, `OQ-014`, `OQ-027`, `OQ-029` hay Open Question nào khác.
- **Artifact references:** [`../vault/09-ai/qa-benchmark.md`](../vault/09-ai/qa-benchmark.md), [`../vault/00-index.md`](../vault/00-index.md), [`00-project-index.md`](00-project-index.md).
