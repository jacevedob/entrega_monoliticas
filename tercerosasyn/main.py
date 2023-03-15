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

    #topicEventoOrdenes = 'persistent://experimentos-monoliticos/monoliticas/ordenes'
    #topicEventoPedidos = 'persistent://experimentos-monoliticos/monoliticas/eventos-pedidos'
    #topicEventoSagas = 'persistent://experimentos-monoliticos/monoliticas/saga'
    #url = 'pulsar+ssl://pulsar-aws-useast2.streaming.datastax.com:6651'
    #token =  token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2Nzc4OTAzODQsImlzcyI6ImRhdGFzdGF4Iiwic3ViIjoiY2xpZW50O2RjNTk2NmQxLTgxMWUtNDhjNi1hYTlkLThmYzdjNzI1ZjYyZTtaWGh3WlhKcGJXVnVkRzl6TFcxdmJtOXNhWFJwWTI5ejsxZmIzYWEzOGQ1IiwidG9rZW5pZCI6IjFmYjNhYTM4ZDUifQ.jtRQfeQxyDH1Bp84WSPmtsSpqnl0cZjl2nkigqzIMgy_H-qALSAd-Uci79aaeUhagQYIeuNf5z8WJ2OMoA-Xzk3x3JMw3eAOcnFeE6WEODqgtjHdhlScAgM2WBZYCYM3D9dJMTBxdHGYYmQ8stkk9qpv3z3K-2YySzI_xIUa6pn1Mt4htZ1bTPtPyXCWm6JjFHmgbnHgkgtD2PAW00mnBGjgMc6anJ_ac7qup44khF4bA5-spee-jC6SEqfJ-mQl7uwcVrBrcOh8FXI-KXff91tNsTYWp9jaTCuj1l8RCK6LAAtWKi5NwC33Y-xqjCgdi4PPD_QWy07PWSZr0iWEfA'
    subscripcion = 'terceros-subscription-consumer'
    task1 = asyncio.ensure_future(suscribirseOrdenes(topicEventoOrdenes, subscripcion, url, token))
    task2 = asyncio.ensure_future(suscribirsePedidos(topicEventoPedidos, subscripcion, url, token))
    task3 = asyncio.ensure_future(suscribirseSagas(topicEventoSagas, subscripcion, url, token))

    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()
