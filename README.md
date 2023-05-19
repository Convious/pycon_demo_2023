# pycon_demo_2023

## Install deps

Requires `pipenv`. Install it with your package manager.

```
pipenv install --python 3.10
```

In order to deploy the serveless app you need to have `sam-cli` installed locally

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
GUNICORN_WORKERS=num_of_workers gunicorn -c gunicorn_sync.conf.py app.wsgi:application

# gevent workers
GUNICORN_WORKERS=num_of_workers gunicorn -c gunicorn_gevent.conf.py app.wsgi:application
```

## Start locust

```
cd benchmark
locust -H http://localhost:8000 -u 200 -r 10 CPUUser
```