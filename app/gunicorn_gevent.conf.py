import os

worker_class = "gevent"
bind = "0.0.0.0:8000"

# Number of simultaneous clients (only for gevent and eventlet workers),
# by default it's 1000
worker_connections = int(os.getenv("GUNICORN_WORKER_CONNECTIONS", 1000))

# by default it's 1
# 2-4 x $(NUM_CORES) is recommended
workers = int(os.getenv("GUNICORN_WORKERS", 2))
loglevel = "info"
accesslog = "-"
errorlog = "-"
