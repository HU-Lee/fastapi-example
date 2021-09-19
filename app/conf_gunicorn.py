import multiprocessing
import os
import sys
import logging
from covid.covidsaver import CovidController
from loadbalance import LiveUpdater

workers_per_core_str = os.getenv("WORKERS_PER_CORE", "1")
max_workers_str = os.getenv("MAX_WORKERS")
use_max_workers = None
if max_workers_str:
    use_max_workers = int(max_workers_str)
web_concurrency_str = os.getenv("WEB_CONCURRENCY", None)

host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "80")
bind_env = os.getenv("BIND", None)
use_loglevel = os.getenv("LOG_LEVEL", "info")
if bind_env:
    use_bind = bind_env
else:
    use_bind = f"{host}:{port}"

cores = multiprocessing.cpu_count()
workers_per_core = float(workers_per_core_str)
default_web_concurrency = workers_per_core * cores
if web_concurrency_str:
    web_concurrency = int(web_concurrency_str)
    assert web_concurrency > 0
else:
    web_concurrency = max(int(default_web_concurrency), 2)
    if use_max_workers:
        web_concurrency = min(web_concurrency, use_max_workers)
accesslog_var = os.getenv("ACCESS_LOG", "-")
use_accesslog = accesslog_var or None
errorlog_var = os.getenv("ERROR_LOG", "-")
use_errorlog = errorlog_var or None
graceful_timeout_str = os.getenv("GRACEFUL_TIMEOUT", "120")
timeout_str = os.getenv("TIMEOUT", "120")
keepalive_str = os.getenv("KEEP_ALIVE", "5")

# Gunicorn config variables
loglevel = use_loglevel
workers = web_concurrency
bind = use_bind
errorlog = use_errorlog
worker_tmp_dir = "/dev/shm"
accesslog = use_accesslog
graceful_timeout = int(graceful_timeout_str)
timeout = int(timeout_str)
keepalive = int(keepalive_str)

# ---------------------------------------------------------
#                          Custom
# ---------------------------------------------------------

test_urls = [
    "https://www.naver.com",
    "https://www.google.com/",
    "https://www.daum.net/",
]
test_weights = [3,5,2]
port = int(os.getenv("PORT", "8000"))

updater = LiveUpdater(
    test_urls,
    test_weights,
    20,
    logging.getLogger("uvicorn.error")
)
saver = CovidController(300)

def on_starting(server):
    try:
        if not os.path.exists("_file"):
            os.makedirs("_file")
    except OSError:
        print ('Failed to make directory')
    saver.start()
    updater.start()

def on_exit(server):
    updater.stop()
    saver.stop()
    sys.exit()