from flask import request, redirect, url_for
from flask_admin import AdminIndexView, expose, helpers
from flask_login import LoginManager, login_user, logout_user, current_user
from flask_admin.contrib.sqla import ModelView
from app.forms.admin import LoginForm, RegisterForm
from app.models import AdminUser
from handlers.DBHandler import DBHandler

login_manager = LoginManager()

@login_manager.user_loader
def load_user(id):

    return AdminUser.query.get(id)


class AdminHomeView(AdminIndexView):

    @expose('/', methods=['GET'])
    def index(self):

        if not current_user.is_authenticated:

            return redirect(url_for('admin.login'))

        return super(AdminHomeView, self).index()

    @expose('/login', methods=['GET', 'POST'])
    def login(self):

        if request.method == 'POST':

            form = LoginForm(request.form)

            if helpers.validate_form_on_submit(form):

                db_handler = DBHandler()

                admin_user = db_handler.get_admin_user(form.username.data)

                login_user(admin_user)

                return redirect(url_for('admin.index'))

            else:

                self._template_args['form'] = form

        else:

            self._template_args['form'] = LoginForm()

        self._template_args['form_header'] = 'Log in'

        return super(AdminHomeView, self).index()

    @expose('/logout')
    def logout(self):

        logout_user()

        return redirect(url_for('admin.index'))

    @expose('/register', methods=['GET', 'POST'])
    def register(self):

        if request.method == 'POST':

            form = RegisterForm(request.form)

            if helpers.validate_form_on_submit(form):

                db_handler = DBHandler()

                db_handler.insert_admin_user({'user_id': form.username.data, 'password': form.password.data})

                return redirect(url_for('admin.index'))

            else:

                self._template_args['form'] = form

        else:

            self._template_args['form'] = RegisterForm()

        self._template_args['form_header'] = 'Register'

        return super(AdminHomeView, self).index()


class UserView(ModelView):

    column_display_pk = True

    form_columns = ['id', 'display_name', 'playlists']

    def is_accessible(self):

        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):

        return redirect(url_for('admin.index'))


class PlaylistView(ModelView):

    column_display_pk = True

    form_columns = ['id', 'user_id', 'uri', 'href']

    def is_accessible(self):

        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):

        return redirect(url_for('admin.index'))


class AdminUserView(ModelView):

    column_display_pk = True

    form_columns = ['id', 'user_id', 'password']

    def is_accessible(self):

        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):

        return redirect(url_for('admin.index'))
