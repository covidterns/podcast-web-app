"""
Define the REST verbs relative to the eps
"""
from flask_restful import Resource
from flask import request,jsonify

class PodcastEpisodeResource(Resource):
    """ Verbs relative to the episode """

    def get(self):
        """ Return a list of key information about eps """
        podcast_show = request.args.get('podcast_show')
        try:
            response = {
                'podcastShow': podcast_show,
                'podcastEpisode': "Despactio",
                'publisher': 'John Doe',
                'cover':
                'http://res.cloudinary.com/alick/image/upload/v1502689731/Despacito_uvolhp.jpg',
                'src':
                    'http://res.cloudinary.com/alick/video/upload/v1502689683/Luis_Fonsi_-_Despacito_ft._Daddy_Yankee_uyvqw9.mp3'
            }
        except Exception as e:
            print(e)
            return "Record not found", 400
        return jsonify(result=response)