import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


AEROALPES_HOST = os.getenv("AEROALPES_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_reservas(root) -> typing.List["Reserva"]:
    reservas_json = requests.get(f'http://{AEROALPES_HOST}:5000/vuelos/reserva').json()
    reservas = []

    for reserva in reservas_json:
        reservas.append(
            Reserva(
                fecha_creacion=datetime.strptime(reserva.get('fecha_creacion'), FORMATO_FECHA), 
                fecha_actualizacion=datetime.strptime(reserva.get('fecha_actualizacion'), FORMATO_FECHA), 
                id=reserva.get('id'), 
                id_usuario=reserva.get('id_usuario', '')
            )
        )

    return reservas

def crear_orden (root):
    rest = requests.post(
        'http://localhost:5000/compra/ordenes',
        json={ "id_cliente":"131",
            "productos":[
                {
                    "serial":"ABCD-45678",
                    "descripcion":"7777",
                    "precio":"15002",
                    "fecha_vencimiento":"2023-12-2",
                    "tipo_producto":"tipo"
                },{
                    "serial":"7777",
                    "descripcion":"7777",
                    "precio":"15002",
                    "fecha_vencimiento":"2023-12-2",
                    "tipo_producto":"tipo"
                }
            ]
        }
    )
    print("Esta es la respuesta ", rest)
    return rest.text


@strawberry.type
class Itinerario:
    # TODO Completar objeto strawberry para incluir los itinerarios
    ...

@strawberry.type
class Reserva:
    id: str
    id_usuario: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    #itinerarios: typing.List[Itinerario]

@strawberry.type
class ReservaRespuesta:
    mensaje: str
    codigo: int

@strawberry.type
class Orden:
    id: str




