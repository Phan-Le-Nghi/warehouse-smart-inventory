# Mục lục Story Spec

## Trạng thái

Technical Foundation và `US-PUT-001` Story Spec đã được human review ở mức documentation. Chưa có implementation hoặc test execution. Historical Transfer draft được bảo tồn; Transfer technical contract vẫn cần story-specific review.

## Mapping

| Story ID | Người phụ trách | Requirement/Rule | Flow/Design | Taiga | Technical contract | Test | Bằng chứng |
|---|---|---|---|---|---|---|---|
| [`US-PUT-001`](story-specs/putaway.md) | Phan Lê Nghi | `CAND-REQ-003/007/010`, `CAND-BR-003/004`, `DEC-006/010/011/017/020–023` | `SCR-03`; `PF-01` facilitator boundary | [#8](https://tree.taiga.io/project/lenghi-group-07-project/us/8) | Human-reviewed technical spec; proposed `POST /api/v1/putaways` | Planned only; no execution | HUMAN PRODUCT DECISION + HUMAN APPROVED TECHNICAL DECISIONS; canonical AC unchanged |
| `US-TRF-001` | Nguyễn Thị Ly Na | `CAND-REQ-003/004/011`, `CAND-BR-003/007/008/015`, `DEC-007/010/013/017/019` | Canonical execution/confirmation and negative-stock guard flow | [#10](https://tree.taiga.io/project/lenghi-group-07-project/us/10) | Historical draft only; story-specific contract pending | Chưa thực thi | HUMAN PRODUCT DECISIONS / MVP ASSUMPTIONS; `EVD-010`, `EVD-011`, `EVD-019` are context only |
| `US-TRF-002` | Nguyễn Thị Ly Na | `CAND-REQ-004`, `CAND-BR-008`, `DEC-013`, `DEC-017` | Canonical Transfer history flow | [#11](https://tree.taiga.io/project/lenghi-group-07-project/us/11) | Historical draft only; story-specific contract pending | Chưa thực thi | HUMAN PRODUCT DECISIONS / MVP ASSUMPTIONS; `EVD-010`, `EVD-011`, `EVD-019` are context only |

Canonical product story files nằm trong `vault/04-product/stories/`; canonical technical artifacts nằm trong [`../../vault/06-technical/`](../../vault/06-technical/). A full-quantity Putaway fixture is test scope only and does not resolve partial Putaway at `OQ-014`.
