from datetime import datetime
import os
import secrets
from flaskblog import app, mongo
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, session
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
import bcrypt
from bson import ObjectId


def ran(x):
    return range(int(x))


app.jinja_env.filters["ran"] = ran


@app.route("/")
def home():
    check = 0
    if "username" in session:
        check = 1
    reviews = mongo.db["reviews"].find({})
    return render_template("home.html", check=check, reviews=reviews)


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        users = mongo.db.users
        if form.validate_on_submit():
            hashpass = bcrypt.hashpw(
                form.password.data.encode("utf-8"), bcrypt.gensalt()
            )
            users.insert(
                {
                    "name": form.username.data,
                    "password": hashpass,
                    "email": form.email.data,
                }
            )
            session["username"] = request.form["username"]
            return redirect(url_for("home"))

    return render_template("register.html", title="Register", form=form)