import models
from sqlalchemy import exc


class DBHandler:

    def __init__(self, db):

        self.db = db

    def delete_user(self, user_id):
        """
        Cascade deletes a user from the database.
        :param user_id: String
        :return: Bool
            True if the user was deleted. False if otherwise.
        """

        return self.delete(self.get_user(user_id))

    def delete_playlist(self, playlist_id):
        """
        Deletes a playlist from the database.
        :param playlist_id: String
        :return: Bool
            True of the playlist was deleted. False if otherwise.
        """

        return self.delete(self.get_playlist(playlist_id))

    def delete(self, obj):

        was_deleted = False

        db = self.db

        db.session.delete(obj)

        try:

            db.session.commit()

            was_deleted = True

        except exc.SQLAlchemyError:

            db.session.rollback()

        db.session.close()

        return was_deleted

    def get_playlist(self, id):

        return models.Playlist.query.get(id)

    def get_user(self, id):

        return models.User.query.get(id)

    def get_user_playlists(self, user_id):
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
