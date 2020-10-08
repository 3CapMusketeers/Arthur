from project.app.handlers.MerlinAPIHandler import MerlinAPIHandler
from project.app.handlers.spotify.SpotifyAPI import SpotifyAPI


class SpotifyAPIHandler:

    def saved_tracks(self, access_token, search_term):

        spotify_api = SpotifyAPI(access_token)

        merlin_api_handler = MerlinAPIHandler(spotify_api)

        return merlin_api_handler.classify_tracks(search_term)

    def recommended(self, access_token, search_term):

        spotify_api = SpotifyAPI(access_token)

        merlin_api_handler = MerlinAPIHandler(spotify_api)

        return merlin_api_handler.curated_playlist(search_term)






