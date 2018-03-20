build:
	docker build -t livestream-archive .

run:
	docker run -p 5002:5002 -d -v ~/platoon-djs/livestreams/:/var/www/static/streams livestream-archive

dev:
	docker build -t livestream-archive .
	docker run -p 5002:5002 -v ~/platoon-djs/livestreams/:/var/www/static/streams -v `pwd`/app/:/var/www/ livestream-archive
