from entregasalpes.seedwork.aplicacion.servicios import Servicio
from entregasalpes.modulos.unificacion_pedidos.dominio.entidades import Orden
from entregasalpes.modulos.unificacion_pedidos.dominio.fabricas import FabricaCompras
from entregasalpes.modulos.unificacion_pedidos.infraestructura.fabricas import FabricaRepositorio
from entregasalpes.modulos.unificacion_pedidos.infraestructura.repositorios import RepositorioUnificacionPedidos
from .mapeadores import MapeadorUnificacionPedidos

from .dto import UnificacionPedidosDTO

class ServicioUnificacionPedidos(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_unificacion_pedidos: FabricaPedidos = FabricaPedidos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_unificacion_pedidos(self):
        return self._fabrica_unificacion_pedidos

    def crear_unificacion_pedidos(self, unificacion_pedidos_dto: UnificacionPedidosDTO) -> UnificacionPedidosDTO:
        unificacion_pedidos: UnificacionPedidos = self.fabrica_unificacion_pedidos.crear_objeto(unificacion_pedidos_dto, MapeadorUnificacionPedidos())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioUnificacionPedidos.__class__)
        repositorio.agregar(unificacion_pedidos)

        return self.fabrica_ordenes.crear_objeto(unificacion_pedidos, MapeadorUnificacionPedidos())

    def obtener_unificacion_pedidos_por_id(self, id) -> UnificacionPedidosDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioUnificacionPedidos.__class__)
        return repositorio.obtener_por_id(id).__dict__

