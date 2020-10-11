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

        access_token = request.form['access_token']

        spotify_api = SpotifyAPI(access_token)

        merlin_api_handler = MerlinAPIHandler(spotify_api)

        merlin_api_handler.create_model()

        # Get user profile and insert into db if not already.
        user = spotify_api.get_user_profile()

        if 'error' in user:
            return jsonify(error=True, msg=user['error'])

        # TODO: FIX THIS
        # db_handler = DBHandler()
        # DBHandler().insert_user(user)

        return jsonify(user=user['display_name'])

    else:
        return jsonify(error=True, msg='No access token. Use spotify URL to authenticate',
                       url=url_for('spotify_blueprint.authorization'))


@spotify_blueprint.route('/authorization', methods=['GET'])
def authorization():
    """
    Authorization refers to the user granting access to his/her Spotify data.
    :return: String
        A url which points to the Spotify arthur authorization page.
    """
    spotify_api = SpotifyAPI()

    return {'spotify_auth_url': spotify_api.request_authorization_to_access_data_url()}


@spotify_blueprint.route('/users/saved-tracks', methods=['POST']) # Weird name
def saved_tracks():

    if 'access_token' in request.form and 'search_term' in request.args:

        spotify_api = SpotifyAPI(request.form['access_token'])

        model_exists = MerlinAPIHandler(spotify_api).check_model()

        if model_exists is True:

            spotify_handler = SpotifyAPIHandler()

            return spotify_handler.saved_tracks(request.form['access_token'], request.args['search_term'])

        return model_exists

    elif 'search_term' not in request.args:

        return {'error': 'Search term missing.'}

    else:

        return {'error': 'No access token provided.'}


@spotify_blueprint.route('/users/recommended', methods=['POST'])
def recommended():

    if 'access_token' in request.form and 'search_term' in request.args:

        spotify_api = SpotifyAPI(request.form['access_token'])

        model_exists = MerlinAPIHandler(spotify_api).check_model()

        if model_exists is True:

            spotify_handler = SpotifyAPIHandler()

            return spotify_handler.recommended(request.form['access_token'], request.args['search_term'])

        return model_exists

    elif 'search_term' not in request.args:

        return {'error': 'Search term missing.'}

    else:

        return {'error': 'No access token provided.'}


@spotify_blueprint.route('/users/playlists', methods=['POST'])
def playlists():

    if 'access_token' in request.json and 'name' in request.json:

        spotify_handler = SpotifyAPIHandler()

        playlist = spotify_handler.create_playlist(request.json['access_token'], request.json['name'])

        if 'id' in playlist and 'uris' in request.json:

            return spotify_handler.add_items_to_playlist(request.json['access_token'], playlist['id'],
                                                         request.json['uris'])

        return playlist


@spotify_blueprint.route('/users/playlists/<playlist_id>', methods=['POST'])
def add_items_to_playlist(playlist_id):

    if 'access_token' in request.json and 'uris' in request.json:

        spotify_handler = SpotifyAPIHandler()

        return spotify_handler.add_items_to_playlist(request.json['access_token'], playlist_id, request.json['uris'])

