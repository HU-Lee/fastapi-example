import json
from loadbalance.balance.algo import get_random, ip_hash, round_robin, weighted_round_robin
from typing import List
from threading import Timer


class Balancer:
    def __init__(
        self,
        file_path: str,
        lb_method: str,
        update_time: float,
        logger
    ) -> None:
        self.file_path: str = file_path
        self.lb_method: str = lb_method
        self.live_urls: List[str] = [] 
        self.live_weights: List[float] = []
        self.count: int = 0
        self.timer: Timer = None
        self.update_time: float = update_time
        self.fast_update_time: float = update_time/2
        self.logger = logger

    def updateInfo(self) -> None:
        with open(self.file_path, "r") as f:
            info: dict = json.load(f)
        self.live_urls = list(filter(lambda url: info[url]["live"], info))
        self.live_weights = list(map(lambda url: info[url]["weight"], info))
        self.logger.info("Server info on sync")
        interval = self.fast_update_time if len(self.live_urls)==0 else self.update_time
        self.timer = Timer(interval, self.updateInfo)
        self.timer.start()

    # 요청 중 서버가 죽을 시 info를 업데이트하는 함수이지만,
    # 여기서는 사용하지 않습니다.
    def updateInfoEmergently(self, info) -> None:
        pass

    def getUrl(self, ip:str) -> str:
        if self.lb_method == "rr":
            self.count, url = round_robin(self.live_urls, self.count)
        elif self.lb_method == "weight_rr":
            self.count, url = weighted_round_robin(self.live_urls, self.live_weights, self.count)
        elif self.lb_method == "ip_hash":
            url = ip_hash(self.live_urls, ip)
        elif self.lb_method == "random":
            url = get_random(self.live_urls)
        return url

    def start(self) -> None:
        self.updateInfo()

    def stop(self) -> None:
        self.timer.cancel()
        self.timer = None