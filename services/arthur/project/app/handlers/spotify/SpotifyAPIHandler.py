from flask import jsonify

from project.app.handlers.MerlinAPIHandler import MerlinAPIHandler
from project.app.handlers.spotify.SpotifyAPI import SpotifyAPI


class SpotifyAPIHandler:

    def add_items_to_playlist(self, access_token, playlist_id, uris):

        spotify_api = SpotifyAPI(access_token)

        return spotify_api.add_items_to_playlist(playlist_id, uris)

    def create_playlist(self, access_token, name):

        spotify_api = SpotifyAPI(access_token)

        return spotify_api.create_playlist(name)

    def saved_tracks(self, access_token, search_term):

        spotify_api = SpotifyAPI(access_token)

        merlin_api_handler = MerlinAPIHandler(spotify_api)

        return jsonify(tracks=merlin_api_handler.classify_tracks(search_term))

    def recommended(self, access_token, search_term):

        spotify_api = SpotifyAPI(access_token)

        merlin_api_handler = MerlinAPIHandler(spotify_api)

        return merlin_api_handler.curated_playlist(search_term)






