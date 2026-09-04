"""Reset the documented US-PUT-001 fixture in a dedicated test database only."""

from os import getenv
from uuid import UUID

from sqlalchemy import create_engine, delete, select
from sqlalchemy.orm import Session

from warehouse_api.models import (
    InternalLocation,
    PutawayAllocation,
    Receive,
    ReceiveLine,
    Sku,
    StockBalance,
    Warehouse,
)

WAREHOUSE_ID = UUID("00000000-0000-0000-0000-000000000001")
SKU_ID = UUID("00000000-0000-0000-0000-000000000002")
RECEIVE_ID = UUID("00000000-0000-0000-0000-000000000003")
RECEIVE_LINE_ID = UUID("00000000-0000-0000-0000-000000000004")
BACKROOM_ID = UUID("00000000-0000-0000-0000-000000000005")
SALES_SHELF_ID = UUID("00000000-0000-0000-0000-000000000006")


def seed_test_fixture() -> None:
    test_database_url = getenv("TEST_DATABASE_URL")
    if not test_database_url:
        raise RuntimeError("TEST_DATABASE_URL is required for the test-only seed")

    engine = create_engine(test_database_url)
    with Session(engine) as session, session.begin():
        session.execute(
            delete(PutawayAllocation).where(
                PutawayAllocation.receive_line_id == RECEIVE_LINE_ID
            )
        )

        if session.get(Warehouse, WAREHOUSE_ID) is None:
            session.add(Warehouse(id=WAREHOUSE_ID, code="MAIN"))
        if session.get(Sku, SKU_ID) is None:
            session.add(Sku(id=SKU_ID, code="SKU-001"))
        if session.get(Receive, RECEIVE_ID) is None:
            session.add(Receive(id=RECEIVE_ID, warehouse_id=WAREHOUSE_ID))
        if session.get(ReceiveLine, RECEIVE_LINE_ID) is None:
            session.add(
                ReceiveLine(
                    id=RECEIVE_LINE_ID,
                    receive_id=RECEIVE_ID,
                    sku_id=SKU_ID,
                    actual_quantity=16,
                )
            )

        for location_id, code in (
            (BACKROOM_ID, "BACKROOM"),
            (SALES_SHELF_ID, "SALES_SHELF"),
        ):
            if session.get(InternalLocation, location_id) is None:
                session.add(
                    InternalLocation(
                        id=location_id, warehouse_id=WAREHOUSE_ID, code=code
                    )
                )
            balance = session.scalar(
                select(StockBalance).where(
                    StockBalance.sku_id == SKU_ID,
                    StockBalance.location_id == location_id,
                )
            )
            if balance is None:
                session.add(
                    StockBalance(sku_id=SKU_ID, location_id=location_id, quantity=0)
                )
            else:
                balance.quantity = 0
    engine.dispose()


if __name__ == "__main__":
    seed_test_fixture()
    print(f"US-PUT-001 test fixture ready: receive_line_id={RECEIVE_LINE_ID}")
