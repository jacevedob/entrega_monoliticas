from fastapi import FastAPI, Request
import asyncio
import time
import traceback
import uvicorn
import uuid
import datetime
import os
from dotenv import load_dotenv
from pydantic import BaseSettings
from typing import Any
from .consumidores import *
from .despachadores import Despachador
from . import utils
from sse_starlette.sse import EventSourceResponse

class Config(BaseSettings):
    APP_VERSION: str = "1"

settings = Config()
app_configs: dict[str, Any] = {"title": "BFF-Web AeroAlpes"}

app = FastAPI(**app_configs)
tasks = list()
eventos = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    global eventos

    # Cargar variables de entorno
    load_dotenv()
    token = os.getenv('PULSAR_TOKEN')
    url = os.getenv('PULSAR_URL') 
    topicEventoOrdenes = os.getenv('PULSAR_CONSUMER_TERCEROS')
    topicEventoPedidos = os.getenv('PULSAR_PRODUCER_TERCEROS')
    topicEventoSagas = os.getenv('PULSAR_CONSUMER_SAGA')
    topicEventosCompensacion = os.getenv('PULSAR_COMPENSACION')

    subscripcion = 'terceros-subscription-consumer'
    task1 = asyncio.ensure_future(suscribirseOrdenes(topicEventoOrdenes, subscripcion, url, token))
    task2 = asyncio.ensure_future(suscribirsePedidos(topicEventoPedidos, subscripcion, url, token))
    task3 = asyncio.ensure_future(suscribirseSagas(topicEventoSagas, subscripcion, url, token))
    task4 = asyncio.ensure_future(suscribirseCompensacion(topicEventosCompensacion, subscripcion, url, token))

    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)
    tasks.append(task4) 
    

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()
