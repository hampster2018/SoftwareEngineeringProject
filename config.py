from os import environ, path

import flask_pymongo
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration variables from .env file."""

    # General Config
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    SECRET_KEY = environ.get("SECRET_KEY")

    # Flask-Session
    SESSION_TYPE = "mongoDB"
    SESSION_MONGODB = flask_pymongo.MongoClient()
    SESSION_MONGODB_DB = environ.get("MONGO_DB")
    SESSION_MONGODB_COLLECT = environ.get("MONGO_COLLECT")


    # Flask-Assets
    LESS_BIN = environ.get("LESS_BIN")
    ASSETS_DEBUG = False
    LESS_RUN_IN_DEBUG = False

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = True

    MONGO_URI = environ.get("MONGO_URI")
    GOOGLE_MAP_KEY=environ.get("GOOGLE_MAP_KEY")
