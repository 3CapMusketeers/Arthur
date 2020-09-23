import os
import math
import json
import requests
import urllib


class SpotifyAPI:
    """
    A singleton class for Spotify's API.
    """

    __instance__ = None

    # Urls

    BASE_URL = os.getenv('BASE_URL')
    AUTH_URL = os.getenv('AUTH_URL')
    API_TOKEN_URL = os.getenv('API_TOKEN_URL')
    REDIRECT_URI = os.getenv('REDIRECT_URI')

    # Client ids

    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')

    def __init__(self):

        if SpotifyAPI.__instance__ is None:

            SpotifyAPI.__instance__ = self

        else:

            Exception('Cannot create a new SpotifyAPI instance. Use \'get_instance() instead.\'')

        self.access_token = None

        self.refresh_token = None

    def get_user_profile(self):

        url = self.BASE_URL + '/me'

        header = {'Authorization': 'Bearer ' + self.access_token if self.access_token is not None else ''}

        request = requests.get(url, headers=header).json()

        return request

    def get_user_saved_tracks(self, limit=None):

        url = self.BASE_URL + '/me/tracks'

        header = {'Authorization': 'Bearer ' + self.access_token if self.access_token is not None else ''}

        params = {'limit': '50'}

        saved_tracks = []

        while True:

            request = requests.get(url, headers=header, params=params).json()

            if 'items' in request:

                saved_tracks += request['items']

                if 'next' in request and request['next'] is not None:

                    url = request['next']

                else:

                    break

        # List the ids of the saved tracks

        ids = []

        if limit and limit < len(saved_tracks):

            for track in saved_tracks:

                if 'track' in track:

                    ids.append(track['track']['id'])

            # Get the audio features of each track

            audio_features = self.get_audio_features(ids)

            # For each feature, make an ordered list and select 'limit + 1' from the list.

            ids = []

            for feature in ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                            'instrumentalness', 'liveness', 'valence', 'tempo']:

                feature_sorted = sorted(audio_features, key=lambda features: features[feature])

                step = math.floor(len(feature_sorted)/limit)

                curr_index = 0

                for i in range(0, limit + 1):

                    curr_index = len(feature_sorted) - 1 if curr_index >= len(feature_sorted) else curr_index

                    ids.append(feature_sorted[curr_index]['id'])

                    curr_index += step

            # Remove duplicate ids

            ids = list(dict.fromkeys(ids))

            selected_saved_tracks = [track for track in saved_tracks if 'track' in track and track['track']['id'] in
                                     ids]

            return selected_saved_tracks

        return saved_tracks

    def search_playlist(self, search_term, limit=1):

        url = self.BASE_URL + '/search'

        header = {'Authorization': 'Bearer ' + self.access_token if self.access_token is not None else ''}

        params = {'q': search_term.replace(' ', '+').replace('\'', ''), 'type': 'playlist', 'limit': limit}

        request = requests.get(url, headers=header, params=params).json()

        if 'playlists' in request and 'items' in request['playlists']:

            return request['playlists']['items']

        return None

    def search_tracks(self, search_term):

        url = self.BASE_URL + '/search'

        header = {'Authorization': 'Bearer ' + self.access_token if self.access_token is not None else ''}

        params = {'q': search_term.replace(' ', '+').replace('\'', ''), 'type': 'track'}

        request = requests.get(url, headers=header, params=params).json()

        if 'tracks' in request and 'items' in request['tracks']:

            return request['tracks']['items']

        return None

    def get_tracks_from_playlist(self, playlist_id):

        url = self.BASE_URL + '/playlists/' + playlist_id + '/tracks'

        header = {'Authorization': 'Bearer ' + self.access_token}

        params = {'limit': '50'}

        request = requests.get(url, headers=header, params=params).json()

        tracks = []

        if 'items' in request:

            for item in request['items']:

                if 'track' in item and item['track'] is not None:

                    tracks.append(item['track'])

        return tracks

    def get_audio_features(self, ids):

        url = self.BASE_URL + '/audio-features'

        header = {'Authorization': 'Bearer ' + self.access_token}

        audio_features = []

        chunk = []

        # The maximum number of allowed ids per request is 100, according to Spotify API. If ids is larger than 100,
        # then break it down into chunks.

        for i in range(0, len(ids)):

            if i > 0 and i % 100 == 0 or i == len(ids) - 1:

                params = {'ids': ','.join(chunk)}

                response = requests.get(url, headers=header, params=params).json()

                if 'audio_features' in response:

                    audio_features += response['audio_features']

                chunk = []

            chunk.append(ids[i])

        return audio_features

    def request_authorization_to_access_data_url(self):
        """
        Returns a Spotify URL for the user to authorize access to 'user-read-private' and 'user-library-read'.
        :return: String
        """

        return '%s?client_id=%s&response_type=code&redirect_uri=%s&scope=user-read-private,user-library-read' % \
              (self.AUTH_URL, self.CLIENT_ID, self.REDIRECT_URI)

    def request_access_and_refresh_tokens(self, code):
        """
        Requests and returns access and refresh tokens.
        :param code: String
            From Spofity doc: An authorization code that can be exchanged for an access token.
        :return: String, String or None, None if something went wrong.
            The access and refresh tokens.
        """

        data = {'grant_type': 'authorization_code', 'code': code, 'redirect_uri': self.REDIRECT_URI,
                'client_id': self.CLIENT_ID, 'client_secret': self.CLIENT_SECRET}

        request = requests.post(self.API_TOKEN_URL, data=data)

        request_json = json.loads(request.text)

        if 'access_token' in request_json and 'refresh_token' in request_json:

            return request_json['access_token'], request_json['refresh_token']

        return None, None

    def request_new_access_token(self, refresh_token):
        """
        Returns a new access token. This function should be called when the user's access token has expired.
        :param refresh_token: String
            The refresh token that was obtained from the 'request_access_and_refresh_tokens()' function.
        :return: String or None if something went wrong.
            The new access token.
        """

        data = {'grant_type': 'refresh_token', 'refresh_token': refresh_token, 'client_id': self.CLIENT_ID,
                'client_secret': self.CLIENT_SECRET}

        request = requests.post(self.API_TOKEN_URL, data=data)

        request_json = json.loads(request.text)

        if 'access_token' in request_json:

            return request_json['access_token']

        return None

    def set_access_token(self, token):
        """
        Sets a new access token.
        :param token: String
        """

        self.access_token = token

    def set_refresh_token(self, token):
        """
        Sets a new refresh token.
        :param token: String
        """

        self.refresh_token = token

    def is_authenticated(self):

        if self.access_token and self.refresh_token:

            user = self.get_user_profile()

            if 'error' in user and 'message' in user['error'] and user['error']['message'] == 'The access token expired':

                return False

            else:

                return True

        return False

    @staticmethod
    def get_instance():

        if SpotifyAPI.__instance__ is None:

            return SpotifyAPI()

        else:

            return SpotifyAPI.__instance__
