from project.app.handlers.spotify.SpotifyAPI import SpotifyAPI


class SpotifyAPIHandler:

    def authenticate(self, args):
        """
        If the user authorized this arthur, then finish the user authentication by requesting an access and refresh
        tokens. Or if the user did authenticated or his/her token expired then request a new access token (refresh).
        This function should be called whenever a new session is created or the user's access token expired.
        :param args: Dict
        :return: Bool
            True if the user was authenticated. False if otherwise (most likely the user did not authorized this arthur).
        """

        spotify_api = SpotifyAPI()

        # Get and set access token.

        if 'code' in args and args['code'] is not None:

            access_token = spotify_api.request_access_and_refresh_tokens(args['code'])

            if access_token is not None:

                spotify_api.set_access_token(access_token)

                return True

        return False
