import os
import threading
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

        spotify_api_handler = SpotifyAPIHandler(request.form['access_token'])

        is_authenticated = spotify_api_handler.is_authenticated()

        if is_authenticated != True:

            return jsonify(error=True, msg=is_authenticated), 401

        merlin_api_handler = MerlinAPIHandler(spotify_api_handler)

        user = spotify_api_handler.get_user_profile()

        modelCheck = merlin_api_handler.check_model(user['id'])

        print(modelCheck)

        def create_model():

            merlin_api_handler.create_model()

            # Do something here (e.g update database)

        if not modelCheck:

            thread = threading.Thread(target=create_model)

            thread.start()

        # TODO: FIX THIS
        # db_handler = DBHandler()
        # DBHandler().insert_user(user)

        return jsonify(user=user['display_name']), 200 if modelCheck else 202

    else:

        return jsonify(error=True, msg='No access token provided. Retrieve token using the listed URL.',
                       url=url_for('spotify_blueprint.authorization')), 401


@spotify_blueprint.route('/authorization', methods=['GET'])
def authorization():
    """
    Authorization refers to the user granting access to his/her Spotify data.
    :return: String
        A url which points to the Spotify arthur authorization page.
    """

    auth_url = os.environ.get('AUTH_URL')
    client_id = os.environ.get('CLIENT_ID')
    redirect_uri = os.environ.get('REDIRECT_URI')

    authorization_url = '%s?client_id=%s&response_type=code&redirect_uri=%s&scope=user-read-private,' \
                        'user-library-read,playlist-modify-public,playlist-modify-private' % (auth_url, client_id,
                                                                                              redirect_uri), 200

    return {'spotify_auth_url': authorization_url}


@spotify_blueprint.route('/users/saved-tracks', methods=['POST'])
def saved_tracks():

    if 'access_token' in request.form and 'search_term' in request.args:

        spotify_api_handler = SpotifyAPIHandler(request.form['access_token'])

        is_authenticated = spotify_api_handler.is_authenticated()

        if is_authenticated != True:

            return jsonify(error=True, msg=is_authenticated), 401

        merlin_api_handler = MerlinAPIHandler(spotify_api_handler)

        return merlin_api_handler.classify_tracks(request.args['search_term']), 200

    elif 'search_term' not in request.args:

        return {'error': 'Search term missing.'}, 401

    else:

        return jsonify(error=True, msg='No access token provided. Retrieve token using the listed URL.',
                       url=url_for('spotify_blueprint.authorization')), 401


@spotify_blueprint.route('/users/recommended', methods=['POST'])
def recommended():

    if 'access_token' in request.form and 'search_term' in request.args:

        spotify_api_handler = SpotifyAPIHandler(request.form['access_token'])

        is_authenticated = spotify_api_handler.is_authenticated()

        if is_authenticated != True:

            return jsonify(error=True, msg=is_authenticated), 401

        merlin_api_handler = MerlinAPIHandler(spotify_api_handler)

        return merlin_api_handler.curated_playlist(request.args['search_term']), 200

    elif 'search_term' not in request.args:

        return {'error': 'Search term missing.'}, 401

    else:

        return jsonify(error=True, msg='No access token provided. Retrieve token using the listed URL.',
                       url=url_for('spotify_blueprint.authorization')), 401


@spotify_blueprint.route('/users/playlists', methods=['POST'])
def playlists():

    if 'access_token' in request.form and 'name' in request.form:

        spotify_api_handler = SpotifyAPIHandler(request.form['access_token'])

        playlist = spotify_api_handler.create_playlist(request.form['name'])

        if 'id' in playlist and 'uris' in request.form:

            return spotify_api_handler.add_items_to_playlist(request.form['access_token'], playlist['id'],
                                                             request.form['uris']), 201

        return playlist, 201

    elif 'name' not in request.form:

        return {'error': 'Playlist name missing.'}, 401

    else:

        return jsonify(error=True, msg='No access token provided. Retrieve token using the listed URL.',
                       url=url_for('spotify_blueprint.authorization')), 401


@spotify_blueprint.route('/users/playlists/<playlist_id>', methods=['POST'])
def add_items_to_playlist(playlist_id):

    if 'access_token' in request.json and 'uris' in request.json:

        spotify_api_handler = SpotifyAPIHandler(request.form['access_token'])

        return spotify_api_handler.add_items_to_playlist(playlist_id, request.json['uris']), 201

    elif 'uris' not in request.json:

        return {'error': 'Uris missing.'}, 401

    else:

        return jsonify(error=True, msg='No access token provided. Retrieve token using the listed URL.',
                       url=url_for('spotify_blueprint.authorization')), 401

