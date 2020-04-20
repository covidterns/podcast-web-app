"""
Define the Podcast Episode model
"""
from . import db
from .abc import BaseModel
import datetime

class PodcastEpisode(db.Model, BaseModel):
    """ The podcast Episode model """
    __tablename__ = 'PodcastEpisode'

    #TODO
    id = db.Column(db.Integer, primary_key=True)
    episode_name = db.Column(db.String(300), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    show_id = db.Column(db.Integer, db.ForeignKey('PodcastShow.id'), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    ad_timestamps = db.Column(db.ARRAY(db.Integer), nullable= True) 
    highlights_timestamps = db.Column(db.ARRAY(db.Integer), nullable= True) 

    def __init__(self, id, episode_name, description=None, show_id, created_at, modified_at, ad_timestamps=None, highlights_timestamps=None):
        """ Create a new User """
        self.id = id
        self.episode_name = episode_name
        self.description = description
        self.show_id = show_id
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()
        self.ad_timestamps = ad_timestamps
        self.highlights_timestamps = highlights_timestamps