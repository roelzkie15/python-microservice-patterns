"""Initial migrations

Revision ID: fa1e57d87087
Revises: 
Create Date: 2022-07-23 18:17:54.439068

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "fa1e57d87087"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "bookings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(), server_default="created", nullable=False),
        sa.Column("parking_slot_ref_no", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_bookings_id"), "bookings", ["id"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_bookings_id"), table_name="bookings")
    op.drop_table("bookings")
    # ### end Alembic commands ###
