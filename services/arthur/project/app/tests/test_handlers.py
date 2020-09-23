import os
import unittest
from sqlalchemy import create_engine
from app.models import *
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

    def test_delete_playlist(self):
        """
        Test that the 'delete_playlist' function can delete a playlist.
        """
        with app.app_context():

            # Assert that there are no playlists in the db

            self.assertFalse(Playlist.query.all())

            # Create a user with three playlists

            user_id = 'johndoe'

            self.create_user(id=user_id)

            playlist_ids = ['playlistA', 'playlistB', 'playlistC']

            for id in playlist_ids:

                self.create_playlist(user_id, id=id)

            # Assert that there are exactly 3 playlists in the db

            self.assertTrue(len(Playlist.query.all()) == 3)

            # Delete each playlist one by one

            db_handler = DBHandler()

            for id in playlist_ids:

                db_handler.delete_playlist(id)

                # Assert that the playlist was deleted

                self.assertIsNone(Playlist.query.get(id))

            # Assert that there are no playlists in the db

            self.assertTrue(not Playlist.query.all())

    def test_delete_user(self):
        """
        Test that the 'delete_user' function can delete a user and all of its playlists.
        """
        with app.app_context():

            # Assert that there are no current playlists in the db

            self.assertFalse(Playlist.query.all())

            user_id = 'johndoe'

            user = self.create_user(id=user_id)

            for id in ['playlistA', 'playlistB', 'playlistC']:

                self.create_playlist(user_id, id=id)

            db_handler = DBHandler()

            user = db_handler.get_user(user_id)

            # Assert that the user owns 3 playlists

            self.assertTrue(len(user.playlists) == 3)

            # Assert that there are only 3 playlists in the db

            playlists = Playlist.query.all()

            self.assertTrue(len(playlists) == 3)

            # Delete the user

            db_handler.delete_user(user.id)

            # Assert that the user does not exist

            self.assertIsNone(User.query.get(user_id))

            # Assert that there are no playlists in the database

            self.assertTrue(not Playlist.query.all())

    def test_insert_user(self):
        """
        Test that the 'insert_user' function can insert a user when no other user with the same id exists.
        """

        with app.app_context():

            user = {'id': 'johndoe', 'display_name': 'johndoe'}

            self.insert_user_test_wrapper(user)

    def test_insert_admin_user(self):
        """
        Test that the 'insert_admin_user' function can insert a new admin user when the parent user exists.
        """

        with app.app_context():

            # Assert that there are no admin users in the db

            self.assertFalse(AdminUser.query.all())

            # Try to create a new admin user

            admin_user = {'user_id': 'johndoe', 'password': 'not-password'}

            db_handler = DBHandler()

            # Assert that the admin user is not created since user with 'johndoe' does not exist

            self.assertFalse(db_handler.insert_admin_user(admin_user))

            # Create a new user

            self.create_user(id=admin_user['user_id'])

            # Assert that the admin user is created

            self.assertTrue(db_handler.insert_admin_user(admin_user))

            admin_user = db_handler.get_admin_user(admin_user['user_id'])

            self.assertTrue(admin_user)

            self.assertEqual(admin_user.user_id, 'johndoe')

            self.assertEqual(len(AdminUser.query.all()), 1)

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

    def create_playlist(self, user_id, id='johndoesplaylist', uri='johndoesplaylisturi', href='johndoesplaylisthref'):

        playlist = {'id': id, 'uri': uri, 'href': href}

        db_handler = DBHandler()

        # Insert a playlist into the database

        db_handler.insert_playlist(playlist, user_id)

        playlist = db_handler.get_playlist(playlist['id'])

        self.assertIsNotNone(playlist)

        return playlist

    def create_user(self, id='johndoe', display_name='johndoe'):

        user = {'id': id, 'display_name': display_name}

        db_handler = DBHandler()

        # Insert the user into the database.

        db_handler.insert_user(user)

        user = db_handler.get_user(user['id'])

        self.assertIsNotNone(user)

        return user


if __name__ == '__main__':

    unittest.main()