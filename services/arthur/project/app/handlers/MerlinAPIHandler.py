from project.app.handlers.MerlinAPI import MerlinAPI


class MerlinAPIHandler:

    def __init__(self, spotify_api):

        self.merlin_api = MerlinAPI(spotify_api)

        self.is_user_authenticated = spotify_api.is_authenticated()

    def create_model(self):

        if self.is_user_authenticated is True:

            result = self.merlin_api.create_model()

            return 'msg' in result and result['msg'] == 'ok'

        return self.is_user_authenticated

    def check_model(self, user_id):

        result = self.merlin_api.check_model(user_id)

        if 'msg' in result:

            return result['msg']

        return None

    def classify_tracks(self, search_term):

        if self.is_user_authenticated is True:

            return self.merlin_api.classify_tracks(search_term)

        return self.is_user_authenticated

    def curated_playlist(self, search_term):

        if self.is_user_authenticated is True:

            return self.merlin_api.curated_playlist(search_term)

        return self.is_user_authenticated
