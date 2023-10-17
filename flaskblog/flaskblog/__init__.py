from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from authlib.integrations.flask_client import OAuth
from flask_mail import Mail

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
"""app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True"""


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

mail = Mail(app)
oauth = OAuth(app)

from flaskblog import routes
