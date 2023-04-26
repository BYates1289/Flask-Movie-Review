from datetime import datetime
from sqlalchemy.sql.schema import ForeignKey
from flixreviews import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    super_user = db.Column(db.Boolean, default=False)
    reviews = db.relationship("Reviews", backref="author", lazy=True)


    def __repr__(self):
        return f"User('{self.username}', '{self.id}', '{self.image_file}')" 
    

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(30), nullable=False)
    review = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(30), nullable=False)
    star = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id",ondelete="CASCADE"), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Reviews('{self.title}', '{self.date_posted}')"