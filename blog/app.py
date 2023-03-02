from flask import Flask

from blog.article.views import article
from blog.models.database import db
from blog.report.views import report
from blog.user.views import user


def create_app() -> Flask:
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '(cb!h&a)y8j*i-x62*d#t@3u2t!%6^5c8=n9l3339y)7gq&+o)'

    db.init_app(app)

    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(article)
