"""
Define the Podcast Show model
"""
from . import db
from .abc import BaseModel


class PodcastShow(db.Model, BaseModel):
    """ The PodcastShow model """
    __tablename__ = 'PodcastShow'
    
    ## TODO
    
    first_name = db.Column(db.String(300), primary_key=True)
    last_name = db.Column(db.String(300), primary_key=True)
    # The age of our user
    age = db.Column(db.Integer, nullable=True)

    def __init__(self, first_name, last_name, age=None):
        """ Create a new User """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age