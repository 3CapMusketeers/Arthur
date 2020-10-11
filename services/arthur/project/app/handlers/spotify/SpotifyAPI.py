import os
import json
import requests
import urllib


class SpotifyAPI:
    """
    A class for Spotify's API.
    """

    # Urls

    BASE_URL = os.environ.get('BASE_URL')
    AUTH_URL = os.environ.get('AUTH_URL')
    API_TOKEN_URL = os.environ.get('API_TOKEN_URL')
    REDIRECT_URI = os.environ.get('REDIRECT_URI')

    # Client ids

    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

    def __init__(self, access_token=None):

        self.access_token = access_token

    def add_items_to_playlist(self, playlist_id, uris):

        url = self.BASE_URL + '/playlists/' + playlist_id + '/tracks'

        header = {'Authorization': 'Bearer ' + self.access_token if self.access_token is not None else ''}

        json = {'uris': uris}

        return requests.post(url, headers=header, json=json).json()

    def create_playlist(self, name):

        user = self.get_user_profile()

        url = self.BASE_URL + '/users/' + user['id'] + '/playlists'

        header = {'Authorization': 'Bearer ' + self.access_token if self.access_token is not None else ''}

        json = {'name': name, 'description': 'Created using Camelot.'}

        return requests.post(url, headers=header, json=json).json()

    def get_several_tracks(self, ids):

        url = self.BASE_URL + '/tracks'

        header = {'Authorization': 'Bearer ' + self.access_token}

        # The maximum number of allowed ids per request is 50, according to Spotify API. If ids is larger than 50,
        # then break it down into chunks.

        tracks = []

        chunk = []

        for i in range(0, len(ids)):

            chunk.append(ids[i])

            if len(chunk) == 50 or i == len(ids) - 1:

                params = {'ids': ','.join(chunk)}

                response = requests.get(url, headers=header, params=params).json()

                tracks += response['tracks'] if 'tracks' in response else []

                chunk = []

        return tracks

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

            if 'error' in request:

                break

            if 'items' in request:

                saved_tracks += request['items']

                if 'next' in request and request['next'] is not None:

                    url = request['next']

                else:

                    break

        return saved_tracks

    def search_playlist(self, search_term, limit=5):

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

    def get_tracks_from_playlist(self, playlist_id, limit=50):

        url = self.BASE_URL + '/playlists/' + playlist_id + '/tracks'

        header = {'Authorization': 'Bearer ' + self.access_token}

        params = {'limit': limit}

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

    def set_access_token(self, token):
        """
        Sets a new access token.
        :param token: String
        """

        self.access_token = token

    def is_authenticated(self):

        if self.access_token:

            user = self.get_user_profile()

            if 'error' in user and 'message' in user['error'] and user['error']['message'] == 'The access token expired':

                return False

            else:

                return True

        return False
