"""empty message

Revision ID: 955996901b47
Revises: 8cc18c708931
Create Date: 2020-10-04 14:42:27.468802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '955996901b47'
down_revision = '8cc18c708931'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_link_timestamp'), 'link', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_link_timestamp'), table_name='link')
    # ### end Alembic commands ###
