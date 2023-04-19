from datetime import datetime
from flixreviews import app,bcrypt,db
from PIL import Image
from flask import render_template, url_for, flash, redirect, request,  session
from flask_login import login_user, current_user, logout_user, login_required
from flixreviews.forms import RegistrationForm, LoginForm,UpdateAccountForm, PostForm
from flixreviews.models import User, Reviews
import os
import secrets

def ran(x):
    return range(int(x))


app.jinja_env.filters['ran'] = ran


@app.route('/')
def home():
    reviews = Reviews.query.all()
    return render_template('home.html', reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data,  password=hashed_password, 
            email=form.email.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, "static/profile-images", picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm() 

    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated!", "success")
        return redirect(url_for("account"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for("static", filename="profile-images/" + current_user.image_file)
    return render_template(
        "account.html", title="Account", image_file=image_file, form=form
    )

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/give-review', methods=['GET', 'POST'])
def new_review():
    form = PostForm()
    if form.validate_on_submit():
        review = Reviews(
            title=form.title.data,
            link=form.link.data,
            review=form.review.data,
            content=form.content.data,
            star=request.form['star'],
            author= current_user,
        )
        db.session.add(review)
        db.session.commit()
        flash('Your Review has been Submitted!', 'success')
        return redirect(url_for('home'))
    return render_template('create_review.html', title='New Review',
                           form=form)


@app.route('/reviews')
def reviews():
    reviews = Reviews.query.all()
    return render_template('reviews.html', reviews=reviews) 


@app.route('/review_delete/<string:review_id>', methods=['Post'])
def review_delete(review_id):
    if current_user.is_authenticated:
        dlt = Reviews.query.get_or_404(review_id)
        if dlt.author == current_user or current_user.super_user:
            db.session.delete(dlt) 
            db.session.commit()
            flash('Your review has been deleted!', 'success')
            return redirect(url_for('reviews'))
        return redirect(url_for('logout'))
    return redirect(url_for('login'))


@app.route('/review_show/<string:review_id>', methods=['GET'])
def review_show(review_id):
    review = Reviews.query.filter_by(id=review_id).first()
    return render_template('single_review.html', review=review)


@app.route("/review_edit/<string:review_id>", methods=["GET", "POST"])
def review_edit(review_id):
    if current_user.is_authenticated:
        review = Reviews.query.filter_by(id=review_id).first()
        if review.author == current_user:
            form = PostForm()
            if request.method == "POST":
                if form.validate_on_submit():
                    review.star = request.form["star"]
                    review.link = form.link.data
                    review.review = form.review.data
                    review.content = form.content.data
                    review.title = form.title.data

                    db.session.add(review)
                    db.session.commit()
                    flash("Your review has been updated!", "success")
                    return redirect(url_for("reviews"))
                return render_template("register.html", title="Register", form=form)
            elif request.method == "GET":
                form.title.data = review.title
                form.link.data = review.link
                form.review.data = review.review
                form.content.data = review.content
                return render_template(
                    "edit_review.html",
                    title="New Review",
                    form=form,
                    star=review.star,
                )
        return redirect(url_for('logout'))
    return redirect(url_for('login'))


@app.route("/admin", methods=["GET"])
def admin():
    if current_user.is_authenticated and current_user.super_user:
        reviews = Reviews.query.all()
        return render_template(
            "admin.html",
            title="admin",
            reviews=reviews,
        )
    else:
        logout_user()
        return redirect(url_for('login'))
    
@app.route("/review_edit_admin/<string:review_id>", methods=["GET", "POST"])
def review_edit_admin(review_id):
    if current_user.is_authenticated:
        review = Reviews.query.filter_by(id=review_id).first()
        if current_user.super_user:
            form = PostForm()
            if request.method == "POST":
                if form.validate_on_submit():
                    review.star = request.form["star"]
                    review.link = form.link.data
                    review.review = form.review.data
                    review.content = form.content.data
                    review.title = form.title.data

                    db.session.add(review)
                    db.session.commit()
                    flash("Review has been updated!", "success")
                    return redirect(url_for("admin"))
                return render_template("register.html", title="Register", form=form)
            elif request.method == "GET":
                form.title.data = review.title
                form.link.data = review.link
                form.review.data = review.review
                form.content.data = review.content
                return render_template(
                    "edit_review.html",
                    title="Review edit",
                    form=form,
                    star=review.star,
                )
        return redirect(url_for('logout'))
    return redirect(url_for('login'))


@app.route('/review_delete_admin/<string:review_id>', methods=['Get'])
def review_delete_admin(review_id):
    if current_user.is_authenticated:
        dlt = Reviews.query.get_or_404(review_id)
        if current_user.super_user:
            db.session.delete(dlt) 
            db.session.commit()
            flash('Your review has been deleted!', 'success')
            return redirect(url_for('admin'))
        return redirect(url_for('logout'))
    return redirect(url_for('login'))