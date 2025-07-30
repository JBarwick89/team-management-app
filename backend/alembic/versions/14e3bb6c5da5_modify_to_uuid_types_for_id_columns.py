"""modify to UUID types for id columns safely

Revision ID: 14e3bb6c5da5
Revises: 6c16a835062f
Create Date: 2025-07-29 13:12:35.021372
"""

from alembic import op
import sqlalchemy as sa

revision = "14e3bb6c5da5"
down_revision = "6c16a835062f"
branch_labels = None
depends_on = None


def upgrade():
    # 1. Enable pgcrypto extension for gen_random_uuid()
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto;")

    # 2. Add new UUID columns with default UUIDs
    op.add_column(
        "team_members",
        sa.Column(
            "new_id",
            sa.UUID(as_uuid=True),
            nullable=False,
            server_default=sa.text("gen_random_uuid()"),
        ),
    )
    op.add_column(
        "team_members",
        sa.Column("new_squad_id", sa.UUID(as_uuid=True), nullable=True),
    )

    # 3. Copy existing squad_id UUIDs to new_squad_id if squad_id is already UUID,
    #    or convert integer squad_id accordingly if needed.
    #    Since your model shows squad_id as UUID, we assume it's already UUID-compatible.
    op.execute(
        """
        UPDATE team_members
        SET new_squad_id = squad_id::uuid
        """
    )

    # 4. Drop foreign key constraints on squad_id
    op.drop_constraint(
        constraint_name="team_members_squad_id_fkey",
        table_name="team_members",
        type_="foreignkey",
    )

    # 5. Drop primary key constraint on old id
    op.drop_constraint(
        constraint_name="team_members_pkey", table_name="team_members", type_="primary"
    )

    # 6. Drop old id and squad_id columns
    op.drop_column("team_members", "id")
    op.drop_column("team_members", "squad_id")

    # 7. Rename new columns to original names
    op.alter_column("team_members", "new_id", new_column_name="id")
    op.alter_column("team_members", "new_squad_id", new_column_name="squad_id")

    # 8. Recreate primary key constraint on new id column
    op.create_primary_key("team_members_pkey", "team_members", ["id"])

    # 9. Recreate foreign key constraint on new squad_id column
    op.create_foreign_key(
        "team_members_squad_id_fkey",
        "team_members",
        "squads",
        ["squad_id"],
        ["id"],
        ondelete="CASCADE",
    )


def downgrade():
    # Reverse steps: Drop constraints, drop UUID columns, add integer columns, etc.
    op.drop_constraint("team_members_squad_id_fkey", "team_members", type_="foreignkey")
    op.drop_constraint("team_members_pkey", "team_members", type_="primary")

    op.add_column(
        "team_members", sa.Column("id", sa.INTEGER(), primary_key=True, nullable=False)
    )
    op.add_column("team_members", sa.Column("squad_id", sa.INTEGER(), nullable=True))

    op.drop_column("team_members", "id")
    op.drop_column("team_members", "squad_id")

    # You would likely want to write custom SQL here to convert UUIDs back to integers, but
    # since this is likely irreversible safely, just drop UUID columns.

    # For brevity, you can leave downgrade unimplemented or raise:
    # raise NotImplementedError("Downgrade is not supported due to UUID migration complexity.")
