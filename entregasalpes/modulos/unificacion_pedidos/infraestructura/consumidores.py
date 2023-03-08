import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime
import os
from dotenv import load_dotenv

from entregasalpes.modulos.unificacion_pedidos.infraestructura.schema.v1.eventos import EventoUnificacionPedidosCreada
from entregasalpes.modulos.unificacion_pedidos.infraestructura.schema.v1.comandos import ComandoCrearUnificacionPedidos


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
        consumidor = client.subscribe(pulsar_consumer, 'test-subscription')
        #cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-pedidos', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='entregasalpes-sub-eventos', schema=AvroSchema(EventoUnificacionPedidosCreada))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.data()
            print(f'Evento recibido: {datos}')

            # TODO Identificar el tipo de CRUD del evento: Creacion, actualización o eliminación.
            #ejecutar_proyeccion(ProyeccionReservasTotales(datos.fecha_creacion, ProyeccionReservasTotales.ADD), app=app)
            #ejecutar_proyeccion(ProyeccionReservasLista(datos.id_reserva, datos.id_cliente, datos.estado, datos.fecha_creacion, datos.fecha_creacion), app=app)
            
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

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