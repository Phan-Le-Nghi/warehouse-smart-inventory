from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Warehouse(Base):
    __tablename__ = "warehouses"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    code: Mapped[str] = mapped_column(String(64), unique=True)


class InternalLocation(Base):
    __tablename__ = "internal_locations"
    __table_args__ = (
        UniqueConstraint("warehouse_id", "code", name="uq_location_warehouse_code"),
        CheckConstraint(
            "code IN ('BACKROOM', 'SALES_SHELF')", name="ck_location_tracked_code"
        ),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    warehouse_id: Mapped[UUID] = mapped_column(
        ForeignKey("warehouses.id", ondelete="RESTRICT"), index=True
    )
    code: Mapped[str] = mapped_column(String(32))


class Sku(Base):
    __tablename__ = "skus"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    code: Mapped[str] = mapped_column(String(64), unique=True)


class Receive(Base):
    __tablename__ = "receives"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    warehouse_id: Mapped[UUID] = mapped_column(
        ForeignKey("warehouses.id", ondelete="RESTRICT"), index=True
    )


class ReceiveLine(Base):
    __tablename__ = "receive_lines"
    __table_args__ = (
        CheckConstraint(
            "actual_quantity >= 0", name="ck_receive_line_actual_nonnegative"
        ),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    receive_id: Mapped[UUID] = mapped_column(
        ForeignKey("receives.id", ondelete="RESTRICT"), index=True
    )
    sku_id: Mapped[UUID] = mapped_column(
        ForeignKey("skus.id", ondelete="RESTRICT"), index=True
    )
    actual_quantity: Mapped[int] = mapped_column(Integer)


class StockBalance(Base):
    __tablename__ = "stock_balances"
    __table_args__ = (
        UniqueConstraint("sku_id", "location_id", name="uq_stock_sku_location"),
        CheckConstraint("quantity >= 0", name="ck_stock_quantity_nonnegative"),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    sku_id: Mapped[UUID] = mapped_column(
        ForeignKey("skus.id", ondelete="RESTRICT"), index=True
    )
    location_id: Mapped[UUID] = mapped_column(
        ForeignKey("internal_locations.id", ondelete="RESTRICT"), index=True
    )
    quantity: Mapped[int] = mapped_column(Integer, default=0)


class PutawayAllocation(Base):
    __tablename__ = "putaway_allocations"
    __table_args__ = (
        CheckConstraint("quantity > 0", name="ck_putaway_quantity_positive"),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    receive_line_id: Mapped[UUID] = mapped_column(
        ForeignKey("receive_lines.id", ondelete="RESTRICT"), index=True
    )
    sku_id: Mapped[UUID] = mapped_column(
        ForeignKey("skus.id", ondelete="RESTRICT"), index=True
    )
    quantity: Mapped[int] = mapped_column(Integer)
    destination_location_id: Mapped[UUID] = mapped_column(
        ForeignKey("internal_locations.id", ondelete="RESTRICT"), index=True
    )
    confirmed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    idempotency_key: Mapped[str] = mapped_column(String(255), unique=True)
    request_fingerprint: Mapped[str] = mapped_column(String(64))
