import unittest
import requests
from SpotifyAPI import SpotifyAPI
from handlers.SpotifyAPIHandler import SpotifyAPIHandler


class SpotifyAPIHandlerTestCase(unittest.TestCase):

    spotify_api = SpotifyAPI()

    def setUp(self):

        response = requests.get(self.spotify_api.request_authorization_to_access_data_url())

        print(response)

    def test_authentication(self):

        spotify_api_handler = SpotifyAPIHandler()


if __name__ == '__main__':
    unittest.main()