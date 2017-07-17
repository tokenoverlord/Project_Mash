# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    # flask config
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # database init
    db.init_app(app)

    migrate = Migrate(app, db)

    # load the db models
    from app import models

    # create the blueprints
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
