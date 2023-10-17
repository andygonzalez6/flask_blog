import os
from os import environ

SECRET_KEY=environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_USERNAME= os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD= os.environ.get('MAIL_PASSWORD')
MAIL_SERVER='smtp.gmail.com'
MAIL_PORT= 465
MAIL_USE_TLS= False
MAIL_USE_SSL= True
