from covid.covidsaver import CovidController
from loadbalance import LiveUpdater
import uvicorn
import sys
import logging
import os

test_urls = [
    "https://www.naver.com",
    "https://www.google.com/",
    "https://www.daum.net/",
]
test_weights = [3,5,2]
port = int(os.getenv("PORT", "8000"))

if __name__ == "__main__":
    try:
        updater = LiveUpdater(
            test_urls,
            test_weights,
            20,
            logging.getLogger("uvicorn.error")
        )
        saver = CovidController(300)
        saver.start()
        updater.start()
        uvicorn.run("app.main:app",host="0.0.0.0",port=port,reload=True,log_config = "app/conf_uvicorn_log.yaml")
    finally:
        updater.stop()
        saver.stop()
        sys.exit()