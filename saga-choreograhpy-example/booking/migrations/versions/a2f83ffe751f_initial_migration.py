"""Initial migration

Revision ID: a2f83ffe751f
Revises: 
Create Date: 2022-05-23 19:49:37.182505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2f83ffe751f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('status', sa.String(), server_default='created', nullable=False),
    sa.Column('parking_space_uuid', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='booking_schema'
    )
    op.create_index(op.f('ix_booking_schema_bookings_id'), 'bookings', ['id'], unique=True, schema='booking_schema')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_booking_schema_bookings_id'), table_name='bookings', schema='booking_schema')
    op.drop_table('bookings', schema='booking_schema')
    # ### end Alembic commands ###