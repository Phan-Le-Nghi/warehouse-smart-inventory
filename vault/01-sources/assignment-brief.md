# Assignment Brief — Bản tóm tắt được bảo tồn

## Provenance của nguồn

| Source ID | Nguồn do giảng viên cung cấp | Mục đích sử dụng trong scaffold | Metadata hiện có |
|---|---|---|---|
| `SRC-01` | `MIS3032_1_Aug2026_Plan_Master / De_Tai / Group 10` | Thông tin dự án Nhóm 10 đã được giảng viên xác nhận | File/vị trí, phiên bản, trang/mục và URL: TBD |
| `SRC-02` | `Output_BaoCao` | Yêu cầu môn học/báo cáo và theo dõi artifact Report Round 1 | File/vị trí, phiên bản, trang/mục và URL: TBD |
| `SRC-03` | `Giao_trinh_Thuc_hanh_Lap_trinh_Ung_dung_Doanh_nghiep_AI_Thuc_hanh_Chi_tiet_2026` | Phương pháp làm việc và hướng dẫn thực hành của môn học | File/vị trí, phiên bản, trang/mục và URL: TBD |
| `SRC-04` | `Huong_dan_Thuc_hanh_VSCode_Codex_Vault_VoiceCommerce_v2` | Hướng dẫn VS Code + Codex + Project Vault và triết lý tham chiếu | File/vị trí, phiên bản, trang/mục và URL: TBD |

Các file gốc do giảng viên cung cấp chưa có trong repository này. Vị trí chính xác và tham chiếu trang/mục vẫn là TBD. Không suy đoán URL, phiên bản, ngày xuất bản hoặc số trang.

File này bảo tồn các đoạn thông tin do con người cung cấp để tạo scaffold repository. Không được viết lại nguồn cho phù hợp với kết luận sản phẩm về sau.

## Thông tin dự án đã được giảng viên xác nhận

Provenance: `SRC-01` — `MIS3032_1_Aug2026_Plan_Master / De_Tai / Group 10`, theo xác nhận rõ ràng của người review.

- Project: Warehouse & Smart Inventory Management
- Bài toán nghiệp vụ: kiểm soát nhập/xuất/chuyển kho và tồn
- Role tối thiểu: Warehouse Staff, Manager, Purchasing, Admin
- Quy trình bắt buộc: Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit
- Hướng AI: Inventory Q&A; Explain inventory anomalies; Reorder recommendation
- Core domain: SKU, Warehouse, Stock, Movement, Transfer, Alert, Audit
- Quy mô nhóm: 5 thành viên
- Mỗi sinh viên phải sở hữu ít nhất một User Story hoàn chỉnh end-to-end.

## Phương pháp và hướng dẫn làm việc

Provenance: `SRC-03` và `SRC-04`. Mục/trang nguồn chính xác là TBD.

`Requirement -> Vault -> User Story -> Codex Plan -> Artifact / Code -> Test -> Review -> Traceability -> Release`

## Yêu cầu môn học/báo cáo

Provenance: `SRC-02` — `Output_BaoCao`. Mục/trang nguồn chính xác là TBD.

- Hạn: 04/09/2026
- Đánh giá cả Bài 1 và Bài 2.

### Deliverable Bài 1

1. Project Charter
2. User Research + Synthesis
3. Requirements + Business Rules
4. Project Vault
5. Vault Q&A Benchmark
6. AI Usage Log v1

Q&A Benchmark cần ít nhất 20 câu hỏi thuộc các loại fact, rule, edge case và unknown. Câu trả lời không có nguồn hỗ trợ phải trả về `KHÔNG ĐỦ DỮ LIỆU`.

### Deliverable Bài 2

1. PRD
2. User Flow
3. Functional Prototype
4. Usability Test
5. User Stories + Acceptance Criteria
6. Taiga Backlog
7. Figma + Design System
8. Architecture + ADR
9. ERD / Data Model
10. API Contract
11. Story Specs + Traceability v1

Mục tiêu hiện tại là 8–12 User Story thật, được dẫn xuất từ yêu cầu đã xác nhận. Acceptance Criteria phải có thể kiểm thử.

Các deliverable này là nghĩa vụ môn học/báo cáo, không phải ID yêu cầu sản phẩm Warehouse. Tiến độ được theo dõi trong [`docs/00-project-index.md`](../../docs/00-project-index.md).
