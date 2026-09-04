# Warehouse & Smart Inventory Management — US-PUT-001 Vertical Slice

This directory contains the runnable first vertical slice for `US-PUT-001`,
from React through FastAPI and PostgreSQL persistence.

## Prerequisites

- Node.js 24 and npm
- Python 3.13
- [uv](https://docs.astral.sh/uv/)
- Docker with Docker Compose (for local PostgreSQL)

## Environment

Create a local environment file from the committed placeholder values:

```powershell
Copy-Item .env.example .env
```

`.env` is ignored by Git. The example credentials are for local development
only. Do not reuse them in a shared or production environment.

## PostgreSQL and backend

Start PostgreSQL from `apps/docker`, then apply the explicit migration and load
the documented test-only fixture:

```powershell
docker compose --env-file ../.env up -d
Set-Location ../backend
uv sync --locked
uv run --env-file ../.env alembic upgrade head
uv run --env-file ../.env python -m warehouse_api.test_seed
uv run --env-file ../.env uvicorn warehouse_api.main:app --reload
```

The API is available at `http://localhost:8000`. Importing the application does
not create tables or run migrations.

Backend checks:

```powershell
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

Without `TEST_DATABASE_URL`, pytest uses SQLite for component-level feedback.
Set that variable to a real PostgreSQL test database for PostgreSQL evidence.

## Frontend

`VITE_API_BASE_URL` selects the FastAPI origin. `VITE_RECEIVE_LINE_ID` supplies
the explicit Putaway context without inventing an automatic Receive handoff.

```powershell
Set-Location frontend
npm ci
npm run dev
```

Frontend checks:

```powershell
npm run lint
npm run typecheck
npm run test
npm run build
```

The Playwright test refuses to run without a real PostgreSQL URL. It migrates
that database, resets the test-only fixture, and starts FastAPI and Vite:

```powershell
$env:TEST_DATABASE_URL = "postgresql+psycopg://warehouse_dev:warehouse_dev_only@localhost:5432/warehouse"
npm run test:e2e
```

## Scope boundary

Only the `US-PUT-001` vertical slice is implemented. Production authentication,
deployment, other stories, and real secrets remain out of scope. The
`WAREHOUSE_TEST_ACTOR_ROLE` switch exists only for controlled tests; production
authentication remains TBD. `OQ-012`, `OQ-013`, and `OQ-014` remain open.
