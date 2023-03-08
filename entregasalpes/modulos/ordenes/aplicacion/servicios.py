from entregasalpes.seedwork.aplicacion.servicios import Servicio
from entregasalpes.modulos.ordenes.dominio.entidades import Orden
from entregasalpes.modulos.ordenes.dominio.fabricas import FabricaCompras
from entregasalpes.modulos.ordenes.infraestructura.fabricas import FabricaRepositorio
from entregasalpes.modulos.ordenes.infraestructura.repositorios import RepositorioOrdenes
from .mapeadores import MapeadorOrden

from .dto import OrdenDTO

class ServicioOrden(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_ordenes: FabricaCompras = FabricaCompras()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_ordenes(self):
        return self._fabrica_ordenes

    def crear_orden(self, orden_dto: OrdenDTO) -> OrdenDTO:
        print ("- -- -- - -- -- crear orden Servicios ")
        orden: Orden = self.fabrica_ordenes.crear_objeto(orden_dto, MapeadorOrden())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrdenes.__class__)
        repositorio.agregar(orden)

        return self.fabrica_ordenes.crear_objeto(orden, MapeadorOrden())

    def obtener_orden_por_id(self, id) -> OrdenDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrdenes.__class__)
        return repositorio.obtener_por_id(id).__dict__

