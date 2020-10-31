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

    def __init__(self, access_token):

        self.access_token = access_token

    def add_items_to_playlist(self, playlist_id, uris):
        """
        Sends request to Spotify to add items to a playlist.
        :param playlist_id: String
        :param uris: String
        :return: json
        """

        url = self.BASE_URL + '/playlists/' + playlist_id + '/tracks'

        header = {'Authorization': 'Bearer ' + self.access_token if self.access_token is not None else ''}

        json = {'uris': uris}

        return requests.post(url, headers=header, json=json).json()

    def create_playlist(self, name, description='Created using Camelot.'):
        """
        Sends request to Spotify to create a new playlist.
        :param name: String
        :param description: String
        :return: json
        """

        user = self.get_user_profile()

        url = self.BASE_URL + '/users/' + user['id'] + '/playlists'

        header = {'Authorization': 'Bearer ' + self.access_token if self.access_token is not None else ''}

        json = {'name': name, 'description': description}

        return requests.post(url, headers=header, json=json).json()

    def get_several_tracks(self, ids):
        """
        Sends request to Spotify to return a list of tracks that matches the provided ids.
        :param ids: String (each id separated by comma)
        :return: json
        """

        url = self.BASE_URL + '/tracks'

        header = {'Authorization': 'Bearer ' + self.access_token}

        params = {'ids': ids}

        return requests.get(url, headers=header, params=params).json()

    def get_user_profile(self):
        """
        Sends request to Spotify to return the user's profile.
        :return:
        """

        url = self.BASE_URL + '/me'

        header = {'Authorization': 'Bearer ' + self.access_token if self.access_token is not None else ''}

        request = requests.get(url, headers=header).json()

        return request

    def get_user_saved_tracks(self):
        """
        Sends a request to Spotify to return the user's saved tracks (max limit 50/request).
        :return: json
        """

        url = self.BASE_URL + '/me/tracks'

        header = {'Authorization': 'Bearer ' + self.access_token if self.access_token is not None else ''}

        params = {'limit': '50'}

        return requests.get(url, headers=header, params=params).json()

    def search_playlist(self, search_term, limit):
        """
        Send a request to Spotify to return playlist(s) that matches the search term.
        :param search_term: String
        :param limit: Int
        :return: json
        """

        url = self.BASE_URL + '/search'

        header = {'Authorization': 'Bearer ' + self.access_token if self.access_token is not None else ''}

        params = {'q': search_term.replace(' ', '+').replace('\'', ''), 'type': 'playlist', 'limit': limit}

        return requests.get(url, headers=header, params=params).json()

    def search_tracks(self, search_term):
        """
        Send a request to Spotify to return track(s) that matches the search term.
        :param search_term: String
        :return: json
        """

        url = self.BASE_URL + '/search'

        header = {'Authorization': 'Bearer ' + self.access_token if self.access_token is not None else ''}

        params = {'q': search_term.replace(' ', '+').replace('\'', ''), 'type': 'track'}

        return requests.get(url, headers=header, params=params).json()

    def get_tracks_from_playlist(self, playlist_id, limit):
        """
        Sends a request to Spotify to return a list of tracks from a playlist that matches the provided id.
        :param playlist_id: String
        :param limit: Int
        :return:
        """

        url = self.BASE_URL + '/playlists/' + playlist_id + '/tracks'

        header = {'Authorization': 'Bearer ' + self.access_token}

        params = {'limit': limit}

        return requests.get(url, headers=header, params=params).json()

    def request_authorization_to_access_data_url(self):
        """
        Returns a Spotify URL for the user to authorize access to 'user-read-private', 'user-library-read',
        'playlist-modify-public', and 'playlist-modify-private'.
        :return: String
        """

        return '%s?client_id=%s&response_type=code&redirect_uri=%s&scope=user-read-private,user-library-read,playlist-modify-public,playlist-modify-private' % \
              (self.AUTH_URL, self.CLIENT_ID, self.REDIRECT_URI)

    def set_access_token(self, token):
        """
        Sets a new access token.
        :param token: String
        """

        self.access_token = token

    def is_authenticated(self):
        """
        Verifies that the user is authenticated by requesting the user's profile. If the response is the user's
        profile, then the token is assumed valid and the user is considered authenticated.
        :return: dict/True
        """

        if self.access_token:

            user = self.get_user_profile()

            if 'error' in user and 'message' in user['error']:

                return user

            else:

                return True

        return {'error', 'No access token provided'}
