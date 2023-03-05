""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from .entidades import Orden
from .reglas import MinimoUnProducto
from .excepciones import TipoObjetoNoExisteEnDominioOrdenesExcepcion
from entregasalpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from entregasalpes.seedwork.dominio.fabricas import Fabrica
from entregasalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaOrdenes(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            orden: Orden = mapeador.dto_a_entidad(obj)

            self.validar_regla(MinimoUnProducto(orden.productos))
            return orden


@dataclass
class FabricaCompras(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Orden.__class__:
            fabrica_orden = _FabricaOrdenes()
            return fabrica_orden.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioOrdenesExcepcion

