# Podcasts Web App API 
- Backend service to provide CRUD API operations for user creation and user subscriptions to podcasts (Work in progress)
- provides podcasts classifications (work in progress)
### Example request and response 
GET request from the command line:
```
curl -i http://127.0.0.1:5000/application/podcast_episode/podcast_show=Top10s
```
Example response: 
```
{"result":{"cover":"http://res.cloudinary.com/alick/image/upload/v1502689731/Despacito_uvolhp.jpg","podcastEpisode":"Despacito","podcastShow":"Top10s","publisher":"John Doe","src":"http://res.cloudinary.com/alick/video/upload/v1502689683/Luis_Fonsi_-_Despacito_ft._Daddy_Yankee_uyvqw9.mp3"}}
```


## Install & run locally
You will need [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/).

### install dependencies and check that it works

```bash
$ make install      # Install the pip dependencies on the docker container
$ make start        # Run the container containing your local python server
```
- checkout out the Makefile to see additional scripts