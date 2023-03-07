""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from entregasalpes.config.db import db
from entregasalpes.modulos.unificacion_pedidos.dominio.repositorios import RepositorioUnificacionPedidos, RepositorioEventosUnificacionPedidos
from entregasalpes.modulos.unificacion_pedidos.dominio.entidades import UnificacionPedidos
from entregasalpes.modulos.unificacion_pedidos.dominio.fabricas import FabricaPedidos
from .mapeadores import MapeadorUnificacionPedidos, MapadeadorEventosUnificacionPedidos
from uuid import UUID
from .dto import EventosUnificacionPedidos
from ..aplicacion.dto import UnificacionPedidosDTO


class RepositorioUnificacionPedidosSQLite(RepositorioUnificacionPedidos):

    def __init__(self):
        self._fabrica_unificacion_pedidos: FabricaPedidos = FabricaPedidos()

    @property
    def fabrica_ordenes(self):
        return self._fabrica_unificacion_pedidos

    def obtener_por_id(self, id: UUID) -> UnificacionPedidos:
        unificacion_pedidos_dto = db.session.query(UnificacionPedidosDTO).filter_by(id=str(id)).one()
        return self.fabrica_unificacion_pedidos.crear_objeto(unificacion_pedidos_dto, MapeadorUnificacionPedidos())

    def obtener_todos(self) -> list[UnificacionPedidos]:
        # TODO
        raise NotImplementedError

    def agregar(self, unificacion_pedidos: UnificacionPedidos):
        unificacion_pedidos_dto = self.fabrica_unificacion_pedidos.crear_objeto(unificacion_pedidos, MapeadorUnificacionPedidos())
        db.session.add(unificacion_pedidos_dto)
        db.session.commit()

    def actualizar(self, unificacion_pedidos: UnificacionPedidos):
        # TODO
        raise NotImplementedError

    def eliminar(self, unificacion_pedidos_id: UUID):
        # TODO
        raise NotImplementedError

class RepositorioEventosUnificacionPedidosSQLAlchemy(RepositorioEventosUnificacionPedidos):

    def __init__(self):
        self._fabrica_unificacion_pedidos: FabricaPedidos = FabricaPedidos()

    @property
    def fabrica_unificacion_pedidos(self):
        return self._fabrica_unificacion_pedidos

    def obtener_por_id(self, id: UUID) -> Orden:
        unificacion_pedidos_dto = db.session.query(UnificacionPedidosDTO).filter_by(id=str(id)).one()
        return self.fabrica_unificacion_pedidos.crear_objeto(unificacion_pedidos_dto, MapadeadorEventosUnificacionPedidos())

    def obtener_todos(self) -> list[UnificacionPedidos]:
        raise NotImplementedError

    def agregar(self, evento):
        unificacion_pedidos_evento = self.fabrica_unificacion_pedidos.crear_objeto(evento, MapadeadorEventosUnificacionPedidos())

        parser_payload = JsonSchema(unificacion_pedidos_evento.data.__class__)
        json_str = parser_payload.encode(unificacion_pedidos_evento.data)
		
        unificacion_pedidos_dto = EventosUnificacionPedidos()
        unificacion_pedidos_dto.id = str(evento.id)
        unificacion_pedidos_dto.id_entidad = str(evento.id_pedido)
        unificacion_pedidos_dto.fecha_evento = evento.fecha_creacion
        unificacion_pedidos_dto.version = str(unificacion_pedidos_evento.specversion)
        unificacion_pedidos_dto.tipo_evento = evento.__class__.__name__
        unificacion_pedidos_dto.formato_contenido = 'JSON'
        unificacion_pedidos_dto.nombre_servicio = str(unificacion_pedidos_evento.service_name)
        unificacion_pedidos_dto.contenido = json_str

        db.session.add(unificacion_pedidos_dto)

    def actualizar(self, unificacion_pedidos: UnificacionPedidos):
        raise NotImplementedError

    def eliminar(self, unificacion_pedidos_id: UUID):
        raise NotImplementedError
