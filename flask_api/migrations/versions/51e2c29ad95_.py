""" create the User table

Revision ID: 51e2c29ad95
Revises: 4f2e2c180af
Create Date: 2016-10-02 16:00:01.042947

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '51e2c29ad95'
down_revision = '4f2e2c180af'


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=300), nullable=False),
        sa.Column('last_name', sa.String(length=300), nullable=False),
        sa.Column('email', sa.String(length=300), nullable=False),
        sa.Column('password', sa.String(length=300), nullable=False),
        sa.Column('created_at', sa.String(length=300), nullable=False),
        sa.Column('modified_at', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('user')
