import os
from flask import Flask, redirect, request
from SpotifyAPI import SpotifyAPI
from handlers.SpotifyAPIHandler import SpotifyAPIHandler

app = Flask(__name__)

spotify_api = SpotifyAPI()


@app.route('/')
def hello_world():

    return {'hello': 'world'}


@app.route('/authentication', methods=['GET'])
def authentication():

    # TODO: Handle case when user does NOT authorize the app

    spotify_api_handler = SpotifyAPIHandler()

    authenticated = spotify_api_handler.authenticate(request.args)

    if not authenticated:

        return redirect(spotify_api.request_authorization_to_access_data_url())


if __name__ == '__main__':
    if os.environ.get('IS_PROD'):
        app.run()
    else:
        app.run(debug=True, use_debugger=True)
