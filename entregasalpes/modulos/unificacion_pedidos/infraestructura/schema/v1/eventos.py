from pulsar.schema import *
from entregasalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from entregasalpes.seedwork.infraestructura.utils import time_millis
import uuid

class UnificacionPedidosCreadaPayload(Record):
    id = String()
    direccion_recogida = String()
    direccion_entrega = String()
    fecha_recogida = String()
    fecha_entrega = String()
    estado = String()


class EventoUnificacionPedidosCreada(EventoIntegracion):
    # NOTE La librería Record de Pulsar no es capaz de reconocer campos heredados,
    # por lo que los mensajes al ser codificados pierden sus valores
    # Dupliqué el los cambios que ya se encuentran en la clase Mensaje

    print('ingreso a EventoUnificacionPedidosCreada----------------------------------------')

    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = UnificacionPedidosCreadaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)