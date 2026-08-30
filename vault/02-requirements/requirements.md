# Yêu cầu sản phẩm Warehouse

File này chỉ chứa yêu cầu sản phẩm/nghiệp vụ Warehouse được dẫn xuất từ bối cảnh dự án đã được giảng viên xác nhận và, về sau, từ nghiên cứu đã được kiểm chứng. Không đưa deliverable môn học/báo cáo vào đây.

## Bối cảnh sản phẩm đã được giảng viên xác nhận

Các mục dưới đây chỉ bảo tồn phát biểu phạm vi đã được giảng viên xác nhận rõ ràng. Chúng không ngầm xác định hành vi hệ thống chi tiết.

| ID | Loại | Nội dung | Nguồn | Trạng thái |
|---|---|---|---|---|
| REQ-001 | Bài toán nghiệp vụ | Kiểm soát nhập, xuất, chuyển kho và tồn kho. | `SRC-01`, đoạn xác nhận nguyên văn: “Business problem: Kiểm soát nhập/xuất/chuyển kho và tồn.” | CONFIRMED bài toán; hành vi giải pháp TBD |
| REQ-002 | Phạm vi quy trình bắt buộc | Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit | `SRC-01`, đoạn xác nhận nguyên văn: “Required workflow: Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit” | CONFIRMED các khu vực quy trình và chuỗi đã nêu; trigger, trạng thái, ngoại lệ và ý nghĩa trình tự TBD |
| REQ-003 | Phạm vi role tối thiểu | Warehouse Staff; Manager; Purchasing; Admin | `SRC-01`, đoạn xác nhận nguyên văn: “Minimum roles: Warehouse Staff, Manager, Purchasing, Admin” | CONFIRMED tên role tối thiểu; quyền hạn và hành vi TBD |
| REQ-004 | Phạm vi core domain | SKU; Warehouse; Stock; Movement; Transfer; Alert; Audit | `SRC-01`, đoạn xác nhận nguyên văn: “Core domain: SKU, Warehouse, Stock, Movement, Transfer, Alert, Audit” | CONFIRMED thuật ngữ domain; định nghĩa, quan hệ, thuộc tính và hành vi TBD |

`SRC-01` được xác định trong [`../01-sources/assignment-brief.md`](../01-sources/assignment-brief.md) là bối cảnh dự án Nhóm 10 được giảng viên xác nhận từ `MIS3032_1_Aug2026_Plan_Master / De_Tai / Group 10`. Các đoạn nguyên văn phía trên là phát biểu do con người cung cấp và xác nhận để dùng cho scaffold này.

## Hướng AI đã xác nhận

Các mục này được giữ riêng khỏi yêu cầu sản phẩm đã cam kết vì giảng viên mô tả chúng là hướng tính năng AI. Chúng chưa phải yêu cầu tính năng chi tiết hoặc đã có Acceptance Criteria.

| ID | Loại | Nội dung | Nguồn | Trạng thái |
|---|---|---|---|---|
| AI-DIR-001 | Hướng tính năng AI | Inventory Q&A | `SRC-01`, đoạn xác nhận nguyên văn: “AI feature direction: Inventory Q&A” | CONFIRMED hướng; phạm vi tính năng và Acceptance Criteria TBD |
| AI-DIR-002 | Hướng tính năng AI | Explain inventory anomalies | `SRC-01`, đoạn xác nhận nguyên văn: “AI feature direction: Explain inventory anomalies” | CONFIRMED hướng; định nghĩa anomaly, bằng chứng và Acceptance Criteria TBD |
| AI-DIR-003 | Hướng tính năng AI | Reorder recommendation | `SRC-01`, đoạn xác nhận nguyên văn: “AI feature direction: Reorder recommendation” | CONFIRMED hướng; đầu vào, thẩm quyền, biện pháp an toàn và Acceptance Criteria TBD |

## Quy tắc tiếp nhận yêu cầu

Yêu cầu mới phải dẫn xác nhận của giảng viên hoặc bằng chứng nghiên cứu đã được kiểm chứng, có stable ID và được con người review. Không được âm thầm nâng giả định hoặc đề xuất AI thành yêu cầu.
