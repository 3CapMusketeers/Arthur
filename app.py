import os
from flask import Flask, redirect, request
from SpotifyAPI import SpotifyAPI
from handlers.SpotifyAPIHandler import SpotifyAPIHandler

app = Flask(__name__)

spotify_api = SpotifyAPI()


@app.route('/')
def hello_world():

    if spotify_api.access_token is None and spotify_api.refresh_token is None:

        return redirect('/authorization')

    return {'hello': 'world'}


@app.route('/authorization', methods=['GET'])
def authorization():

    return redirect(spotify_api.request_authorization_to_access_data_url())


@app.route('/authentication', methods=['GET'])
def authentication():

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
