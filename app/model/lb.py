from typing import Optional
from pydantic import BaseModel

class LBRequest(BaseModel):
    ip_name: str

class LBResponse(BaseModel):
    req_ip: str
    ip_name: str
    target: str
    status: Optional[int] = 0