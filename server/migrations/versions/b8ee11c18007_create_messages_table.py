"""create messages table
Revision ID: b8ee11c18007
Revises: 
Create Date: 2026-01-15 18:53:02.025949
"""
from alembic import op
import sqlalchemy as sa

revision = 'b8ee11c18007'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('messages')