# Pick — Product Artifact Draft

## Status

`DRAFT / NEEDS HUMAN REVIEW`

This is a Pick-only product-artifact draft. It is not an approved User Story, a new Requirement, a Business Rule, or a Story Spec. It must not be treated as confirmation of any behavior marked `DRAFT / INTERPRETATION` or `TBD / OPEN QUESTION` below.

## Scope and information classification

### CONFIRMED

- Pick is a required workflow area in `Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`. The stated sequence does not confirm that every item or transaction traverses all six areas. Source: `REQ-002`.
- No approved Business Rule directly specifies Pick behavior.

### DRAFT / INTERPRETATION

- The User Story below is intentionally limited to the confirmed workflow scope. It is not a confirmed functional product behavior.

### HUMAN PRODUCT DECISIONS

- `CAND-REQ-003` is `APPROVED — HUMAN PRODUCT DECISION`: the MVP supports recording and looking up inventory information related to area-level internal locations `Backroom` and `Sales Shelf`; one SKU may be recorded at multiple internal locations in the same Warehouse.
- Pick is modeled as taking quantity from a source internal location for a downstream purpose (`DEC-009`).
- The MVP manages one Warehouse, and Transfer is limited to subsequent relocation between tracked internal locations in that Warehouse (`DEC-005`, `DEC-007`).
- These decisions are product scope/modeling, not research findings. They do not approve Pick trigger, downstream purpose, Stock effect, completion, exceptions, automatic location update, or Movement system record creation.

### CURRENT-STATE CONTEXT / EVIDENCE

- The observed minimart has a backroom storage area and a sales shelf area. Source: `EVD-006`.
- After receiving, goods may be placed in the backroom or moved to the sales shelf. Source: `EVD-007`.
- In the observed current operation, knowing goods' location in the backroom/shelf area mainly depends on physical arrangement and staff experience; inventory quantity is tracked in KiotViet. Source: `EVD-008`, `EVD-009`.
- This context remains research evidence only. The location capability and Pick boundary above come from HUMAN PRODUCT DECISIONS, not from this evidence.

### TBD / OPEN QUESTION

- Pick trigger, preconditions, item/quantity input, completion state, exceptions, and relationship to other workflow areas are unresolved. Source: `OQ-013`.
- No behavior is assumed for barcode/QR/scanning, lot/batch/serial/expiry, FIFO/FEFO, stock reservation, partial Pick, negative stock, stock update, Movement system record creation, source-location selection, downstream purpose, or role permission.

## DRAFT User Story

### DRAFT-US-PICK-001

- **Status:** `DRAFT / NEEDS HUMAN REVIEW`
- **Classification:** `DRAFT / INTERPRETATION`

> As a person performing Pick, I need to take quantity from a source internal location for a downstream purpose, so that Pick is represented within the required inventory workflow.

This DRAFT wording reflects `REQ-002`, `CAND-REQ-003`, and HUMAN PRODUCT MODELING in `DEC-009`. It does not define the Pick trigger, downstream purpose, source-location selection rule, system action, Stock effect, completion, exception, or role permission.

### Supporting sources

| Source type | IDs | Use in this draft |
|---|---|---|
| Requirement | `REQ-002`, `CAND-REQ-003` | Confirms Pick as a mandatory workflow area and the approved area-level internal-location capability. |
| Human decisions | `DEC-005`, `DEC-006`, `DEC-007`, `DEC-008`, `DEC-009` | Define the one-Warehouse MVP, internal-location/cardinality scope, Transfer boundary, minimum Stock terminology, and Pick modeling boundary. |
| Business Rule | None | No approved Business Rule directly covers Pick. |
| Evidence | `EVD-006`, `EVD-007`, `EVD-008`, `EVD-009` | Current-state context only; does not confirm functional behavior. |
| Open Questions | `OQ-011`, `OQ-012`, `OQ-013`, `OQ-014`, `OQ-015`, `OQ-020`, `OQ-022` | Constrain unresolved Pick behavior. `OQ-016` is resolved by `DEC-007`. |

## DRAFT Acceptance Criteria

### AC-PICK-001 — workflow scope

- **Classification:** `CONFIRMED / scope-level / non-functional`
- **Given** the required workflow areas are reviewed,
- **When** the workflow scope is checked,
- **Then** Pick is identified as a required area in `Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`.
- **Expected result:** Pick is included in the confirmed workflow scope only. This is not a functional Pick Acceptance Criterion and does not assert a Pick trigger, interaction, stock effect, Movement, Transfer, or completion behavior.
- **Supporting source:** `REQ-002`.

### Functional Acceptance Criteria

`TBD / OPEN QUESTION` — `CAND-REQ-003` approves the shared area-level location recording/lookup capability, but no functional Pick AC is approved for SKU/quantity input, use of that capability within Pick, source-location selection, Pick confirmation, completion, stock deduction, Movement system record, Transfer system behavior, exception handling, partial Pick, barcode/scanner, FIFO/FEFO, or role permission.

## High-level Pick User Flow

```text
[TBD: Pick trigger — OQ-013]
        ↓
[Pick workflow area — CONFIRMED: REQ-002]
        ↓
[TBD: Identify item / quantity — OQ-011, OQ-013]
        ↓
[Pick boundary: take quantity from a source internal location — DEC-009]
        ↓
[TBD: Complete / record Pick — OQ-013]
        ↓
[TBD: Downstream purpose and impact — OQ-011, OQ-013]
```

The physical-location information in `CURRENT-STATE CONTEXT / EVIDENCE` is deliberately outside this directed flow. It is not a system step. The flow does not assume scanning, FIFO/FEFO, reservation, automatic stock reduction, Movement creation, Transfer behavior, partial Pick, or permissions.

`OQ-016` is resolved for MVP scope by `DEC-007`, but that resolution does not approve Pick/Transfer system behavior, Stock effect, automatic location update, or Movement system record creation. `OQ-020` prevents assigning a specific Pick actor or permission.

## Potential Edge Cases / Needs Clarification

| Potential edge case | Classification | Source / reason |
|---|---|---|
| Item is not found at an expected physical area. | `TBD / OPEN QUESTION` | No confirmed Pick exception behavior; `OQ-013`. |
| Available physical quantity is insufficient. | `TBD / OPEN QUESTION` | Stock definitions and Pick exception behavior are unresolved; `OQ-011`, `OQ-013`. |
| One SKU is held in more than one location. | `APPROVED PRODUCT MODELING; behavior TBD` | Multiple internal locations per SKU is approved by `DEC-006`; source selection, quantity granularity and Pick behavior remain TBD. |
| Partial Pick. | `TBD / OPEN QUESTION` | `OQ-014`. |
| Negative stock. | `TBD / OPEN QUESTION` | `OQ-015`. |
| Boundary between Pick and an internal Transfer. | `PARTIALLY DECIDED / OPEN` | Transfer is subsequent relocation between tracked internal locations (`DEC-007`, `DEC-009`); Pick downstream purpose and exact behavior remain TBD. |
| Barcode, QR, scanner, mobile, or offline operation. | `TBD / OPEN QUESTION` | `OQ-022`. |
| Lot/batch, serial, expiry, unit conversion, FIFO, or FEFO. | `TBD / OPEN QUESTION` | `OQ-012`; no selection rule is assumed. |
| Actor authority or permission to perform Pick. | `TBD / OPEN QUESTION` | `OQ-020`; no role is assigned by this draft. |

## Open Questions affecting Pick

| ID | Unresolved impact on Pick |
|---|---|
| `OQ-011` | `PARTIALLY DECIDED / OPEN`: MVP uses `system stock quantity`; location granularity, aggregation, workflow effect, and change timing remain unresolved. |
| `OQ-012` | Whether lot/batch, serial, expiry, unit of measure, or conversion apply. |
| `OQ-013` | Trigger, preconditions, success outcome, exceptions, and completion state. |
| `OQ-014` | Whether partial Pick is supported. |
| `OQ-015` | Whether negative stock is allowed. |
| `OQ-020` | Official permissions for the minimum roles; resolve before approving role-specific Pick behavior. |
| `OQ-022` | Whether barcode/QR, scanners, mobile/offline, or external integration are in scope. |

## Proposed shared-file update

Do not update shared files in this task. After human approval of a canonical Pick Requirement or Business Rule, propose review of `docs/TRACEABILITY.md` to add only approved links.

## Requirement update needed

`CAND-REQ-003` now approves area-level internal-location recording and lookup as a product capability. It does not by itself approve a Pick system interaction, source-selection rule, quantity handling, Stock effect, automatic location update, or Movement system record.

Any future rule for Pick source selection, quantity handling, completion, stock impact, Movement, or the Transfer boundary requires an approved canonical Requirement and/or Business Rule.
