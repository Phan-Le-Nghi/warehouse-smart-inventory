# Technical Architecture — Warehouse & Smart Inventory Management

## Status

`HUMAN APPROVED TECHNICAL FOUNDATION — DOCUMENTATION ONLY`

Architecture and tooling are approved by `DEC-020`. Application code, infrastructure implementation and production authentication are not created in this phase.

## System shape

```text
Browser
  -> React + TypeScript + Vite frontend
  -> HTTP/JSON
  -> FastAPI backend API
  -> application service / transaction boundary
  -> SQLAlchemy 2 persistence
  -> PostgreSQL 18
```

The system is a modular monolith with:

- one frontend;
- one backend API;
- one PostgreSQL database;
- Docker for local database runtime;
- Alembic for schema migrations;
- pytest for backend tests and Playwright for end-to-end tests.

The foundation explicitly excludes microservices, CQRS, an event bus and a generic workflow engine.

## Layer responsibilities

| Layer | Responsibility | Boundary |
|---|---|---|
| Frontend | Present canonical UI states, collect input and call HTTP endpoints | Does not own or calculate authoritative stock |
| FastAPI route/schema | Parse HTTP, validate request shape, call actor/auth dependency and map application results to HTTP | Does not contain stock mutation logic |
| Actor/auth dependency | Supply an authenticated actor and enforce canonical role outcomes | Production authentication mechanism remains `TBD`; tests may inject a Warehouse Staff actor |
| Application service | Orchestrate the use case, enforce approved rules and own the transaction boundary | Does not invent unresolved workflow lifecycle |
| Persistence | Use SQLAlchemy 2 for queries, row locks and writes | Does not contain UI/navigation behavior |
| PostgreSQL | Persist authoritative state and enforce FK, uniqueness and `quantity >= 0` constraints | Warehouse total is not persisted |
| Alembic | Version database schema changes | Migration implementation is not created in this documentation phase |

## Request flow for a stock-changing command

1. The frontend sends an HTTP/JSON command.
2. FastAPI validates request shape and resolves the actor through the auth dependency boundary.
3. The application service starts a PostgreSQL transaction.
4. Persistence locks affected rows when concurrent commands could conflict.
5. The service validates canonical invariants and operation-specific technical guards.
6. The operational record and stock effect are written in the same transaction.
7. On success the transaction commits; on failure all effects roll back.
8. The response reports the committed result; Warehouse total, when returned, is derived from location balances.

## Module boundaries

Initial backend modules should follow business capabilities without becoming separate services: catalog/inventory, Receive, Putaway, Pick, Transfer, Audit and Adjust. Shared infrastructure is limited to database/session, configuration, actor/auth boundary and error mapping.

The first implemented module is intended to be `US-PUT-001`. Other modules remain conceptual until their technical contracts are reviewed.

## Configuration and delivery boundaries

- Runtime configuration must come from environment variables; repository examples must contain placeholders only.
- Exact lint/format packages and version pins remain implementation-tooling choices to review when scaffolding is authorized.
- CI may later run frontend lint/typecheck, backend lint/test and Playwright; no CI or deploy implementation is created in this phase.
- Deployment target and production authentication mechanism remain `TBD`.
- Quantitative NFR targets remain open at `OQ-033`.

## Decision trace

- `DEC-020`: approved stack, persistence tooling and modular-monolith shape.
- `DEC-021` / `ADR-001`: authoritative per-location stock and derived Warehouse total.
- `DEC-022` / `ADR-002`: transactions and non-negative stock.
- `DEC-023` / `ADR-003`: Receive records actual quantity; Putaway performs initial stock posting.

