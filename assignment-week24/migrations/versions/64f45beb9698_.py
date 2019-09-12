"""empty message

Revision ID: 64f45beb9698
Revises: 
Create Date: 2019-09-09 22:44:33.091678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64f45beb9698'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('homes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sell', sa.Integer(), nullable=True),
    sa.Column('list', sa.Integer(), nullable=True),
    sa.Column('living', sa.Integer(), nullable=True),
    sa.Column('rooms', sa.Integer(), nullable=True),
    sa.Column('beds', sa.Integer(), nullable=True),
    sa.Column('baths', sa.Integer(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('acres', sa.Float(), nullable=True),
    sa.Column('taxes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('homes')
    # ### end Alembic commands ###