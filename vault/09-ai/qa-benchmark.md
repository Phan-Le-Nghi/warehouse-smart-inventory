# AI Q&A Benchmark

**Trạng thái:** COMPLETED — HUMAN REVIEWED / PASS
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
| QA-018 | Rule      | Hệ thống có cho phép negative stock không?                                                                               | Không. `system stock quantity` tại internal location không được âm; Pick, Transfer và Adjust bị chặn nếu operation sẽ tạo quantity âm. Không suy diễn retry/cancel lifecycle. | `DEC-019`, `CAND-BR-015`, resolved `OQ-015`                |
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
* Mô tả behavior trái `CAND-BR-015`, hoặc tự suy diễn retry/cancel lifecycle sau negative-stock validation.
* Tự biến Candidate/Draft thành requirement chính thức.
* Trả lời chắc chắn khi Vault chưa có dữ liệu.

## Kết quả thực thi

Mỗi dòng dưới đây nối với Question, Expected answer và Expected supporting source trong bảng `Benchmark Questions` bằng stable Question ID.

Quy ước chấm Round 1:

- `Correct`: Actual answer phù hợp đầy đủ với expected answer và có nguồn Vault hỗ trợ.
- `Partial`: Actual answer có phần đúng nhưng thiếu hoặc lệch một phần quan trọng so với expected answer.
- `Wrong`: Actual answer mâu thuẫn với expected answer hoặc trạng thái hiện hành của Vault.
- `Unsupported`: Actual answer đưa ra khẳng định mà nguồn Vault được dẫn không hỗ trợ.
- Một câu hỏi chưa có quyết định vẫn được chấm `Correct` khi expected answer yêu cầu fallback và Actual answer trả lời đúng `KHÔNG ĐỦ DỮ LIỆU` với OQ còn mở làm nguồn.

| Question ID | Actual answer | Actual supporting source | Result | Reviewer note | Human review status |
|---|---|---|---|---|---|
| QA-001 | Quy trình/capability bắt buộc gồm Receive → Putaway → Pick → Transfer → Adjust → Audit. Đây không phải một transaction tuần tự bắt buộc cho mọi hàng hóa. | `vault/03-domain/workflow-overview.md`; `DEC-018` | Correct | Khớp đủ chuỗi và scope guard của expected answer. | REVIEWED / PASS |
| QA-002 | Các role đã xác nhận là Warehouse Staff, Manager, Purchasing và Admin. | `vault/03-domain/roles.md`; `REQ-003`; `DEC-017` | Correct | Khớp đủ bốn role đã xác nhận. | REVIEWED / PASS |
| QA-003 | Các core domain object đã xác nhận là SKU, Warehouse, Stock, Movement, Transfer, Alert và Audit. | `vault/02-requirements/requirements.md` (`REQ-004`) | Correct | Khớp đầy đủ danh sách tại `REQ-004`. | REVIEWED / PASS |
| QA-004 | Có. Khi Receive, item được kiểm tra và số lượng thực nhận được đếm. | `vault/01-sources/research-evidence.md` (`EVD-002`) | Correct | Trả lời trực tiếp theo evidence đã human-confirmed. | REVIEWED / PASS |
| QA-005 | Ghi nhận số lượng thực nhận, không thay bằng số lượng dự kiến. | `vault/01-sources/research-evidence.md` (`EVD-003`, `EVD-004`); `vault/02-requirements/business-rules.md` (`CAND-BR-001`) | Correct | Khớp evidence và business rule đã human review. | REVIEWED / PASS |
| QA-006 | Phải kiểm tra lại chênh lệch trước khi thực hiện adjustment. | `vault/01-sources/research-evidence.md` (`EVD-012`, `EVD-017`); `vault/02-requirements/business-rules.md` (`CAND-BR-002`) | Correct | Không suy diễn thêm cách xử lý sau re-check. | REVIEWED / PASS |
| QA-007 | Evidence hiện xác nhận hai khu vực là Backroom và Sales Shelf. | `vault/01-sources/research-evidence.md` (`EVD-006`, `EVD-007`) | Correct | Giới hạn câu trả lời đúng hai khu vực có evidence. | REVIEWED / PASS |
| QA-008 | Có. Vận hành hiện tại có việc di chuyển hàng giữa Backroom và Sales Shelf. | `vault/01-sources/research-evidence.md` (`EVD-010`) | Correct | Chỉ khẳng định physical movement như evidence. | REVIEWED / PASS |
| QA-009 | Không được tự xác định ngoài permission model. Warehouse Staff có thể tạo discrepancy/Adjust request; Manager approve hoặc reject trước khi apply; Purchasing không có warehouse adjustment permission. | `vault/03-domain/roles.md`; `DEC-017`; `vault/02-requirements/business-rules.md` (`CAND-BR-011`) | Correct | Phân biệt tạo request với approve/apply đúng expected answer. | REVIEWED / PASS |
| QA-010 | Không. AI không được tự tạo API Transfer chưa được phê duyệt; các artifact Transfer được đọc không định nghĩa endpoint như `POST /api/transfers`. | `vault/09-ai/ai-usage-guidance.md`; `vault/04-product/stories/US-TRF-001.md`; `vault/04-product/transfer-draft.md` (scope guard: không định nghĩa API) | Correct | Khớp nguyên tắc không invent; tên nguồn expected “Transfer Story Spec” cần được canonicalize. | REVIEWED / PASS |
| QA-011 | Không. Receive ghi nhận actual received quantity, kể cả khi thấp hơn expected quantity; không ghi expected quantity để bù đủ. | `vault/01-sources/research-evidence.md` (`EVD-004`); `vault/02-requirements/business-rules.md` (`CAND-BR-001`) | Correct | Khớp rule ghi nhận số lượng thực nhận. | REVIEWED / PASS |
| QA-012 | Không. Discrepancy giữa Stock thực tế và hệ thống phải được kiểm tra lại trước khi adjustment. | `vault/01-sources/research-evidence.md` (`EVD-012`); `vault/02-requirements/business-rules.md` (`CAND-BR-002`) | Correct | Không đóng các lifecycle gap sau re-check. | REVIEWED / PASS |
| QA-013 | KHÔNG ĐỦ DỮ LIỆU. Transfer yêu cầu source và destination, nhưng xử lý cụ thể khi không xác định được một trong hai vẫn thuộc exception/lifecycle chưa được quyết định. | `vault/02-requirements/open-questions.md` (`OQ-013`); `vault/04-product/stories/US-TRF-001.md` (Remaining gaps) | Correct | Fallback đúng; không suy diễn auto-confirm hoặc auto-fail. | REVIEWED / PASS |
| QA-014 | KHÔNG ĐỦ DỮ LIỆU. Partial Transfer vẫn là OPEN QUESTION. | `vault/02-requirements/open-questions.md` (`OQ-014`); `vault/04-product/stories/US-TRF-001.md` (Remaining gaps) | Correct | Giữ nguyên `OQ-014`, không biến Pick partial thành Transfer partial. | REVIEWED / PASS |
| QA-015 | Có. Khi Transfer được confirm, quantity giảm tại source internal location, tăng cùng quantity tại destination và Warehouse total không đổi. | `vault/02-requirements/business-rules.md` (`CAND-BR-007`); `DEC-013` | Correct | Khớp đầy đủ quantity effect đã duyệt. | REVIEWED / PASS |
| QA-016 | Confirmed Transfer chuyển cùng quantity từ source internal location sang destination internal location trong cùng một Warehouse. | `vault/02-requirements/requirements.md` (`CAND-REQ-004`); `vault/02-requirements/business-rules.md` (`CAND-BR-007`); `DEC-013` | Correct | Nêu đúng source/destination effect và boundary. | REVIEWED / PASS |
| QA-017 | Không. MVP chỉ hỗ trợ Transfer giữa tracked internal locations trong cùng một Warehouse; cross-Warehouse Transfer nằm ngoài MVP. | `DEC-005`; `DEC-007`; `DEC-013` | Correct | Khớp boundary một Warehouse đã duyệt. | REVIEWED / PASS |
| QA-018 | Không. `system stock quantity` tại internal location không được âm; Pick, Transfer và Adjust bị chặn nếu operation sẽ tạo quantity âm. Không suy diễn retry/cancel lifecycle. | `DEC-019`; `vault/02-requirements/business-rules.md` (`CAND-BR-015`); resolved `OQ-015` | Correct | Khớp guard và giữ nguyên lifecycle gap. | REVIEWED / PASS |
| QA-019 | KHÔNG ĐỦ DỮ LIỆU. Chưa có quyết định reorder recommendation chỉ mang tính advisory hay có thể khởi tạo hành động Purchasing. | `vault/02-requirements/open-questions.md` (`OQ-029`); `vault/02-requirements/requirements.md` (`AI-DIR-003`) | Correct | Fallback đúng; không nâng AI direction thành authority. | REVIEWED / PASS |
| QA-020 | Không nên tự suy diễn. Khi nguồn dữ liệu chưa được xác định và Vault không đủ bằng chứng, AI phải trả lời `KHÔNG ĐỦ DỮ LIỆU`. | `vault/09-ai/ai-usage-guidance.md`; `vault/02-requirements/open-questions.md` (`OQ-027`); `vault/02-requirements/requirements.md` (`AI-DIR-001`) | Correct | Khớp safe fallback và giữ `OQ-027` mở. | REVIEWED / PASS |

## Accuracy Round 1

- Total: 20
- Correct: 20
- Partial: 0
- Wrong: 0
- Unsupported: 0
- Accuracy: `Correct / Total × 100 = 20 / 20 × 100 = 100%`
- Mục tiêu `>= 80% Correct`: đạt; kết quả 20/20 Correct đã được human review và chấp nhận.

## Improvements sau benchmark

1. **PROPOSED** — Canonicalize nguồn kỳ vọng của `QA-010`: thay nhãn chung “Transfer Story Spec” bằng đường dẫn chính xác tới artifact canonical; hiện tại `US-TRF-001` là story canonical còn `transfer-draft.md` đã superseded. Expected supporting source chưa được thay đổi trong lần finalization này.
2. **DONE** — Duy trì rubric bốn mức `Correct / Partial / Wrong / Unsupported` và giải thích rõ rằng fallback `KHÔNG ĐỦ DỮ LIỆU` có thể là `Correct` khi expected answer và OQ còn mở yêu cầu fallback đó.
3. **DONE** — Dùng stable ID kèm đường dẫn artifact trong Actual supporting source để giảm mơ hồ giữa evidence, approved business rule, human decision và open question.
4. **DONE** — Tách rõ `OQ-013` còn mở khỏi `OQ-016` đã resolved khi đánh giá edge case Transfer, tránh dùng trạng thái lịch sử của OQ làm bằng chứng hiện hành.

## Review handoff

- AI hỗ trợ thực thi: đọc Vault, tạo Actual answer draft, so khớp Expected/Actual và tính score draft.
- Human reviewer: đã kiểm tra Expected answer, Actual answer, supporting source và score; đã chấp nhận kết quả hiện tại cho đủ 20 câu.
- Không OQ nào được đóng trong lần benchmark này.

**Trạng thái Benchmark:** Completed — 20 questions — Human reviewed — Accuracy: 100%.
