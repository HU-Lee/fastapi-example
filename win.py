from loadbalance import LiveUpdater
import uvicorn
import sys
import logging

test_urls = [
    "https://www.naver.com",
    "https://www.google.com/",
    "https://www.daum.net/",
]
test_weights = [3,5,2]

if __name__ == "__main__":
    try:
        updater = LiveUpdater(
            test_urls,
            test_weights,
            2000,
            logging.getLogger("uvicorn.error")
        )
        updater.start()
        uvicorn.run("app.main:app",host="0.0.0.0",port=8000,reload=True,log_config = "app/conf_uvicorn_log.yaml")
    finally:
        updater.stop()
        sys.exit()