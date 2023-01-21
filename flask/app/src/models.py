from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Column, Integer, INT, TEXT, VARCHAR, BIGINT, BOOLEAN, TIMESTAMP  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore

import datetime
import json
import requests  # type: ignore
import os

# Define the models using SQLAlchemy and declare the database as db
db = SQLAlchemy()

# Create the Models for the database

# Create a class to represent the games table.
# This holds all the games available on Nexus Mods.


class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    name_lower = db.Column(db.String(255), nullable=False)
    forum_url = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    file_count = db.Column(db.BIGINT, nullable=False)
    downloads = db.Column(db.BIGINT, nullable=False)
    domain_name = db.Column(db.String(255), nullable=False)
    approved_date = db.Column(db.TIMESTAMP, nullable=False)
    mods_count = db.Column(db.BIGINT)
    mods_url = db.Column(db.String(255))
    collections = db.Column(db.Integer, nullable=False)

    def __init__(id, self, name, name_lower, forum_url, genre,
                 file_count, downloads, domain_name, approved_date,
                 mods_count, mods_url, collections):
        self.id = id
        self.name = name
        self.name_lower = name_lower
        self.forum_url = forum_url
        self.genre = genre
        self.file_count = file_count
        self.downloads = downloads
        self.domain_name = domain_name
        self.approved_date = approved_date
        self.mods_count = mods_count
        self.mods_url = mods_url
        self.collections = collections

    def __repr__(self) -> str:
        return '<Game %r>'.format(self.name)

# Create a function to insert the data into the database from the external facing API endpoint

    def insert_games():
        # Make a request to the API endpoint
        response = requests.get(
            'https://api.nexusmods.com/v1/games.json?include_unapproved=false')

# Parse the JSON response
        data = json.loads(response.text)

# Create a list of dictionaries to hold the data
    games_data = []
    for game in games_data:
        games_data.append({'id': game['id'], 'name': game['name'], 'name_lower': game['name'].lower(),
                           'forum_url': game['forum_url'], 'genre': game['genre'], 'file_count': game['file_count'],
                           'downloads': game['downloads'], 'domain_name': game['domain_name'], 'approved_date': game['approved_date'],
                           'mods_count': game['mods_count'], 'mods_url': game['mods_url'], 'collections': game['collections']})


# Create a function to insert the data into the database
def insert_games(games_data):
    # Use the bulk_insert_mappings() method to insert the data
    db.session.bulk_insert_mappings(Game, games_data)

# Commit the data to the database
    db.session.commit()


# Create a class to represent the NewMods table.
# This holds the "10 Newest Mods" for a named game on Nexus Mods.
# The endpoint for this is https://api.nexusmods.com/v1/games/{game_domain_name}/mods/latest_added.json
# For development purposes, the game_domain_name is "skyrim"

class New_Mods(db.Model):
    __tablename__ = 'new_mods'
    uid = db.Column(db.BigInteger, nullable=False)
    # Possibly change mod_id to BIGINT and make it the primary_key
    mod_id = db.Column(db.BigInteger, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    allow_rating = db.Column(db.Boolean, nullable=False)
    domain_name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    version = db.Column(db.String(255), nullable=False)
    endorsement_count = db.Column(db.Integer, nullable=False)
    created_timestamp = db.Column(db.BigInteger, nullable=False)
    created_time = db.Column(db.String(255), nullable=False)
    updated_timestamp = db.Column(db.BigInteger, nullable=False)
    updated_time = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    uploaded_by = db.Column(db.String(255), nullable=False)
    uploaded_users_profile_url = db.Column(db.String, nullable=False)
    contains_adult_content = db.Column(db.Boolean, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    available = db.Column(db.Boolean, nullable=False)
    member_id = db.Column(db.Integer)
    member_group_id = db.Column(db.Integer)
    user_name = db.Column(db.String(255))
    endorsement = db.Column(db.String(255))

# The __init__ method is used to initialize the class attributes the first time the class is instantiated
    def __init__(uid, self, mod_id, game_id, allow_rating, domain_name,
                 category_id, version, endorsement_count, created_timestamp,
                 created_time, updated_timestamp, updated_time, author,
                 uploaded_by, uploaded_users_profile_url, contains_adult_content,
                 status, available, member_id, member_group_id, user_name,
                 endorsement):
        self.uid = uid
        self.mod_id = mod_id
        self.game_id = game_id
        self.allow_rating = allow_rating
        self.domain_name = domain_name
        self.category_id = category_id
        self.version = version
        self.endorsement_count = endorsement_count
        self.created_timestamp = created_timestamp
        self.created_time = created_time
        self.updated_timestamp = updated_timestamp
        self.updated_time = updated_time
        self.author = author
        self.uploaded_by = uploaded_by
        self.uploaded_users_profile_url = uploaded_users_profile_url
        self.contains_adult_content = contains_adult_content
        self.status = status
        self.available = available
        self.member_id = member_id
        self.member_group_id = member_group_id
        self.user_name = user_name
        self.endorsement = endorsement

# The __repr__ method is used to return a string representation of the class when it is queried.
    def __rep__(self) -> str:
        return '<New Mods %r>'.format(self.mod_id)

# Create a function to insert the data into the database from the external facing API endpoint

    def insert_new_mods():
        # Make a request to the API endpoint
        response = requests.get(
            'https://api.nexusmods.com/v1/games/skyrim/mods/latest_added.json')

# Parse the JSON response
        data = json.loads(response.text)

# Create a list of dictionaries to hold the data
    new_mods_data = []
    for mod in new_mods_data:
        new_mods_data.append({'uid': mod['uid'], 'mod_id': mod['mod_id'], 'game_id': mod['game_id'],
                              'allow_rating': mod['allow_rating'], 'domain_name': mod['domain_name'], 'category_id': mod['category_id'],
                              'version': mod['version'], 'endorsement_count': mod['endorsement_count'], 'created_timestamp': mod['created_timestamp'],
                              'created_time': mod['created_time'], 'updated_timestamp': mod['updated_timestamp'], 'updated_time': mod['updated_time'],
                              'author': mod['author'], 'uploaded_by': mod['uploaded_by'], 'uploaded_users_profile_url': mod['uploaded_users_profile_url'],
                              'contains_adult_content': mod['contains_adult_content'], 'status': mod['status'], 'available': mod['available'],
                              'member_id': mod['member_id'], 'member_group_id': mod['member_group_id'], 'user_name': mod['user_name'],
                              'endorsement': mod['endorsement']})


# This function is used to insert the data into the database
def insert_new_mods(new_mods_data):
    # Use the bulk_insert_mappings() method to insert the data
    db.session.bulk_insert_mappings(New_Mods, new_mods_data)
# Then commit the data to the database
    db.session.commit()


# Create a class to represent the trending_mods table.
# This holds all of the trending mods on Nexus Mods
class Trending(db.Model):
    __tablename__ = 'trending_mods'
    name = db.Column(db.Text, primary_key=True)
    summary = db.Column(db.Text)
    description = db.Column(db.Text)
    picture_url = db.Column(db.String(255))
    mod_downloads = db.Column(db.BigInteger)
    mod_unique_downloads = db.Column(db.BigInteger)
    uid = db.Column(db.String(255))
    mod_id = db.Column(db.Integer)
    game_id = db.Column(db.Integer)
    allow_ratings = db.Column(db.Boolean)
    domain_name = db.Column(db.String(255))
    category_id = db.Column(db.Integer)
    version = db.Column(db.String(255))
    endorsement_count = db.Column(db.Integer)
    created_timestamp = db.Column(db.String(255))
    updated_timestamp = db.Column(db.String(255))
    updated_time = db.Column(db.TIMESTAMP)
    author = db.Column(db.String(255))
    uploaded_by = db.Column(db.String(255))
    uploaded_user_profile_url = db.Column(db.String(255))
    contains_adult_content = db.Column(db.Boolean)
    status = db.Column(db.String(255))
    available = db.Column(db.Boolean)
    user_member_id = db.Column(db.BigInteger)
    user_member_group_id = db.Column(db.BigInteger)
    user_name = db.Column(db.String(255))
    endorsement = db.Column(db.Text)

# The __init__ method is used to initialize the class when it is created.
    def __init__(name, self, summary, description, picture_url, mod_downloads,
                 mod_unique_downloads, uid, mod_id, game_id, allow_ratings,
                 domain_name, category_id, version, endorsement_count,
                 created_timestamp, updated_timestamp, updated_time, author,
                 uploaded_by, uploaded_user_profile_url, contains_adult_content,
                 status, available, user_member_id, user_member_group_id,
                 user_name, endorsement):
        self.name = name
        self.summary = summary
        self.description = description
        self.picture_url = picture_url
        self.mod_downloads = mod_downloads
        self.mod_unique_downloads = mod_unique_downloads
        self.uid = uid
        self.mod_id = mod_id
        self.game_id = game_id
        self.allow_ratings = allow_ratings
        self.domain_name = domain_name
        self.category_id = category_id
        self.version = version
        self.endorsement_count = endorsement_count
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp
        self.updated_time = updated_time
        self.author = author
        self.uploaded_by = uploaded_by
        self.uploaded_user_profile_url = uploaded_user_profile_url
        self.contains_adult_content = contains_adult_content
        self.status = status
        self.available = available
        self.user_member_id = user_member_id
        self.user_member_group_id = user_member_group_id
        self.user_name = user_name
        self.endorsement = endorsement

    def __repr__(self) -> str:
        return '<Trending Mods %r>'.format(self.name)


# Create a function to insert the data into the database from the external facing API endpoint


    def insert_trending():
        # Make a request to the API endpoint
        response = requests.get(
            'https://api.nexusmods.com/v1/games/morrowind/mods/trending.json')

# Parse the JSON response
        data = json.loads(response.text)

# Create a list of dictionaries to hold the data
    trending_data = []
    for trending in trending_data:
        trending_data.append({'name': trending['name'], 'summary': trending['summary'], 'description': trending['description'],
                              'picture_url': trending['picture_url'], 'mod_downloads': trending['mod_downloads'], 'mod_unique_downloads': trending['mod_unique_downloads'],
                              'uid': trending['uid'], 'mod_id': trending['mod_id'], 'game_id': trending['game_id'], 'allow_ratings': trending['allow_ratings'],
                              'domain_name': trending['domain_name'], 'category_id': trending['category_id'], 'version': trending['version'], 'endorsement_count': trending['endorsement_count'],
                              'created_timestamp': trending['created_timestamp'], 'updated_timestamp': trending['updated_timestamp'], 'updated_time': trending['updated_time'],
                              'author': trending['author'], 'uploaded_by': trending['uploaded_by'], 'uploaded_user_profile_url': trending['uploaded_user_profile_url'],
                              'contains_adult_content': trending['contains_adult_content'], 'status': trending['status'], 'available': trending['available'],
                              'user_member_id': trending['user_member_id'], 'user_member_group_id': trending['user_member_group_id'], 'user_name': trending['user_name'],
                              'endorsement': trending['endorsement']})


# Create a function to insert the data into the database
def insert_trending(trending_data):
    # Use the bulk_insert_mappings() method to insert the data
    db.session.bulk_insert_mappings(Trending, trending_data)
# Commit the data to the database
    db.session.commit()
