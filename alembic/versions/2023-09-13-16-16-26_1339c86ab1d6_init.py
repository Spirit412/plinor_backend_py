"""init

Revision ID: 1339c86ab1d6
Revises: 
Create Date: 2023-09-13 16:16:26.702174

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision: str = '1339c86ab1d6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=320), unique=True, index=True, nullable=False),
    sa.Column('middle_name', sa.String(length=1024), nullable=True),
    sa.Column('last_name', sa.String(length=1024), nullable=True),
    sa.Column('phone', sa.String(length=30), nullable=True),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),

    sa.Column('properties_config', postgresql.JSONB(), nullable=False, default={}),

    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),

    sa.Column("is_active", sa.Boolean(), default=False, nullable=False),
    sa.Column("is_superuser", sa.Boolean(), default=False, nullable=False),
    sa.Column("is_verified", sa.Boolean(), default=False, nullable=False),

    sa.PrimaryKeyConstraint('id', name=op.f('pk__user')),
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
