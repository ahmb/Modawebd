"""empty message

Revision ID: c7ab9eab4b8
Revises: 3aaeeb035785
Create Date: 2014-11-12 17:58:35.043000

"""

# revision identifiers, used by Alembic.
revision = 'c7ab9eab4b8'
down_revision = '3aaeeb035785'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    ### end Alembic commands ###
