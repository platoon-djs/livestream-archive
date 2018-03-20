FROM python:alpine

WORKDIR /var/www

RUN pip install Flask

COPY app /var/www/

ENTRYPOINT ["python", "webserver.py"] 
