# Ownership của User Story và flow

Mỗi sinh viên cuối cùng phải sở hữu ít nhất một User Story hoàn chỉnh end-to-end. Ownership của role xuyên suốt không thay thế ownership của User Story.

## Ownership đã xác nhận

| Thành viên | Canonical User Story/flow | Ownership/hỗ trợ bắt buộc bổ sung | Role xuyên suốt |
|---|---|---|---|
| Nguyễn Thị Nghĩa | `US-REC-001` — Receive | — | UX/UI |
| Phan Lê Nghi | `US-PUT-001` — Putaway | `US-AUD-001`, `US-AUD-002` — Audit | Engineering |
| Trương Huỳnh Thảo Ngân | `US-PICK-001` — Pick | — | QA/Release |
| Nguyễn Thị Ly Na | `US-TRF-001`, `US-TRF-002` — Transfer | — | AI/Vault |
| Đặng Thị Thanh Ngân | `US-ADJ-001`, `US-ADJ-002` — Adjust | — | Product/BA |

## Traceability cuối cùng bắt buộc

Đối với User Story chính của mỗi sinh viên:

`Requirement -> User Story / Acceptance Criteria -> User Flow / Design / Spec -> Taiga task -> Implementation -> Test -> Evidence / Traceability`

## Canonical backlog hiện tại

| Flow | Story ID | Trạng thái |
|---|---|---|
| Receive | `US-REC-001` | CANONICAL — HUMAN APPROVED |
| Putaway | `US-PUT-001` | CANONICAL — HUMAN APPROVED |
| Pick | `US-PICK-001` | CANONICAL — HUMAN APPROVED |
| Transfer | `US-TRF-001`, `US-TRF-002` | CANONICAL — HUMAN APPROVED |
| Audit | `US-AUD-001`, `US-AUD-002` | CANONICAL — HUMAN APPROVED |
| Adjust | `US-ADJ-001`, `US-ADJ-002` | CANONICAL — HUMAN APPROVED |

Final backlog có **9 canonical User Stories** đã được human approve. Receive reference mismatch là AC/scenario trong `US-REC-001`; `PARTIAL / INSUFFICIENT` là AC/scenario trong `US-PICK-001`. Transfer, Audit và Adjust được tách theo actor/value đã duyệt.

Historical draft IDs được bảo tồn trong các artifact superseded khi cần audit history; chúng không còn là active backlog items.
