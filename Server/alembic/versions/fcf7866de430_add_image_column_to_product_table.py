"""Add image column to product table

Revision ID: fcf7866de430
Revises: 891517a347ea
Create Date: 2024-06-16 13:55:25.708152

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fcf7866de430'
down_revision: Union[str, None] = '891517a347ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('product', sa.Column('image', sa.String(100), nullable=True))


def downgrade() -> None:
    op.drop_column('product', 'image')
