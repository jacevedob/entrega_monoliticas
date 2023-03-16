import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime
import os
import json
from dotenv import load_dotenv
from pulsar import ConsumerType
import ast

from entregasalpes.modulos.unificacion_pedidos.infraestructura.schema.v1.eventos import EventoUnificacionPedidosCreada
from entregasalpes.modulos.unificacion_pedidos.infraestructura.schema.v1.comandos import ComandoCrearUnificacionPedidos
from entregasalpes.modulos.unificacion_pedidos.infraestructura.ejecutadores import registra_unificacion_pedidos
from entregasalpes.modulos.unificacion_pedidos.aplicacion.dto import UnificacionPedidosDTO
from entregasalpes.modulos.unificacion_pedidos.aplicacion.dto import ProductoDTO


from entregasalpes.seedwork.infraestructura.proyecciones import ejecutar_proyeccion
from entregasalpes.seedwork.infraestructura import utils

def suscribirse_a_eventos(app=None):
    cliente = None
    try:

        load_dotenv()
        token = os.getenv('PULSAR_TOKEN')
        service_url = os.getenv('PULSAR_URL') 
        pulsar_consumer = os.getenv('PULSAR_CONSUMER_PEDIDOS') 
        client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
        consumidor = client.subscribe(pulsar_consumer, 'pedidos-subscription-consumer', ConsumerType.Shared)
        #cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        #consumidor = cliente.subscribe(pulsar_consumer,  'pedidos-subscription-consumer', consumer_type=_pulsar.ConsumerType.Shared)

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.data()
            print(f'Evento recibido Topico Pedidos: {datos}')
            eldato = str(datos)
            mensaje2 =  eldato[1:]
            
           
            #entrada = str('{"id":"53", "direccion_recogida":"882 AmberPinesLakeJulie MI37734" , "direccion_entrega":"ManuelStreamAptFL93980", "fecha_recogida":"1998-07-07" , "fecha_entrega":"2023-02-10" , "estado":"true", "productos": [{ "serial": "4455", "descripcion": "132", "precio": "15002", "fecha_vencimiento": "2023-12-2", "tipo_producto": "tipo" } , { "serial": "4450",	"descripcion": "132", "precio": "15002", "fecha_vencimiento": "2023-12-2", "tipo_producto": "tipo"}]}')
            entrada = str('{"id":"200", "direccion_recogida":"882 AmberPinesLakeJulie MI37734" , "direccion_entrega":"ManuelStreamAptFL93980", "fecha_recogida":"1998-07-07" , "fecha_entrega":"2023-02-10" , "estado":"true"}') 
            diccionario = json.loads(entrada)

            print('llego al externo_a_dto222222222222........................................',diccionario)
            unificacion_dto = externo_a_dto(diccionario)
            registra_unificacion_pedidos(unificacion_dto)
            consumidor.acknowledge(mensaje)
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def _procesar_producto(self, producto: dict) -> ProductoDTO:
        productos_dto: list[ProductoDTO] = list()

        produc_dto: ProductoDTO = ProductoDTO(producto.get('serial'), producto.get('descripcion'),
                                               producto.get('precio'),producto.get('fecha_vencimiento'),
                                              producto.get('tipo_producto'))

        productos_dto.append(produc_dto)

        return productos_dto

def externo_a_dto(externo: dict) -> UnificacionPedidosDTO:
        print('llego al mapeador.............................................')
        unificacion_pedidos_dto: UnificacionPedidosDTO = UnificacionPedidosDTO(externo.get('id'), externo.get('direccion_recogida'),
        externo.get('direccion_entrega'),externo.get('fecha_recogida'),
        externo.get('fecha_entrega'), externo.get('estado'))
        productos: list[ProductoDTO] = list()
        for producto in externo.get('productos', list()):
            unificacion_pedidos_dto.productos.append(_procesar_producto(producto))
        return unificacion_pedidos_dto

def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-pedidos', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='entregasalpes-sub-comandos', schema=AvroSchema(ComandoCrearUnificacionPedidos))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()