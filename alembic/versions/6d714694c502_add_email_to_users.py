"""Add email to users

Revision ID: 6d714694c502
Revises: 0f9e668dfbd7
Create Date: 2023-07-20 15:37:36.541544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d714694c502'
down_revision = '0f9e668dfbd7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('email', sa.String(100), nullable=False))


def downgrade():
    op.drop_column('users', 'email')
