"""Inital migrations

Revision ID: 3a414c21545c
Revises: 
Create Date: 2022-05-23 18:52:57.406382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a414c21545c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parking_slots',
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('uuid'),
    schema='parking_schema'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parking_slots', schema='parking_schema')
    # ### end Alembic commands ###