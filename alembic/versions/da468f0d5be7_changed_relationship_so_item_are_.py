"""Changed relationship so Item are deleted upon user term.

Revision ID: da468f0d5be7
Revises: 7744814d38fb
Create Date: 2024-04-18 15:13:39.345366

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da468f0d5be7'
down_revision: Union[str, None] = '7744814d38fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###