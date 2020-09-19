import models
from sqlalchemy import exc


class DBHandler:

    def __init__(self, db):

        self.db = db

    def get_user(self, id):

        return models.User.query.get(id)

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

        if user and 'id' in user and 'display_name' in user and not models.User.query.get(user['id']):

            db.session.add(models.User(user['id'], user['display_name']))

            try:

                db.session.commit()

                was_inserted = True

            except exc.SQLAlchemyError:

                db.session.rollback()

            db.session.close()

        return was_inserted
