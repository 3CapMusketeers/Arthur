import os
import json
import requests
from flask import jsonify


class MerlinAPI:
    """
    A class for Merlin's API.
    """

    # Urls

    MERLIN_BASE_URL = os.environ.get('MERLIN_BASE_URL')

    def __init__(self, spotify_api):

        self.spotify_api = spotify_api

    def create_model(self):

        url = self.MERLIN_BASE_URL + '/personal-models'

        user = self.spotify_api.get_user_profile()

        saved_tracks = self.spotify_api.get_user_saved_tracks()

        tracks = []

        for track in saved_tracks:

            if 'track' in track and 'preview_url' in track['track'] and track['track']['preview_url'] is not None:

                tracks.append({'id': track['track']['id'], 'url': track['track']['preview_url']})

        json = {'uid': user['id'], 'tracks': tracks}

        request = requests.post(url, json=json).json()

        return request

    def classify_tracks(self, search_term):

        url = self.MERLIN_BASE_URL + '/classifier'

        user = self.spotify_api.get_user_profile()

        tracks = self.spotify_api.get_user_saved_tracks()

        classify_tracks = []

        for track in tracks:

            if 'track' in track and 'preview_url' in track['track'] and track['track']['preview_url'] is not None:

                classify_tracks.append({'id': track['track']['id'], 'url': track['track']['preview_url']})

        playlists = self.spotify_api.search_playlist(search_term, limit=5)

        tracks = []

        for playlist in playlists:

            tracks += self.spotify_api.get_tracks_from_playlist(playlist['id'])

        training_tracks = []

        for track in tracks:

            if 'preview_url' in track and track['preview_url'] is not None:

                training_tracks.append({'id': track['id'], 'url': track['preview_url']})

        json = {'uid': user['id'], 'search_term': search_term,'training_tracks': training_tracks, 'classify_tracks': classify_tracks}

        request = requests.post(url, json=json).json()

        return request['tracks'] if 'tracks' in request else None

    def curated_playlist(self, search_term):

        user = self.spotify_api.get_user_profile()

        url = self.MERLIN_BASE_URL + '/personal-models/' + user['id'] + '/classification' # user['id'] error if expired. put error here

        tracks = []

        playlists = self.spotify_api.search_playlist(search_term)

        for playlist in playlists:

            if 'id' in playlist:

                tracks += self.spotify_api.get_tracks_from_playlist(playlist['id'])

        classify_tracks = []
        for track in tracks:
            if 'preview_url' in track and track['preview_url'] is not None:
                classify_tracks.append({'id': track['id'], 'url': track['preview_url']})

        json = {'classify_tracks': classify_tracks}

        request = requests.post(url, json=json).json()

        return request['tracks'] if 'tracks' in request else {'error':True, 'msg':request['msg']}

