from project.app.handlers.MerlinAPI import MerlinAPI


class MerlinAPIHandler:

    def __init__(self, spotify_api):

        self.merlin_api = MerlinAPI(spotify_api)

    def create_model(self):

        result = self.merlin_api.create_model()

        return 'msg' in result and result['msg'] == 'ok'

    def check_model(self):

        result = self.merlin_api.check_model()

        if 'msg' in result:

            return result['msg']

        return None

    def classify_tracks(self, search_term):

        return self.merlin_api.classify_tracks(search_term)

    def curated_playlist(self, search_term):

        return self.merlin_api.curated_playlist(search_term)