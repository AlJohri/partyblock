"""empty message

Revision ID: 392bf3d16726
Revises: 2a8ec83e1d60
Create Date: 2014-05-31 21:19:26.794455

"""

# revision identifiers, used by Alembic.
revision = '392bf3d16726'
down_revision = '2a8ec83e1d60'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reporter',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('witty_title', sa.String(), nullable=True),
    sa.Column('civic_points', sa.BigInteger(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reporter')
    ### end Alembic commands ###
