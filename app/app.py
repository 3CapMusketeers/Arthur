import os
from flask import Flask, redirect, request
from lib.spotify.SpotifyAPIHandler import SpotifyAPIHandler
from lib.spotify.SpotifyAPI import SpotifyAPI

app = Flask(__name__)

spotify_api = SpotifyAPI()

@app.route('/')
def hello_world():

    if spotify_api.access_token is None and spotify_api.refresh_token is None:

        return redirect('/authorization')

    return {'hello': 'world'}


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
