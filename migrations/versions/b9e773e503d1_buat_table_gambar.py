"""buat table gambar

Revision ID: b9e773e503d1
Revises: 6c707f511352
Create Date: 2024-07-23 17:41:49.370332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9e773e503d1'
down_revision = '6c707f511352'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gambar',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('judul', sa.String(length=38), nullable=False),
    sa.Column('pathname', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gambar')
    # ### end Alembic commands ###
