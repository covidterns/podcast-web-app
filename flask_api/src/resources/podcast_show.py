"""
Define the REST verbs relative to the show
"""
from flask_restful import Resource


class PodcastShowResource(Resource):
    """ Verbs relative to the show """

    def get(self):
        """ Return a list of key information about show """

        return 'such show'