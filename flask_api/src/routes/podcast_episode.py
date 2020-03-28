"""
Defines the blueprint for the podcast_episode
"""
from flask import Blueprint
from flask_restful import Api

from resources import PodcastEpisodeResource


PODCAST_EPISODE_BLUEPRINT = Blueprint('podcast_episode', __name__)
Api(PODCAST_EPISODE_BLUEPRINT).add_resource(PodcastEpisodeResource, '/podcast_episode')