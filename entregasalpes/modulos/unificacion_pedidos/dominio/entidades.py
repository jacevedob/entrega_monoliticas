"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de vuelos

"""

from __future__ import annotations
from dataclasses import dataclass, field

import entregasalpes.modulos.unificacion_pedidos.dominio.objetos_valor as ov
from entregasalpes.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad


@dataclass
class UnificacionPedidos(AgregacionRaiz):
    productos: list[ov.Producto] = field(default_factory=list[ov.Producto])
