# Vault Q&A Benchmark

## Yêu cầu

- Có ít nhất 20 câu hỏi đã review trước Report Round 1.
- Phải bao phủ câu hỏi loại fact, rule, edge case và unknown.
- Khi bằng chứng không đủ, câu trả lời mong đợi là `KHÔNG ĐỦ DỮ LIỆU`.

## Trạng thái hiện tại

`TBD`: Câu hỏi benchmark, câu trả lời mong đợi, kết quả chạy và bản tổng hợp đạt/chưa đạt chưa được soạn hoặc review.

Câu hỏi phải dựa trên trạng thái Vault thực tế; không được tự tạo quy tắc chỉ để benchmark có câu trả lời.

## Schema cho mỗi mục

| Trường | Mô tả |
|---|---|
| Question ID | Định danh ổn định `QA-###` |
| Loại | fact, rule, edge case hoặc unknown |
| Câu hỏi | Prompt benchmark đã được review |
| Hành vi mong đợi | Câu trả lời có nguồn hỗ trợ hoặc `KHÔNG ĐỦ DỮ LIỆU` |
| Nguồn hỗ trợ | Path trong Vault và stable ID khi có hỗ trợ |
| Kết quả thực tế | Ghi lại khi thực thi |
| Kết luận | pass/fail kèm ghi chú của người review |

Kết quả phục vụ báo cáo nằm trong [`../../docs/02-requirements/vault-qa-benchmark.md`](../../docs/02-requirements/vault-qa-benchmark.md).
