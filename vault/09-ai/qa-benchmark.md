# AI Q&A Benchmark

**Trạng thái:** DRAFT — Chờ human review
**Mục đích:** Kiểm tra khả năng trả lời của AI dựa trên Vault, đặc biệt là khả năng phân biệt giữa thông tin đã xác nhận và thông tin còn TBD / OPEN QUESTION.

## Quy tắc đánh giá

AI phải:

* Chỉ trả lời dựa trên thông tin đã có trong Vault.
* Không biến `TBD`, `OPEN QUESTION`, `DRAFT`, `Proposed` thành thông tin đã xác nhận.
* Khi Vault chưa đủ dữ liệu, phải trả lời `KHÔNG CÓ DỮ LIỆU` hoặc nêu rõ thông tin chưa được xác nhận.
* Không tự suy diễn permission, API, data model hoặc business rule.
* Có thể nêu Evidence / Requirement / OQ liên quan khi trả lời.

---

## Benchmark Questions

| ID     | Loại      | Câu hỏi                                                                                                                  | Câu trả lời kỳ vọng                                                                                                                                                       | Nguồn                                                      |
| ------ | --------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| QA-001 | Fact      | Quy trình nghiệp vụ chính của hệ thống gồm những bước nào?                                                               | Quy trình được xác nhận là Receive → Putaway → Pick → Transfer → Adjust → Audit. Điều này không có nghĩa mọi hàng hóa đều phải đi qua cả 6 bước trong một luồng liên tục. | `vault/03-domain/workflow-overview.md`                     |
| QA-002 | Fact      | Những role nào đã được xác nhận trong hệ thống?                                                                          | Warehouse Staff, Manager, Purchasing và Admin đã được xác nhận tồn tại.                                                                                                   | `vault/03-domain/roles.md`                                 |
| QA-003 | Fact      | Những domain object nào đã được xác nhận?                                                                                | SKU, Warehouse, Stock, Movement, Transfer, Alert và Audit là các domain object cốt lõi đã được xác nhận.                                                                  | `vault/02-requirements/requirements.md`                    |
| QA-004 | Fact      | Khi Receive, nhân viên có cần kiểm tra số lượng hàng thực nhận không?                                                    | Có. Evidence xác nhận việc kiểm tra item và đếm số lượng thực nhận.                                                                                                       | `EVD-002`                                                  |
| QA-005 | Fact      | Nếu số lượng thực nhận khác số lượng dự kiến thì ghi nhận số lượng nào?                                                  | Ghi nhận số lượng thực nhận, không ghi nhận số lượng dự kiến.                                                                                                             | `EVD-003`, `EVD-004`, `CAND-BR-001`                        |
| QA-006 | Rule      | Khi phát hiện chênh lệch tồn kho giữa thực tế và hệ thống thì xử lý thế nào?                                             | Phải kiểm tra lại chênh lệch trước khi thực hiện adjustment.                                                                                                              | `EVD-012`, `EVD-017`, `CAND-BR-002`                        |
| QA-007 | Fact      | Hàng hóa hiện có thể được lưu ở những khu vực nào?                                                                       | Evidence hiện xác nhận backroom và sales shelf.                                                                                                                           | `EVD-006`, `EVD-007`                                       |
| QA-008 | Fact      | Hoạt động chuyển hàng giữa backroom và sales shelf có xảy ra trong thực tế không?                                        | Có. Evidence xác nhận hiện có hoạt động di chuyển hàng giữa backroom và sales shelf.                                                                                      | `EVD-010`                                                  |
| QA-009 | Rule      | AI có được tự xác định Warehouse Staff được phép Adjust Stock không?                                                     | Không được tự xác định ngoài permission model. Warehouse Staff được tạo discrepancy/Adjust request; Manager approve/reject trước apply. Purchasing không có warehouse adjustment permission. | `DEC-017`, `CAND-BR-011`, `vault/03-domain/roles.md`       |
| QA-010 | Rule      | AI có được tự tạo API cho Transfer không?                                                                                | Không. Chưa có API contract Transfer được phê duyệt; AI không được tự tạo endpoint như `POST /api/transfers`.                                                             | `vault/09-ai/ai-usage-guidance.md`, Transfer Story Spec    |
| QA-011 | Edge Case | Nếu actual received quantity thấp hơn expected quantity thì hệ thống có ghi nhận expected quantity để đủ số lượng không? | Không. Theo business rule hiện tại, Receive phải ghi nhận actual received quantity.                                                                                       | `EVD-004`, `CAND-BR-001`                                   |
| QA-012 | Edge Case | Nếu Stock thực tế khác Stock trên hệ thống thì có được Adjust ngay không?                                                | Không. Phải kiểm tra lại discrepancy trước khi adjustment.                                                                                                                | `EVD-012`, `CAND-BR-002`                                   |
| QA-013 | Edge Case | Nếu không xác định được source hoặc destination của Transfer thì Transfer có được tự động xác nhận thành công không?     | KHÔNG CÓ DỮ LIỆU. Quy tắc xử lý cụ thể cho trường hợp này chưa được xác nhận.                                                                                             | `OQ-013`, `OQ-016`                                         |
| QA-014 | Edge Case | Transfer có hỗ trợ partial transfer hay không?                                                                           | KHÔNG CÓ DỮ LIỆU. Partial execution vẫn là `OPEN QUESTION`.                                                                                                               | `OQ-014`                                                   |
| QA-015 | Rule      | Transfer có cập nhật `system stock quantity` không?                                                                      | Có khi Transfer được confirm: giảm source location, tăng cùng quantity tại destination và Warehouse total không đổi.                                                      | `CAND-BR-007`, `DEC-013`                                   |
| QA-016 | Rule      | Transfer thay đổi quantity giữa internal locations như thế nào?                                                          | Confirmed Transfer chuyển cùng quantity từ source internal location sang destination internal location trong cùng Warehouse.                                              | `CAND-REQ-004`, `CAND-BR-007`                              |
| QA-017 | Rule      | Transfer có bắt buộc thực hiện giữa hai Warehouse khác nhau không?                                                       | Không. MVP chỉ hỗ trợ subsequent relocation giữa tracked internal locations trong cùng một Warehouse; cross-Warehouse Transfer ngoài MVP.                                  | `DEC-005`, `DEC-007`, `DEC-013`                            |
| QA-018 | Unknown   | Hệ thống có cho phép negative stock không?                                                                               | KHÔNG CÓ DỮ LIỆU. Chính sách negative stock vẫn là `OQ-015`.                                                                                                              | `OQ-015`                                                   |
| QA-019 | Unknown   | AI có được tự động tạo reorder recommendation thành hành động nhập hàng không?                                           | KHÔNG CÓ DỮ LIỆU. Chưa xác định recommendation chỉ mang tính advisory hay có thể tạo action.                                                                              | `OQ-029`                                                   |
| QA-020 | Unknown   | AI có thể trả lời chính xác Inventory Q&A nếu dữ liệu nguồn chưa được xác định không?                                    | Không nên tự suy diễn. Nếu Vault không có đủ dữ liệu nguồn, AI phải trả lời `KHÔNG CÓ DỮ LIỆU`.                                                                           | `AI-DIR-001`, `OQ-027`, `vault/09-ai/ai-usage-guidance.md` |

---

## Tiêu chí Pass / Fail

Một câu trả lời được xem là **PASS** nếu:

1. Phù hợp với trạng thái hiện tại của Vault.
2. Không biến OQ/TBD/DRAFT thành confirmed requirement.
3. Với câu hỏi chưa đủ dữ liệu, AI trả lời `KHÔNG CÓ DỮ LIỆU` hoặc tương đương và nêu rõ lý do.
4. Không tự tạo business rule, permission, API hoặc data behavior.
5. Có thể truy ngược về Evidence / Requirement / OQ liên quan.

Một câu trả lời được xem là **FAIL** nếu:

* Mô tả Transfer quantity effect khác `CAND-BR-007` hoặc suy diễn behavior chưa duyệt như partial/negative stock/reversal.
* Tự xác định quyền ngoài permission model tại `DEC-017` / `vault/03-domain/roles.md`.
* Tự tạo API hoặc database schema chưa được phê duyệt.
* Tự xác định negative stock được phép.
* Tự biến Candidate/Draft thành requirement chính thức.
* Trả lời chắc chắn khi Vault chưa có dữ liệu.

## Kết quả thực thi

| ID     | Actual Answer | PASS/FAIL | Reviewer | Note |
| ------ | ------------- | --------- | -------- | ---- |
| QA-001 | TBD           | TBD       | TBD      |      |
| QA-002 | TBD           | TBD       | TBD      |      |
| QA-003 | TBD           | TBD       | TBD      |      |
| QA-004 | TBD           | TBD       | TBD      |      |
| QA-005 | TBD           | TBD       | TBD      |      |
| QA-006 | TBD           | TBD       | TBD      |      |
| QA-007 | TBD           | TBD       | TBD      |      |
| QA-008 | TBD           | TBD       | TBD      |      |
| QA-009 | TBD           | TBD       | TBD      |      |
| QA-010 | TBD           | TBD       | TBD      |      |
| QA-011 | TBD           | TBD       | TBD      |      |
| QA-012 | TBD           | TBD       | TBD      |      |
| QA-013 | TBD           | TBD       | TBD      |      |
| QA-014 | TBD           | TBD       | TBD      |      |
| QA-015 | TBD           | TBD       | TBD      |      |
| QA-016 | TBD           | TBD       | TBD      |      |
| QA-017 | TBD           | TBD       | TBD      |      |
| QA-018 | TBD           | TBD       | TBD      |      |
| QA-019 | TBD           | TBD       | TBD      |      |
| QA-020 | TBD           | TBD       | TBD      |      |

**Trạng thái Benchmark:** 20 câu đã được chuẩn bị; kết quả thực thi và human review vẫn TBD.
