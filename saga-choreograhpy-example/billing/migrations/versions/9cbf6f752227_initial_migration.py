"""Initial migration

Revision ID: 9cbf6f752227
Revises: 
Create Date: 2022-05-22 17:22:49.274560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cbf6f752227'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('billing_requests',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('total', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('reference_no', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('reference_no'),
    schema='billing_schema'
    )
    op.create_table('payment_reconciliations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('amount', sa.Numeric(precision=12, scale=2), nullable=False),
    sa.Column('billing_request_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['billing_request_id'], ['billing_schema.billing_requests.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='billing_schema'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment_reconciliations', schema='billing_schema')
    op.drop_table('billing_requests', schema='billing_schema')
    # ### end Alembic commands ###