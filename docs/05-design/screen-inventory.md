# Screen Inventory — Critical-flow prototype

## Phạm vi

- Prototype: [Warehouse — Smart Inventory Management (Figma)](https://www.figma.com/design/d5XrKKZGoeVefVGqVVTwlu/Warehouse---Smart-Inventory-Management?node-id=0-1)
- Tổng cộng: **10 base screens**, tổ chức thành **3 prototype flows**.
- Inventory này mô tả logical screen/state cần có theo canonical stories và human-reviewed findings. Figma là downstream design artifact, không phải nguồn Requirement/Business Rule.

## 10 base screens

| Screen | Base screen | Key states / clarity treatment | Related Story IDs |
|---|---|---|---|
| `SCR-01` | Receive — quantity check | expected quantity; actual quantity; match/mismatch visibility | `US-REC-001` |
| `SCR-02` | Receive — discrepancy/reference review | quantity discrepancy; reference mismatch requires review; Receive completion không được suy diễn | `US-REC-001` |
| `SCR-03` | Putaway — destination allocation | separate flow; destination `Backroom`/`Sales Shelf`; no production CTA tự động từ Receive | `US-PUT-001` |
| `SCR-04` | Pick — request and source allocation | requested quantity; allocation từ `Backroom` và/hoặc `Sales Shelf` | `US-PICK-001` |
| `SCR-05` | Pick — result | full; `PARTIAL / INSUFFICIENT`; partial copy: “Pick is not fully completed. 4 units remain unfulfilled.” | `US-PICK-001` |
| `SCR-06` | Pick — blocked confirmation | selected source quantity không đủ; operation not confirmed; quantity unchanged | `US-PICK-001` |
| `SCR-07` | Audit — count and compare | selected scope; physical count vs `system stock quantity`; match/mismatch | `US-AUD-001` |
| `SCR-08` | Audit — discrepancy re-check | mismatch creates discrepancy context; mandatory re-check; no automatic Adjust; quantity unchanged | `US-AUD-002` |
| `SCR-09` | Adjust — request | Warehouse Staff; required reason; waiting for Manager; quantity unchanged | `US-ADJ-001` |
| `SCR-10` | Adjust — Manager decision/outcome | Manager approve/reject; reject leaves quantity unchanged; only approved/applied updates quantity; negative-stock apply guard | `US-ADJ-002` |

## 3 prototype flows

| Flow | Screen path | Key states | Related Story IDs |
|---|---|---|---|
| `PF-01 — Receive → Putaway` | `SCR-01 → SCR-02` then **facilitator transition** to `SCR-03` | quantity match/mismatch; reference review; explicit Receive/Putaway boundary | `US-REC-001`, `US-PUT-001` |
| `PF-02 — Pick` | `SCR-04 → SCR-05`; `SCR-06` as blocked branch | multi-location allocation; full; `PARTIAL / INSUFFICIENT`; negative-stock blocked/no quantity change | `US-PICK-001` |
| `PF-03 — Audit → Adjust` | `SCR-07 → SCR-08 → SCR-09 → SCR-10` | mismatch/no change; re-check/no auto Adjust; waiting/no change; reject/no change; approved/applied update | `US-AUD-001`, `US-AUD-002`, `US-ADJ-001`, `US-ADJ-002` |

## Boundary notes

- `PF-01`: arrow between Receive and Putaway represents facilitator navigation only. It must not be implemented as an automatic production CTA or interpreted as Receive completion.
- `PF-02`: recording a `PARTIAL / INSUFFICIENT` result does not make the Pick fully completed.
- `PF-03`: actor and quantity status must remain visible through the Warehouse Staff → Manager handoff.
