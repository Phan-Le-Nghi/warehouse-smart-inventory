# Câu hỏi mở

Ownership của Audit đã được xác nhận và không phải câu hỏi mở: Nghi sở hữu Putaway như User Story cá nhân chính, đồng thời sở hữu/hỗ trợ quy trình Audit bắt buộc.

## Môn học và phê duyệt

| ID | Câu hỏi mở | Hạng mục bị chặn |
|---|---|---|
| OQ-001 | Thời điểm nộp bài chính xác và múi giờ áp dụng ngày 04/09/2026 là gì? | Kế hoạch nộp bài cuối |
| OQ-002 | Gói nộp bài gồm repository, báo cáo, slide, live demo hay kết hợp các hình thức nào? | Đóng gói báo cáo |
| OQ-003 | Số người tham gia/phương pháp tối thiểu cho User Research và Usability Test là gì? | Bằng chứng nghiên cứu và usability |
| OQ-004 | Ngoài ít nhất 20 câu và các loại câu hỏi bắt buộc, Q&A Benchmark có format, cách chạy hoặc ngưỡng đạt nào khác không? | Hoàn thành benchmark |
| OQ-005 | Template hoặc tiêu chí chấm nào xác định một AI Usage Log cá nhân có ý nghĩa? | Bằng chứng AI cá nhân |
| OQ-006 | Mỗi sinh viên phải nộp bằng chứng đóng góp cá nhân nào? | Bằng chứng báo cáo theo sinh viên |
| OQ-007 | Ai là người phê duyệt cuối cùng cho yêu cầu sản phẩm và quy tắc nghiệp vụ? | Phê duyệt yêu cầu |
| OQ-008 | Nguồn course/assignment gốc, có thẩm quyền và đúng encoding cần bảo tồn là nguồn nào? | Tính toàn vẹn của nguồn thô |

## Nghiên cứu, sản phẩm và thiết kế

| ID | Câu hỏi mở | Hạng mục bị chặn |
|---|---|---|
| OQ-009 | Nhóm có thể tiếp cận stakeholder hoặc người tham gia thực tế nào cho nghiên cứu và usability testing? | Nghiên cứu đã kiểm chứng |
| OQ-010 | Phạm vi hệ thống gồm một Warehouse hay nhiều Warehouse? | `RESOLVED — HUMAN PRODUCT DECISION`: MVP quản lý một Warehouse duy nhất; multi-Warehouse ngoài MVP. Đây là product-scope choice, không phải research conclusion (`DEC-005`). |
| OQ-011 | Stock on-hand, available, reserved, damaged và in-transit được định nghĩa như thế nào, nếu có áp dụng? | `PARTIALLY DECIDED / OPEN`: MVP dùng `system stock quantity`; không canonicalize các bucket đã nêu. Granularity, aggregation, workflow effect và thời điểm thay đổi vẫn OPEN (`DEC-008`). |
| OQ-012 | Lot/batch, serial number, expiry date, unit of measure hoặc unit conversion có thuộc phạm vi không? | Mô hình SKU/Stock |
| OQ-013 | Trigger, điều kiện trước, kết quả thành công, ngoại lệ và trạng thái hoàn tất của từng khu vực quy trình bắt buộc là gì? | User Story và quy trình |
| OQ-014 | Có hỗ trợ thực hiện một phần đối với Receive, Putaway, Pick hoặc Transfer không? | Quy tắc quy trình |
| OQ-015 | Có cho phép tồn kho âm không? | Quy tắc Stock |
| OQ-016 | Transfer là giữa các location, giữa các Warehouse hay cả hai? | `RESOLVED — HUMAN PRODUCT DECISION`: trong MVP, Transfer chỉ là subsequent relocation giữa tracked internal locations trong cùng một Warehouse; cross-Warehouse Transfer ngoài MVP (`DEC-007`). |
| OQ-017 | Adjust và Audit yêu cầu lý do, bằng chứng và phê duyệt nào? | Quy tắc Adjust/Audit |
| OQ-018 | Audit là cycle count, full stocktake hay cả hai? | Quy trình Audit |
| OQ-019 | Purchasing tham gia như thế nào và Purchase Order có thuộc phạm vi sản phẩm không? | Yêu cầu Purchasing |
| OQ-020 | Warehouse Staff, Manager, Purchasing và Admin có những quyền nào? | Yêu cầu truy cập |
| OQ-021 | Alert nào thuộc phạm vi, điều kiện nào kích hoạt và ai nhận Alert? | Yêu cầu Alert |
| OQ-022 | Barcode/QR, scanner, sử dụng mobile/offline hoặc tích hợp bên ngoài có thuộc phạm vi không? | Ranh giới sản phẩm |
| OQ-023 | Yêu cầu bổ sung nào chứng minh các User Story còn lại cần có để đạt mục tiêu 8–12 và ai sẽ sở hữu chúng? | Mục tiêu backlog |
| OQ-024 | Functional Prototype bắt buộc làm trong Figma hay có thể dùng công cụ prototype khác bên cạnh bằng chứng Figma/Design System bắt buộc? | Kế hoạch prototype |
| OQ-025 | URL dự án Taiga, URL dự án Figma, quyền truy cập và người phụ trách công cụ là gì? | Traceability với công cụ bên ngoài |
| OQ-026 | Ngôn ngữ canonical/báo cáo là tiếng Việt, English hay song ngữ? | Tính nhất quán tài liệu |

## AI và nền tảng kỹ thuật

| ID | Câu hỏi mở | Hạng mục bị chặn |
|---|---|---|
| OQ-027 | Inventory Q&A được phép sử dụng nguồn dữ liệu nào? | Phạm vi AI |
| OQ-028 | Inventory anomaly được định nghĩa và chứng minh bằng bằng chứng như thế nào? | Explain inventory anomalies |
| OQ-029 | Reorder recommendation chỉ mang tính tư vấn hay có thể khởi tạo hành động Purchasing? | Phạm vi và độ an toàn của reorder |
| OQ-030 | Có dữ liệu mẫu hoặc dữ liệu lịch sử nào cho các hướng AI? | Tính khả thi/đánh giá AI |
| OQ-031 | Tiêu chí groundedness, accuracy, explainability và safe fallback nào áp dụng cho output AI? | Acceptance Criteria cho AI |
| OQ-032 | Con người sẽ phê duyệt hướng frontend, backend, database, authentication, architecture và deployment nào? | Technical contract và code scaffold |
| OQ-033 | Non-functional requirement nào bắt buộc cho Report Round 1 hoặc sản phẩm cuối? | Architecture và chất lượng |

Khi câu trả lời được phê duyệt, phải dẫn nguồn, cập nhật artifact canonical bị ảnh hưởng và ghi quyết định khi phù hợp. Không âm thầm xóa câu hỏi lịch sử.

## Human decision status cho Domain và Workflow MVP

- `OQ-010` — `RESOLVED — HUMAN PRODUCT DECISION`: MVP quản lý một Warehouse duy nhất. Quyết định này giới hạn product scope và không phải kết luận từ research.
- `OQ-011` — `PARTIALLY DECIDED / OPEN`: dùng `system stock quantity`; không canonicalize `on-hand`, `available`, `reserved`, `damaged` hoặc `in-transit`. Vẫn OPEN: quantity có được duy trì theo location hay không, Warehouse total là stored hay derived, aggregation rule, workflow nào thay đổi quantity và thời điểm quantity thay đổi.
- `OQ-016` — `RESOLVED — HUMAN PRODUCT DECISION`: Transfer trong MVP chỉ là subsequent relocation giữa tracked internal locations trong cùng một Warehouse. Resolution này không xác nhận system Transfer transaction, Movement system record, Stock effect hoặc automatic location update.
- Location cardinality không có canonical OQ ID. `DEC-006` xác nhận như product modeling rằng một SKU có thể liên kết với nhiều internal locations trong cùng Warehouse; không tạo OQ ID mới.
- `OQ-013` vẫn OPEN. Human product modeling đã xác định boundary Putaway/Transfer/Pick, nhưng trigger, precondition, success outcome, exception và completion state chi tiết vẫn chưa rõ.

## Research Synthesis v1 — trạng thái được thông tin một phần

Evidence P1/P2/P3 trong [`../01-sources/research-evidence.md`](../01-sources/research-evidence.md) chỉ mô tả vận hành hiện tại tại một minimart. Tại thời điểm Research Synthesis v1, evidence này không tự đóng các OQ dưới đây. Các HUMAN PRODUCT DECISIONS về sau được ghi riêng; trong đó `DEC-007` đã resolve `OQ-016` cho phạm vi MVP mà không biến quyết định đó thành research finding.

| ID | Evidence đã thông tin | Nội dung vẫn `OPEN QUESTION` |
|---|---|---|
| OQ-009 | Có evidence từ ba participant tại một minimart (`EVD-018`, `EVD-019`). | Khả năng tiếp cận stakeholder/participant bổ sung và usability testing vẫn chưa rõ. |
| OQ-013 | Có mô tả cấp cao từ research (`EVD-002` đến `EVD-017`) và boundary Putaway/Transfer/Pick từ HUMAN PRODUCT DECISION `DEC-009`. | Trigger, precondition, success outcome, exception và completion state chi tiết vẫn chưa rõ; câu hỏi tiếp tục OPEN. |
| OQ-016 | Có physical movement giữa backroom và sales shelf (`EVD-010`). HUMAN PRODUCT DECISION `DEC-007` đã giới hạn Transfer trong MVP là subsequent relocation giữa tracked internal locations trong cùng một Warehouse. | System Transfer transaction, Movement system record, Stock effect và automatic location update chưa được xác nhận; chúng không phải nội dung được resolution của `OQ-016` tự động quyết định. |
| OQ-017 | Có re-check chênh lệch và manager involvement trong vận hành hiện tại (`EVD-012`, `EVD-013`, `EVD-017`). | Lý do, evidence, approval và authority bắt buộc vẫn chưa rõ. |
| OQ-018 | Có inventory checking hằng ngày, gồm đếm và đối chiếu (`EVD-015`, `EVD-016`). | Audit là cycle count, full stocktake hay cả hai vẫn chưa rõ. |
| OQ-020 | Staff hiện report/escalate chênh lệch cho manager (`EVD-013`). | Quyền chính thức của Warehouse Staff, Manager, Purchasing và Admin vẫn chưa rõ. |
| OQ-028 | Có chênh lệch actual-vs-system trong vận hành hiện tại (`EVD-012`, `EVD-017`). | Định nghĩa anomaly, nguyên nhân, tần suất và cách chứng minh vẫn chưa rõ. |
