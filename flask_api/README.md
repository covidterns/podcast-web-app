# Podcasts Web App API 
- Backend service to provide CRUD API operations for user creation and user subscriptions to podcasts (Work in progress)
- provides podcasts classifications (work in progress)
### Example request and response 
GET request from the command line:
```
curl -i http://127.0.0.1:5000/api/podcasts?podcast_show="Top10s"&podcast_episode="Despacito"
```
Example response: 
```
{"result":{"cover":"http://res.cloudinary.com/alick/image/upload/v1502689731/Despacito_uvolhp.jpg","podcastEpisode":"Despacito","podcastShow":"Top10s","publisher":"John Doe","src":"http://res.cloudinary.com/alick/video/upload/v1502689683/Luis_Fonsi_-_Despacito_ft._Daddy_Yankee_uyvqw9.mp3"}}
```


## Install & run locally

Install:
```
git clone git@github.com:covidterns/podcast-web-app.git
cd flask_api
```  
Create a virtualenv:  
```
python3 -m venv env0  
```  
Activate it on Linux:
```
. envo/bin/activate  
```  
Or on Windows cmd:  
```
env0\Scripts\activate.bat  
```  
Install requirements:
```
pip install -r requirements.txt  
```  

export variables
```
export FLASK_APP=routes.py
```

Run app 
```
FLASK run
```

or via the Procfile with Gunicorn (for production use)
```
gunicorn routes:app
```


View on [localhost:5000](http://127.0.0.1:5000)

