from shared import spotify_api
from SpotifyAPI import SpotifyAPI


class SpotifyAPIHandler:

    def authenticate(self, args):
        """
        If the user authorized this app, then finish the user authentication by requesting an access and refresh
        tokens. Or if the user did authenticated or his/her token expired then request a new access token (refresh).
        This function should be called whenever a new session is created or the user's access token expired.
        :param args: Dict
        :return: Bool
            True if the user was authenticated. False if otherwise (most likely the user did not authorized this app).
        """

        # Get and set access and refresh tokens.

        if spotify_api.access_token is None and 'code' in args and args['code'] is not None:

            access_token, refresh_token = spotify_api.request_access_and_refresh_tokens(args['code'])

            if access_token is not None and refresh_token is not None:

                spotify_api.set_access_token(access_token)

                spotify_api.set_refresh_token(refresh_token)

                return True

        # Refresh access token.

        elif spotify_api.refresh_token is not None:

            access_token = spotify_api.request_new_access_token(spotify_api.refresh_token)

            if access_token is not None:

                spotify_api.set_access_token(access_token)

                return True

        return False
