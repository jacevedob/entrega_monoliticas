from pulsar.schema import *
from dataclasses import dataclass, field
from entregasalpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearUnificacionPedidosPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoCrearUnificacionPedidos(ComandoIntegracion):
    data = ComandoCrearUnificacionPedidosPayload()