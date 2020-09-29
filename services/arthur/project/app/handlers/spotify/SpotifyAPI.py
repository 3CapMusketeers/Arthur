import os
import json
import requests
import urllib

class SpotifyAPI:

    # Urls
    BASE_URL = os.environ.get('BASE_URL')
    
    AUTH_URL = os.environ.get('AUTH_URL')
    API_TOKEN_URL = os.environ.get('API_TOKEN_URL')
    REDIRECT_URI = os.environ.get('REDIRECT_URI')

    # Client ids
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

    def __init__(self):

        self.access_token = None

        self.refresh_token = None

    def get_user_profile(self):

        url = self.BASE_URL + '/me'

        header = {'Authorization': 'Bearer ' + self.access_token if self.access_token is not None else ''}

        request = requests.get(url, headers=header).json()

        return request

    def request_authorization_to_access_data_url(self):
        """
        Returns a Spotify URL for the user to authorize access to 'user-read-private' and 'user-library-read'.
        :return: String
        """

        return '%s?client_id=%s&response_type=code&redirect_uri=%s&scope=user-read-private,user-library-read' % \
              (self.AUTH_URL, self.CLIENT_ID, urllib.parse.quote_plus(self.REDIRECT_URI))

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
