"""empty message

Revision ID: 40c175e229c2
Revises: None
Create Date: 2014-11-10 21:56:58.996000

"""

# revision identifiers, used by Alembic.
revision = '40c175e229c2'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table(u'blogpost')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(u'blogpost',
    sa.Column(u'id', sa.INTEGER(), nullable=False),
    sa.Column(u'title', sa.VARCHAR(length=128), nullable=False),
    sa.Column(u'description', sa.TEXT(), nullable=True),
    sa.Column(u'slides', sa.TEXT(), nullable=True),
    sa.Column(u'video', sa.TEXT(), nullable=True),
    sa.Column(u'user_id', sa.INTEGER(), nullable=True),
    sa.Column(u'venue', sa.VARCHAR(length=128), nullable=True),
    sa.Column(u'venue_url', sa.VARCHAR(length=128), nullable=True),
    sa.Column(u'date', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'users.id'], ),
    sa.PrimaryKeyConstraint(u'id')
    )
    ### end Alembic commands ###
