# Quy tắc nghiệp vụ Warehouse

## Trạng thái hiện tại

Hai business rule được human review từ Research Synthesis v1 được bảo tồn. Mười hai business rule bổ sung được phê duyệt như HUMAN PRODUCT DECISIONS / MVP ASSUMPTIONS từ Round 2; `CAND-BR-015` được phê duyệt sau đó cho baseline Product Definition. Các rule dựa trên decision không phải verified research findings.

Tên quy trình và các khái niệm domain đã xác nhận chưa đủ để suy ra ngưỡng phê duyệt, chuyển trạng thái, cách tính tồn kho, hành vi ngoại lệ, quy tắc phân quyền hoặc quy tắc kiểm tra hợp lệ.

Quy tắc trong tương lai phải dùng stable ID, dẫn bằng chứng, xác định yêu cầu/User Story bị ảnh hưởng và được con người phê duyệt.

## Khu vực cần discovery — chưa phải quy tắc

- Trạng thái tồn kho và ý nghĩa các loại số lượng
- Điều kiện bắt đầu và hoàn tất Receive, Putaway, Pick, Transfer, Adjust và Audit
- Hành vi khi thực hiện một phần
- Hành vi retry/cancel sau khi operation bị chặn bởi negative-stock guard
- Yêu cầu phê duyệt và bằng chứng
- Điều kiện kích hoạt và người nhận Alert
- Quyền của role

Tất cả mục trên vẫn là câu hỏi, chưa phải quy tắc được chấp nhận.

## Business Rules từ Research Synthesis v1

Các mục này được dẫn xuất có giới hạn từ vận hành hiện tại của một minimart và đã được human review. Phạm vi áp dụng không được mở rộng vượt quá wording và evidence được trích dẫn.

| ID | Candidate Business Rule | Evidence -> Insight | Trạng thái |
|---|---|---|---|
| CAND-BR-001 | Khi số lượng thực nhận khác số lượng kỳ vọng, việc ghi nhận Receive nên sử dụng số lượng thực nhận thay vì thay thế bằng số lượng kỳ vọng. | `EVD-002`, `EVD-003`, `EVD-004` -> minimart hiện chỉ nhập số lượng thực nhận khi có giao thiếu/chênh lệch. | APPROVED — human reviewed |
| CAND-BR-002 | Khi phát hiện chênh lệch giữa tồn thực tế và tồn hệ thống, phải kiểm tra lại trước khi thực hiện điều chỉnh tồn. | `EVD-012`, `EVD-017` -> vận hành hiện tại yêu cầu kiểm tra lại chênh lệch trước khi xử lý. | APPROVED — human reviewed |
| CAND-BR-003 | `system stock quantity` của một SKU được duy trì theo từng internal location. Warehouse total quantity của SKU bằng tổng quantity tại các internal locations. | `DEC-010` — HUMAN PRODUCT DECISION / MVP ASSUMPTION. | APPROVED — HUMAN PRODUCT DECISION |
| CAND-BR-004 | Khi Putaway được confirm, Putaway quantity được phân bổ vào destination internal location đã xác nhận. Putaway không tự tạo Transfer hoặc Movement system record. | `DEC-011` — HUMAN PRODUCT DECISION / MVP ASSUMPTION. | APPROVED — HUMAN PRODUCT DECISION |
| CAND-BR-005 | Khi Pick được confirm, confirmed Pick quantity được giảm tại source internal location hoặc các source internal locations tương ứng. | `DEC-012` — HUMAN PRODUCT DECISION / MVP ASSUMPTION. | APPROVED — HUMAN PRODUCT DECISION |
| CAND-BR-006 | Pick chỉ được xem là fully completed khi full requested quantity đã được lấy và confirm. Nếu không đủ quantity, Pick phải được ghi `PARTIAL / INSUFFICIENT` và chưa được xem là fully completed. | `DEC-012` — HUMAN PRODUCT DECISION / MVP ASSUMPTION. | APPROVED — HUMAN PRODUCT DECISION |
| CAND-BR-007 | Khi Transfer được confirm, Transfer quantity được giảm tại source internal location và tăng cùng quantity tại destination internal location. Internal Transfer không làm thay đổi Warehouse total quantity. | `DEC-013` — HUMAN PRODUCT DECISION / MVP ASSUMPTION. | APPROVED — HUMAN PRODUCT DECISION |
| CAND-BR-008 | Một confirmed Transfer phải có system Transfer record gồm tối thiểu SKU, quantity, source internal location, destination internal location và confirmation timestamp. | `DEC-013` — HUMAN PRODUCT DECISION / MVP ASSUMPTION. | APPROVED — HUMAN PRODUCT DECISION |
| CAND-BR-009 | Audit phải so sánh physical count với `system stock quantity` tại selected scope/location và ghi nhận kết quả so sánh. | `DEC-014` — HUMAN PRODUCT DECISION / MVP ASSUMPTION; `EVD-015`, `EVD-016` chỉ hỗ trợ current-state count/compare. | APPROVED — HUMAN PRODUCT DECISION |
| CAND-BR-010 | Audit discrepancy không được tự động apply Adjust. Discrepancy phải được re-check và chuyển sang review riêng trước khi Adjust được cân nhắc. | `DEC-014`, `DEC-015` — HUMAN PRODUCT DECISION / MVP ASSUMPTION; bảo tồn re-check rule tại `CAND-BR-002`. | APPROVED — HUMAN PRODUCT DECISION |
| CAND-BR-011 | Adjust chỉ được apply sau khi discrepancy đã được re-check, Adjust reason đã được ghi nhận và Manager đã approve. | `DEC-015` — HUMAN PRODUCT DECISION / MVP ASSUMPTION. | APPROVED — HUMAN PRODUCT DECISION |
| CAND-BR-012 | Attachment/evidence là optional đối với Adjust trong MVP. | `DEC-015` — HUMAN PRODUCT DECISION / MVP ASSUMPTION. | APPROVED — HUMAN PRODUCT DECISION |
| CAND-BR-013 | Approved Adjust cập nhật `system stock quantity` tại affected internal location. Nếu re-check không còn discrepancy hoặc Manager reject, quantity không được thay đổi. | `DEC-015` — HUMAN PRODUCT DECISION / MVP ASSUMPTION. | APPROVED — HUMAN PRODUCT DECISION |
| CAND-BR-014 | Khi system reference và document reference khác nhau, Receive không được tự chọn authoritative source; user phải review reference mismatch trước khi hoàn tất Receive. | `DEC-016` — HUMAN PRODUCT DECISION / MVP ASSUMPTION. | APPROVED — HUMAN PRODUCT DECISION |
| CAND-BR-015 | `system stock quantity` tại internal location không được phép âm. Pick không được confirm vượt tổng quantity tại các selected source locations; Transfer không được confirm vượt source location quantity; Adjust không được tạo affected-location quantity nhỏ hơn 0. Nếu validation không đạt, không apply quantity change và operation được báo không hợp lệ/không thể confirm. | `DEC-019` — HUMAN PRODUCT DECISION / MVP ASSUMPTION; resolve `OQ-015`. | APPROVED — HUMAN PRODUCT DECISION |

Các khoảng trống chưa được quyết định vẫn là `TBD` / `OPEN QUESTION`, gồm partial Receive/Putaway/Transfer, lifecycle gaps tại `OQ-013`, retry/cancel behavior ngoài negative-stock guard và device/integration behavior tại `OQ-022`.
