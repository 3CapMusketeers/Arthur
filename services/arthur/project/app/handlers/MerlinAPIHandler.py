from flask import jsonify
from project.app.handlers.MerlinAPI import MerlinAPI


class MerlinAPIHandler:

    def __init__(self, spotify_api):

        self.merlin_api = MerlinAPI()

        self.spotify_api = spotify_api

    def create_model(self):

        saved_tracks = self.spotify_api.get_user_saved_tracks()

        tracks = []

        for track in saved_tracks:

            if 'track' in track and 'preview_url' in track['track'] and track['track']['preview_url'] is not None:

                tracks.append({'id': track['track']['id'], 'url': track['track']['preview_url']})

        result = self.merlin_api.create_model(saved_tracks)

        return 'msg' in result and result['msg'] == 'ok'

    def check_model(self, user_id):

        result = self.merlin_api.check_model(user_id)

        return result

        # return None

    def classify_tracks(self, search_term):

        saved_tracks = self.spotify_api.get_user_saved_tracks()

        classify_tracks = []

        for track in saved_tracks:

            if 'track' in track and 'preview_url' in track['track'] and track['track']['preview_url'] is not None:

                classify_tracks.append({'id': track['track']['id'], 'url': track['track']['preview_url']})

        playlists = self.spotify_api.search_playlist(search_term, limit=5)

        playlist_tracks = []

        for playlist in playlists:

            playlist_tracks += self.spotify_api.get_tracks_from_playlist(playlist['id'])

        training_tracks = []

        for track in playlist_tracks:

            if 'preview_url' in track and track['preview_url'] is not None:

                training_tracks.append({'id': track['id'], 'url': track['preview_url']})

        response_tracks = self.merlin_api.classify_tracks(search_term)

        if 'msg' in response_tracks:

            return jsonify(tracks={'error': True, 'msg': response_tracks['msg']})

        results = []

        if 'tracks' in response_tracks:

            tracks = self.spotify_api.get_several_tracks(response_tracks['tracks'])

            for track in tracks:

                artists = []

                if 'artists' in track:

                    artist_list = [artist['name'] for artist in track['artists']]

                    artists = ", ".join(map(str, artist_list))

                results.append({'id': track['id'], 'name': track['name'], 'uri': track['uri'], 'artists': artists})

        return jsonify(tracks=results)

    def curated_playlist(self, search_term):

        playlist_tracks = []

        playlists = self.spotify_api.search_playlist(search_term)

        for playlist in playlists:

            if 'id' in playlist:

                playlist_tracks += self.spotify_api.get_tracks_from_playlist(playlist['id'])

        tracks = []

        for track in playlist_tracks:

            if 'preview_url' in track and track['preview_url'] is not None:

                tracks.append({'id': track['id'], 'url': track['preview_url']})

        response_tracks = self.merlin_api.curated_playlist(search_term, tracks)

        if 'msg' in response_tracks:

            return jsonify(tracks={'error': True, 'msg': response_tracks['msg']})

        results = []

        if 'tracks' in response_tracks:

            tracks = self.spotify_api.get_several_tracks(response_tracks['tracks'])

            for track in tracks:

                results.append({'id': track['id'], 'name': track['name'], 'uri': track['uri'],
                                'artists': track['artists']})

        return jsonify(tracks=results)
