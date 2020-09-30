# Package Imports
from flask import Blueprint, redirect, request, url_for

# Project imports
from project.app.handlers import DBHandler
from project.app.handlers.spotify.SpotifyAPI import SpotifyAPI
from project.app.handlers.spotify.SpotifyAPIHandler import SpotifyAPIHandler
from project.app.handlers import DBHandler
from project.app.models import User
from project import db

spotify_blueprint = Blueprint('spotify_blueprint', __name__)

@spotify_blueprint.route('/', methods=['GET'])
def index():

    if 'access_token' in request.args:

        spotify_api = SpotifyAPI()

        spotify_api.set_access_token(request.args['access_token'])

        # Get user profile and insert into db if not already.

        user = spotify_api.get_user_profile()

        if 'error' in user:

            return user

        # db_handler = DBHandler()
        DBHandler().insert_user(user)

        return {'user': user['display_name']}

    else:

        return {'arthur_auth_url': url_for('spotify_blueprint.authorization')}

@spotify_blueprint.route('/authorization', methods=['GET'])
def authorization():
    """
    Authorization refers to the user granting access to his/her Spotify data.
    :return: String
        A url which points to the Spotify arthur authorization page.
    """

    spotify_api = SpotifyAPI()

    return {'spotify_auth_url': spotify_api.request_authorization_to_access_data_url()}