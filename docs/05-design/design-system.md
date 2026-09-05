# Figma và Design System

## Trạng thái

- URL dự án Figma: [Warehouse — Smart Inventory Management](https://www.figma.com/design/d5XrKKZGoeVefVGqVVTwlu/Warehouse---Smart-Inventory-Management?node-id=0-1)
- Quyền truy cập: **HUMAN VERIFIED** — file mở được trực tiếp trên browser; người phụ trách công cụ: TBD
- Phiên bản Design System: TBD
- Figma có đủ **8 pages**: `00 - Cover`, `01 - User Flow`, `02 - Wireframe`, `03 - Design System`, `04 - Components`, `05 - High Fidelity`, `06 - Prototype`, `07 - Dev Handoff`.
- Screen inventory phục vụ 3 critical flows: **10 logical base screens**, triển khai thành **31 wireframe state frames** và **31 prototype counterparts**; xem [`screen-inventory.md`](screen-inventory.md).

Các dữ kiện trên được con người xác minh trực tiếp trong Figma. MCP read-back chỉ trả `00 - Cover`, vì vậy MCP page inventory được phân loại **INCOMPLETE / NON-AUTHORITATIVE** và không được dùng để kết luận file chỉ có Cover.

## Foundations — human verified

- Gray palette: `Gray 0`, `Gray 50`, `Gray 200`, `Gray 500`, `Gray 900`.
- Typography: `Heading XL — 32/40 Bold`; `Heading L — 24/32 Semi Bold`; `Body — 16/24 Regular`; `Label — 14/20 Semi Bold`; `Caption — 12/18 Regular`.
- Spacing: `8 / 16 / 24 / 32 px`; section gap `24 px`.
- Content max-width: `1080 px`; desktop grid: `12 columns`.
- Top bar: `64 px`; form controls: `44 px`.
- Status styles: `Neutral`, `Success`, `Warning/error`.

Trạng thái Design System: **PASS / human-verified foundations; exact metadata counts not fully verified**. Không claim radius, shadow, variables hoặc text-style counts khi chưa được xác minh.

## Components — human verified

Page `04 - Components` có reusable components. Những component nhìn thấy gồm Primary button, Secondary button, Action footer, Adjust decision summary, Re-check status block và Status block.

Trạng thái Components: **PASS/PARTIAL — reusable components human-verified; exact inventory count pending**. Không claim exact component count.

## Round 1 boundaries

- `05 - High Fidelity`: tồn tại nhưng trống — **DEFERRED / NOT COMPLETED FOR ROUND 1**.
- `07 - Dev Handoff`: tồn tại nhưng trống — **PARTIAL / NOT COMPLETED**; không tạo nội dung mới và không claim handoff complete.
- Round 1 evidence dựa trên low-fidelity wireframe/prototype.
- Exact hotspot total và full interaction-level wiring chưa được independently verified.
- Cân nhắc accessibility: TBD
- ID User Story/Flow được bao phủ: `US-REC-001`, `US-PUT-001`, `US-PICK-001`, `US-AUD-001/002`, `US-ADJ-001/002`; `PF-01/02/03`
- Quan hệ giữa prototype và Usability Test: xem [`usability-test-script.md`](usability-test-script.md) và [`usability-findings.md`](usability-findings.md)

Visual asset trong Figma phải được dẫn xuất từ User Story, flow và phát hiện đã xác nhận; chúng không được trở thành nguồn yêu cầu nghiệp vụ cạnh tranh.
