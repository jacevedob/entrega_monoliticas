import uuid
from dataclasses import dataclass, field
from entregasalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoOrden(EventoDominio):
    ...

@dataclass
class OrdenCreada(EventoOrden):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    
@dataclass
class OrdenCancelada(EventoOrden):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

