# Package Imports
from flask import Blueprint, redirect, request, url_for

# Project imports
from project.app.handlers import DBHandler
from project.app.handlers.spotify.SpotifyAPIHandler import SpotifyAPIHandler, spotify_api

spotify_blueprint = Blueprint('spotify_blueprint', __name__)

@spotify_blueprint.route('/')
def index():
    # Verify user is authenticated. Otherwise authenticate.
    if not spotify_api.is_authenticated():
        return redirect(url_for('spotify_blueprint.authorization'))

    # Get user profile and insert into db if not already.
    user = spotify_api.get_user_profile()

    if 'error' in user:
        return user

    db_handler = DBHandler()
    db_handler.insert_user(user)
    #
    return {'user': user['display_name']}

@spotify_blueprint.route('/authorization', methods=['GET'])
def authorization():
    """
    Authorization refers to the user granting access to his/her Spotify data.
    :return: String
        A url which points to the Spotify arthur authorization page.
    """
    return {'spotify_auth_url': spotify_api.request_authorization_to_access_data_url()}

@spotify_blueprint.route('/authentication', methods=['GET'])
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

        # return {'auth': True}
        return redirect(url_for('spotify_blueprint.index'))

    # The user was not authenticated.

    return {'error': 'There was a problem authenticating the user.'}