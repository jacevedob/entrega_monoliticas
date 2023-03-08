""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""
import datetime
from entregasalpes.seedwork.infraestructura.utils import unix_time_millis
from entregasalpes.modulos.ordenes.dominio.eventos import OrdenCreada, OrdenCancelada, EventoOrden


from entregasalpes.seedwork.dominio.repositorios  import Mapeador
from entregasalpes.modulos.ordenes.dominio.objetos_valor  import Producto
from entregasalpes.modulos.ordenes.dominio.entidades import Orden
from .dto import Orden as OrdenDTO
from .dto import Producto as ProductoDTO
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion


class MapeadorOrden(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Orden.__class__

    def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
        
        orden_dto = OrdenDTO()
        orden_dto.fecha_creacion = "21/2/2021" #entidad.fecha_creacion
        orden_dto.id_cliente = "1" #entidad.id_cliente
        orden_dto.id = str(entidad.id)

        productos_dto = list()
        print("                                       lista -------> ", productos_dto)
        for producto in entidad.productos:
            print(" sssssssss                           uno --------------------------> ", producto.serial)
            producto_dto = ProductoDTO()
            producto_dto.serial = producto[0].serial
            producto_dto.precio = producto[0].precio
            producto_dto.fecha_vencimiento= producto[0].fecha_vencimiento
            producto_dto.descripcion = producto[0].descripcion
            productos_dto.append(producto_dto)

        orden_dto.productos = productos_dto

        return orden_dto

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        orden = Orden(dto.id, dto.id_cliente, dto.fecha_creacion)
        orden.productos = list()

        productos_dto: list[ProductoDTO] = dto.productos

        for product in productos_dto:
            print(' Procesa producto dto                 ---dto_a_entidad - -                     ->', product[0])
            serial = product[0].serial
            tipo_producto = 'product.tipo_producto'
            precio = product[0].precio
            descripcion = product[0].descripcion
            fecha_vencimiento = product[0].fecha_vencimiento
            orden.productos.append(Producto(serial, descripcion, precio, fecha_vencimiento))
        

        return orden

    def _procesar_producto_dto(self, productos_dto: list) -> list[Producto]:
        prod_dict = dict()
        print(' Procesa producto dto     longitud            --- - -                     ->', len(productos_dto))

        for product in productos_dto:
            print(' Procesa producto dto                 --- - -                     ->', product)
            serial = product.serial
            tipo_producto = 'product.tipo_producto'
            precio = product.precio
            descripcion = product.descripcion
            fecha_vencimiento = product.fecha_vencimiento
            prod_dict.setdefault( Producto(serial, descripcion, precio, fecha_vencimiento))
            print(' Procesa producto dto     longitud            --- - -                     ->',prod_dict)

        return [Producto]


class MapadeadorEventosOrden(Mapeador):
    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            OrdenCreada: self._entidad_a_orden_creada,
            OrdenCancelada: self._entidad_a_orden_cancelada,
        }

    def obtener_tipo(self) -> type:
        return EventoOrden.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_reserva_creada(self, entidad: OrdenCreada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import OrdenCreadaPayload, EventoOrdenCreada

            payload = OrdenCreadaPayload(
                id_reserva=str(evento.id_reserva),
                id_cliente=str(evento.id_cliente),
                estado=str(evento.estado),
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
            )
            evento_integracion = EventoOrdenCreada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'ReservaCreada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'aeroalpes'
            evento_integracion.data = payload

            return evento_integracion

        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)

    def _entidad_a_orden_creada(self, entidad: OrdenCreada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError

    def _entidad_a_orden_cancelada(self, entidad: OrdenCancelada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError


    def entidad_a_dto(self, entidad: EventoOrden, version=LATEST_VERSION) -> OrdenDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    def dto_a_entidad(self, dto: OrdenDTO, version=LATEST_VERSION) -> Orden:
        raise NotImplementedError
