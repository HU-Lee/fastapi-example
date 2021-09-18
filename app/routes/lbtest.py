from loadbalance import Controller
from app.model.lb import LBRequest
from fastapi import APIRouter, Request
import logging

router = APIRouter(
    prefix="/loadbal",
    tags=["loadbalancing"],
)

test_urls = [
    "https://www.naver.com",
    "https://www.google.com/",
    "https://www.daum.net/",
]
test_weights = [3,5,2]
lb_options = [
    "rr", 
    "weight_rr",
    "ip_hash",
    "random"
]

ct = Controller(
    lb_method=lb_options[3],
    update_time=20,
    logger=logging.getLogger("uvicorn.error"),
    urls=test_urls,
    weights=test_weights
)

@router.post("/test")
def rr_test(req:Request, body:LBRequest):
    ip = req.client.host
    url, code = ct.getResponse(ip)
    return {
        "req_ip": ip,
        "ip_name": body.ip_name, 
        "target": url,
        "status": code
    }