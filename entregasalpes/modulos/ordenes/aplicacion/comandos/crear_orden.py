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
import json

@dataclass
class CrearOrden(Comando):
    fecha_creacion: str
    id_cliente: str
    id: str
    productos: list[ProductoDTO]


class CrearOrdenHandler(CrearOrdenBaseHandler):
    
    def handle(self, comando: CrearOrden):
        
    
        orden_dto = OrdenDTO(
                id_cliente=comando.id_cliente
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   productos=comando.productos)

        fecha_creacion: str = field(default_factory=str)
        id_cliente: str = field(default_factory=str)
        id: str = field(default_factory=str)
        productos: list[ProductoDTO] = field(default_factory=list)
        orden: Orden = self.fabrica_compras.crear_objeto(orden_dto, MapeadorOrden())
        print('               handle                     - - - - - -  - - - -   - > ')
        load_dotenv()
        token = os.getenv('PULSAR_TOKEN')
        service_url = os.getenv('PULSAR_URL') 
        producer_pulsar = os.getenv('PULSAR_PROD_ORDENES') 

        client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
        producer = client.create_producer(producer_pulsar)
        
        producer.send((str(orden)).encode('utf-8'))
        client.close() 
        #send_topic(orden_dto)

    #orden: Orden = self.fabrica_compras.crear_objeto(orden_dto, MapeadorOrden())
    #orden.crear_orden(orden)

    #repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrdenes)
    #repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosOrdenes)

    #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, orden, repositorio_eventos_func=repositorio_eventos.agregar)
    #UnidadTrabajoPuerto.commit()



@comando.register(CrearOrden)
def ejecutar_comando_crear_reserva(comando: CrearOrden):
    
    handler = CrearOrdenHandler()
    handler.handle(comando)
    
   