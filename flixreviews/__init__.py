import os
from flask import Flask
from flask_pymongo import PyMongo
import flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager

app = flask.Flask(__name__)

# app.config['SECRET_KEY'] =  os.environ['SECRET_KEY']
# app.config['MONGO_URI'] =  os.environ['MONGO_URI']
app.config['SECRET_KEY'] =  "sapdpsadksapdk111msdmsmdsld@"
app.config['MONGO_URI'] =  "mongodb+srv://root:Pakchk12345@cluster0.6idju9p.mongodb.net/movie-review?retryWrites=true&w=majority"

mongo = PyMongo(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    users = mongo.db.users
    return users.find_one({'id': user_id})

from flixreviews import routes
