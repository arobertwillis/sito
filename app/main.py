# main.py

from typing import Optional
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel


class ServiceState(Enum):
    OK = "OK",
    NOTOK = "NOTOK"


class Service(BaseModel):
    name: str
    state: ServiceState


services = [
    Service(**{'name': "egsp", 'state': ServiceState.OK})
]

app = FastAPI()


@app.get("/diagnostics/")
async def diagnostics():
    return services
