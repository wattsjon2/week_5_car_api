"""added car table

Revision ID: 36682e4cd82c
Revises: bf77fb3a7030
Create Date: 2021-11-10 16:42:00.343139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36682e4cd82c'
down_revision = 'bf77fb3a7030'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('make', sa.String(length=150), nullable=True),
    sa.Column('model', sa.String(length=150), nullable=True),
    sa.Column('year', sa.String(length=150), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car')
    # ### end Alembic commands ###