# Usability Findings — 3 critical prototype flows

## Trạng thái và giới hạn bằng chứng

Các finding dưới đây là nội dung **HUMAN-REVIEWED USABILITY FINDINGS** được cung cấp để hoàn thiện artifact. Tài liệu giữ đúng ba participant và không thêm participant quote hoặc behavior. Các decision ở đây là UX wording/clarity và prototype-transition decisions; chúng không tạo Requirement hoặc Business Rule mới.

## P1 — Flow 1: Receive → Putaway

### Observation

- Participant nhận biết được expected quantity và actual quantity, đồng thời thấy discrepancy khi hai số khác nhau.
- Participant hiểu reference mismatch cần được review, nhưng chưa chắc bước sau review có đồng nghĩa Receive đã hoàn tất hay không.

### Issue

Boundary giữa Receive và Putaway chưa đủ rõ, có thể khiến participant hiểu Putaway là bước tự động tiếp theo của Receive.

### Decision

- Giữ Receive và Putaway là hai flow tách biệt.
- Không tạo production CTA tự động nối Receive sang Putaway; chỉ dùng facilitator transition trong prototype.
- Decision này làm rõ presentation của boundary đã có tại `DEC-018`; không quyết định Receive final completion đang còn mở tại `OQ-013`.

## P2 — Flow 2: Pick

### Observation

- Participant hiểu có thể phân bổ Pick từ `Backroom` và `Sales Shelf` để đạt requested quantity.
- Participant phân biệt được full Pick và negative-stock blocked, nhưng có thể hiểu `PARTIAL / INSUFFICIENT` là một Pick đã hoàn tất vì kết quả vẫn được ghi nhận.

### Issue

Trạng thái `PARTIAL / INSUFFICIENT` chưa nhấn mạnh đủ rằng Pick chưa fully completed.

### Decision

- Giữ partial Pick như một kết quả hợp lệ nhưng bổ sung copy: **“Pick is not fully completed. 4 units remain unfulfilled.”**
- Giữ nguyên negative-stock guard: operation không được confirm nếu source quantity không đủ và `system stock quantity` không thay đổi.
- Decision này làm rõ UI copy cho behavior đã có tại `DEC-012` và `DEC-019`; không tạo Pick lifecycle mới.

## P3 — Flow 3: Audit → Adjust

### Observation

- Participant nhận biết được Audit mismatch và hiểu rằng mismatch chỉ tạo discrepancy context, chưa tự động thay đổi `system stock quantity`.
- Participant hiểu re-check là bắt buộc trước Adjust, nhưng chưa chắc quantity được cập nhật ở bước nào khi flow chuyển từ Adjust request sang Manager approval.

### Issue

Flow có nhiều bước và đổi actor giữa Warehouse Staff và Manager, dễ khiến participant hiểu nhầm quantity đã thay đổi trước khi Manager approve.

### Decision

- Giữ Audit và Adjust tách biệt.
- Làm rõ trạng thái quantity ở từng bước:
  - sau Audit mismatch: no quantity change;
  - sau re-check: no automatic Adjust;
  - khi waiting for Manager: quantity unchanged;
  - khi reject: quantity unchanged;
  - chỉ khi approved/applied mới cập nhật `system stock quantity`.
- Decision này làm rõ status/copy cho behavior đã có tại `DEC-014`, `DEC-015` và `DEC-018`; không tạo approval rule mới.

## Decision-log assessment

Không thêm entry vào `vault/08-decisions/decision-log.md`: ba decision usability không thay đổi product behavior canonical. Chúng áp dụng wording, state visibility và prototype facilitation cho các decision hiện hữu; mapping đầy đủ nằm tại [Traceability](../TRACEABILITY.md#prototype--usability-traceability).
