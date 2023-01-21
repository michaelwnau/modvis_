"""create game

Revision ID: ad1e6b3ea540
Revises: 
Create Date: 2023-01-18 11:55:54.967914

"""
from alembic import op  # type: ignore
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad1e6b3ea540'
down_revision = None  # type: ignore
branch_labels = None  # type: ignore
depends_on = None  # type: ignore


def upgrade():
    op.execute(
        """
    CREATE TABLE game (
        id SERIAL,
        name VARCHAR(255) NOT NULL,
        name_lower VARCHAR(255) NOT NULL,
        forum_url VARCHAR(255) NOT NULL,
        nexusmods_url VARCHAR(255) NOT NULL,
        genre VARCHAR(255) NOT NULL,
        file_count bigint,
        downloads bigint,
        domain_name VARCHAR(255) NOT NULL,
        approved_date TIMESTAMP NOT NULL,
        mods_count bigint,
        mods_url VARCHAR(255) NOT NULL,
        collections INT NOT NULL,
        PRIMARY KEY (id)
);
    """
    )


def downgrade():
    op.execute(
        """
    DROP TABLE games;
    
    """
    )
