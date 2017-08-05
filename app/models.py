#script to describe the user table
from app import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    social_id=db.Column(db.String(64), nullable=False, unique=True)
    posts=db.relationship('Post',backref='author',lazy='dynamic')

    @lm.user_loader
    def load_user(id):
        return User.query.get(int(id))

    #returns True unless the object represents a user that should not be allowed to authenticate for some reason.
    @property
    def is_authenticated(self):
        return True

    # returns True for users unless they are inactive, for example because they have been banned.
    @property
    def is_active(self):
        return True

    #returns True only for fake users that are not supposed to log in to the system.
    @property
    def is_anonymous(self):
        return True

    #returns a unique identifier for the user, in unicode format(for both py2 and py3).
    def get_id(self):
        try:
            return unicode(self.id)   #for python2
        except NameError:
            return str(self.id)       #for python3


    def __repr__(self): #__repr__ tells python how to print objects of this class
        return '<User %r>' % (self.nickname)


class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    body=db.Column(db.String(140))
    timestamp=db.Column(db.DateTime)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self): #__repr__ tells python how to print objects of this class
        return '<Post %r>' % (self.body)
