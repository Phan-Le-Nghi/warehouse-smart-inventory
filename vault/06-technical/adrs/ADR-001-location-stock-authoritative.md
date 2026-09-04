# ADR-001 — Per-location stock is authoritative; Warehouse total is derived

## Status

`ACCEPTED — HUMAN APPROVED TECHNICAL DECISION`

Decision Log trace: `DEC-021`.

## Context

The product baseline requires `system stock quantity` by internal location for one MVP Warehouse with `BACKROOM` and `SALES_SHELF`. A SKU may have quantity at both locations, and Warehouse total equals the sum of location quantities.

Persisting both location balances and an independent Warehouse total would create two writable representations of the same quantity.

## Decision

- Persist authoritative stock by `SKU + internal location`.
- Enforce one balance row per SKU/location.
- Derive a SKU's Warehouse total by summing its location balances.
- Do not create a `warehouse_totals` table.

## Consequences

- All stock reads and mutations share one authoritative granularity.
- Internal Transfer preserves Warehouse total when its source and destination effects commit together.
- Aggregate read performance must be measured before introducing any future optimization; no NFR target is currently approved.
- This ADR does not introduce stock buckets such as reserved, damaged or in-transit.

## Traceability

`CAND-REQ-003`, `CAND-BR-003`, `DEC-006`, `DEC-010`, `US-PUT-001` and other stock-changing stories.

