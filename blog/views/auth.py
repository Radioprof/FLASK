from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from blog.forms.auth import AuthForm
from blog.forms.user import UserRegisterForm
from blog.models.user import User

auth_app = Blueprint('auth_app', __name__)

login_manager = LoginManager()
login_manager.login_view = "auth_app.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_app.login"))


__all__ = [
    "login_manager",
    "auth_app",
]


@auth_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('articles_app.list'))

    form = UserRegisterForm(request.form)
    errors = []

    if request.method == "POST" and form.validate_on_submit():
        _user = User.query.filter_by(username=form.username.data).one_or_none()
    if _user is None:
        return render_template("auth/login.html", form=form, error="username doesn't exist")
    if not _user.validate_password(form.password.data):
        return render_template("auth/login.html", form=form, error="invalid username or password")

    login_user(_user)
    return redirect(url_for('articles_app.list'))


@auth_app.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_app.login"))


@auth_app.route("/secret/")
@login_required
def secret_view():
    return "Super secret data"
