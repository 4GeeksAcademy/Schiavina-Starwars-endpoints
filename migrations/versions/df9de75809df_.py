"""empty message

Revision ID: df9de75809df
Revises: 0b8fb001d6a9
Create Date: 2023-05-26 19:10:51.470095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df9de75809df'
down_revision = '0b8fb001d6a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('personaje', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=250), nullable=False))
        batch_op.add_column(sa.Column('eye_color', sa.String(length=250), nullable=False))
        batch_op.add_column(sa.Column('hair_color', sa.String(length=250), nullable=False))

    with op.batch_alter_table('personaje_favorito', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('personaje_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'personaje', ['personaje_id'], ['id'])
        batch_op.create_foreign_key(None, 'usuario', ['usuario_id'], ['id'])

    with op.batch_alter_table('planeta', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=250), nullable=False))
        batch_op.add_column(sa.Column('population', sa.String(length=250), nullable=False))
        batch_op.add_column(sa.Column('terrain', sa.String(length=250), nullable=False))

    with op.batch_alter_table('planeta_favorito', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('planeta_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'usuario', ['usuario_id'], ['id'])
        batch_op.create_foreign_key(None, 'planeta', ['planeta_id'], ['id'])

    with op.batch_alter_table('vehicle', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=250), nullable=False))
        batch_op.add_column(sa.Column('crew', sa.String(length=250), nullable=False))
        batch_op.add_column(sa.Column('vehicle_class', sa.String(length=250), nullable=False))

    with op.batch_alter_table('vehicle_favorito', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('vehicle_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'vehicle', ['vehicle_id'], ['id'])
        batch_op.create_foreign_key(None, 'usuario', ['usuario_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicle_favorito', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('vehicle_id')
        batch_op.drop_column('usuario_id')

    with op.batch_alter_table('vehicle', schema=None) as batch_op:
        batch_op.drop_column('vehicle_class')
        batch_op.drop_column('crew')
        batch_op.drop_column('name')

    with op.batch_alter_table('planeta_favorito', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('planeta_id')
        batch_op.drop_column('usuario_id')

    with op.batch_alter_table('planeta', schema=None) as batch_op:
        batch_op.drop_column('terrain')
        batch_op.drop_column('population')
        batch_op.drop_column('name')

    with op.batch_alter_table('personaje_favorito', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('personaje_id')
        batch_op.drop_column('usuario_id')

    with op.batch_alter_table('personaje', schema=None) as batch_op:
        batch_op.drop_column('hair_color')
        batch_op.drop_column('eye_color')
        batch_op.drop_column('name')

    # ### end Alembic commands ###