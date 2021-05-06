"""add a shopping cart table

Revision ID: 27c6a30d7c24
Revises: 1975ea83b712
Create Date: 2021-05-05 21:15:19.244940

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '27c6a30d7c24'
down_revision = '1975ea83b712'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'shopping_cart',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name_shop', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200))
    )


def downgrade():
    op.drop_table('shopping_cart')
