""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""
import datetime
from entregasalpes.seedwork.infraestructura.utils import unix_time_millis
from entregasalpes.modulos.unificacion_pedidos.dominio.eventos import UnificacionPedidosCreada, UnificacionPedidosCancelada, EventoUnificacionPedidos


from entregasalpes.seedwork.dominio.repositorios  import Mapeador
from entregasalpes.modulos.unificacion_pedidos.dominio.objetos_valor  import Producto
from entregasalpes.modulos.unificacion_pedidos.dominio.entidades import UnificacionPedidos
from .dto import UnificacionPedidos as UnificacionPedidosDTO
from .dto import Producto as ProductoDTO
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion


class MapeadorUnificacionPedidos(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return UnificacionPedidos.__class__

    def entidad_a_dto(self, entidad: UnificacionPedidos) -> UnificacionPedidosDTO:
	    
        unificacion_pedidos_dto = UnificacionPedidosDTO()
        unificacion_pedidos_dto.id = entidad.id
        unificacion_pedidos_dto.direccion_recogida = entidad.direccion_recogida
        unificacion_pedidos_dto.direccion_entrega = entidad.direccion_entrega
        unificacion_pedidos_dto.fecha_recogida = entidad.fecha_recogida
        unificacion_pedidos_dto.fecha_entrega = entidad.fecha_entrega
        unificacion_pedidos_dto.estado = entidad.estado

        productos_dto = list()
        
        for producto in entidad.productos:
            producto_dto = ProductoDTO()
            producto_dto.serial = producto.serial
            producto_dto.precio = producto.precio
            producto_dto.fecha_vencimiento= producto.fecha_vencimiento
            producto_dto.descripcion = producto.descripcion
            productos_dto.append(producto_dto)

        unificacion_pedidos_dto.productos = productos_dto
        return unificacion_pedidos_dto

    def dto_a_entidad(self, dto: UnificacionPedidosDTO) -> UnificacionPedidos:
        unificacion_pedidos = UnificacionPedidos(dto.id, dto.direccion_recogida, dto.direccion_entrega, dto.fecha_recogida, dto.fecha_entrega, dto.estado )
        unificacion_pedidos.productos = list()

        productos_dto: list[ProductoDTO] = dto.productos

        unificacion_pedidos.productos.extend(self._procesar_producto_dto(productos_dto))

        return unificacion_pedidos

    def _procesar_producto_dto(self, productos_dto: list) -> list[Producto]:
        prod_dict = dict()

        for product in productos_dto:
            print(' ingreso al ciclo de productos ------>', product)
            serial = product.serial
            tipo_producto = 'product.tipo_producto'
            precio = product.precio
            descripcion = product.descripcion
            fecha_vencimiento = product.fecha_vencimiento
            prod_dict.setdefault( Producto(serial, descripcion, precio, fecha_vencimiento))

        return [Producto]


class MapadeadorEventosUnificacionPedidos(Mapeador):
    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            UnificacionPedidosCreada: self._entidad_a_unificacion_pedidos_creada,
            UnificacionPedidosCancelada: self._entidad_a_orden_cancelada,
        }

    def obtener_tipo(self) -> type:
        return EventoOrden.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_unificacion_pedidos_creada(self, entidad: UnificacionPedidosCreada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import UnificacionPedidosCreadaPayload, EventoUnificacionPedidosCreada

            print('en los mapeadores aguas'+entidad)

            payload = UnificacionPedidosCreadaPayload(
			 id = str(evento.id_pedido),
        	 direccion_recogida = evento.direccion_recogida, 
			 direccion_entrega = evento.direccion_entrega, 
			 fecha_recogida = evento.fecha_recogida, 
			 fecha_entrega = evento.fecha_entrega, 
			 estado = evento.estado
			)
            evento_integracion = EventoUnificacionPedidosCreada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'UnificacionPedidosCreada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'aeroalpes'
            evento_integracion.data = payload

            return evento_integracion

        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)

    def _entidad_a_orden_creada(self, entidad: UnificacionPedidosCreada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError

    def _entidad_a_orden_cancelada(self, entidad: UnificacionPedidosCancelada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError


    def entidad_a_dto(self, entidad: EventoUnificacionPedidos, version=LATEST_VERSION) -> UnificacionPedidosDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    def dto_a_entidad(self, dto: UnificacionPedidosDTO, version=LATEST_VERSION) -> UnificacionPedidos:
        raise NotImplementedError
