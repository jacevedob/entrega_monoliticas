import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime
import os
from dotenv import load_dotenv
from pulsar import ConsumerType

from entregasalpes.modulos.ordenes.infraestructura.schema.v1.eventos import EventoOrdenCreada
from entregasalpes.modulos.ordenes.infraestructura.schema.v1.comandos import ComandoCrearOrden


from entregasalpes.seedwork.infraestructura.proyecciones import ejecutar_proyeccion
from entregasalpes.modulos.ordenes.infraestructura.ejecutadores import compensacion_orden
from entregasalpes.seedwork.infraestructura import utils

def suscribirse_a_eventos(app=None):
    print('- - -- - - -  suscribirse_a_eventos                         ----- >')
    cliente = None
    try:

        load_dotenv()
        token = os.getenv('PULSAR_TOKEN')
        service_url = os.getenv('PULSAR_URL') 
        pulsar_consumer = os.getenv('PULSAR_PROD_ORDENES') 
        client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
        consumer = client.subscribe(pulsar_consumer, 'orden-subscription-consumer', ConsumerType.Shared)
        while True:
            msg = consumer.receive()
            print("MENSAJE suscribirse_a_eventos ",msg.data())
            #topic = (str(msg.data())[2:-1])

            #if topic == "insertar":
            #    insert.insert_db()
            #    productor.send_topic('enviar_recogida')
            consumer.acknowledge(msg)

        client.close()


        #cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        #consumidor = cliente.subscribe('eventos-ordenes', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='entregasalpes-sub-eventos', schema=AvroSchema(EventoOrdenCreada))
#
        #while True:
        #    mensaje = consumidor.receive()
        #    datos = mensaje.value().data
        #    print(f'Evento recibido: {datos}')
#
        #    # TODO Identificar el tipo de CRUD del evento: Creacion, actualización o eliminación.
        #    #ejecutar_proyeccion(ProyeccionReservasTotales(datos.fecha_creacion, ProyeccionReservasTotales.ADD), app=app)
        #    #ejecutar_proyeccion(ProyeccionReservasLista(datos.id_reserva, datos.id_cliente, datos.estado, datos.fecha_creacion, datos.fecha_creacion), app=app)
        #    
        #    consumidor.acknowledge(mensaje)     
#
        #cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_eventoscompensador(app=None):
    print('- - -- - - -  suscribirse_a_eventos compensacion_orden                         ----- >')
    cliente = None
    try:

        load_dotenv()
        token = os.getenv('PULSAR_TOKEN')
        service_url = os.getenv('PULSAR_URL') 
        pulsar_consumer = os.getenv('PULSAR_COMPENSACION') 
        client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
        consumer = client.subscribe(pulsar_consumer, 'orden-subscription-consumer', ConsumerType.Shared)
        while True:
            msg = consumer.receive()
            print("MENSAJE susc ribirse_a_eventos compensador ",msg.data())
            print("MENSAJE susc VALUES  compensador ",msg.value())
            compensacion_orden(msg.data())
            #topic = (str(msg.data())[2:-1])

            #if topic == "insertar":
            #    insert.insert_db()
            #    productor.send_topic('enviar_recogida')
            consumer.acknowledge(msg)

        client.close()


        #cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        #consumidor = cliente.subscribe('eventos-ordenes', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='entregasalpes-sub-eventos', schema=AvroSchema(EventoOrdenCreada))
#
        #while True:
        #    mensaje = consumidor.receive()
        #    datos = mensaje.value().data
        #    print(f'Evento recibido: {datos}')
#
        #    # TODO Identificar el tipo de CRUD del evento: Creacion, actualización o eliminación.
        #    #ejecutar_proyeccion(ProyeccionReservasTotales(datos.fecha_creacion, ProyeccionReservasTotales.ADD), app=app)
        #    #ejecutar_proyeccion(ProyeccionReservasLista(datos.id_reserva, datos.id_cliente, datos.estado, datos.fecha_creacion, datos.fecha_creacion), app=app)
        #    
        #    consumidor.acknowledge(mensaje)     
#
        #cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos(app=None):
    print('- - -- - - -  suscribirse_a_comandos                         ----- >')

    cliente = None

    try:
        load_dotenv()
        token = os.getenv('PULSAR_TOKEN')
        service_url = os.getenv('PULSAR_URL') 
        pulsar_consumer = os.getenv('PULSAR_PROD_ORDENES') 
        client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
        consumer = client.subscribe(pulsar_consumer, 'ordenes-subscription-consumer',ConsumerType.Shared)
        while True:
            msg = consumer.receive()
            print("MENSAJE suscribirse_a_comandos ",msg.data())
            #topic = (str(msg.data())[2:-1])

            #if topic == "insertar":
            #    insert.insert_db()
            #    productor.send_topic('enviar_recogida')
            consumer.acknowledge(msg)

        client.close()

    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if client:
            client.close()
   #try:
   #    cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
   #    consumidor = cliente.subscribe('comandos-orden', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='entregasalpes-sub-comandos', schema=AvroSchema(ComandoCrearOrden))

   #    while True:
   #        mensaje = consumidor.receive()
   #        print(f'Comando recibido: {mensaje.value().data}')

   #        consumidor.acknowledge(mensaje)     
   #        
   #    cliente.close()
   #except:
   #    logging.error('ERROR: Suscribiendose al tópico de comandos!')
   #    traceback.print_exc()
   #    if cliente:
   #        cliente.close()