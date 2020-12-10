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

    def __init__(self, user_id):

        self.user_id = user_id

    def create_model(self, tracks):
        """
        Sends a request to Merlin to create a model.
        :param tracks: A dict of the tracks. Each track must contain its respective id and url.
        :return: json
        """

        url = self.MERLIN_BASE_URL + '/personal-models'

        json = {'uid': self.user_id, 'tracks': tracks}

        return requests.post(url, json=json).json()

    def check_model(self, user_id):
        """
        Sends a request to Merlin to check if the personal model exists.
        :param user_id: String
        :return: bool
        """

        url = self.MERLIN_BASE_URL + '/personal-models/' + user_id

        return requests.get(url).json()['msg']

    def classify_tracks(self, search_term, saved_tracks, training_tracks):
        """
        Sends a request to Merlin to return a list of the user's saved tracks filtered by a search term.
        :param search_term: String
        :param saved_tracks: A dict of the saved tracks. Each track must contain its respective id and url.
        :param training_tracks: A dict of the training tracks. Each track must contain its respective id and url.
        :return: json (a list of track ids that matched the search term)
        """

        url = self.MERLIN_BASE_URL + '/classifier'

        request_json = {'uid': self.user_id, 'search_term': search_term,'training_tracks': training_tracks,
                        'classify_tracks': saved_tracks}

        return requests.post(url, json=request_json).json()

    def curated_playlist(self, tracks):
        """
        Sends a request to Merlin to return a list of tracks that match the user's profile..
        :param tracks: A dict of the tracks to be considered. Each track must contain its respective id and url.
        :return: json (a list of track ids that matched the user's profile)
        """

        url = self.MERLIN_BASE_URL + '/personal-models/' + self.user_id + '/classification'

        json = {'classify_tracks': tracks}

        return requests.post(url, json=json).json()

