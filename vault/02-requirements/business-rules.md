# Quy tắc nghiệp vụ Warehouse

## Trạng thái hiện tại

Có hai business rule được human review và phê duyệt từ Research Synthesis v1; các quy tắc chi tiết khác vẫn là `TBD`.

Tên quy trình và các khái niệm domain đã xác nhận chưa đủ để suy ra ngưỡng phê duyệt, chuyển trạng thái, cách tính tồn kho, hành vi ngoại lệ, quy tắc phân quyền hoặc quy tắc kiểm tra hợp lệ.

Quy tắc trong tương lai phải dùng stable ID, dẫn bằng chứng, xác định yêu cầu/User Story bị ảnh hưởng và được con người phê duyệt.

## Khu vực cần discovery — chưa phải quy tắc

- Trạng thái tồn kho và ý nghĩa các loại số lượng
- Điều kiện bắt đầu và hoàn tất Receive, Putaway, Pick, Transfer, Adjust và Audit
- Hành vi khi thực hiện một phần
- Hành vi khi tồn kho âm
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

Phạm vi áp dụng, exception, bằng chứng cần lưu, approval và role authority của các candidate rule trên vẫn là `TBD` / `OPEN QUESTION`.
