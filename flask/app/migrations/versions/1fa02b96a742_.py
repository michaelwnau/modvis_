"""empty message

Revision ID: 1fa02b96a742
Revises: 64c2a977bbd3
Create Date: 2023-01-20 13:39:31.454604

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1fa02b96a742'
down_revision = '64c2a977bbd3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('new_mods',
    sa.Column('uid', sa.BigInteger(), nullable=False),
    sa.Column('mod_id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('allow_rating', sa.Boolean(), nullable=False),
    sa.Column('domain_name', sa.String(length=255), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('version', sa.String(length=255), nullable=False),
    sa.Column('endorsement_count', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.BigInteger(), nullable=False),
    sa.Column('created_time', sa.String(length=255), nullable=False),
    sa.Column('updated_timestamp', sa.BigInteger(), nullable=False),
    sa.Column('updated_time', sa.String(length=255), nullable=False),
    sa.Column('author', sa.String(length=255), nullable=False),
    sa.Column('uploaded_by', sa.String(length=255), nullable=False),
    sa.Column('uploaded_users_profile_url', sa.String(), nullable=False),
    sa.Column('contains_adult_content', sa.Boolean(), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('available', sa.Boolean(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('member_group_id', sa.Integer(), nullable=True),
    sa.Column('user_name', sa.String(length=255), nullable=True),
    sa.Column('endorsement', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.drop_table('game')
    op.drop_table('skyrim_trending')
    op.drop_table('skyrim')
    op.add_column('games', sa.Column('mods_count', sa.BIGINT(), nullable=True))
    op.add_column('games', sa.Column('mods_url', sa.String(length=255), nullable=True))
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
    op.add_column('trending_mods', sa.Column('summary', sa.Text(), nullable=True))
    op.add_column('trending_mods', sa.Column('endorsement_count', sa.Integer(), nullable=True))
    op.alter_column('trending_mods', 'picture_url',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('trending_mods', 'game_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('trending_mods', 'allow_ratings',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('trending_mods', 'domain_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('trending_mods', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('trending_mods', 'version',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('trending_mods', 'created_timestamp',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('trending_mods', 'updated_timestamp',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('trending_mods', 'updated_time',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('trending_mods', 'author',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('trending_mods', 'uploaded_by',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('trending_mods', 'uploaded_user_profile_url',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('trending_mods', 'contains_adult_content',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('trending_mods', 'status',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('trending_mods', 'available',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('trending_mods', 'user_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_constraint('unq_trending_mods_mod_id', 'trending_mods', type_='unique')
    op.drop_column('trending_mods', 'endoresement_count')
    op.drop_column('trending_mods', 'summmary')
    op.drop_column('trending_mods', 'created_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trending_mods', sa.Column('created_time', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.add_column('trending_mods', sa.Column('summmary', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('trending_mods', sa.Column('endoresement_count', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_unique_constraint('unq_trending_mods_mod_id', 'trending_mods', ['mod_id'])
    op.alter_column('trending_mods', 'user_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('trending_mods', 'available',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('trending_mods', 'status',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('trending_mods', 'contains_adult_content',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('trending_mods', 'uploaded_user_profile_url',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('trending_mods', 'uploaded_by',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('trending_mods', 'author',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('trending_mods', 'updated_time',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('trending_mods', 'updated_timestamp',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('trending_mods', 'created_timestamp',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('trending_mods', 'version',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('trending_mods', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('trending_mods', 'domain_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('trending_mods', 'allow_ratings',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('trending_mods', 'game_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('trending_mods', 'picture_url',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.drop_column('trending_mods', 'endorsement_count')
    op.drop_column('trending_mods', 'summary')
    op.add_column('games', sa.Column('nexusmods_url', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('games', sa.Column('mods', sa.BIGINT(), autoincrement=False, nullable=True))
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
    op.create_table('skyrim',
    sa.Column('id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('forum_url', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('nexusmods_url', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('genre', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('file_count', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('downloads', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('domain_name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('approved_date', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('file_views', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('authors', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('file_endorsements', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('mods', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('categories', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_skyrim')
    )
    op.create_table('skyrim_trending',
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('summary', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('picture_url', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('mod_downloads', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('mod_unique_downloads', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('uid', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('mod_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('game_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('allow_rating', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('domain_name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('category_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('version', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('endorsement_count', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('created_timestamp', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('created_time', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('updated_timestamp', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('updated_time', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('author', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('uploaded_by', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('uploaded_users_profile_url', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('contains_adult_content', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('status', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('available', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('user.member_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('user.member_group_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('user.name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('endorsement', sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.create_table('game',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('name_lower', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('forum_url', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('genre', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('file_count', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('downloads', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('domain_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('approved_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('mods_count', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('mods_url', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('collections', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='game_pkey')
    )
    op.drop_table('new_mods')
    # ### end Alembic commands ###