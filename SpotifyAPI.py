import os
import json
import requests
import urllib


class SpotifyAPI:
    """
    A singleton class for Spotify's API.
    """

    __instance__ = None

    # Urls

    # export BASE_URL=https://api.spotify.com
    # export AUTH_URL=https://accounts.spotify.com/authorize
    # export API_TOKEN_URL=https://accounts.spotify.com/api/token
    # export REDIRECT_URI=127.0.0.1:5000/home
    # export CLIENT_ID=369a6c4b828e4dda98c6a47e891d5b2f
    # export CLIENT_SECRET=5be944b9cb9b4897849438c3f586f9e5

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

        header = {'Authorization': 'Bearer ' + self.access_token}

        request = requests.get(url, headers=header).json()

        return request

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

    @staticmethod
    def get_instance():

        if SpotifyAPI.__instance__ is None:

            return SpotifyAPI()

        else:

            return SpotifyAPI.__instance__
