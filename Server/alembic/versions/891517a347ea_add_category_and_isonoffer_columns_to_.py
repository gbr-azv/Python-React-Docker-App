"""Add category and isOnOffer columns to product table

Revision ID: 891517a347ea
Revises: 
Create Date: 2024-06-15 18:09:24.256615

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '891517a347ea'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('product', sa.Column('category', sa.String(100), nullable=True))
    op.add_column('product', sa.Column('isOnOffer', sa.Boolean(), nullable=True))


def downgrade() -> None:
    op.drop_column('product', 'category')
    op.drop_column('product', 'isOnOffer')
