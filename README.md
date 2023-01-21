# modvis_

## Project name: modvis

## Description

modvis is a tool that allows users to easily access and analyze data on the latest mods for various games, as well as track trends and patterns within the video game modding community. This project utilizes external APIs to gather data on the latest mods on Nexus Mods and stores them in a database using SQLAlchemy, an ORM for Python, where they can be queried and displayed on a 1PA or dashboard.

## Technology

The technology stack used for this project includes the following:

- Python 3.9.9
- Flask 1.
- Flask-SQLAlchemy for ORM
- HTTP requests library for API calls with apikey
- PostgreSQL
- ALembic
- psycopg2

The backend architecture for this project is based on a standard Flask app structure. The main file, app.py, initializes the Flask app and sets up the routes for the API endpoints. The models for the database are defined in a separate models.py file using Flask-SQLAlchemy. The database connection is established in the config.py file. The insert_new_mods() function, which calls the external API and inserts the data into the database, is located in the utils.py file.
The APIs endpoints used in this project are shown in the table below.

## Retrospective

Throughout the development of this project, the design evolved to better suit the needs of the user. Initially, the plan was to simply gather data and store it in a database, but as the project progressed, the decision was made to also include analytics and visualization features.

An ORM, specifically SQLAlchemy, was chosen for this project due to its ease of use and ability to handle multiple databases. This allowed for flexibility in the event that the project needed to be scaled to include more games and data in the future. 

It is important to note that the design of the project evolved over time as we had a better understanding of the requirements and constraints. We chose to use the ORM SQLAlchemy due to its flexibility and support for multiple database engines, allowing us to easily switch between different DBs without changing the codebase.

As for the future improvements, it was noted that machine learning models and a pipeline architecture will be implemented to analyze sentiment on forums for particular mods, and on the descriptions of mods themselves by their creators. Also, modelling that will use time-series to predict the creation of categories of mods for different game genres from specific studios. A dashboard visualizing data infographics for specific queries and results from batch queries is also planned to be developed.

## Future Improvements

In the future, machine learning models will be implemented to analyze both sentiment on forums for particular mods, and on the descriptions of mods themselves by their creators. Additionally, time-series analysis will be used to predict the creation of categories of mods for different game genres from specific studios (ie. “within 60 days of a new RPG release from Bethesda Games, the modding community will have created the following types of mods: lighting mods, texture mods, clipping mods.“).

The next milestone feature on the roadmap will be a dashboard visualizing data infographics for specific queries and results from batch queries, making it easier for users to understand and make use of the data. Overall, this project will continue to evolve and improve to provide users with the most comprehensive and accurate data on the modding community.


| Endpoint Path | Method | Parameters |
| --- | --- | --- |
| https://api.nexusmods.com/v1/games/{game_id}/mods/latest_added.json | GET | game_id
: ID of the game to retrieve latest added mods for. |
| https://api.nexusmods.com/v1/games/%7Bgame_id%7D/mods/latest_updated.json | GET | game_id
: ID of the game to retrieve latest updated mods for. |
| https://api.nexusmods.com/v1/games/%7Bgame_id%7D/mods/most_downloaded.json | GET | game_id
: ID of the game to retrieve most downloaded mods for. |
| https://api.nexusmods.com/v1/games/%7Bgame_id%7D/mods/top_rated.json | GET | game_id
: ID of the game to retrieve top rated mods for. |
| https://api.nexusmods.com/v1/games/%7Bgame_id%7D/mods/trending.json | GET | game_id
: ID of the game to retrieve trending mods for. |
