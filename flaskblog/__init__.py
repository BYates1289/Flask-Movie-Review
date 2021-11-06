import os
from flask import Flask
from flask_pymongo import PyMongo
import flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager

app = flask.Flask(__name__)

app.config['SECRET_KEY'] =  os.environ['SECRET_KEY']
app.config['MONGO_URI'] =  os.environ['MONGO_URI']
mongo = PyMongo(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    users = mongo.db.users
    return users.find_one({'id': user_id})

from flaskblog import routes