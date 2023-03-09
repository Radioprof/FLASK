from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators


class AuthForm(FlaskForm):
    username = StringField('username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')
