# Group Round 1 Report — Warehouse & Smart Inventory Management

## 1. Project Overview

Warehouse & Smart Inventory Management có MVP giới hạn trong **một Warehouse**, hỗ trợ sáu workflow cốt lõi: **Receive, Putaway, Pick, Internal Transfer, Audit và Adjust**. Baseline duy trì `system stock quantity` theo internal location và tính Warehouse total từ tổng quantity tại các location.

Round 1 hiện bao phủ product baseline, design/prototype artifacts, Technical Foundation, repo/CI baseline và first vertical slice `US-PUT-001` đã hoàn thành theo recorded verification evidence. Báo cáo này không tuyên bố full MVP đã được implement, production-ready, deployed, tất cả story đã được code hoặc production authentication đã hoàn tất.

## 2. Round 1 Highlights

| ID | Highlight | Evidence và verification boundary |
|---|---|---|
| `H-01` | Problem, objective và MVP scope đã được phê duyệt: một Warehouse, sáu workflow và per-location stock baseline. | [Project Charter](../01-discovery/project-charter.md), [PRD](../03-product/PRD.md), [MVP Scope](../03-product/mvp-scope.md); human-approved baseline. |
| `H-02` | Research có ba participant `P1/P2/P3` và evidence `EVD-001–019`. | [User Research](../01-discovery/user-research.md), [Research Evidence](../../vault/01-sources/research-evidence.md); cả ba cùng một minimart nên không generalize cho mọi Warehouse. |
| `H-03` | Requirements baseline gồm **12 active FR, 5 canonical NFR và 15 Business Rules**, với priority coverage đầy đủ. | [Requirements and Business Rules](../02-requirements/requirements-and-business-rules.md), [canonical requirements](../../vault/02-requirements/requirements.md); các OQ chưa quyết định vẫn được giữ mở. |
| `H-04` | Q&A Benchmark đạt **20/20 Correct, 100%**, đã được human review. | [Q&A Benchmark](../../vault/09-ai/qa-benchmark.md). |
| `H-05` | Backlog có **9 canonical User Stories**, kèm ownership và traceability. | [User Stories](../04-backlog/user-stories.md), [Story Ownership](../../vault/04-product/story-ownership.md), [Traceability](../TRACEABILITY.md); chỉ `US-PUT-001` đã được implement. |
| `H-06` | Taiga ghi nhận **6 Epics, 9 Stories và 27 Tasks**. | [Taiga Backlog](../04-backlog/taiga-backlog.md), [External Tools](../../vault/04-product/external-tools.md); đây là repository-recorded/API read-back evidence, không phải live verification trong phiên lập report. |
| `H-07` | Prototype được mô tả bằng **10 base screens, 3 critical flows và 3 participant findings**. | [Screen Inventory](../05-design/screen-inventory.md), [Usability Findings](../05-design/usability-findings.md); exact Figma frame parity và raw usability provenance vẫn là limitation. |
| `H-08` | Technical Foundation dùng modular monolith, React/FastAPI/PostgreSQL và có ba ADR. | [Architecture](../06-technical/architecture.md), [canonical technical foundation](../../vault/06-technical/README.md); phần ngoài Putaway chủ yếu vẫn là foundation/conceptual contract. |
| `H-09` | First vertical slice `US-PUT-001` đi qua React → FastAPI → PostgreSQL 18, Alembic migration, automated tests, Playwright và recorded CI evidence. | [Putaway Story Spec](../06-technical/story-specs/putaway.md), [Traceability](../TRACEABILITY.md), [CI workflow](../../.github/workflows/ci.yml); đây chỉ là first slice, không phải full MVP implementation. |
| `H-10` | Traceability và AI Usage Log duy trì provenance, human verification và scope guards. | [Traceability](../TRACEABILITY.md), [AI Usage Log](../AI_USAGE_LOG.md). |

## 3. Bài 1 Status

| Artifact | Status | Evidence | Remaining action |
|---|---|---|---|
| Charter | **PASS** | [Project Charter](../01-discovery/project-charter.md); human-approved và đã merge trong current branch baseline | Duy trì consistency khi quyết định canonical thay đổi. |
| Research | **PARTIAL** | [User Research](../01-discovery/user-research.md); `P1/P2/P3`, `EVD-001–019` được bảo tồn | Giữ giới hạn một minimart; raw recording, consent artifact và participant quote không có trong repository. |
| Requirements / BR / NFR | **PASS** | [Requirements and Business Rules](../02-requirements/requirements-and-business-rules.md) | Không biến `OPEN/TBD` thành approved behavior. |
| Project Vault | **PASS** | [Vault Index](../../vault/00-index.md) | Tiếp tục dùng Vault làm canonical source of truth. |
| Q&A Benchmark | **PASS** | [Q&A Benchmark](../../vault/09-ai/qa-benchmark.md) | Giữ stable question/source mapping khi cập nhật. |
| AI Usage Log | **PARTIAL** | [AI Usage Log](../AI_USAGE_LOG.md) | Hoàn thiện member attribution và individual Round 1 evidence cho đủ năm thành viên. |

## 4. Bài 2 Status

| Artifact | Status | Evidence | Remaining action |
|---|---|---|---|
| PRD / MVP Scope | **PASS** | [PRD](../03-product/PRD.md), [MVP Scope](../03-product/mvp-scope.md) | Giữ ranh giới `IN`, `OPEN/TBD` và `OUT/DEFERRED`. |
| Prototype | **PARTIAL** | [Functional Prototype](../03-product/functional-prototype.md), [Screen Inventory](../05-design/screen-inventory.md) | Đối chiếu 10 logical screens với exact Figma frames. |
| Usability | **PARTIAL** | [Usability Test](../03-product/usability-test.md), [Findings](../05-design/usability-findings.md) | Raw notes/recording/consent hiện không có; chỉ dùng human-reviewed findings. |
| User Stories | **PASS** | [9 canonical stories](../04-backlog/user-stories.md) | Baseline đạt; tám story ngoài `US-PUT-001` chưa được implement. |
| Taiga | **PARTIAL** | [Taiga Backlog](../04-backlog/taiga-backlog.md) | Live-verify refs/status/access nếu cần cho trình bày. |
| Figma / Design System | **PARTIAL** | [Design System](../05-design/design-system.md) | Xác minh access, version và exact frame parity. |
| Technical Foundation | **PASS** | [Architecture](../06-technical/architecture.md), [Data Model](../06-technical/data-model.md), [API](../06-technical/API.md) | Thực hiện story-specific technical review cho các slice sau. |
| Repo / CI baseline | **PASS** | [Apps README](../../apps/README.md), [CI workflow](../../.github/workflows/ci.yml) | PASS theo recorded evidence; không suy rộng thành full-MVP verification. |
| Vertical Slice | **PASS** | [Putaway Story Spec](../06-technical/story-specs/putaway.md), [Traceability](../TRACEABILITY.md) | Chỉ `US-PUT-001`; production auth/deployment vẫn TBD. |
| Traceability | **PASS** | [Traceability](../TRACEABILITY.md) | Cập nhật khi approved behavior, implementation hoặc test thay đổi. |

## 5. First Vertical Slice Evidence

First vertical slice `US-PUT-001` có trace:

`Requirement / Decision` → Taiga Story [#8](https://tree.taiga.io/project/lenghi-group-07-project/us/8) → Tasks [#19](https://tree.taiga.io/project/lenghi-group-07-project/task/19), [#20](https://tree.taiga.io/project/lenghi-group-07-project/task/20), [#21](https://tree.taiga.io/project/lenghi-group-07-project/task/21) → `PF-01` / `SCR-03` → [Technical Story Spec](../06-technical/story-specs/putaway.md) → React UI → `POST /api/v1/putaways` → Alembic migration → backend tests → Playwright → GitHub Actions recorded PASS → Taiga Done.

Recorded evidence cho biết `backend-checks` đã chạy với PostgreSQL 18, `frontend-checks` đã pass và `putaway-e2e` đã đi qua React → FastAPI → PostgreSQL 18. Các kết quả này được ghi tại [Traceability](../TRACEABILITY.md); chúng không được live-verify lại trong phiên lập report và không phải bằng chứng rằng full MVP đã được implement.

## 6. Open Risks

| Risk ID | Risk | Impact | Current mitigation | Owner / TBD | Related OQ / artifact |
|---|---|---|---|---|---|
| `R-01` | Lot/batch, serial, expiry và UOM/conversion chưa quyết định. | Data model và quantity contract chưa thể mở rộng an toàn cho các trường hợp này. | Slice hiện dùng integer quantity như technical simplification và giữ boundary rõ. | TBD | `OQ-012`; [Data Model](../06-technical/data-model.md) |
| `R-02` | Lifecycle, completion và handoff còn khoảng trống. | Một số workflow chưa có contract end-to-end hoàn chỉnh. | Chỉ mô tả behavior đã duyệt; giữ gap trong PRD và Traceability. | TBD | `OQ-013`; [PRD](../03-product/PRD.md) |
| `R-03` | Partial Receive, Putaway và Transfer chưa quyết định. | Có thể gây hiểu sai status, validation hoặc stock effect. | Full 16-unit Putaway chỉ được ghi là fixture scope, không phải business rule. | TBD | `OQ-014`; [Putaway Story Spec](../06-technical/story-specs/putaway.md) |
| `R-04` | Production authentication và deployment target còn TBD. | Chưa thể claim production-ready hoặc deployed. | Architecture có actor/auth boundary; test actor chỉ dùng trong controlled tests. | TBD | `OQ-032`; [Architecture](../06-technical/architecture.md) |
| `R-05` | Research chỉ có ba participant tại cùng một minimart. | Khả năng tổng quát hóa sang mọi Warehouse bị giới hạn. | Giới hạn claim vào context đã nghiên cứu và dẫn `EVD-001–019`. | TBD | [User Research](../01-discovery/user-research.md) |
| `R-06` | Figma access, version và frame parity chưa được independently verified đầy đủ. | Chưa thể bảo đảm visual frames khớp logical screen inventory. | Lưu Figma URL và 10-screen inventory để human đối chiếu. | TBD | [Design System](../05-design/design-system.md); [External Tools](../../vault/04-product/external-tools.md) |
| `R-07` | Repository không có raw usability recording hoặc consent artifact. | Findings không thể được independently audited từ raw session evidence. | Chỉ trình bày human-reviewed findings; không tạo quote hoặc session evidence. | TBD | [Usability Test Script](../05-design/usability-test-script.md); [Findings](../05-design/usability-findings.md) |
| `R-08` | Tám trong chín canonical stories chưa được implement. | Full MVP hiện chưa hoàn thành. | Traceability ghi rõ status từng story; chỉ claim first Putaway slice. | TBD | [Traceability](../TRACEABILITY.md) |
| `R-09` | Quantitative production NFR cho performance, uptime và load chưa quyết định. | Chưa đủ target để đánh giá production readiness định lượng. | Duy trì năm NFR đã duyệt và theo dõi phần định lượng còn mở. | TBD | `OQ-033`; [PRD](../03-product/PRD.md) |

## 7. Open Questions / Deferred Items

### OPEN / TBD

- `OQ-012`: lot/batch, serial, expiry, UOM/conversion.
- `OQ-013`: các phần lifecycle, completion, exception và handoff chưa quyết định.
- `OQ-014`: partial Receive, Putaway và Transfer.
- `OQ-021`: định nghĩa Alert trigger/recipient.
- `OQ-022`: device, barcode/QR, mobile/offline và external integration.
- `OQ-032`: production authentication và deployment.
- `OQ-033`: quantitative NFR và operating/deployment context.

### OUT / DEFERRED — current MVP

- AI implementation/directions.
- Alert implementation; định nghĩa Alert tại `OQ-021` vẫn là câu hỏi mở riêng.
- Multi-Warehouse.
- Cross-Warehouse Transfer.

Các mục `OPEN/TBD` không được xem là permanently out of scope.

## 8. Team Contribution Summary

| Thành viên | Evidence-backed contribution |
|---|---|
| **Nguyễn Thị Nghĩa** | Phụ trách UX/UI và Receive; đóng góp research synthesis, user flow, prototype và usability artifacts. Figma parity còn chờ xác minh. |
| **Phan Lê Nghi** | Phụ trách Engineering và Putaway, hỗ trợ Audit; xây dựng Technical Foundation và first Putaway vertical slice có recorded CI evidence. |
| **Trương Huỳnh Thảo Ngân** | Phụ trách QA/Release và Pick; tham gia usability artifacts và điều phối backlog Taiga. |
| **Nguyễn Thị Ly Na** | Phụ trách AI/Vault và Transfer; duy trì Vault, Q&A Benchmark, AI Usage Log và consistency/traceability. |
| **Đặng Thị Thanh Ngân** | Phụ trách Product/BA và Adjust; dẫn dắt Charter, Requirements, PRD và MVP Scope baseline. |

## 9. Next Steps

1. Xác minh phần Figma/design evidence còn lại, gồm access, version và exact frame parity.
2. Xác minh evidence trên Taiga, Figma và GitHub Actions nếu cần dùng trực tiếp khi trình bày.
3. Hoàn thiện individual Round 1 evidence và AI Usage Log attribution cho đủ năm thành viên.
4. Đóng các Open Question ưu tiên khi có human/business evidence phù hợp.
5. Triển khai các canonical story còn lại trong phase sau; đây không phải điều kiện được suy diễn thêm để hoàn tất Bài 2 Round 1.
