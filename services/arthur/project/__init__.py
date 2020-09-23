import os
from flask import Flask, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from project.app.models import User, Playlist, AdminUser
from project.app.handlers.DBHandler import *
from project.app.handlers.spotify.SpotifyAPIHandler import SpotifyAPIHandler
from project.app.handlers.spotify.SpotifyAPI import SpotifyAPI

# instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()
spotify_api = SpotifyAPI()


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

    from project.app.blueprint import spotify_blueprint
    app.register_blueprint(spotify_blueprint)

    #Routes

    @app.route('/authorization', methods=['GET'])
    def authorization():
        """
        Authorization refers to the user granting access to his/her Spotify data.
        :return: String
            A url which points to the Spotify arthur authorization page.
        """
        return redirect(spotify_api.request_authorization_to_access_data_url())

    @app.route('/authentication', methods=['GET'])
    def authentication():
        """
        Authentication refers to the user's access and refresh keys which are stored and used to send requests to the
        Spotify Web API.
        :return: Response object (if successful) that redirects the user to another location. Dict (if unsuccessful).
        """

        # The user pressed 'Cancel' on the Spotify authorization page.

        if 'error' in request.args and request.args['error'] == 'access_denied':
            return {'error': 'The user did not authorized this arthur to access data.'}

        # Authenticate user

        spotify_api_handler = SpotifyAPIHandler()

        if spotify_api_handler.authenticate(request.args):
            # If the user was authenticated, return to home page.

            return redirect('/')

        # The user was not authenticated.

        return {'error': 'There was a problem authenticating the user.'}

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app