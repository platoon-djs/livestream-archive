# Livestream Archive
An docker container with [Flask](http://flask.pocoo.org/). It's used to simply  view recorded livestreams within Platoon DJs. The livestreams are located at Platoon NAS in folder `~/platoon-djs/livestreams`.
## Prereqs
In order to run the image, [Docker](https://www.docker.com/) is reqiured.
## Setup
There are two ways of building the image.   

**Recommended build:** the easiest way is to use make:   
```make build```

**Manual build:** if you want to build it yourself you can do so by cloning the repo and then build it:
* `git clone https://github.com/platoon-djs/livestream-archive.git`
* `cd livestream-archive`
* `docker build -t livestream-archive .`

### Running
To run the container; use:   
`make run`
or 
```docker run -p 5002:5002 -d -v ~/platoon-djs/livestreams/:/var/www/static/streams livestream-archive```

Stuff should now be running at [http://localhost:5002](http://localhost:5002). 

### Parsing of folder names
The server uses the folder name for each video to create a title to the video. Underscores and dashes are replaced by whitespaces.

### Dev
To setup dev environment, do a manual build and then run `make dev`. This ensures that edited files are automatically copied to the docker container once they're saved.


