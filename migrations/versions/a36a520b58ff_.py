"""empty message

Revision ID: a36a520b58ff
Revises: 62df5d76ee47
Create Date: 2021-11-22 21:11:35.724588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a36a520b58ff'
down_revision = '62df5d76ee47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hashfiles', sa.Column('name2', sa.TEXT(length=256), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hashfiles', 'name2')
    # ### end Alembic commands ###