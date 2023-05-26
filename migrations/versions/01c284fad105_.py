"""empty message

Revision ID: 01c284fad105
Revises: 5aa0e8cb43a7
Create Date: 2023-05-26 18:51:50.340362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01c284fad105'
down_revision = '5aa0e8cb43a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planeta_favorito',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicle_favorito',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicle_favorito')
    op.drop_table('planeta_favorito')
    # ### end Alembic commands ###