# pycon_demo_2023

## Install deps

Requires `pipenv`. Install it with your package manager.

```
pipenv install --python 3.10
```

## Run app tests

```
pipenv shell
cd app
DJANGO_SETTINGS_MODULE=app.settings pytest
```

## Run app under gunicorn

```
pipenv shell
cd app

# sync workers
gunicorn -c gunicorn_sync.conf.py app.wsgi:application

# gevent workers
gunicorn -c gunicorn_gevent.conf.py app.wsgi:application
```
