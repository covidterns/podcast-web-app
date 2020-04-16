"""
Defines the blueprint for the podcastShow
"""
from flask import Blueprint
from flask_restful import Api

from resources import PodcastShowResource


PODCAST_SHOW_BLUEPRINT = Blueprint('podcast_show', __name__)
Api(PODCAST_SHOW_BLUEPRINT).add_resource(PodcastShowResource, '/podcast_show')