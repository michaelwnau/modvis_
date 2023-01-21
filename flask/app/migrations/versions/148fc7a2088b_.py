"""empty message

Revision ID: 148fc7a2088b
Revises: 6743e22d67bb
Create Date: 2023-01-18 19:20:49.195964

"""
from alembic import op  # type: ignore
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql  # type: ignore

# revision identifiers, used by Alembic.
revision = '148fc7a2088b'
down_revision = '6743e22d67bb'
branch_labels = None  # type: ignore
depends_on = None  # type: ignore


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('skyrim_trending')
    op.drop_table('trending_mods')
    op.drop_table('skyrim')
    op.drop_table('game')
    op.add_column('games', sa.Column(
        'mods_count', sa.BIGINT(), nullable=False))
    op.add_column('games', sa.Column(
        'mods_url', sa.VARCHAR(length=255), nullable=False))
    op.alter_column('games', 'id',
                    existing_type=sa.BIGINT(),
                    nullable=False,
                    autoincrement=True)
    op.alter_column('games', 'name',
                    existing_type=sa.TEXT(),
                    nullable=False)
    op.alter_column('games', 'name_lower',
                    existing_type=sa.TEXT(),
                    nullable=False)
    op.alter_column('games', 'forum_url',
                    existing_type=sa.TEXT(),
                    nullable=False)
    op.alter_column('games', 'genre',
                    existing_type=sa.TEXT(),
                    nullable=False)
    op.alter_column('games', 'file_count',
                    existing_type=sa.BIGINT(),
                    nullable=False)
    op.alter_column('games', 'downloads',
                    existing_type=sa.BIGINT(),
                    nullable=False)
    op.alter_column('games', 'domain_name',
                    existing_type=sa.TEXT(),
                    nullable=False)
    op.alter_column('games', 'approved_date',
                    existing_type=sa.BIGINT(),
                    nullable=False)
    op.alter_column('games', 'collections',
                    existing_type=sa.BIGINT(),
                    nullable=False)
    op.drop_column('games', 'mods')
    op.drop_column('games', 'nexusmods_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('nexusmods_url', sa.TEXT(),
                  autoincrement=False, nullable=True))
    op.add_column('games', sa.Column('mods', sa.BIGINT(),
                  autoincrement=False, nullable=True))
    op.alter_column('games', 'collections',
                    existing_type=sa.BIGINT(),
                    nullable=True)
    op.alter_column('games', 'approved_date',
                    existing_type=sa.BIGINT(),
                    nullable=True)
    op.alter_column('games', 'domain_name',
                    existing_type=sa.TEXT(),
                    nullable=True)
    op.alter_column('games', 'downloads',
                    existing_type=sa.BIGINT(),
                    nullable=True)
    op.alter_column('games', 'file_count',
                    existing_type=sa.BIGINT(),
                    nullable=True)
    op.alter_column('games', 'genre',
                    existing_type=sa.TEXT(),
                    nullable=True)
    op.alter_column('games', 'forum_url',
                    existing_type=sa.TEXT(),
                    nullable=True)
    op.alter_column('games', 'name_lower',
                    existing_type=sa.TEXT(),
                    nullable=True)
    op.alter_column('games', 'name',
                    existing_type=sa.TEXT(),
                    nullable=True)
    op.alter_column('games', 'id',
                    existing_type=sa.BIGINT(),
                    nullable=True,
                    autoincrement=True)
    op.drop_column('games', 'mods_url')
    op.drop_column('games', 'mods_count')
    op.create_table('game',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('name_lower', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('forum_url', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('nexusmods_url', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('genre', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('file_count', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('downloads', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('domain_name', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('approved_date', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('mods_count', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('mods_url', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('collections', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='game_pkey')
                    )
    op.create_table('skyrim',
                    sa.Column('id', sa.BIGINT(),
                              autoincrement=False, nullable=False),
                    sa.Column('name', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('forum_url', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('nexusmods_url', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('genre', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('file_count', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('downloads', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('domain_name', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('approved_date', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('file_views', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('authors', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('file_endorsements', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('mods', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('categories', postgresql.JSON(
                        astext_type=sa.Text()), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='pk_skyrim')
                    )
    op.create_table('trending_mods',
                    sa.Column('name', sa.TEXT(),
                              autoincrement=False, nullable=False),
                    sa.Column('summmary', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('description', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('picture_url', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('mod_downloads', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('mod_unique_downloads', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('uid', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('mod_id', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('game_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.Column('allow_ratings', sa.BOOLEAN(),
                              autoincrement=False, nullable=False),
                    sa.Column('domain_name', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('category_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.Column('version', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('endoresement_count', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.Column('created_timestamp', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.Column('created_time', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('updated_timestamp', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.Column('updated_time', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('author', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('uploaded_by', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('uploaded_user_profile_url', sa.VARCHAR(
                        length=255), autoincrement=False, nullable=False),
                    sa.Column('contains_adult_content', sa.BOOLEAN(),
                              autoincrement=False, nullable=False),
                    sa.Column('status', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('available', sa.BOOLEAN(),
                              autoincrement=False, nullable=False),
                    sa.Column('user_member_id', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('user_member_group_id', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('user_name', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('endorsement', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.UniqueConstraint(
                        'mod_id', name='unq_trending_mods_mod_id')
                    )
    op.create_table('skyrim_trending',
                    sa.Column('name', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('summary', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('description', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('picture_url', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('mod_downloads', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('mod_unique_downloads', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('uid', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('mod_id', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('game_id', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('allow_rating', sa.BOOLEAN(),
                              autoincrement=False, nullable=True),
                    sa.Column('domain_name', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('category_id', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('version', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('endorsement_count', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('created_timestamp', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('created_time', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('updated_timestamp', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('updated_time', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('author', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('uploaded_by', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('uploaded_users_profile_url', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('contains_adult_content', sa.BOOLEAN(),
                              autoincrement=False, nullable=True),
                    sa.Column('status', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('available', sa.BOOLEAN(),
                              autoincrement=False, nullable=True),
                    sa.Column('user.member_id', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('user.member_group_id', sa.BIGINT(),
                              autoincrement=False, nullable=True),
                    sa.Column('user.name', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('endorsement', sa.TEXT(),
                              autoincrement=False, nullable=True)
                    )
    # ### end Alembic commands ###
