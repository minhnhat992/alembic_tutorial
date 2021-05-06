"""merge 2 branches

Revision ID: 79891bffab08
Revises: ae1027a6acf, 27c6a30d7c24
Create Date: 2021-05-05 22:25:41.816167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79891bffab08'
down_revision = ('ae1027a6acf', '27c6a30d7c24')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
