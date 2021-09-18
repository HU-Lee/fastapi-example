from typing import List
from threading import Timer
import json

class Updater:
    def __init__(
        self,
        urls: List[str],
        weights: List[float],
    ) -> None:
        self.urls: List[str] = urls
        self.weights: List[float] = weights
        self.fake_count: int = 0

    def getInfo(self) -> dict:
        dic = {}
        for i, url in enumerate(self.urls):
            dic[url] = {
                "live": self.fake_count%(2**(i+1)) < 2**i,
                "weight": self.weights[i]
            }
        self.fake_count += 1
        return dic


class LiveUpdater(Updater):
    def __init__(
        self,
        urls: List[str],
        weights: List[float],        
        update_time: float,
        logger,
        file_path: str = "_file/info.txt",
    ) -> None:
        super().__init__(urls, weights)
        self.timer: Timer = None
        self.update_time: float = update_time
        self.fast_update_time: float = update_time/2
        self.file_path = file_path
        self.logger = logger

    def updateInfo(self) -> None:
        info: dict = self.getInfo()
        with open(self.file_path, "w") as f:
            json.dump(info, f)
        self.logger.info("Server updated")
        dead = len(list(filter(lambda url: not info[url]["live"], info)))
        interval = self.fast_update_time if dead==len(self.urls) else self.update_time
        self.timer = Timer(interval, self.updateInfo)
        self.timer.start()

    def start(self) -> None:
        self.updateInfo()

    def stop(self) -> None:
        self.timer.cancel()
        self.timer = None