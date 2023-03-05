from entregasalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from entregasalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from entregasalpes.modulos.ordenes.dominio.entidades import Orden
from entregasalpes.modulos.ordenes.dominio.objetos_valor import Producto
from .dto import ProductoDTO, OrdenDTO

from datetime import datetime

class MapeadorOrdenDTOJson(AppMap):
    def _procesar_producto(self, producto: dict) -> ProductoDTO:
        productos_dto: list[ProductoDTO] = list()

        produc_dto: ProductoDTO = ProductoDTO(producto.get('serial'), producto.get('descripcion'),
                                               producto.get('precio'),producto.get('fecha_vencimiento'),
                                              producto.get('tipo_producto'))

        productos_dto.append(produc_dto)

        return productos_dto
    
    def externo_a_dto(self, externo: dict) -> OrdenDTO:
        orden_dto = OrdenDTO()

        productos: list[ProductoDTO] = list()
        for producto in externo.get('productos', list()):
            orden_dto.productos.append(self._procesar_producto(producto))

        return orden_dto

    def dto_a_externo(self, dto: OrdenDTO) -> dict:
        return dto.__dict__

class MapeadorOrden(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def obtener_tipo(self) -> type:
        return Orden.__class__


    def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
        
        #fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        #id_cliente = str(entidad.id_cliente)
        _id = str(entidad.id)

        return OrdenDTO( _id, list())

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        orden = Orden()
        orden.productos = list()
        print('  Entro dijo la M.....da       ')
        print('  DTO       ',dto)
        productos_dto: list[ProductoDTO] = dto.productos
        print('  PRODUCCTOS        ',productos_dto)
        for producto in productos_dto:
            print('producto  INDIVIDUIAL ',producto[0])
            serial = producto[0].serial
            precio = producto[0].precio
            fecha_vencimiento = producto[0].fecha_vencimiento
            descripcion = producto[0].descripcion

            producto: Producto = Producto(serial, precio, fecha_vencimiento, descripcion)

            orden.productos.append(producto)
        
        return orden



