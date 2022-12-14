FROM python:3.10.6-slim-bullseye

RUN apt-get update \
    # lipq-dev and gg for psycopg2 build
    && apt-get install -y libpq-dev gcc libjpeg62-turbo-dev zlib1g-dev libwebp-dev \
    && pip install pip-tools==6.8.0


# set the working directory
RUN mkdir /app/
WORKDIR /app/
ADD . /app/

COPY requirements.* /app/

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

EXPOSE 80

CMD uwsgi --http=0.0.0.0:80 --module=wsgi --ignore-sigpipe --ignore-write-errors --disable-write-exception