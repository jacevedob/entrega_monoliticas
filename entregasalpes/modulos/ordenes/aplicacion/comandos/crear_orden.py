from entregasalpes.seedwork.aplicacion.comandos import Comando
from entregasalpes.modulos.ordenes.aplicacion.dto import ProductoDTO, OrdenDTO
from .base import CrearOrdenBaseHandler
from dataclasses import dataclass, field
from entregasalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from entregasalpes.modulos.ordenes.dominio.entidades import Orden
from entregasalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from entregasalpes.modulos.ordenes.aplicacion.mapeadores import MapeadorOrden
from entregasalpes.modulos.ordenes.infraestructura.repositorios import RepositorioOrdenes, RepositorioEventosOrdenes
import os
from dotenv import load_dotenv
import pulsar

@dataclass
class CrearOrden(Comando):
    fecha_creacion: str
    id_cliente: str
    id: str
    productos: list[ProductoDTO]


class CrearOrdenHandler(CrearOrdenBaseHandler):
    
    def handle(self, comando: CrearOrden):
        print('               handle                     - > ')
    
        orden_dto = OrdenDTO(
                id_cliente=comando.id_cliente
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   productos=comando.productos)

    fecha_creacion: str = field(default_factory=str)
    id_cliente: str = field(default_factory=str)
    id: str = field(default_factory=str)
    productos: list[ProductoDTO] = field(default_factory=list)

    load_dotenv()
    token = os.getenv('PULSAR_TOKEN')
    service_url = os.getenv('PULSAR_URL') 
    producer_pulsar = os.getenv('PULSAR_PROD_ORDENES') 

    client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
    producer = client.create_producer(producer_pulsar)
    producer.send((topic).encode('utf-8'))
    client.close() 
    #send_topic(orden_dto)

    #orden: Orden = self.fabrica_compras.crear_objeto(orden_dto, MapeadorOrden())
    #orden.crear_orden(orden)

    #repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrdenes)
    #repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosOrdenes)

    #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, orden, repositorio_eventos_func=repositorio_eventos.agregar)
    #UnidadTrabajoPuerto.commit()

    def send_topic(topic):
        load_dotenv()
        token = os.getenv('PULSAR_TOKEN')
        token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzgwNDk5MTIsImlzcyI6ImRhdGFzdGF4Iiwic3ViIjoiY2xpZW50O2RjNTk2NmQxLTgxMWUtNDhjNi1hYTlkLThmYzdjNzI1ZjYyZTtaWGh3WlhKcGJXVnVkRzl6TFcxdmJtOXNhWFJwWTI5ejs4NDU5YzQ5NzQzIiwidG9rZW5pZCI6Ijg0NTljNDk3NDMifQ.GzqhGMWpPLANjAU6x3wF4cfgj_1ovQrGEy5O129LKs3N1Gc1GFSZXHaLhHCQyQaJ91VwGjM1XhEhudt8HlhcK5ony7RTjL7q2DcZwK8MaQkVeR0PksCcHxNP-z64GFn4d3TQabZrmYK48GWLDUNipcyGse1wvGngNobXZUGK6XM2z-0Cwf8I-ef-__AJLmnaNZr9N6uOCqyz6165PffQhSS_IsTlK57Q6I_eCU8TrQ9Pm9vPh0BWqqJqTON4MN54i_E-jr4hJ_7nJYj1fiSgW-vlvlBHXUWFE8JMAz75T-yIrOhD3L-X91nDMBD9xv3PMSgJj0DyOGJR50X5P5r9kw'
        service_url = os.getenv('PULSAR_URL') 
        service_url = 'pulsar+ssl://pulsar-aws-useast1.streaming.datastax.com:6651'
        producer_pulsar = os.getenv('PULSAR_PROD_ORDENES') 
        producer = client.create_producer('persistent://experimentos-monoliticos/monoliticas/ordenes')
        print('               ejecutar_comando_crear_reserva                                 - > ',producer_pulsar)
        client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
        producer = client.create_producer(producer_pulsar)
        producer.send((topic).encode('utf-8'))
        client.close() 


@comando.register(CrearOrden)
def ejecutar_comando_crear_reserva(comando: CrearOrden):
    
    handler = CrearOrdenHandler()
    handler.handle(comando)
    
   