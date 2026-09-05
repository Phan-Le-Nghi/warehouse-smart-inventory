# User Research và tổng hợp

## Trạng thái hiện tại

Report-facing summary này phản ánh research evidence do con người cung cấp và xác nhận, được lập mục lục canonical thành `EVD-001` đến `EVD-019` tại [`../../vault/01-sources/research-evidence.md`](../../vault/01-sources/research-evidence.md). Tài liệu không tạo evidence, transcript, participant quote, Requirement hoặc Business Rule mới.

## Research context và phương pháp

- Mục tiêu: hiểu cách manager/staff tại minimart hiện thực hiện Receive, Putaway, Pick, Transfer, Adjust và Audit.
- Participant: `P1`, `P2`, `P3`; tên thật không được lưu trong Vault.
- `P1`: quản lý minimart; self-report / mini-interview.
- `P2`, `P3`: nhân viên minimart; written confirmation của prepared workflow summary.
- Current tool: KiotViet được dùng để theo dõi inventory quantity.
- Tuyển dụng/tiếp cận stakeholder hoặc participant bổ sung và usability testing: `OQ-009` vẫn mở.
- Kỳ vọng tối thiểu của môn học về participant/phương pháp: `OQ-003` vẫn mở.
- Privacy/consent handling: `TBD`.

Không có transcript hoặc direct quote được ghi cho `P2` và `P3`.

## Evidence

Nguồn chi tiết và provenance được bảo tồn tại:

- [`../../vault/01-sources/interview-notes.md`](../../vault/01-sources/interview-notes.md) — participant context và notes.
- [`../../vault/01-sources/research-evidence.md`](../../vault/01-sources/research-evidence.md) — evidence index `EVD-001–019`.

Evidence hiện có bao phủ current tooling; Receive actual-versus-expected; quantity discrepancy; `Backroom`/`Sales Shelf` physical context; physical location knowledge; internal movement; Audit count/compare; discrepancy re-check và manager involvement. Các chi tiết không được evidence hỗ trợ tiếp tục là `TBD` hoặc `OPEN QUESTION`.

## Human-reviewed synthesis

- Receive tại minimart kiểm item, đếm actual quantity, compare với expected quantity và ghi actual quantity khi có chênh lệch (`EVD-002–005`).
- Minimart có backroom storage area và sales shelf area; knowledge về physical location chủ yếu dựa vào arrangement và staff experience (`EVD-006–009`).
- Có physical movement giữa backroom và sales shelf, nhưng research không xác nhận current system ghi movement thành transaction riêng (`EVD-010/011`).
- Inventory checking được thực hiện hằng ngày tại minimart, gồm physical count và compare với KiotViet (`EVD-015/016`).
- Khi actual stock khác system data, discrepancy phải được re-check; staff report/escalate cho manager trong current operation (`EVD-012/013/017`).
- `P2` và `P3` xác nhận prepared workflow summary và không báo correction; không có transcript/direct quote cho hai participant này (`EVD-018`).

Hai Business Rules được dẫn xuất có giới hạn từ Research Synthesis v1 và đã được human review nằm tại `CAND-BR-001` và `CAND-BR-002`. Các product behavior khác được phê duyệt về sau là HUMAN PRODUCT DECISIONS / MVP ASSUMPTIONS, không phải verified research findings.

## Research limitations

- `P1`, `P2` và `P3` đều làm việc tại cùng một minimart.
- Evidence chỉ phản ánh current operation tại minimart đó và không được generalize cho mọi Warehouse.
- Không participant nào được mô tả là warehouse specialist.
- Không có raw recording, consent artifact hoặc participant quote trong repository ngoài notes/status đã được ghi.
- Current KiotViet scope và permissions, detailed workflow lifecycle, discrepancy causes/frequency và các behavior không được hỗ trợ vẫn là `TBD` / `OPEN QUESTION`.

Danh sách Open Questions canonical nằm tại [`../../vault/02-requirements/open-questions.md`](../../vault/02-requirements/open-questions.md).
