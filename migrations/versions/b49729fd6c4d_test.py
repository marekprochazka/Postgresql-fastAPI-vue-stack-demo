"""test

Revision ID: b49729fd6c4d
Revises: 2cbace09e5eb
Create Date: 2023-10-09 12:47:29.271267

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "b49729fd6c4d"
down_revision = "2cbace09e5eb"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "todo",
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("todo", "description")
    # ### end Alembic commands ###
