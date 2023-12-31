"""Create database

Revision ID: 0668e2f041ea
Revises: 
Create Date: 2023-05-26 12:18:15.966106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0668e2f041ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('player', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('player', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('player', 'number',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('player', 'team',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('player', 'team',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('player', 'number',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('player', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('player', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
