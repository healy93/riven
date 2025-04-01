"""add trakt_id attribute to mediaitem

Revision ID: 834cba7d26b4
Revises: d6c06f357feb
Create Date: 2025-03-31 21:36:38.574921

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '834cba7d26b4'
down_revision: Union[str, None] = 'd6c06f357feb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('MediaItem', schema=None) as batch_op:
        batch_op.add_column(sa.Column('trakt_id', sa.String(), nullable=True))
        batch_op.alter_column('failed_attempts',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('MediaItem', schema=None) as batch_op:
        batch_op.alter_column('failed_attempts',
               existing_type=sa.INTEGER(),
               server_default=sa.text('0'),
               existing_nullable=True)
        batch_op.drop_column('trakt_id')

    # ### end Alembic commands ###
