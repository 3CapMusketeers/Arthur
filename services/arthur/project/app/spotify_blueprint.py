# Package Imports
from flask import Blueprint, redirect, request, url_for, jsonify

# Project imports
from project.app.handlers import DBHandler
from project.app.handlers.MerlinAPIHandler import MerlinAPIHandler
from project.app.handlers.spotify.SpotifyAPI import SpotifyAPI
from project.app.handlers.spotify.SpotifyAPIHandler import SpotifyAPIHandler
from project.app.handlers import DBHandler
from project.app.models import User
from project import db

spotify_blueprint = Blueprint('spotify_blueprint', __name__)

@spotify_blueprint.route('/', methods=['POST'])
def index():
    if 'access_token' in request.form:
        at = request.form['access_token']
        spotify_api = SpotifyAPI(at)

        # spotify_api.set_access_token(request.args['access_token'])

        # Get user profile and insert into db if not already.
        user = spotify_api.get_user_profile()
        if 'error' in user:
            return user

        # TODO: FIX THIS
        # db_handler = DBHandler()
        # DBHandler().insert_user(user)

        return jsonify(user=user['display_name'])
        # else:
        #     return jsonify(error=True, msg='Model not created')
    else:
        return jsonify(error=True,msg='No access token. Use spotify URL to authenticate', url=url_for('spotify_blueprint.authorization'))
    # if 'access_token' in request.args:


@spotify_blueprint.route('/authorization', methods=['GET'])
def authorization():
    """
    Authorization refers to the user granting access to his/her Spotify data.
    :return: String
        A url which points to the Spotify arthur authorization page.
    """

    spotify_api = SpotifyAPI()

    return {'spotify_auth_url': spotify_api.request_authorization_to_access_data_url()}

@spotify_blueprint.route('/users/<access_token>/saved-tracks', methods=['POST'])
def saved_tracks(access_token):

    if 'search_term' in request.args:

        spotify_handler = SpotifyAPIHandler()

        return spotify_handler.saved_tracks(access_token, request.args['search_term'])

    return {'Error': 'Search term missing.'}

@spotify_blueprint.route('/users/<access_token>/recommended', methods=['POST'])
def recommended(access_token):

    if 'search_term' in request.args:

        spotify_api = SpotifyAPI(access_token)
        spotify_handler = SpotifyAPIHandler()
        recommend = spotify_handler.recommended(access_token, request.args['search_term'])
        if('error' in recommend):
            merlin_api_handler = MerlinAPIHandler(spotify_api)
            merlin_api_handler.create_model()
            return recommend
    
    return {'Error': 'Search term missing.'}
