from entregasalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from entregasalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from entregasalpes.modulos.unificacion_pedidos.dominio.entidades import UnificacionPedidos
from entregasalpes.modulos.unificacion_pedidos.dominio.objetos_valor import Producto
from .dto import ProductoDTO, UnificacionPedidosDTO

from datetime import datetime

class MapeadorUnificacionPedidosDTOJson(AppMap):
    def _procesar_producto(self, producto: dict) -> ProductoDTO:
        productos_dto: list[ProductoDTO] = list()

        produc_dto: ProductoDTO = ProductoDTO(producto.get('serial'), producto.get('descripcion'),
                                              producto.get('precio'),producto.get('fecha_vencimiento'),
                                              producto.get('tipo_producto'))

        productos_dto.append(produc_dto)

        return productos_dto
    
    def externo_a_dto(self, externo: dict) -> UnificacionPedidosDTO:
        unificacion_pedidos_dto = UnificacionPedidosDTO()

        productos: list[ProductoDTO] = list()
        for producto in externo.get('productos', list()):
            unificacion_pedidos_dto.productos.append(self._procesar_producto(producto))

        return unificacion_pedidos_dto

    def dto_a_externo(self, dto: UnificacionPedidosDTO) -> dict:
        return dto.__dict__

class MapeadorUnificacionPedidos(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def obtener_tipo(self) -> type:
        return UnificacionPedidos.__class__


    def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
        
        #fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        #id_cliente = str(entidad.id_cliente)
        _id = str(entidad.id)

        return OrdenDTO( _id, list())

    def dto_a_entidad(self, dto: UnificacionPedidosDTO) -> UnificacionPedidos:
        unificacion_pedidos = UnificacionPedidos()
        unificacion_pedidos.productos = list()
        print('  Entro en el metodod dto_a_entidad  ')
        print('  DTO       ',dto)
        productos_dto: list[ProductoDTO] = dto.productos
        print('.....productos.....',productos_dto)
        for producto in productos_dto:
            print('producto  INDIVIDUIAL ',producto[0])
            serial = producto[0].serial
            precio = producto[0].precio
            fecha_vencimiento = producto[0].fecha_vencimiento
            descripcion = producto[0].descripcion
            producto: Producto = Producto(serial, precio, fecha_vencimiento, descripcion)
            unificacion_pedidos.productos.append(producto)
        
        return unificacion_pedidos



