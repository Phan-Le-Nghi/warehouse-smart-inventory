# Pick — Product Artifact Draft

## Status

`DRAFT / NEEDS HUMAN REVIEW`

This is a Pick-only product-artifact draft. It is not an approved User Story, a new Requirement, a Business Rule, or a Story Spec. It must not be treated as confirmation of any behavior marked `DRAFT / INTERPRETATION` or `TBD / OPEN QUESTION` below.

## Scope and information classification

### CONFIRMED

- Pick is a required workflow area in `Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`. The stated sequence does not confirm that every item or transaction traverses all six areas. Source: `REQ-002`.
- The observed minimart has a backroom storage area and a sales shelf area. Source: `EVD-006`.
- After receiving, goods may be placed in the backroom or moved to the sales shelf. Source: `EVD-007`.
- In the observed current operation, knowing goods' location in the backroom/shelf area mainly depends on physical arrangement and staff experience; inventory quantity is tracked in KiotViet. Source: `EVD-008`, `EVD-009`.
- No approved Business Rule directly specifies Pick behavior.

### DRAFT / INTERPRETATION

- The User Story below interprets the current location-knowledge dependency as a possible user value for Pick. This interpretation is supported by research evidence but is not an approved product behavior.
- `CAND-REQ-003` is related to location support, but remains `DRAFT` and is not used as a confirmed Requirement in this artifact.

### TBD / OPEN QUESTION

- Pick trigger, preconditions, item/quantity input, completion state, exceptions, and relationship to other workflow areas are unresolved. Source: `OQ-013`.
- No behavior is assumed for barcode/QR/scanning, lot/batch/serial/expiry, FIFO/FEFO, stock reservation, partial Pick, negative stock, stock update, Movement creation, location cardinality, or role permission.

## DRAFT User Story

### US-PICK-001

- **Status:** `DRAFT / NEEDS HUMAN REVIEW`
- **Classification:** `DRAFT / INTERPRETATION`

> As a person performing Pick, I want to identify the actual storage area of an item—backroom or sales shelf, when applicable—so that I can locate it without relying solely on physical arrangement and personal experience.

This wording does not identify a confirmed system action, a role permission, a single location per SKU, or a rule for selecting a location.

### Supporting sources

| Source type | IDs | Use in this draft |
|---|---|---|
| Requirement | `REQ-002` | Confirms Pick as a mandatory workflow area. |
| Business Rule | None | No approved Business Rule directly covers Pick. |
| Evidence | `EVD-006`, `EVD-007`, `EVD-008`, `EVD-009` | Confirms the observed physical-area context and current reliance on arrangement/experience. |
| Open Questions | `OQ-011`, `OQ-012`, `OQ-013`, `OQ-014`, `OQ-015`, `OQ-016`, `OQ-020`, `OQ-022` | Constrain unresolved Pick behavior. |

## DRAFT Acceptance Criteria

### AC-PICK-001 — workflow scope

- **Classification:** `CONFIRMED`
- **Given** the required workflow areas are reviewed,
- **When** the workflow scope is checked,
- **Then** Pick is identified as a required area in `Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`.
- **Expected result:** Pick is included in the confirmed workflow scope only. This does not assert a Pick trigger, interaction, stock effect, Movement, or completion behavior.
- **Supporting source:** `REQ-002`.

### Functional Acceptance Criteria

`TBD / OPEN QUESTION` — Functional ACs for location lookup/recording, identifying an item or quantity, selecting a source location, confirming Pick, handling exceptions, or changing Stock/Movement are not yet confirmed by an approved Requirement or Business Rule. Current evidence describes observed operation but does not independently establish those product behaviors.

## High-level Pick User Flow

```text
[TBD: Pick trigger — OQ-013]
        ↓
[Pick workflow area — CONFIRMED: REQ-002]
        ↓
[TBD: Identify item / quantity — OQ-011, OQ-013]
        ↓
[Current physical-location context — CONFIRMED evidence:
 backroom and sales shelf exist; location knowledge currently
 depends mainly on physical arrangement and experience
 — EVD-006, EVD-007, EVD-008, EVD-009]
        ↓
[TBD: Select / confirm source location]
        ↓
[TBD: Complete / record Pick — OQ-013]
        ↓
[TBD: Stock / Movement / Transfer impact — OQ-011, OQ-016]
```

The flow is not an interaction or system design. It does not assume scanning, FIFO/FEFO, reservation, automatic stock reduction, Movement creation, partial Pick, or permissions.

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
| `OQ-016` | Whether Transfer is between locations, Warehouses, or both. |
| `OQ-020` | Official permissions for the minimum roles. |
| `OQ-022` | Whether barcode/QR, scanners, mobile/offline, or external integration are in scope. |

## Proposed shared-file update

Do not update shared files in this draft task. After human approval, propose review of `docs/TRACEABILITY.md` to add a truthful `REQ-002 -> US-PICK-001 / AC-PICK-001 -> Pick flow` reference, with the User Story retained as `DRAFT / NEEDS HUMAN REVIEW` until approved.
