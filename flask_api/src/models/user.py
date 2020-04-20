"""
Define the User model
"""
from . import db
from .abc import BaseModel
import datetime


class User(db.Model, BaseModel):
    """ The User model """
    __tablename__ = 'user'

    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(300))
    last_name = db.Column(db.String(300))
    email = db.Column(db.String(300), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    subscriptions = db.relationship('podcast_show', backref='user', lazy=True)

    def __init__(self, id, first_name, last_name, email, password, created_at, modified_at, subscriptions=None):
        """ Create a new User """
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()
        self.subscriptions = subscriptions