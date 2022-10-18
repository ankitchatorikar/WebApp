from flask import Flask,session
from flask_login import LoginManager, UserMixin
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

migrate = Migrate(app, db)
db.init_app(app)

from app import routes,models #models define structure of db


