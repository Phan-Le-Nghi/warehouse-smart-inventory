# Ownership của User Story và flow

Mỗi sinh viên cuối cùng phải sở hữu ít nhất một User Story hoàn chỉnh end-to-end. Ownership của role xuyên suốt không thay thế ownership của User Story.

## Ownership đã xác nhận

| Thành viên | User Story/flow cá nhân chính | Ownership/hỗ trợ bắt buộc bổ sung | Role xuyên suốt |
|---|---|---|---|
| Nghĩa | Receive | — | UX/UI |
| Nghi | Putaway | Sở hữu/hỗ trợ Audit ngoài Putaway | Engineering |
| Thảo Ngân | Pick | — | QA/Release |
| Ly Na | Transfer | — | AI/Vault |
| Thanh Ngân | Adjust | — | Product/BA |

## Traceability cuối cùng bắt buộc

Đối với User Story chính của mỗi sinh viên:

`Requirement -> User Story / Acceptance Criteria -> User Flow / Design / Spec -> Taiga task -> Implementation -> Test -> Evidence / Traceability`

## Trạng thái Story/flow hiện tại

| Flow | Story ID | Trạng thái |
|---|---|---|
| Receive | `US-REC-001` | BA CONFIRMED; `AC-01` đến `AC-03` |
| Putaway | `DRAFT-US-PUT-001` | DRAFT; chưa canonical |
| Pick | `DRAFT-US-PICK-001` | DRAFT / NEEDS HUMAN REVIEW |
| Transfer | `DRAFT-US-TRF-001` | DRAFT / NEEDS HUMAN REVIEW |
| Adjust | `DRAFT-US-ADJ-001` | DRAFT; chưa canonical |
| Audit | `DRAFT-US-AUD-001` | DRAFT; chưa canonical |

Hiện có **1** User Story BA CONFIRMED và **5** User Story DRAFT. Draft ID chỉ phục vụ theo dõi và không làm cho story, Acceptance Criteria, flow hoặc behavior trở thành canonical.

Chỉ được đạt mục tiêu tổng cộng 8–12 User Story bằng các Story dẫn xuất từ yêu cầu đã xác nhận.
