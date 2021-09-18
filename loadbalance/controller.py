import requests
from loadbalance.checker import Updater
from loadbalance.balance.balancer import Balancer
from typing import List

class Controller:
    def __init__(
        self,
        lb_method: str,
        update_time: float,
        logger,
        urls: List[str],
        weights: List[float] = None,
        file_path: str = "_file/info.txt",
    ) -> None:
        self.balancer = Balancer(file_path, lb_method, update_time, logger)
        self.updater = Updater(urls, weights)

    # 비동기 http request에는 httpx를 사용하지만,
    # 여기서는 편의상 requests를 이용합니다.
    def getResponse(self, ip:str):
        if not self.balancer.live_urls:
            return "None", 404
        url = self.balancer.getUrl(ip)
        res: requests.Response = requests.get(url)
        # 요청 중 서버가 죽을 시 info를 업데이트 로직이 있지만,
        # 여기서는 사용하지 않습니다.
        return url, res.status_code

    def start(self):
        self.balancer.start()
    
    def stop(self):
        self.balancer.stop()