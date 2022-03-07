from email.policy import default
from enum import unique
from importlib_metadata import email
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import date, datetime

class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.Integer)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id')) #tels alchemy foreign key and is the primary key of roles

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(movie_id=id).all()
        return reviews

class User(UserMixin, db.Model): #arg helps connect  to db
    __tablename__ = 'users' #table name
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    pitch = db.relationship('Pitch',backref = 'user',lazy = "dynamic")

    @property #create write only class property password
    def password(self):
        raise AttributeError('You cannot read the password attribute') #we raise an attribute error to block access to the password property

    @password.setter
    def password(self, password):  #save hash to pass_secure column in database
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self, password): #takes pass hashes it and checks if it is the same
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(255), unique=True)
    pitch = db.Column('Pitch', backref = 'category', lazy='dynamic')

    def save_category(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.category}'

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.Integer)
    posted = db.Column(db.DateTime, index = True, default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id')) #tels alchemy foreign key and is the primary key of roles

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.comment}'

class UpVote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id')) #tels alchemy foreign key and is the primary key of roles

    def save_vote(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.id}'

class UpVote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id')) #tels alchemy foreign key and is the primary key of roles

    def save_vote(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.id}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))