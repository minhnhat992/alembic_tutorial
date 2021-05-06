"""Add a column

Revision ID: 79891bffab08
Revises: 2cdbd6535f5a
Create Date: 2021-05-05 21:15:19.244940

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '79891bffab08'
down_revision = '2cdbd6535f5a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account',sa.Column('last_transaction_date', sa.DateTime))


def downgrade():
    op.drop_column('account','last_transaction_date')
