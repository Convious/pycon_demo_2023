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


## Interesting repos

[uvloop](https://github.com/MagicStack/uvloop)
[pyuv](https://github.com/saghul/pyuv)
[gevent](https://github.com/gevent/gevent)
[greenlet](https://github.com/python-greenlet/greenlet)
[libuv](https://github.com/libuv/libuv)
[django-db-geventpool](https://github.com/jneight/django-db-geventpool)

## Useful links

[uvloop design](http://docs.libuv.org/en/v1.x/design.html)
[GIL](https://wiki.python.org/moin/GlobalInterpreterLock)
[stackless wiki](https://github.com/stackless-dev/stackless/wiki/)
[gunicorn workers choice guide](https://luis-sena.medium.com/gunicorn-worker-types-youre-probably-using-them-wrong-381239e13594)
