"""Update long for password

Revision ID: 103f28f4d72b
Revises: a8290ba306c0
Create Date: 2023-07-24 10:42:53.003469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '103f28f4d72e'
down_revision = 'a8290ba306c0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('users', 'password', type_=sa.String(length=256))


def downgrade():
    op.alter_column('users', 'password', type_=sa.String(length=50))
