from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class PutawayRequest(BaseModel):
    receive_line_id: UUID
    sku_id: UUID
    quantity: int
    destination_location_id: UUID


class StockResult(BaseModel):
    destination_quantity: int
    warehouse_total: int


class PutawayResponse(BaseModel):
    putaway_id: UUID
    receive_line_id: UUID
    sku_id: UUID
    quantity: int
    destination_location_id: UUID
    destination_location: str
    confirmed_at: datetime
    stock: StockResult


class LocationOption(BaseModel):
    id: UUID
    code: str


class PutawayContextResponse(BaseModel):
    receive_line_id: UUID
    sku_id: UUID
    sku: str
    actual_quantity: int
    confirmed_quantity: int
    eligible_quantity: int
    locations: list[LocationOption]
