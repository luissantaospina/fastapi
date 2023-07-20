"""Add is activate to users

Revision ID: a8290ba306c0
Revises: b6bc1ba22959
Create Date: 2023-07-20 15:42:57.668403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8290ba306c0'
down_revision = 'b6bc1ba22959'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('is_activate', sa.Boolean, default=True))


def downgrade():
    op.drop_column('users', 'is_activate')
