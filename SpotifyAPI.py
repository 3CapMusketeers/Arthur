import os
import json
import requests


class SpotifyAPI:
    """
    A singleton class for Spotify's API.
    """

    __instance__ = None

    # Urls

    BASE_URL = os.environ.get('BASE_URL')
    AUTH_URL = os.environ.get('AUTH_URL')
    API_TOKEN_URL = os.environ.get('API_TOKEN_URL')
    REDIRECT_URI = os.environ.get('REDIRECT_URI')

    # Client ids

    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

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

    def get_user_saved_tracks(self):

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

        return self.access_token and self.refresh_token

    @staticmethod
    def get_instance():

        if SpotifyAPI.__instance__ is None:

            return SpotifyAPI()

        else:

            return SpotifyAPI.__instance__
