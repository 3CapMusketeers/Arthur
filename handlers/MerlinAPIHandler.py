from MerlinAPI import MerlinAPI


class MerlinAPIHandler:

    def create_model(self):

        merlin_api = MerlinAPI()

        result = merlin_api.create_model()

        return 'msg' in result and result['msg'] == 'ok'

    def classify_tracks(self, search_term):

        merlin_api = MerlinAPI()

        return merlin_api.classify_tracks(search_term)

    def curated_playlist(self):

        merlin_api = MerlinAPI()

        return merlin_api.curated_playlist()