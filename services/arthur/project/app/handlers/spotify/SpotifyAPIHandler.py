from flask import jsonify

from project.app.handlers.spotify.SpotifyAPI import SpotifyAPI


class SpotifyAPIHandler:

    def __init__(self, access_token):

        self.spotify_api = SpotifyAPI(access_token)

    def add_items_to_playlist(self, playlist_id, uris):

        return self.spotify_api.add_items_to_playlist(playlist_id, uris)

    def create_playlist(self, name):

        return self.spotify_api.create_playlist(name)

    def get_several_tracks(self, ids):

        # The maximum number of allowed ids per request is 50, according to Spotify API. If ids is larger than 50,
        # then break it down into chunks.

        tracks = []

        chunk = []

        for i in range(0, len(ids)):

            chunk.append(ids[i])

            if len(chunk) == 50 or i == len(ids) - 1:

                response = self.spotify_api.get_several_tracks(','.join(chunk))

                tracks += response['tracks'] if 'tracks' in response else []

                chunk = []

        return tracks

    def get_user_profile(self):

        return self.spotify_api.get_user_profile()

    def get_user_saved_tracks(self):

        saved_tracks = []

        while True:

            request = self.spotify_api.get_user_saved_tracks()

            if 'error' in request:

                break

            if 'items' in request:

                saved_tracks += request['items']

                break

                if 'next' in request and request['next'] is not None:

                    url = request['next']

                else:

                    break

        return saved_tracks

    def search_playlist(self, search_term, limit=5):

        request = self.spotify_api.search_playlist(search_term, limit)

        if 'playlists' in request and 'items' in request['playlists']:

            return request['playlists']['items']

        return None

    def search_tracks(self, search_term):

        request = self.spotify_api.search_tracks(search_term)

        if 'tracks' in request and 'items' in request['tracks']:

            return request['tracks']['items']

        return None

    def get_tracks_from_playlist(self, playlist_id, limit=50):

        request = self.spotify_api.get_tracks_from_playlist(playlist_id, limit)

        tracks = []

        if 'items' in request:

            for item in request['items']:

                if 'track' in item and item['track'] is not None:

                    tracks.append(item['track'])

        return tracks

    def is_authenticated(self):

        return self.spotify_api.is_authenticated()

