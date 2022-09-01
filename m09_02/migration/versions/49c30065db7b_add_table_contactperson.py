"""add table ContactPerson

Revision ID: 49c30065db7b
Revises: 13f015ab50be
Create Date: 2022-09-01 20:49:43.758967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49c30065db7b'
down_revision = '13f015ab50be'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_persons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('cell_phone', sa.String(length=100), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact_persons')
    # ### end Alembic commands ###
