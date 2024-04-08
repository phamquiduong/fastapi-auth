"""Add users id for primary key

Revision ID: 3e4a38fc7864
Revises: 65c69ade2c89
Create Date: 2024-04-08 22:34:39.763806

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '3e4a38fc7864'
down_revision: Union[str, None] = '65c69ade2c89'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Rename user table to user temp table
    op.rename_table('users', 'users_temp')

    # Create user table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('email', sa.Unicode(255), unique=True, nullable=False),
        sa.Column('password', sa.Unicode(255), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['group_id'], ['groups.id'])
    )

    # Restore data from user temp to user table
    op.execute('INSERT INTO users (email, password, group_id) SELECT email, password, group_id FROM users_temp;')

    # Drop the temp table
    op.drop_table('users_temp')


def downgrade() -> None:
    # Rename user table to user temp table
    op.rename_table('users', 'users_temp')

    # Create user table
    op.create_table(
        'users',
        sa.Column('email', sa.Unicode(255), primary_key=True),
        sa.Column('password', sa.Unicode(255), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['group_id'], ['groups.id'])
    )

    # Restore data from user temp to user table
    op.execute('INSERT INTO users (email, password, group_id) SELECT email, password, group_id FROM users_temp;')

    # Drop the temp table
    op.drop_table('users_temp')
