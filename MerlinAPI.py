import os
import json
import requests
from shared import spotify_api


class MerlinAPI:
    """
    A singleton class for Merlin's API.
    """

    __instance__ = None

    # Urls

    BASE_URL = os.environ.get('MERLIN_BASE_URL')

    def __init__(self):

        if MerlinAPI.__instance__ is None:

            MerlinAPI.__instance__ = self

        else:

            Exception('Cannot create a new MerlinAPI instance. Use \'get_instance() instead.\'')

        self.access_token = None

        self.refresh_token = None

    def create_model(self):

        url = self.BASE_URL + '/personal-models'

        user = spotify_api.get_user_profile()

        saved_tracks = spotify_api.get_user_saved_tracks()

        tracks = []

        for track in saved_tracks:

            if 'track' in track and 'preview_url' in track['track'] and track['track']['preview_url'] is not None:

                tracks.append({'id': track['track']['id'], 'url': track['track']['preview_url']})

        json = {'uid': user['id'], 'tracks': tracks}

        request = requests.post(url, json=json).json()

        return request

    def classify_tracks(self, search_term):

        url = self.BASE_URL + '/classifier'

        user = spotify_api.get_user_profile()

        tracks = spotify_api.get_user_saved_tracks()

        classify_tracks = []

        for track in tracks:

            if 'track' in track and 'preview_url' in track['track'] and track['track']['preview_url'] is not None:

                classify_tracks.append({'id': track['track']['id'], 'url': track['track']['preview_url']})

        playlists = spotify_api.search_playlist(search_term)

        tracks = []

        for playlist in playlists:

            tracks += spotify_api.get_tracks_from_playlist(playlist['id'])

        training_tracks = []

        for track in tracks:

            if 'preview_url' in track and track['preview_url'] is not None:

                training_tracks.append({'id': track['id'], 'url': track['preview_url']})

        json = {'uid': user['id'], 'search_term': search_term,'training_tracks': training_tracks, 'classify_tracks': classify_tracks}

        request = requests.post(url, json=json).json()

        if 'tracks' in request:

            return request['tracks']

        return None

    @staticmethod
    def get_instance():

        if MerlinAPI.__instance__ is None:

            return MerlinAPI()

        else:

            return MerlinAPI.__instance__
