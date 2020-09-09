import os
import unittest
from sqlalchemy import create_engine
from handlers.DBHandler import DBHandler
from app import db


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

        db_handler = DBHandler(db)

        # Insert a user into the database.

        user = {'id': 'johndoe', 'display_name': 'johndoe'}

        was_inserted = db_handler.insert_user(user)

        returned_user = db_handler.get_user(user['id'])

        # Assert that the user was inserted.

        self.assertTrue(was_inserted)

        self.assertEqual(returned_user.id, user['id'])

        # Insert the same user (same id) again.

        was_inserted = db_handler.insert_user(user)

        # Assert that the user was not inserted.

        self.assertFalse(was_inserted)

    def test_insert_playlist(self):
        """
        Test that the 'insert_user' function can insert a user when no other user with the same id exists.
        """

        db_handler = DBHandler(db)

        # Insert a user into the database.

        user = {'id': 'johndoe', 'display_name': 'johndoe'}

        db_handler.insert_user(user)

        returned_user = db_handler.get_user(user['id'])

        # Insert a playlist into the database

        playlist = {'id': 'johndoesplaylist', 'uri': 'johndoesplaylisturi', 'href': 'johndoesplaylisthref'}

        was_inserted = db_handler.insert_playlist(playlist, returned_user.id)

        returned_playlist = db_handler.get_playlist(playlist['id'])

        # Assert that the playlist was inserted.

        self.assertTrue(was_inserted)

        self.assertEqual(returned_playlist.id, playlist['id'])

        # Insert the same playlist (same id) again.

        was_inserted = db_handler.insert_user(playlist)

        # Assert that the playlist was not inserted.

        self.assertFalse(was_inserted)


if __name__ == '__main__':

    unittest.main()