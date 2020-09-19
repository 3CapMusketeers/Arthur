import os
from flask import Flask, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from SpotifyAPI import SpotifyAPI
from handlers.SpotifyAPIHandler import SpotifyAPIHandler

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from handlers import DBHandler as dh

from models import *

spotify_api = SpotifyAPI()


@app.route('/')
def home():

    # Verify user is authenticated. Otherwise authenticate.

    if not spotify_api.is_authenticated():

        return redirect('/authorization')

    # Get user profile and insert into db if not already.

    user = spotify_api.get_user_profile()

    if 'error' in user:

        return user

    db_handler = dh.DBHandler(db)

    db_handler.insert_user(user)

    return {'user': user['display_name']}


@app.route('/authorization', methods=['GET'])
def authorization():
    """
    Authorization refers to the user granting access to his/her Spotify data.
    :return: String
        A url which points to the Spotify app authorization page.
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

        return {'error': 'The user did not authorized this app to access data.'}

    # Authenticate user

    spotify_api_handler = SpotifyAPIHandler()

    if spotify_api_handler.authenticate(request.args):

        # If the user was authenticated, return to home page.

        return redirect('/')

    # The user was not authenticated.

    return {'error': 'There was a problem authenticating the user.'}


if __name__ == '__main__':
    if os.environ.get('IS_PROD'):
        app.run()
    else:
        app.run(debug=True, use_debugger=True)
