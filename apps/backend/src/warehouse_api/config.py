from dataclasses import dataclass
from functools import lru_cache
from os import getenv

DEFAULT_DATABASE_URL = (
    "postgresql+psycopg://warehouse_dev:warehouse_dev_only@localhost:5432/warehouse"
)


@dataclass(frozen=True, slots=True)
class Settings:
    database_url: str
    test_actor_role: str | None
    cors_origins: tuple[str, ...]


@lru_cache
def get_settings() -> Settings:
    origins = getenv("CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:4173")
    return Settings(
        database_url=getenv("DATABASE_URL", DEFAULT_DATABASE_URL),
        test_actor_role=getenv("WAREHOUSE_TEST_ACTOR_ROLE"),
        cors_origins=tuple(
            origin.strip() for origin in origins.split(",") if origin.strip()
        ),
    )
