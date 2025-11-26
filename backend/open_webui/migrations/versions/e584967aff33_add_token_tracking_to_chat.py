"""Add token tracking to chat table

Revision ID: add_token_tracking_to_chat
Revises: a5c220713937
Create Date: 2025-11-25 12:51:00.000000

"""


from alembic import op
import sqlalchemy as sa

revision = "e584967aff33"
down_revision = "a5c220713937"
branch_labels = None
depends_on = None

def upgrade():
    op.add_column(
        "chat",
        sa.Column("tokens_sent", sa.Float(), nullable=True, server_default="0.0"),
    )
    op.add_column(
        "chat",
        sa.Column("tokens_received", sa.Float(), nullable=True, server_default="0.0"),
    )
    op.add_column(
        "chat",
        sa.Column("total_tokens", sa.Float(), nullable=True, server_default="0.0"),
    )


def downgrade():
    op.drop_column("chat", "tokens_sent")
    op.drop_column("chat", "tokens_received")
    op.drop_column("chat", "total_tokens")
