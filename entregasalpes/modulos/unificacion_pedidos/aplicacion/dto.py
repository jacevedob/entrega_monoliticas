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
class UnificacionPedidosDTO(DTO):
    id: str = field(default_factory=str)
    direccion_recogida: str = field(default_factory=str)
    direccion_entrega: str = field(default_factory=str)
    fecha_recogida: str = field(default_factory=str)
    fecha_entrega: str = field(default_factory=str)
    estado: str = field(default_factory=str)
    productos: list[ProductoDTO] = field(default_factory=list)

