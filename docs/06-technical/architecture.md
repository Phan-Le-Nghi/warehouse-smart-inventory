# Architecture và ADR — Bản phục vụ báo cáo

## Trạng thái

`HUMAN APPROVED TECHNICAL FOUNDATION — DOCUMENTATION ONLY`

Canonical technical source: [`../../vault/06-technical/architecture.md`](../../vault/06-technical/architecture.md). Quyết định được ghi append-only tại `DEC-020` đến `DEC-023`; `DEC-020` supersede phần stack/architecture/persistence còn TBD của `DEC-004` mà không xóa lịch sử.

## Kiến trúc được duyệt

- Modular monolith.
- Một React + TypeScript + Vite frontend, quản lý package bằng npm.
- Một Python 3.13 + FastAPI backend API, quản lý package bằng uv và test bằng pytest.
- Một PostgreSQL 18 database; Docker dùng cho local database runtime.
- SQLAlchemy 2 và Alembic cho persistence/migrations.
- Playwright cho E2E.
- Không microservices, CQRS, event bus hoặc generic workflow engine.

```text
React frontend
  -> HTTP/JSON
  -> FastAPI route + actor/auth dependency
  -> application service / PostgreSQL transaction
  -> SQLAlchemy 2
  -> PostgreSQL 18
```

Frontend không sở hữu authoritative stock. Application service giữ use-case và transaction boundary; persistence thực hiện query/lock/write; PostgreSQL giữ constraints. Production authentication chưa được chọn, nhưng architecture có actor/auth dependency boundary để giữ canonical role outcomes. Test `US-PUT-001` có thể inject Warehouse Staff actor qua boundary này.

## ADR

| ADR | Accepted decision |
|---|---|
| [`ADR-001`](../../vault/06-technical/adrs/ADR-001-location-stock-authoritative.md) | Persist stock theo SKU/location; derive Warehouse total; không tạo `warehouse_totals` |
| [`ADR-002`](../../vault/06-technical/adrs/ADR-002-transactional-stock-consistency.md) | Stock-changing operations dùng transaction/row locking khi cần và enforce non-negative stock ở application + database |
| [`ADR-003`](../../vault/06-technical/adrs/ADR-003-receive-putaway-stock-posting.md) | Receive ghi actual quantity nhưng không tăng location stock; Putaway thực hiện initial posting và không tạo Transfer/Movement side effect |

## Vẫn TBD / OPEN

- Production authentication mechanism và deployment target.
- Adjust dùng target quantity hay signed delta; attachment storage.
- Advanced pagination/filtering và quantitative NFR tại `OQ-033`.
- `OQ-012`, `OQ-013` và `OQ-014` không bị đóng bởi Technical Foundation.

Chưa có application, Docker hoặc CI implementation trong phase này.
