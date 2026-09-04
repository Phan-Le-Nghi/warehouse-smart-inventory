# ADR-002 — Transactional stock consistency and non-negative location stock

## Status

`ACCEPTED — HUMAN APPROVED TECHNICAL DECISION`

Decision Log trace: `DEC-022`.

## Context

Putaway, Pick, Transfer and approved Adjust change authoritative location balances. Transfer changes two balances, Pick may change multiple source balances and concurrent commands may otherwise validate against stale quantity.

The canonical product rule prohibits negative `system stock quantity` at an internal location.

## Decision

- Putaway, Pick, Transfer and approved Adjust use a PostgreSQL transaction boundary.
- The application service validates operation-specific quantity rules before mutation.
- Affected rows are locked when needed to prevent conflicting concurrent mutations.
- A rejected operation applies no quantity change.
- The database enforces `CHECK quantity >= 0` as a final integrity guard.
- Multi-row mutations commit or roll back as one unit.

## Consequences

- Source/destination or record/balance partial writes are prevented.
- Application errors can explain canonical failures while the database remains the final invariant boundary.
- Lock ordering and concurrency tests are required when multi-row Pick and Transfer are implemented.
- This ADR does not define retry/cancel lifecycle or reservation semantics.

## Traceability

`CAND-REQ-011`, `CAND-BR-015`, `DEC-019`, `US-PICK-001`, `US-TRF-001`, `US-ADJ-002` and the initial-posting transaction in `US-PUT-001`.

