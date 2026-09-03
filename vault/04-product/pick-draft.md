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
- `CAND-REQ-003` is related to location support, but remains `DRAFT` and is not used as a confirmed Requirement in this artifact.

### CURRENT-STATE CONTEXT / EVIDENCE

- The observed minimart has a backroom storage area and a sales shelf area. Source: `EVD-006`.
- After receiving, goods may be placed in the backroom or moved to the sales shelf. Source: `EVD-007`.
- In the observed current operation, knowing goods' location in the backroom/shelf area mainly depends on physical arrangement and staff experience; inventory quantity is tracked in KiotViet. Source: `EVD-008`, `EVD-009`.
- This context is not a confirmed system behavior, Pick step, location-support requirement, or source-location selection rule.

### TBD / OPEN QUESTION

- Pick trigger, preconditions, item/quantity input, completion state, exceptions, and relationship to other workflow areas are unresolved. Source: `OQ-013`.
- No behavior is assumed for barcode/QR/scanning, lot/batch/serial/expiry, FIFO/FEFO, stock reservation, partial Pick, negative stock, stock update, Movement creation, location cardinality, or role permission.

## DRAFT User Story

### US-PICK-001

- **Status:** `DRAFT / NEEDS HUMAN REVIEW`
- **Classification:** `DRAFT / INTERPRETATION`

> As a person performing Pick, I need Pick to be included in the required inventory workflow, so that Pick is within the defined process scope.

This wording is limited to `REQ-002`. It does not assert location support, a system action, a role permission, a single location per SKU, a source-location rule, or an inventory outcome.

### Supporting sources

| Source type | IDs | Use in this draft |
|---|---|---|
| Requirement | `REQ-002` | Confirms Pick as a mandatory workflow area. |
| Business Rule | None | No approved Business Rule directly covers Pick. |
| Evidence | `EVD-006`, `EVD-007`, `EVD-008`, `EVD-009` | Current-state context only; does not confirm functional behavior. |
| Open Questions | `OQ-011`, `OQ-012`, `OQ-013`, `OQ-014`, `OQ-015`, `OQ-016`, `OQ-020`, `OQ-022` | Constrain unresolved Pick behavior. |

## DRAFT Acceptance Criteria

### AC-PICK-001 — workflow scope

- **Classification:** `CONFIRMED / scope-level / non-functional`
- **Given** the required workflow areas are reviewed,
- **When** the workflow scope is checked,
- **Then** Pick is identified as a required area in `Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`.
- **Expected result:** Pick is included in the confirmed workflow scope only. This is not a functional Pick Acceptance Criterion and does not assert a Pick trigger, interaction, stock effect, Movement, Transfer, or completion behavior.
- **Supporting source:** `REQ-002`.

### Functional Acceptance Criteria

`TBD / OPEN QUESTION` — Functional ACs for SKU selection, item quantity, location lookup/recording, source-location selection, Pick confirmation, completion, stock deduction, Movement, Transfer, exception handling, partial Pick, barcode/scanner, FIFO/FEFO, or role permission are not yet confirmed by an approved Requirement or Business Rule.

## High-level Pick User Flow

```text
[TBD: Pick trigger — OQ-013]
        ↓
[Pick workflow area — CONFIRMED: REQ-002]
        ↓
[TBD: Identify item / quantity — OQ-011, OQ-013]
        ↓
[TBD: Select / confirm source location]
        ↓
[TBD: Complete / record Pick — OQ-013]
        ↓
[TBD: Downstream impact / boundary — OQ-011, OQ-016]
```

The physical-location information in `CURRENT-STATE CONTEXT / EVIDENCE` is deliberately outside this directed flow. It is not a system step. The flow does not assume scanning, FIFO/FEFO, reservation, automatic stock reduction, Movement creation, Transfer behavior, partial Pick, or permissions.

`OQ-016` must remain unresolved before downstream Pick/Transfer/Movement behavior can be finalized. `OQ-020` prevents assigning a specific Pick actor or permission.

## Potential Edge Cases / Needs Clarification

| Potential edge case | Classification | Source / reason |
|---|---|---|
| Item is not found at an expected physical area. | `TBD / OPEN QUESTION` | No confirmed Pick exception behavior; `OQ-013`. |
| Available physical quantity is insufficient. | `TBD / OPEN QUESTION` | Stock definitions and Pick exception behavior are unresolved; `OQ-011`, `OQ-013`. |
| One SKU is held in more than one location. | `TBD / OPEN QUESTION` | Location cardinality is not confirmed; `EVD-008`, `OQ-013`. |
| Partial Pick. | `TBD / OPEN QUESTION` | `OQ-014`. |
| Negative stock. | `TBD / OPEN QUESTION` | `OQ-015`. |
| Boundary between Pick and a backroom-to-shelf Transfer. | `TBD / OPEN QUESTION` | Movement exists in current operation, but formal Transfer scope is unresolved; `EVD-010`, `EVD-011`, `OQ-016`. |
| Barcode, QR, scanner, mobile, or offline operation. | `TBD / OPEN QUESTION` | `OQ-022`. |
| Lot/batch, serial, expiry, unit conversion, FIFO, or FEFO. | `TBD / OPEN QUESTION` | `OQ-012`; no selection rule is assumed. |
| Actor authority or permission to perform Pick. | `TBD / OPEN QUESTION` | `OQ-020`; no role is assigned by this draft. |

## Open Questions affecting Pick

| ID | Unresolved impact on Pick |
|---|---|
| `OQ-011` | Definitions and applicability of stock quantities, including available/reserved. |
| `OQ-012` | Whether lot/batch, serial, expiry, unit of measure, or conversion apply. |
| `OQ-013` | Trigger, preconditions, success outcome, exceptions, and completion state. |
| `OQ-014` | Whether partial Pick is supported. |
| `OQ-015` | Whether negative stock is allowed. |
| `OQ-016` | Whether Transfer is between locations, Warehouses, or both; resolve before finalizing downstream Pick/Transfer/Movement behavior. |
| `OQ-020` | Official permissions for the minimum roles; resolve before approving role-specific Pick behavior. |
| `OQ-022` | Whether barcode/QR, scanners, mobile/offline, or external integration are in scope. |

## Proposed shared-file update

Do not update shared files in this task. After human approval of a canonical Pick Requirement or Business Rule, propose review of `docs/TRACEABILITY.md` to add only approved links.

## Requirement update needed

Location lookup, recording, or support must not be treated as a Pick function unless Product/BA obtains human approval and updates a canonical Requirement. `CAND-REQ-003` remains a related `DRAFT` candidate and is not promoted by this artifact.

Any future rule for Pick source selection, quantity handling, completion, stock impact, Movement, or the Transfer boundary requires an approved canonical Requirement and/or Business Rule.
