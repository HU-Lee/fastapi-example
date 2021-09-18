from typing import List
from pydantic import BaseModel

class TestResponse(BaseModel):
    name: str 
    date: str = ""
    available_servers: List[str] = []
    dummy: int = None