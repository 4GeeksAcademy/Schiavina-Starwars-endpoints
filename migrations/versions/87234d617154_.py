"""empty message

Revision ID: 87234d617154
Revises: 3b3f1453b63f
Create Date: 2023-05-26 18:47:04.370222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87234d617154'
down_revision = '3b3f1453b63f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personaje',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('personaje')
    # ### end Alembic commands ###