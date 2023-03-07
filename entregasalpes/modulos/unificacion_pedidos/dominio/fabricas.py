""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from .entidades import UnificacionPedidos
from .reglas import MinimoUnProducto
from .excepciones import TipoObjetoNoExisteEnDominioUnificacionPedidosExcepcion
from entregasalpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from entregasalpes.seedwork.dominio.fabricas import Fabrica
from entregasalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaUnificacionPedidos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            unificacion_pedidos_dto: UnificacionPedidos = mapeador.dto_a_entidad(obj)

            self.validar_regla(MinimoUnProducto(unificacion_pedidos_dto.productos))
            return unificacion_pedidos_dto


@dataclass
class FabricaPedidos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == UnificacionPedidos.__class__:
            fabrica_unificacion_pedidos = _FabricaUnificacionPedidos()
            return fabrica_unificacion_pedidos.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioOrdenesExcepcion

