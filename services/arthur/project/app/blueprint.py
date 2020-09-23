from flask import Blueprint, redirect

from project.app.handlers import DBHandler
from project import spotify_api

spotify_blueprint = Blueprint('', __name__)

@spotify_blueprint.route('/')
def home():
    # Verify user is authenticated. Otherwise authenticate.
    if not spotify_api.is_authenticated():
        return redirect('/authorization')

    # Get user profile and insert into db if not already.
    user = spotify_api.get_user_profile()

    if 'error' in user:
        return user

    db_handler = DBHandler()
    db_handler.insert_user(user)

    return {'user': user['display_name']}
