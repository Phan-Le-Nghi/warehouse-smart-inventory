# Mục lục Story Spec

## Trạng thái

Có một historical Story Spec DRAFT cho Transfer. Product stories đã được canonicalize và split thành `US-TRF-001` và `US-TRF-002`; technical contract vẫn chưa được phê duyệt nên spec chưa implementation-ready.

## Mapping bắt buộc trong tương lai

| Story ID | Người phụ trách | Requirement/Rule | Flow/Design | Taiga | Technical contract | Test | Bằng chứng |
|---|---|---|---|---|---|---|---|
| `US-TRF-001` | Nguyễn Thị Ly Na | `CAND-REQ-003`, `CAND-REQ-004`, `CAND-BR-003`, `CAND-BR-007`, `CAND-BR-008`, `DEC-007`, `DEC-010`, `DEC-013`, `DEC-017` | Canonical execution/confirmation flow | Chưa tạo | Architecture/API/data model remain TBD | Chưa thực thi | HUMAN PRODUCT DECISIONS / MVP ASSUMPTIONS; `EVD-010`, `EVD-011`, `EVD-019` are context only |
| `US-TRF-002` | Nguyễn Thị Ly Na | `CAND-REQ-004`, `CAND-BR-008`, `DEC-013`, `DEC-017` | Canonical Transfer history flow | Chưa tạo | Architecture/API/data model remain TBD | Chưa thực thi | HUMAN PRODUCT DECISIONS / MVP ASSUMPTIONS; `EVD-010`, `EVD-011`, `EVD-019` are context only |

Canonical story files nằm trong `vault/04-product/stories/`. Story Spec technical chỉ được canonicalize sau separate technical review.
