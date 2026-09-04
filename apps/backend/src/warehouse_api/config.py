from dataclasses import dataclass
from functools import lru_cache
from os import getenv

DEFAULT_DATABASE_URL = (
    "postgresql+psycopg://warehouse_dev:warehouse_dev_only@localhost:5432/warehouse"
)


@dataclass(frozen=True, slots=True)
class Settings:
    database_url: str


@lru_cache
def get_settings() -> Settings:
    return Settings(database_url=getenv("DATABASE_URL", DEFAULT_DATABASE_URL))
