# This file is used to inject raw SQL values into the game table in the database.
# The format of this file can be replicated for other tables in the database.
# The file adds the new data with the command: $ alembic upgrade head
# The file removes data with the command: alembic downgrade base
# Other commands can be found here: https://alembic.sqlalchemy.org/en/latest/tutorial.html

# Import psycopg2 to connect to the database
import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    """
    dbname='modvis_nm' user='postgres' host='localhost'
    """
)

# This method sets the autocommit flag of the connection to True.
conn.set_session(autocommit=True)

# Open a cursor to perform database operations
cur = conn.cursor()

#
cur.execute(
    """
    DROP TABLE IF EXISTS game;
    """
)

# Insert data into table game that follows the schema:
# id SERIAL, name VARCHAR(255) NOT NULL, name_lower VARCHAR(255) NOT NULL, forum_url VARCHAR(255) NOT NULL, nexusmods_url VARCHAR(255) NOT NULL, genre VARCHAR(255) NOT NULL, file_count bigint, downloads bigint, domain_name VARCHAR(255) NOT NULL, approved_date TIMESTAMP NOT NULL, mods_count bigint, mods_url VARCHAR(255) NOT NULL, collections INT NOT NULL, PRIMARY KEY (id)
cur.execute(
    """
    INSERT INTO game VALUES
    (1, 'Skyrim', 'skyrim', 'https://forums.nexusmods.com/index.php?/forum/43-skyrim/', 'https://www.nexusmods.com/skyrim/', 'RPG', 0, 0, 'nexusmods.com', '2020-01-01 00)
    """
)


cur.execute(
    """
    SELECT [column name(s)] FROM [table name]
    """
)

game_records = cur.fetchall()
for v in game_records:
    print(v[0], v[1],)


print(game_records)


print(' ')  # new line

cur.execute(
    """
    SELECT [column name(s)] FROM [table name] ORDER BY [column name]
    """
)

game_records = cur.fetchall()

for i, v in enumerate(game_records):
    print(str(i+1) + ".", v[0].capitalize(), v[1].capitalize())
