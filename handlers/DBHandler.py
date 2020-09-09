import models
from sqlalchemy import exc


class DBHandler:

    def __init__(self, db):

        self.db = db

    def get_playlist(self, id):

        return models.Playlist.query.get(id)

    def get_playlists(self, user_id):
        """
        Returns all the playlist that belongs to the user with specified user_id.
        :param user_id: Int
            The id of the user
        :return: Playlist object or None
        """

        user = self.get_user(user_id)

        if user:

            return user.playlists

        return None

    def get_user(self, id):

        return models.User.query.get(id)

    def insert_playlist(self, playlist, user_id):
        """
        Inserts a playlist into the database.
        :param playlist: Dict
            The playlist dict. See Playlist model.
        :param user_id: String
            The id of the user for which the playlist belongs to.
        :return: Bool
            True if the playlist was inserted into the database.
        """

        # Verify that the user exists

        if not self.get_user(user_id):

            return False

        was_inserted = False

        db = self.db

        if playlist and 'id' in playlist and 'uri' in playlist and 'href' in playlist and not \
                self.get_user(playlist['id']):

            db.session.add(models.Playlist(playlist['id'], user_id, playlist['uri'], playlist['href']))

            try:

                db.session.commit()

                was_inserted = True

            except exc.SQLAlchemyError:

                db.session.rollback()

            db.session.close()

        return was_inserted

    def insert_user(self, user):
        """
        Inserts a user into the database.
        :param user: Dict
            The user dict. See User model.
        :return: Bool
            True if the user was inserted into the database.
        """

        was_inserted = False

        db = self.db

        if user and 'id' in user and 'display_name' in user and not self.get_user(user['id']):

            db.session.add(models.User(user['id'], user['display_name']))

            try:

                db.session.commit()

                was_inserted = True

            except exc.SQLAlchemyError:

                db.session.rollback()

            db.session.close()

        return was_inserted
