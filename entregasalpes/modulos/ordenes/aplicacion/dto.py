from dataclasses import dataclass, field
from entregasalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ProductoDTO(DTO):
    serial: str
    descripcion: str
    precio: str
    fecha_vencimiento: str
    tipo_producto : str

@dataclass(frozen=True)
class OrdenDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    id_cliente: str = field(default_factory=str)
    id: str = field(default_factory=str)
    productos: list[ProductoDTO] = field(default_factory=list)

