from pydantic import BaseModel

class TestResponse(BaseModel):
    name: str 
    date: str = ""
    dummy: int = None