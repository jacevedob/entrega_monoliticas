import logging
import traceback
import pulsar, _pulsar
import aiopulsar
import asyncio
from pulsar.schema import *
from . import ruta
from . import basedatos
from . import productor
from .despachadores import Despachador

# Suscribirse al topico Ordenes para ser consumido por los terceros
async def suscribirseOrdenes(topico: str, suscripcion: str, url: str, token: str):

    tipo_consumidor:_pulsar.ConsumerType=_pulsar.ConsumerType.Shared
    despachador = Despachador()
    try:
        async with aiopulsar.connect(url, authentication=pulsar.AuthenticationToken(token)) as cliente:
            async with cliente.subscribe(
                topico, 
                consumer_type=tipo_consumidor,
                subscription_name=suscripcion, 
            ) as consumidor:
                while True:
                    msg_receive = await consumidor.receive()
                    mensaje = str(msg_receive.data())
                    print(f'Evento recibido ordenes: {mensaje}')

                    posIni = mensaje.find("id=")
                    posFin = mensaje[posIni:].find(",")
                    id = mensaje[posIni+3: posIni+posFin]
                    print("Id orden ", id)

                    basedatos.insert_db(id)
                    
                    msg_transmission = ruta.enviarRuta(mensaje, id)
                    print(f'La orden de ruta: {msg_transmission}')
                    productor.publicarPedido(msg_transmission, 'persistent://experimentos-monoliticos/monoliticas/eventos-pedidos' )
                 
                    msg_saga = '{"source": "Terceros", "status": "success", "id":"' + str(id) +  '"}'
                    productor.publicarSaga(msg_saga,'persistent://experimentos-monoliticos/monoliticas/saga')
                    

                    await consumidor.acknowledge(msg_receive)    

    except Exception as e:
        print("Exepcion ", e)
        logging.error(f'ERROR: Suscribiendose al tópico! {topico}, {suscripcion}')
        traceback.print_exc()


async def suscribirseSagas(topico: str, suscripcion: str, url: str, token: str):

    tipo_consumidor:_pulsar.ConsumerType=_pulsar.ConsumerType.Shared
    
    try:
        async with aiopulsar.connect(url, authentication=pulsar.AuthenticationToken(token)) as cliente:
            async with cliente.subscribe(
                topico, 
                consumer_type=tipo_consumidor,
                subscription_name=suscripcion, 
            ) as consumidor:
                while True:
                    mensaje = await consumidor.receive()
                    datos = mensaje.value()
                    print(f'Evento recibido sagas: {datos}')
                    await consumidor.acknowledge(mensaje)    

    except Exception as e:
        print("Exepcion ", e)
        logging.error(f'ERROR: Suscribiendose al tópico! {topico}, {suscripcion}')
        traceback.print_exc()

async def suscribirsePedidos(topico: str, suscripcion: str, url: str, token: str):

    tipo_consumidor:_pulsar.ConsumerType=_pulsar.ConsumerType.Shared
    
    try:
        async with aiopulsar.connect(url, authentication=pulsar.AuthenticationToken(token)) as cliente:
            async with cliente.subscribe(
                topico, 
                consumer_type=tipo_consumidor,
                subscription_name=suscripcion, 
            ) as consumidor:
                while True:
                    mensaje = await consumidor.receive()
                    datos = mensaje.value()
                    print(f'Evento recibido pedidos: {datos}')
                    await consumidor.acknowledge(mensaje)    

    except Exception as e:
        print("Exepcion ", e)
        logging.error(f'ERROR: Suscribiendose al tópico! {topico}, {suscripcion}')
        traceback.print_exc()

async def suscribirseCompensacion(topico: str, suscripcion: str, url: str, token: str):

    tipo_consumidor:_pulsar.ConsumerType=_pulsar.ConsumerType.Shared
    
    try:
        async with aiopulsar.connect(url, authentication=pulsar.AuthenticationToken(token)) as cliente:
            async with cliente.subscribe(
                topico, 
                consumer_type=tipo_consumidor,
                subscription_name=suscripcion, 
            ) as consumidor:
                while True:
                    mensaje = await consumidor.receive()
                    datos = mensaje.value()
                    print(f'Evento recibido compensación: {datos}')
                    id = str(datos)[9:-3]
                    print("El id para compesar ", str(id))
                    basedatos.delete_db(id)
                    await consumidor.acknowledge(mensaje)    

    except Exception as e:
        print("Exepcion ", e)
        logging.error(f'ERROR: Suscribiendose al tópico! {topico}, {suscripcion}')
        traceback.print_exc()