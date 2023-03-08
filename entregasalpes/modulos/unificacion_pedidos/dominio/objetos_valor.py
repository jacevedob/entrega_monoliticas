"""Objetos valor del dominio de vuelos

En este archivo usted encontrará los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass, field
from entregasalpes.seedwork.dominio.objetos_valor import ObjetoValor
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class Producto(ObjetoValor):
    serial : str
    descripcion : str
    precio : str
    fecha_vencimiento : str


    def serial(self) -> str:
        return self.serial

    def descripcion(self) -> str:
        return self.descripcion

    def precio(self) -> str:
        return self.precio

    def fecha_vencimiento(self) -> str:
        return self.fecha_vencimiento

