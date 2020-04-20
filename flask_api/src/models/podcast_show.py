"""
Define the Podcast Show model
"""
from . import db
from .abc import BaseModel


class PodcastShow(db.Model, BaseModel):
    """ The PodcastShow model """
    __tablename__ = 'PodcastShow'

    id = db.Column(db.Integer, primary_key=True)
    show_name = db.Column(db.String(300), unique=True)
    author = db.Column(db.String(300), nullable=True)
    description = db.Column(db.String(300), nullable=True)
    episodes = db.relationship('podcast_episode', backref='PodcastShow', lazy=True)

    def __init__(self, id, show_name, author, description=None,episodes=None):
        """ Create a new User """
        self.id = id
        self.show_name = show_name
        self.author = author
        self.description = description
        self.episodes = episodes