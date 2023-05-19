import os

worker_class = "sync"
bind = "0.0.0.0:8000"

# by default it's 1
# 2-4 x $(NUM_CORES) is recommended
workers = int(os.getenv("GUNICORN_WORKERS", 20))
loglevel = "info"
accesslog = "-"
errorlog = "-"
