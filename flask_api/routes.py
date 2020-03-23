from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
from flask import Flask, make_response
import json
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/podcasts', methods=['GET'])
@cross_origin()
def get_tasks():
    podcast_show = request.args.get('podcast_show')
    podcast_episode = request.arg.get('podcast_episode')
    try:
        response = {
            'podcastShow': podcast_show,
            'podcastEpisode': podcast_episode,
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


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
