"""Add a column

Revision ID: ae1027a6acf
Revises: 1975ea83b712
Create Date: 2021-05-05 21:15:19.244940

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ae1027a6acf'
down_revision = '1975ea83b712'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account',sa.Column('last_transaction_date', sa.DateTime))


def downgrade():
    op.drop_column('account','last_transaction_date')
