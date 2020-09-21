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

    @staticmethod
    def get_instance():

        if MerlinAPI.__instance__ is None:

            return MerlinAPI()

        else:

            return MerlinAPI.__instance__
