from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from models import User, AdminUser


class LoginForm(FlaskForm):

    username = StringField('username', validators=[DataRequired()])

    password = PasswordField('password', validators=[DataRequired()])

    submit = SubmitField('Log in')

    def validate_password(self, field):

        admin_user = AdminUser.query.filter_by(user_id=self.username.data).first()

        if not admin_user or not admin_user.check_password(self.password.data):

            raise ValidationError('Incorrect username of password.')


class RegisterForm(FlaskForm):

    username = StringField('username', validators=[DataRequired()])

    password = PasswordField('password', validators=[DataRequired(), EqualTo('confirm_password',
                                                                             message='Passwords must match.')])

    confirm_password = PasswordField('confirm-password', validators=[DataRequired()])

    submit = SubmitField('Register')

    def validate_username(self, field):

        user = User.query.get(self.username.data)

        if not user:

            raise ValidationError('Not a user.')

        elif AdminUser.query.filter_by(user_id=self.username.data).first():

            raise ValidationError('User already an admin.')
