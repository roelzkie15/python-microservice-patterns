"""Update ParkingSlot.status default value to available

Revision ID: 5e95058bcf50
Revises: 6935a5c10469
Create Date: 2022-06-10 20:41:18.696370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e95058bcf50'
down_revision = '6935a5c10469'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parking_slots', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(),
               server_default='available',
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parking_slots', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(),
               server_default=sa.text("'pending'"),
               existing_nullable=False)

    # ### end Alembic commands ###
