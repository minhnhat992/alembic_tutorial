"""create account table

Revision ID: 2cdbd6535f5a
Revises: 
Create Date: 2021-05-05 21:03:26.178274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cdbd6535f5a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('name',sa.String(50),nullable=False),
        sa.Column('description',sa.Unicode(200))
    )



def downgrade():
    op.drop_table('account')
