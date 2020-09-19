from app import db


class User(db.Model):

    id = db.Column(db.String(), primary_key=True)

    display_name = db.Column(db.String())

    playlists = db.relationship('Playlist', backref='user')

    def __init__(self, id, display_name):

        self.id = id

        self.display_name = display_name

    def __repr__(self):
        return '<User: %s, Id: %s>' % self.display_name, self.id


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
