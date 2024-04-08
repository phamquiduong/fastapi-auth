"""create_user_group_table

Revision ID: 65c69ade2c89
Revises:
Create Date: 2024-03-13 23:20:24.202868

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '65c69ade2c89'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create group table
    op.create_table(
        'groups',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.Unicode(255), unique=True, nullable=False)
    )

    # Create user table
    op.create_table(
        'users',
        sa.Column('email', sa.Unicode(255), primary_key=True),
        sa.Column('password', sa.Unicode(255), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['group_id'], ['groups.id'])
    )


def downgrade() -> None:
    op.drop_table('groups')
    op.drop_table('users')
