# Import the necessary packages and modules from sqlalchemy
import json
import json
from alembic import op  # type: ignore
import requests  # type: ignore
import os
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # type: ignore
from sqlalchemy import Column, Integer, INT, TEXT, VARCHAR, BIGINT, BOOLEAN, TIMESTAMP  # type: ignore
from sqlalchemy import create_engine, Column, Integer, String, DateTime, TIMESTAMP, BigInteger, VARCHAR, BIGINT  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore


# Connect to the PostgreSQL database
engine = create_engine(
    'postgresql://postgres:postgres@localhost:5432/modvis_nm')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Game(Base):  # type: ignore
    __tablename__ = 'game'

    # set autoincrement to True to automatically increment the id
    id = Column(Integer, primary_key=True)  # removed autoincrement=True
    name = Column(VARCHAR(255), nullable=False)
    name_lower = Column(VARCHAR(255), nullable=False)
    forum_url = Column(VARCHAR(255), nullable=False)
    genre = Column(VARCHAR(255), nullable=False)
    file_count = Column(BIGINT, nullable=False)
    downloads = Column(BIGINT, nullable=False)
    domain_name = Column(VARCHAR(255), nullable=False)
    approved_date = Column(TIMESTAMP, nullable=False)
    # removed nullable=False due to error. cf models.py in flask line 22
    mods_count = Column(BIGINT)
    mods_url = Column(VARCHAR(255))  # removed nullable=False due to error
    collections = Column(Integer, nullable=False)

    def formatted_name(self):
        return self.name.title.capitalize()


# Seed the database with data and recreate all the tables each time script is run
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# seed_data = [  # type: ignore
#     # This should be from the API not hard coded
# ]

# Turn the data into a list of objects
game_objects = []
for item in seed_data:
    g = Game(
        name=item['name'],
        name_lower=item['name_lower'],
        forum_url=item['forum_url'],
        genre=item['genre'],
        file_count=item['file_count'],
        downloads=item['downloads'],
        domain_name=item['domain_name'],
        approved_date=item['approved_date'],
        mods_count=item['mods_count'],
        mods_url=item['mods_url'],
        collections=item['collections']
    )
    game_objects.append(g)

# Creaet a session, insert the new records, and commit the changes
session = Session()
session.bulk_save_objects(game_objects)
session.commit()


# Create a new session to query the database
session = Session()

# Run a SELECT * query on the game table
game = session.query(Game).all()

for g in game:
    print(g.name, g.name_lower, g.forum_url, g.genre, g.file_count, g.downloads,
          g.domain_name, g.approved_date, g.mods_count, g.mods_url, g.collections)

# Select * FROM game ORDER BY name
game_objects = session.query(Game).order_by(Game.name).all()

for i, g in enumerate(game_objects):
    print(str(i+1) + ".", g.name, g.name_lower, g.forum_url, g.genre, g.file_count, g.downloads,
          g.domain_name, g.approved_date, g.mods_count, g.mods_url, g.collections)


# connect to the database and create the tables
engine = create_engine('postgresql://username:password@host:port/database')
Base.metadata.create_all(bind=engine)

# Make a request to the API endpoint and get the data
response = requests.get(
    # 'https://api.nexusmods.com/v1/games/mods/7/top.json'
)

# Parse the JSOn response data into a Python dictionary
data = json.loads(response.text)

# Create a session to add the data to the database
Session = sessionmaker(bind=engine)
session = Session()


# Close the session
session.close()
