from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mako import MakoTemplates

__author__ = 'youpengfei'

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)

app.template_folder = "templates"
MakoTemplates(app)

from .views import user, main, post


app.register_blueprint(main.mod)
app.register_blueprint(user.mod)
app.register_blueprint(post.mod, url_prefix='/post')
