# Warehouse & Smart Inventory Management — Application Scaffold

This directory contains the runnable application foundation for the approved
modular-monolith architecture. The current phase provides tooling and delivery
baselines only; it does not implement a Warehouse business feature.

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

## Frontend

```powershell
Set-Location frontend
npm ci
npm run dev
```

The Vite development server is available at `http://localhost:5173` by
default. `VITE_API_BASE_URL` can be supplied by the environment when the
frontend starts calling the backend in a future phase.

Frontend checks:

```powershell
npm run lint
npm run typecheck
npm run test
npm run build
```

The Playwright smoke test starts the Vite server automatically:

```powershell
npx playwright install chromium
npm run test:e2e
```

## Backend

```powershell
Set-Location backend
uv sync
uv run --env-file ../.env uvicorn warehouse_api.main:app --reload
```

The API is available at `http://localhost:8000`. Its only route in this phase
is the technical health endpoint `GET /health`.

Backend checks:

```powershell
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

The SQLAlchemy engine and session infrastructure are initialized lazily. No
database connection or table creation occurs when the package is imported.

## PostgreSQL

From `apps/docker`, validate and start PostgreSQL 18 with:

```powershell
docker compose --env-file ../.env config
docker compose --env-file ../.env up -d
docker compose ps
docker compose down
```

Compose uses a named volume and a PostgreSQL healthcheck. It does not create a
business schema or run Alembic migrations.

## Current scope

This is only the repository scaffold and CI baseline. There are no business
features, `US-PUT-001` is not implemented, and no business database schema or
business migration exists. Production authentication, deployment, and real
secrets remain out of scope.
