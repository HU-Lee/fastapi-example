import datetime
from app.model import TestResponse
from fastapi import FastAPI
from app.routes import lbtest

app = FastAPI()
name = "FastAPI - Example"

app.include_router(lbtest.router)

@app.get("/", response_model=TestResponse, response_model_exclude_none=True)
def read_root():
    return { 
        "name": name,
        "date": str(datetime.datetime.now())
    }