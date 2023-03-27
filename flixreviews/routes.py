from datetime import datetime
import os
import secrets
from flixreviews import app, mongo
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, \
    abort, session
from flask_login import login_user, current_user, logout_user, \
    login_required
from flixreviews.forms import RegistrationForm, LoginForm, \
    UpdateAccountForm, PostForm
import bcrypt
from bson import ObjectId


def ran(x):
    return range(int(x))


app.jinja_env.filters['ran'] = ran


@app.route('/')
def home():
    check = 0
    if 'username' in session:
        check = 1
    reviews = mongo.db['reviews'].find({})
    return render_template('home.html', check=check, reviews=reviews)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        users = mongo.db.users
        if form.validate_on_submit():
            hashpass = bcrypt.hashpw(form.password.data.encode('utf-8'
                    ), bcrypt.gensalt())
            users.insert_one({'name': form.username.data,
                         'password': hashpass,
                         'email': form.email.data})

            session['username'] = request.form['username']
            return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name': form.username.data})
        if login_user:
            if bcrypt.hashpw(form.password.data.encode('utf-8'),
                             login_user['password']) \
                == login_user['password']:
                session['username'] = form.username.data
                return redirect(url_for('home'))
        flash('Login Unsuccessful. Please check email and password',
              'danger')

    return render_template('login.html', title='Login', form=form)


@app.route('/account', methods=['GET', 'POST'])
def account():
    check = 0
    if 'username' in session:
        check = 1
    form = UpdateAccountForm()
    users = mongo.db.users
    user = users.find_one({'name': session['username']})
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.picture.data:
                profile_image = form.picture.data
                mongo.save_file(profile_image.filename, profile_image)
                users.find_one_and_update({'name': session['username'
                        ]},
                        {'$set': {'profile_image_name': profile_image.filename}})

            users.find_one_and_update({'name': session['username']},
                    {'$set': {'name': form.username.data,
                    'email': form.email.data}})
            session.clear()
            session['username'] = form.username.data
            flash('Your account has been updated!', 'success')
            return redirect(url_for('account'))
    form.username.data = user['name']
    form.email.data = user['email']
    try:
        user['profile_image_name']
        image_file = url_for('file', filename=user['profile_image_name'
                             ])
    except:
        image_file = ''
    return render_template(
        'account.html',
        title='Account',
        user=user,
        form=form,
        profile_image=image_file,
        check=check,
        )


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)


@app.route('/give-review', methods=['GET', 'POST'])
def new_review():
    check = 0
    if 'username' in session:
        check = 1
    form = PostForm()
    reviews = mongo.db.reviews
    if form.validate_on_submit():
        reviews.insert_one({
            'title': form.title.data,
            'link': form.link.data,
            'review': form.review.data,
            'content': form.content.data,
            'star': request.form['star'],
            'author': session['username'],
            'created_at': str(datetime.now().date()),
            })

        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_review.html', title='New Review',
                           form=form, check=check)


@app.route('/reviews')
def reviews():
    check = 0
    if 'username' in session:
        check = 1
        user = session['username']
    reviews = mongo.db['reviews'].find({})
    return render_template('reviews.html', reviews=reviews,
                           check=check, user=user)


@app.route('/review_delete/<string:review_id>', methods=['Post'])
def review_delete(review_id):
    reviews = mongo.db.reviews
    delete = reviews.delete_one({'_id': ObjectId(review_id)})
    flash('Your review has been deleted!', 'success')
    return redirect(url_for('reviews'))


@app.route('/review_show/<string:review_id>', methods=['GET'])
def review_show(review_id):
    check = 0
    if 'username' in session:
        check = 1
    reviews = mongo.db.reviews
    review = reviews.find_one({'_id': ObjectId(review_id)})
    return render_template('single_review.html', review=review,
                           check=check)


@app.route("/review_edit/<string:review_id>", methods=["GET", "POST"])
def review_edit(review_id):
    check = 0
    if "username" in session:
        check = 1
    reviews = mongo.db.reviews
    review = reviews.find_one({"_id": ObjectId(review_id)})
    form = PostForm()
    if request.method == "POST":
        if form.validate_on_submit():

            reviews.update_one(
                {"_id": ObjectId(review_id)},
                {
                    "$set": {
                        "title": form.title.data,
                        "link": form.link.data,
                        "review": form.review.data,
                        "content": form.content.data,
                        "star": request.form["star"],
                        "author": session["username"],
                        "created_at": str(datetime.now().date()),
                    }
                },
            )
            flash("Your review has been updated!", "success")
            return redirect(url_for("reviews"))
    elif request.method == "GET":
        form.title.data = review["title"]
        form.link.data = review["link"]
        form.review.data = review["review"]
        form.content.data = review["content"]
        return render_template(
            "edit_review.html",
            title="New Review",
            form=form,
            check=check,
            star=review["star"],
        )
