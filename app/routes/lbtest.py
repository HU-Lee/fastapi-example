from app.model.lb import LBRequest
from fastapi import APIRouter, Request
import requests

router = APIRouter(
    prefix="/loadbal",
    tags=["loadbalancing"],
)

@router.get("/test")
def rr_test(req:Request, body:LBRequest):
    ip = req.client.host
    url = "https://www.google.com"
    res: requests.Response = requests.get(url)
    return {
        "req_ip": ip,
        "ip_name": body.ip_name, 
        "target": url,
        "status": res.status_code
    }