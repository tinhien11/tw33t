# Tw33t
Simple Flask + Vue app that communicates with Twitter API and logs info about each search.



### Front-end
- Using vue and semantic ui framework to display the results, screenshot:

### Back-end
- API get tweets: http://localhost:8000/api/v1/tweets/?user=namkep&count=3
- Log relevant information about each search to a file: app/tw33t/logs/twitter_handle.log


## How to run

Build the docker image and start server:

```
docker build -t cubicasa-developer-test .
docker-compose up web
```

For development (hot reload): http://localhost:8080/   
For staging or production: http://localhost:8000/ 
