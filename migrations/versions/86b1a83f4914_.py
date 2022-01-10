"""empty message

Revision ID: 86b1a83f4914
Revises: 75b8961c9999
Create Date: 2021-12-13 18:05:34.089805

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '86b1a83f4914'
down_revision = '75b8961c9999'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('notify_completed', sa.Boolean(), nullable=False))
    op.alter_column('wordlists', 'size',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('wordlists', 'size',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.drop_column('jobs', 'notify_completed')
    # ### end Alembic commands ###