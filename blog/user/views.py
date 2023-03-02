from flask import Blueprint, render_template, redirect

from blog.models import User
from blog.user import auth

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('/')
def user_list():
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users
    )


@user.route('/<int:user_id>/')
def get_user(user_id: int):
    try:
        user = User.query.filter_by(id=user_id).one_or_none()
    except KeyError:
        return redirect('/users/')
    return render_template('users/details.html', user=user)



