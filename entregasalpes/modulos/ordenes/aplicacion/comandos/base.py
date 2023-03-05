from entregasalpes.seedwork.aplicacion.comandos import ComandoHandler
from entregasalpes.modulos.ordenes.infraestructura.fabricas import FabricaRepositorio
from entregasalpes.modulos.ordenes.dominio.fabricas import FabricaCompras

class CrearOrdenBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_ordenes: FabricaCompras = FabricaCompras()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_compras(self):
        return self._fabrica_ordenes
    