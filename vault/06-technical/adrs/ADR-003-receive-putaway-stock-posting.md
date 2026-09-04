# ADR-003 — Receive records actual quantity; Putaway performs initial stock posting

## Status

`ACCEPTED — HUMAN APPROVED TECHNICAL DECISION`

Decision Log trace: `DEC-023`.

## Context

Receive records actual received quantity and discrepancy/reference context. Putaway is the initial placement into `BACKROOM` or `SALES_SHELF`. If both operations independently increased tracked-location stock, the same received quantity could be counted twice.

## Decision

- Receive records actual received quantity and discrepancy/reference context.
- Receive does not increase tracked internal-location stock.
- Confirmed Putaway performs the initial posting to its confirmed destination.
- Putaway does not create a Transfer record.
- Putaway does not create a generic Movement record.
- Previously posted Putaway allocations are included when validating that a new allocation does not exceed the not-yet-posted Receive quantity.

## Consequences

- Tracked stock is not double-counted across Receive and Putaway.
- Receive actual quantity remains an operational fact and is not rewritten by Putaway.
- A Putaway allocation and its location-balance increment must be atomic and idempotent.
- A full eligible-quantity test fixture may demonstrate the first slice without becoming a full-only rule.

## Open-boundary protection

- This ADR does **not** resolve `OQ-013`. It does not define Receive completion, automatic handoff, Putaway exception or downstream lifecycle.
- This ADR does **not** resolve `OQ-014`. It does not prohibit or define partial Putaway.
- It creates no automatic production CTA between Receive and Putaway.

## Traceability

`CAND-REQ-001/002/003/007`, `CAND-BR-001/003/004`, `DEC-010/011`, `US-REC-001`, `US-PUT-001`, `OQ-013` and `OQ-014`.

