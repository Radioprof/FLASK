from flask import Flask
# from flask_wtf import CSRFProtect

from blog.views.article import articles_app
from blog.views.auth import auth_app, login_manager
from blog.views.users import users_app
from blog.models.database import db
from flask_migrate import Migrate
# import os


app = Flask(__name__)

# cfg_name = os.environ.get('TestingConfig')
# app.config.from_object(f"blog.configs.{cfg_name}")

migrate = Migrate(app, db, compare_type=True)

app.register_blueprint(users_app)
app.register_blueprint(articles_app)
app.register_blueprint(auth_app, url_prefix="/auth")

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '(cb!h&a)y8j*i-x62*d#t@3u2t!%6^5c8=n9l3339y)7gq&+o)'
app.config['WTF_CSRF_ENABLE'] = True

db.init_app(app)

login_manager.init_app(app)
# csrf = CSRFProtect(app)
