"""
Define the REST verbs relative to the users
"""
from flask_restful import Resource


class UserResource(Resource):
    """ Verbs relative to the users """

    def get(self):
        """ Return a list of key information about users """

        return 'such user'