# Usability Test Script — 3 critical prototype flows

## Phạm vi và nguyên tắc

- Prototype: [Warehouse — Smart Inventory Management (Figma)](https://www.figma.com/design/d5XrKKZGoeVefVGqVVTwlu/Warehouse---Smart-Inventory-Management?node-id=0-1)
- Phạm vi: đúng 3 participant (`P1`, `P2`, `P3`) và 3 prototype flow.
- Phương pháp: moderated, task-based walkthrough.
- Facilitator không gợi ý CTA hoặc kết quả mong đợi trong khi participant thực hiện task.
- Chỉ ghi điều participant thực sự nói/làm; không tạo quote hoặc suy diễn behavior.
- Script này hệ thống hóa setup tương ứng với các finding đã được human review; không phải bằng chứng rằng AI đã thực hiện participant test.

## P1 — Flow 1: Receive → Putaway

- **Participant code:** `P1`
- **Flow:** `PF-01 — Receive → Putaway`
- **Starting context:** P1 đóng vai Warehouse Staff. Một Receive context hiển thị expected quantity, cho phép nhập actual quantity, và có system reference khác document reference. Putaway là flow riêng cho initial placement vào `Backroom` hoặc `Sales Shelf`.
- **Task prompt:** “Hãy dùng prototype để ghi nhận lô hàng thực nhận và xử lý thông tin cần review. Khi facilitator thông báo chuyển sang công việc initial placement, hãy tiếp tục đặt quantity vào một destination phù hợp trong các lựa chọn có sẵn.”
- **Facilitator transition:** Sau khi phần Receive kết thúc, facilitator điều hướng participant sang Putaway. Transition này chỉ phục vụ prototype test, không đại diện cho production CTA tự động.
- **Success condition:** Participant nhận biết expected và actual quantity, nhận biết discrepancy khi hai số khác nhau, review reference mismatch mà system không tự chọn authoritative reference, và xử lý Putaway như một flow riêng.
- **Observation points:** Khả năng phân biệt expected/actual; khả năng nhận biết discrepancy; cách hiểu trạng thái sau reference review; cách participant mô tả boundary Receive/Putaway; dấu hiệu participant cho rằng Putaway tự động tiếp nối Receive.

**Câu hỏi sau task (non-leading):**

1. Bạn hiểu trạng thái của Receive ở thời điểm kết thúc task như thế nào?
2. Thông tin nào giúp bạn nhận biết có chênh lệch hoặc reference cần review?
3. Theo bạn, phần Receive kết thúc ở đâu và phần Putaway bắt đầu ở đâu?
4. Nếu mô tả bước tiếp theo bằng lời của mình, bạn sẽ mô tả thế nào?

## P2 — Flow 2: Pick

- **Participant code:** `P2`
- **Flow:** `PF-02 — Pick`
- **Starting context:** P2 đóng vai Warehouse Staff. Pick request có requested quantity; cùng SKU có quantity tại `Backroom` và `Sales Shelf`. Prototype có full, `PARTIAL / INSUFFICIENT`, và negative-stock blocked states.
- **Task prompt:** “Hãy dùng prototype để xử lý Pick request bằng inventory tại các source locations được hiển thị. Sau đó xem các kết quả được cung cấp cho trường hợp đủ, thiếu và không thể confirm.”
- **Success condition:** Participant có thể phân bổ Pick từ một hoặc nhiều source locations, phân biệt full Pick với `PARTIAL / INSUFFICIENT`, hiểu partial là kết quả hợp lệ nhưng chưa fully completed, và nhận biết operation bị block mà quantity không đổi khi source quantity không đủ.
- **Observation points:** Cách participant phân bổ giữa hai locations; cách diễn giải full và partial; liệu trạng thái recorded có bị hiểu là fully completed; cách hiểu remaining quantity; cách hiểu blocked validation và stock effect.

**Câu hỏi sau task (non-leading):**

1. Bạn hiểu kết quả Pick vừa thấy như thế nào?
2. Bạn dựa vào thông tin nào để biết Pick đã hoàn tất hay chưa?
3. Phần quantity còn thiếu có ý nghĩa gì với bạn?
4. Khi operation không thể confirm, bạn kỳ vọng quantity trong hệ thống ở trạng thái nào?

## P3 — Flow 3: Audit → Adjust

- **Participant code:** `P3`
- **Flow:** `PF-03 — Audit → Adjust`
- **Starting context:** P3 bắt đầu với vai Warehouse Staff tại một selected-scope Audit có physical count khác `system stock quantity`. Flow sau đó chuyển qua re-check, Adjust request và Manager decision.
- **Task prompt:** “Hãy dùng prototype để xử lý Audit result đang có mismatch. Tiếp tục qua các bước được cung cấp cho Warehouse Staff và Manager, đồng thời mô tả trạng thái quantity tại mỗi bước.”
- **Success condition:** Participant nhận biết mismatch chỉ tạo discrepancy context; hiểu re-check là bắt buộc và không tự động tạo/apply Adjust; phân biệt Warehouse Staff request với Manager decision; xác định quantity không đổi khi waiting/reject và chỉ đổi khi approved/applied.
- **Observation points:** Cách participant hiểu Audit mismatch; cách hiểu re-check; thời điểm participant cho rằng Adjust được tạo; actor chịu trách nhiệm ở mỗi bước; thời điểm participant cho rằng quantity thay đổi.

**Câu hỏi sau task (non-leading):**

1. Bạn hiểu điều gì đã xảy ra với quantity sau Audit mismatch?
2. Theo bạn, re-check thay đổi điều gì trong flow?
3. Bạn hiểu trách nhiệm của Warehouse Staff và Manager ở những bước nào?
4. Quantity ở trạng thái nào khi request đang chờ quyết định?
5. Trong những kết quả vừa xem, quantity thay đổi ở thời điểm nào?

## Evidence guard

Artifact kết quả chỉ được ghi tại [Usability Findings](usability-findings.md) từ nội dung đã được human review. Notes, recording, consent và raw evidence không được suy diễn từ script này và hiện không được lưu trong repository.
