""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from entregasalpes.seedwork.dominio.fabricas import Fabrica
from entregasalpes.seedwork.dominio.repositorios  import Repositorio
from entregasalpes.modulos.unificacion_pedidos.dominio.repositorios  import RepositorioUnificacionPedidos
from .repositorios import RepositorioUnificacionPedidosSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioUnificacionPedidos.__class__:
            return RepositorioUnificacionPedidosSQLite()
        elif obj == RepositorioUnificacionPedidos.__class__:
            return RepositorioUnificacionPedidosSQLite()
        else:
            raise ExcepcionFabrica()