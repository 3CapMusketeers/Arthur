from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView


class AdminHomeView(AdminIndexView):

    def is_visible(self):

        return False


class UserView(ModelView):

    column_display_pk = True

    form_columns = ['id', 'display_name', 'playlists']


class PlaylistView(ModelView):

    column_display_pk = True

    form_columns = ['id', 'user_id', 'uri', 'href']
