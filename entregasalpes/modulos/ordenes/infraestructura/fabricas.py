""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from entregasalpes.seedwork.dominio.fabricas import Fabrica
from entregasalpes.seedwork.dominio.repositorios  import Repositorio
from entregasalpes.modulos.ordenes.dominio.repositorios  import RepositorioOrdenes, RepositorioEventosOrdenes
from .repositorios import RepositorioOrdenesSQLAlchemy, RepositorioEventosOrdenSQLAlchemy
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    #def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
    #    if obj == RepositorioOrdenes.__class__:
    #        return RepositorioOrdenesSQLite()
    #    elif obj == RepositorioOrdenes.__class__:
    #        return RepositorioOrdenesSQLite()
    #    else:
    #        raise ExcepcionFabrica()
#

    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioOrdenes:
            return RepositorioOrdenesSQLAlchemy()
        elif obj == RepositorioEventosOrdenes:
            return RepositorioEventosOrdenSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
