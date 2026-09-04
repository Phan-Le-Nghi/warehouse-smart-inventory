# Technical Foundation — Canonical Index

## Status and authority

`HUMAN APPROVED TECHNICAL FOUNDATION — DOCUMENTATION ONLY`

Thư mục này là nguồn canonical cho các technical decisions đã được human review. Product requirements, Business Rules và Acceptance Criteria vẫn do các artifact product canonical quản lý; technical documentation không được thay đổi hoặc mở rộng chúng.

Application scaffold, PostgreSQL Compose configuration và CI baseline hiện đã có tại `apps/` và `.github/workflows/ci.yml`, đang chờ human diff review. Chưa có business database schema, business feature hoặc production authentication mechanism; Docker runtime chưa được verify trên máy tạo scaffold.

## Approved foundation

- Frontend: React, TypeScript, Vite, npm.
- Backend: Python 3.13, FastAPI, uv, pytest.
- Database/runtime: PostgreSQL 18, Docker.
- Persistence tooling: SQLAlchemy 2, Alembic.
- E2E: Playwright.
- Architecture: modular monolith với một frontend, một backend API và một PostgreSQL database; không microservices, CQRS, event bus hoặc generic workflow engine.

Decision trace: `DEC-020` đến `DEC-023` tại [`../08-decisions/decision-log.md`](../08-decisions/decision-log.md).

## Canonical artifacts

| Artifact | Status | Purpose |
|---|---|---|
| [`architecture.md`](architecture.md) | HUMAN APPROVED FOUNDATION | Application boundaries, request flow và layer responsibilities |
| [`data-model.md`](data-model.md) | HUMAN APPROVED FOUNDATION / conceptual portions noted | Inventory authority, conceptual MVP model và Putaway slice model |
| [`api-contract.md`](api-contract.md) | PROPOSED CONTRACT | MVP route map và detailed `US-PUT-001` contract; exact routes không phải product requirements |
| [`adrs/ADR-001-location-stock-authoritative.md`](adrs/ADR-001-location-stock-authoritative.md) | ACCEPTED | Per-location stock authority và derived Warehouse total |
| [`adrs/ADR-002-transactional-stock-consistency.md`](adrs/ADR-002-transactional-stock-consistency.md) | ACCEPTED | Transactional stock consistency và non-negative guard |
| [`adrs/ADR-003-receive-putaway-stock-posting.md`](adrs/ADR-003-receive-putaway-stock-posting.md) | ACCEPTED | Receive records actual quantity; Putaway performs initial posting |
| [`story-specs/US-PUT-001.md`](story-specs/US-PUT-001.md) | HUMAN-REVIEWED TECHNICAL SPEC | First vertical slice mapping; no canonical AC changes |

## Preserved open boundaries

- `OQ-012`: UOM, decimal quantity, conversion behavior và precision/scale remain open. Round 1 uses integer units only as a vertical-slice technical simplification.
- `OQ-013`: Receive completion/handoff, Putaway exceptions/downstream handoff và other lifecycle details remain open.
- `OQ-014`: partial Putaway remains open. The full-quantity happy-path fixture is not a rule prohibiting partial Putaway.
- Production authentication, Adjust representation, attachment storage, deployment target, advanced pagination/filtering and NFR targets remain `TBD`.

