import os
import unittest
from sqlalchemy import create_engine
from handlers.DBHandler import DBHandler
from app import app, db


class DBHandlerTestCase(unittest.TestCase):

    def setUp(self):
        """
        Reset the database
        """

        engine = create_engine(os.environ.get('DATABASE_URI'))

        db.session.remove()

        db.metadata.drop_all(bind=engine)

        db.metadata.create_all(bind=engine)

    def test_insert_user(self):
        """
        Test that the 'insert_user' function can insert a user when no other user with the same id exists.
        """

        with app.app_context():

            user = {'id': 'johndoe', 'display_name': 'johndoe'}

            self.insert_user_test_wrapper(user)

    def test_insert_playlist(self):
        """
        Test that the 'insert_playlist' function can insert a playlist when no other playlist with the same id exists.
        """

        with app.app_context():

            # Insert a user into the database.

            user = {'id': 'johndoe', 'display_name': 'johndoe'}

            returned_user = self.insert_user_test_wrapper(user)

            # Insert a playlist into the database

            playlist = {'id': 'johndoesplaylist', 'uri': 'johndoesplaylisturi', 'href': 'johndoesplaylisthref'}

            self.insert_playlist_test_wrapper(playlist, returned_user.id)

            # Insert a playlist using non-existing user.

            playlist_2 = {'id': 'johndoesplaylist2', 'uri': 'johndoesplaylisturi2', 'href': 'johndoesplaylisthref2'}

            self.insert_playlist_test_wrapper(playlist_2, 'janedoe', valid_user=False)

    def insert_user_test_wrapper(self, user):

        db_handler = DBHandler()

        # Insert a user into the database.

        was_inserted = db_handler.insert_user(user)

        returned_user = db_handler.get_user(user['id'])

        # Assert that the user was inserted.

        self.assertTrue(was_inserted)

        self.assertEqual(returned_user.id, user['id'])

        # Insert the same user (same id) again.

        was_inserted = db_handler.insert_user(user)

        # Assert that the user was not inserted.

        self.assertFalse(was_inserted)

        return returned_user

    def insert_playlist_test_wrapper(self, playlist, user_id, valid_user=True):

        db_handler = DBHandler()

        # Insert a playlist into the database

        was_inserted = db_handler.insert_playlist(playlist, user_id)

        returned_playlist = db_handler.get_playlist(playlist['id'])

        if valid_user:

            # Assert that the playlist was inserted.

            self.assertTrue(was_inserted)

            self.assertEqual(returned_playlist.id, playlist['id'])

            # Insert the same playlist (same id) again.

            was_inserted = db_handler.insert_user(playlist)

            # Assert that the playlist was not inserted.

            self.assertFalse(was_inserted)

            return returned_playlist

        # Assert that the playlist was NOT inserted.

        self.assertFalse(was_inserted)

        return None


if __name__ == '__main__':

    unittest.main()