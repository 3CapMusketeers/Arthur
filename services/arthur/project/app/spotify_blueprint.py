import os
import time
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
    start_time = time.time()
    if 'access_token' in request.form:

        spotify_api_handler = SpotifyAPIHandler(request.form['access_token'])

        is_authenticated = spotify_api_handler.is_authenticated()

        if is_authenticated != True:
            return jsonify(error=True, msg=is_authenticated, exec_time=get_execution_time(start_time)), 401

        merlin_api_handler = MerlinAPIHandler(spotify_api_handler)

        user = spotify_api_handler.get_user_profile()

        model_status = merlin_api_handler.check_model(user['id'])
        status_code = get_model_status_code(model_status)

        def create_model():
            merlin_api_handler.create_model()

        exists = False  
        for thread in threading.enumerate(): 
            if thread.name == user['id']:
                status_code = 202

        thread = threading.Thread(target=create_model)
        if status_code == 204:
            print("I would create here.")
            thread.name = user['id'] 
            thread.start()

        # TODO: FIX THIS
        # db_handler = DBHandler()
        # DBHandler().insert_user(user)

        return jsonify(user=user['display_name'], model_status=model_status,
                       exec_time=get_execution_time(start_time)), status_code

    else:
        return jsonify(error=True, msg='No access token provided. Retrieve token using the listed URL.',
                       url=url_for('spotify_blueprint.authorization'),
                       exec_time=get_execution_time(start_time)), 401


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
    start_time = time.time()
    if 'access_token' in request.form and 'search_term' in request.args:

        spotify_api_handler = SpotifyAPIHandler(request.form['access_token'])

        is_authenticated = spotify_api_handler.is_authenticated()

        if is_authenticated != True:
            return jsonify(error=True, msg=is_authenticated, exec_time=get_execution_time(start_time)), 401

        merlin_api_handler = MerlinAPIHandler(spotify_api_handler)
        return jsonify(tracks=merlin_api_handler.classify_tracks(request.args['search_term']),
                       exec_time=get_execution_time(start_time)), 200

    elif 'search_term' not in request.args:
        return jsonify(error=True, msg='Search term missing.', exec_time=get_execution_time(start_time)), 401

    else:
        return jsonify(error=True, msg='No access token provided. Retrieve token using the listed URL.',
                       url=url_for('spotify_blueprint.authorization'),
                       exec_time=get_execution_time(start_time)), 401


@spotify_blueprint.route('/users/recommended', methods=['POST'])
def recommended():
    start_time = time.time()
    if 'access_token' in request.form and 'search_term' in request.args:

        spotify_api_handler = SpotifyAPIHandler(request.form['access_token'])

        is_authenticated = spotify_api_handler.is_authenticated()

        if is_authenticated != True:

            return jsonify(error=True, msg=is_authenticated, exec_time=get_execution_time(start_time)), 401

        merlin_api_handler = MerlinAPIHandler(spotify_api_handler)
        return jsonify(tracks=merlin_api_handler.curated_playlist(request.args['search_term']),
                       exec_time=get_execution_time(start_time)), 200

    elif 'search_term' not in request.args:
        return jsonify(error=True, msg='Search term missing.', exec_time=get_execution_time(start_time)), 401

    else:
        return jsonify(error=True, msg='No access token provided. Retrieve token using the listed URL.',
                       url=url_for('spotify_blueprint.authorization'),
                       exec_time=get_execution_time(start_time)), 401


@spotify_blueprint.route('/users/playlists', methods=['POST'])
def playlists():
    start_time = time.time()
    if 'access_token' in request.form and 'name' in request.form:

        spotify_api_handler = SpotifyAPIHandler(request.form['access_token'])

        playlist = spotify_api_handler.create_playlist(request.form['name'])

        if 'id' in playlist and 'uris' in request.form:
            result = spotify_api_handler.add_items_to_playlist(playlist['id'], request.form['uris'])
            print(result)
            get_execution_time(start_time)
            return result, 201
        get_execution_time(start_time)
        return playlist, 201

    elif 'name' not in request.form:
        return jsonify(error=True, msg='Playlist name missing.', exec_time=get_execution_time(start_time)), 401

    else:
        return jsonify(error=True, msg='No access token provided. Retrieve token using the listed URL.',
                       url=url_for('spotify_blueprint.authorization'),
                       exec_time=get_execution_time(start_time)), 401


@spotify_blueprint.route('/users/playlists/<playlist_id>', methods=['POST'])
def add_items_to_playlist(playlist_id):
    start_time = time.time()
    if 'access_token' in request.form and 'uris' in request.form:

        spotify_api_handler = SpotifyAPIHandler(request.form['access_token'])

        result = spotify_api_handler.add_items_to_playlist(playlist_id, request.form['uris'])
        get_execution_time(start_time)
        return result, 201

    elif 'uris' not in request.form:
        return jsonify(error=True, msg='Uris missing.', exec_time=get_execution_time(start_time)), 401

    else:
        return jsonify(error=True, msg='No access token provided. Retrieve token using the listed URL.',
                       url=url_for('spotify_blueprint.authorization'),
                       exec_time=get_execution_time(start_time)), 401


@spotify_blueprint.route('/users/model', methods=['POST'])
def check_personal_model():
    start_time = time.time()
    if 'access_token' in request.form:

        spotify_api_handler = SpotifyAPIHandler(request.form['access_token'])

        is_authenticated = spotify_api_handler.is_authenticated()

        if is_authenticated != True:
            return jsonify(error=True, msg=is_authenticated, exec_time=get_execution_time(start_time)), 401

        merlin_api_handler = MerlinAPIHandler(spotify_api_handler)

        user = spotify_api_handler.get_user_profile()

        model_status = merlin_api_handler.check_model(user['id'])

        status_code = get_model_status_code(model_status)
        return jsonify(status=model_status, exec_time=get_execution_time(start_time)), status_code

    else:
        return jsonify(error=True, msg='No access token provided. Retrieve token using the listed URL.',
                       url=url_for('spotify_blueprint.authorization'),
                       exec_time=get_execution_time(start_time)), 401


def get_execution_time(start_time):
    exec_time = time.time() - start_time
    print("%s seconds" % exec_time)
    return exec_time


def get_model_status_code(model_status):
    if model_status == -1:
        return 204 # Not Found
    elif model_status == 0:
        return 202 # Accepted
    elif model_status == 1:
        return 200  # Created
    else:
        return 400  # Bad Request :(


