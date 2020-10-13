from flask import jsonify

from project.app.handlers.MerlinAPIHandler import MerlinAPIHandler
from project.app.handlers.spotify.SpotifyAPI import SpotifyAPI


class SpotifyAPIHandler:

    def add_items_to_playlist(self, access_token, playlist_id, uris):

        spotify_api = SpotifyAPI(access_token)

        is_user_authenticated = spotify_api.is_authenticated()

        if is_user_authenticated is True:

            return spotify_api.add_items_to_playlist(playlist_id, uris)

        return is_user_authenticated

    def create_playlist(self, access_token, name):

        spotify_api = SpotifyAPI(access_token)

        is_user_authenticated = spotify_api.is_authenticated()

        if is_user_authenticated is True:

            return spotify_api.create_playlist(name)

        return is_user_authenticated

    def saved_tracks(self, access_token, search_term):

        spotify_api = SpotifyAPI(access_token)

        is_user_authenticated = spotify_api.is_authenticated()

        if is_user_authenticated is True:

            merlin_api_handler = MerlinAPIHandler(spotify_api)

            return jsonify(tracks=merlin_api_handler.classify_tracks(search_term))

        return is_user_authenticated

    def recommended(self, access_token, search_term):

        spotify_api = SpotifyAPI(access_token)

        is_user_authenticated = spotify_api.is_authenticated()

        if is_user_authenticated is True:

            merlin_api_handler = MerlinAPIHandler(spotify_api)

            return jsonify(track=smerlin_api_handler.curated_playlist(search_term))

        return is_user_authenticated






