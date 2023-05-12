import os

worker_class = "gevent"
bind = "0.0.0.0:8000"

# Number of simultaneous clients (only for gevent and eventlet workers)
worker_connections = int(os.getenv("GUNICORN_WORKER_CONNECTIONS", 10))

workers = int(os.getenv("GUNICORN_WORKERS", 2))
loglevel = "info"
accesslog = "-"
errorlog = "-"

# after receiving a restart signal,
# workers have this much time to finish serving requests.
# Workers still alive after the timeout
# (starting from the receipt of the restart signal) are force killed.
graceful_timeout = int(os.getenv("GUNICORN_GRACEFUL_TIMEOUT", 120))

# Restart workers randomly between 0 and 5000 requests after the first 5000 by default.
# This may help with memory consumption,
# as the memory consumption slowly creeps upwards - the longer the worker lives
# Docs: https://docs.gunicorn.org/en/stable/settings.html#max-requests
max_requests = int(os.getenv("GUNICORN_MAX_REQUESTS", 5000))
max_requests_jitter = int(os.getenv("GUNICORN_MAX_REQUESTS_JITTER", 5000))
