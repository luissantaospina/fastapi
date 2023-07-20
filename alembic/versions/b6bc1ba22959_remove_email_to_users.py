"""Remove email to users

Revision ID: b6bc1ba22959
Revises: 6d714694c502
Create Date: 2023-07-20 15:41:04.509906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6bc1ba22959'
down_revision = '6d714694c502'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('users', 'email')


def downgrade() -> None:
    op.add_column('users', sa.Column('email', sa.String(100), nullable=True))
