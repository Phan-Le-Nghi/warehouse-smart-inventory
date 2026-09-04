from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from warehouse_api.config import Settings, get_settings
from warehouse_api.errors import ApiError

WAREHOUSE_STAFF = "WAREHOUSE_STAFF"


@dataclass(frozen=True, slots=True)
class Actor:
    role: str


def get_actor(settings: Annotated[Settings, Depends(get_settings)]) -> Actor:
    """Actor boundary only; production authentication remains intentionally TBD."""
    if settings.test_actor_role is None:
        raise ApiError(
            503,
            "AUTHENTICATION_NOT_CONFIGURED",
            "Production authentication is not configured.",
        )
    return Actor(role=settings.test_actor_role)


def require_warehouse_staff(
    actor: Annotated[Actor, Depends(get_actor)],
) -> Actor:
    if actor.role != WAREHOUSE_STAFF:
        raise ApiError(403, "WAREHOUSE_STAFF_REQUIRED", "Warehouse Staff is required.")
    return actor
