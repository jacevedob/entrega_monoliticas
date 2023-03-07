import uuid
from dataclasses import dataclass, field
from entregasalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoUnificacionPedidos(EventoDominio):
    ...

@dataclass
class UnificacionPedidosCreada(EventoUnificacionPedidos):
    id_pedido: uuid.UUID = None
    direccion_recogida: str = None
    direccion_entrega: str = None
    fecha_recogida: str = None
    fecha_entrega: str = None
    estado: str = None
		
@dataclass
class UnificacionPedidosCancelada(EventoUnificacionPedidos):
    id_pedido: uuid.UUID = None
    direccion_recogida: datetime = None

