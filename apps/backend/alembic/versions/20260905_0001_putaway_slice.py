"""Create the minimal US-PUT-001 vertical-slice schema."""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "20260905_0001"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "warehouses",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("code", sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("code"),
    )
    op.create_table(
        "skus",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("code", sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("code"),
    )
    op.create_table(
        "internal_locations",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("warehouse_id", sa.Uuid(), nullable=False),
        sa.Column("code", sa.String(length=32), nullable=False),
        sa.CheckConstraint(
            "code IN ('BACKROOM', 'SALES_SHELF')", name="ck_location_tracked_code"
        ),
        sa.ForeignKeyConstraint(
            ["warehouse_id"], ["warehouses.id"], ondelete="RESTRICT"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("warehouse_id", "code", name="uq_location_warehouse_code"),
    )
    op.create_index(
        op.f("ix_internal_locations_warehouse_id"),
        "internal_locations",
        ["warehouse_id"],
    )
    op.create_table(
        "receives",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("warehouse_id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["warehouse_id"], ["warehouses.id"], ondelete="RESTRICT"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_receives_warehouse_id"), "receives", ["warehouse_id"])
    op.create_table(
        "receive_lines",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("receive_id", sa.Uuid(), nullable=False),
        sa.Column("sku_id", sa.Uuid(), nullable=False),
        sa.Column("actual_quantity", sa.Integer(), nullable=False),
        sa.CheckConstraint(
            "actual_quantity >= 0", name="ck_receive_line_actual_nonnegative"
        ),
        sa.ForeignKeyConstraint(["receive_id"], ["receives.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["sku_id"], ["skus.id"], ondelete="RESTRICT"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_receive_lines_receive_id"), "receive_lines", ["receive_id"]
    )
    op.create_index(op.f("ix_receive_lines_sku_id"), "receive_lines", ["sku_id"])
    op.create_table(
        "stock_balances",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("sku_id", sa.Uuid(), nullable=False),
        sa.Column("location_id", sa.Uuid(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.CheckConstraint("quantity >= 0", name="ck_stock_quantity_nonnegative"),
        sa.ForeignKeyConstraint(
            ["location_id"], ["internal_locations.id"], ondelete="RESTRICT"
        ),
        sa.ForeignKeyConstraint(["sku_id"], ["skus.id"], ondelete="RESTRICT"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("sku_id", "location_id", name="uq_stock_sku_location"),
    )
    op.create_index(
        op.f("ix_stock_balances_location_id"), "stock_balances", ["location_id"]
    )
    op.create_index(op.f("ix_stock_balances_sku_id"), "stock_balances", ["sku_id"])
    op.create_table(
        "putaway_allocations",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("receive_line_id", sa.Uuid(), nullable=False),
        sa.Column("sku_id", sa.Uuid(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("destination_location_id", sa.Uuid(), nullable=False),
        sa.Column(
            "confirmed_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("idempotency_key", sa.String(length=255), nullable=False),
        sa.Column("request_fingerprint", sa.String(length=64), nullable=False),
        sa.CheckConstraint("quantity > 0", name="ck_putaway_quantity_positive"),
        sa.ForeignKeyConstraint(
            ["destination_location_id"], ["internal_locations.id"], ondelete="RESTRICT"
        ),
        sa.ForeignKeyConstraint(
            ["receive_line_id"], ["receive_lines.id"], ondelete="RESTRICT"
        ),
        sa.ForeignKeyConstraint(["sku_id"], ["skus.id"], ondelete="RESTRICT"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("idempotency_key"),
    )
    op.create_index(
        op.f("ix_putaway_allocations_destination_location_id"),
        "putaway_allocations",
        ["destination_location_id"],
    )
    op.create_index(
        op.f("ix_putaway_allocations_receive_line_id"),
        "putaway_allocations",
        ["receive_line_id"],
    )
    op.create_index(
        op.f("ix_putaway_allocations_sku_id"), "putaway_allocations", ["sku_id"]
    )


def downgrade() -> None:
    op.drop_index(
        op.f("ix_putaway_allocations_sku_id"), table_name="putaway_allocations"
    )
    op.drop_index(
        op.f("ix_putaway_allocations_receive_line_id"),
        table_name="putaway_allocations",
    )
    op.drop_index(
        op.f("ix_putaway_allocations_destination_location_id"),
        table_name="putaway_allocations",
    )
    op.drop_table("putaway_allocations")
    op.drop_index(op.f("ix_stock_balances_sku_id"), table_name="stock_balances")
    op.drop_index(op.f("ix_stock_balances_location_id"), table_name="stock_balances")
    op.drop_table("stock_balances")
    op.drop_index(op.f("ix_receive_lines_sku_id"), table_name="receive_lines")
    op.drop_index(op.f("ix_receive_lines_receive_id"), table_name="receive_lines")
    op.drop_table("receive_lines")
    op.drop_index(op.f("ix_receives_warehouse_id"), table_name="receives")
    op.drop_table("receives")
    op.drop_index(
        op.f("ix_internal_locations_warehouse_id"), table_name="internal_locations"
    )
    op.drop_table("internal_locations")
    op.drop_table("skus")
    op.drop_table("warehouses")
