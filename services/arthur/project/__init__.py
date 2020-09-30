# Package Imports
import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

# Project Imports
from project.config import DevelopmentConfig
from project.app.models import User, Playlist, AdminUser, db
from project.app.handlers.DBHandler import *
# from project.app.handlers.spotify.SpotifyAPIHandler import SpotifyAPIHandler, spotify_api

# instantiate the extensions
migrate = Migrate()

def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    from project.app.spotify_blueprint import spotify_blueprint
    app.register_blueprint(spotify_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app