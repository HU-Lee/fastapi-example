import datetime
import sys
from app.model import TestResponse
from fastapi import FastAPI
from app.routes import lbtest

app = FastAPI()
name = "FastAPI - Example"

app.include_router(lbtest.router)



@app.on_event("startup")
async def startup_event():
    lbtest.ct.start()

@app.on_event("shutdown")
def shutdown_event():
    lbtest.ct.stop()
    sys.exit()

@app.get("/", response_model=TestResponse, response_model_exclude_none=True)
def read_root():
    return { 
        "name": name,
        "date": str(datetime.datetime.now()),
        "available_servers": lbtest.ct.balancer.live_urls
    }