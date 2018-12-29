# Livestream Archive
An docker container with [Flask](http://flask.pocoo.org/). It's used to simply  view recorded livestreams within Platoon DJs. The livestreams are located at Platoon NAS in folder `/sites/archive.platoon.se`.
## Prereqs
In order to run the image, [Docker](https://www.docker.com/) is reqiured.
## Quickstart
To automatically fetch and run the image, simply do this one-liner:   
```docker run -p 5002:5002 -d -v /sites/archive.platoon.se/:/var/www/static/streams --restart always platoondjs/livestream-archive```
## Development
There are two ways of building the image. First do:
* `git clone https://github.com/platoon-djs/livestream-archive.git`
* `cd livestream-archive`   

**Recommended build:** the easiest way is to use make:   
* ```make dev```

**Manual build:** if you want to build it yourself you can do so by cloning the repo and then build it:
* `docker build -t livestream-archive .`

### Running
To run the container; use:   
`make run`    
or     
```docker run -p 5002:5002 -d -v /sites/archive.platoon.se/:/var/www/static/streams livestream-archive```

Stuff should now be running at [http://localhost:5002](http://localhost:5002). 

### Parsing of folder names
The server uses the folder name for each video to create a title to the video. Underscores are replaced by whitespaces.
