"""empty message

Revision ID: 4b45ba775f06
Revises: 392bf3d16726
Create Date: 2014-05-31 22:09:58.228633

"""

# revision identifiers, used by Alembic.
revision = '4b45ba775f06'
down_revision = '392bf3d16726'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('issue', sa.Column('reporter_id', sa.BigInteger(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('issue', 'reporter_id')
    ### end Alembic commands ###
