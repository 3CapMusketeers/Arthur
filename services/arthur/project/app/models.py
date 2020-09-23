from project import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.String(), primary_key=True)
    display_name = db.Column(db.String())
    playlists = db.relationship('Playlist', cascade="all,delete", backref='user')
    admin_user = db.relationship('AdminUser', uselist=False, cascade="all,delete", backref='user')

    def __init__(self, id, display_name):
        self.id = id
        self.display_name = display_name

    def __repr__(self):
        return '<User: %s, Id: %s>' % (self.display_name, self.id, )


class Playlist(db.Model):
    id = db.Column(db.String(), primary_key=True)
    user_id = db.Column(db.String(), db.ForeignKey('user.id'))

    uri = db.Column(db.String())

    href = db.Column(db.String())

    def __init__(self, id, user_id, uri, href):

        self.id = id

        self.user_id = user_id

        self.uri = uri

        self.href = href

    def __repr__(self):
        return '<id %s>' % self.id


class AdminUser(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.String(), db.ForeignKey('user.id'))

    password = db.Column(db.String())

    def __init__(self, user_id, password):

        self.user_id = user_id

        self.password = generate_password_hash(password)

    # Properties required for Flask-Login

    @property
    def is_authenticated(self):

        return True

    @property
    def is_active(self):

        return True

    @property
    def is_anonymous(self):

        return False

    def get_id(self):

        return self.id

    def check_password(self, password):

        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<Admin User Id: %s>' % self.id
