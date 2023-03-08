from entregasalpes.seedwork.aplicacion.comandos import ComandoHandler
from entregasalpes.modulos.unificacion_pedidos.infraestructura.fabricas import FabricaRepositorio
from entregasalpes.modulos.unificacion_pedidos.dominio.fabricas import FabricaPedidos

class CrearUnificacionPedidosBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_unificacion_pedidos: FabricaPedidos = FabricaPedidos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_unificacion_pedidos(self):
        return self._fabrica_unificacion_pedidos
    