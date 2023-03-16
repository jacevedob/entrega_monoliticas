import logging
import traceback
import pulsar, _pulsar
import aiopulsar
import asyncio
from pulsar.schema import *
from . import utils

#async def suscribirse_a_topico(topico: str, suscripcion: str, schema: str, tipo_consumidor:_pulsar.ConsumerType=_pulsar.ConsumerType.Shared, eventos=[]):
async def suscribirse_a_topico(topico: str, suscripcion: str, tipo_consumidor:_pulsar.ConsumerType=_pulsar.ConsumerType.Shared, eventos=[]):
    token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2Nzc4OTAzODQsImlzcyI6ImRhdGFzdGF4Iiwic3ViIjoiY2xpZW50O2RjNTk2NmQxLTgxMWUtNDhjNi1hYTlkLThmYzdjNzI1ZjYyZTtaWGh3WlhKcGJXVnVkRzl6TFcxdmJtOXNhWFJwWTI5ejsxZmIzYWEzOGQ1IiwidG9rZW5pZCI6IjFmYjNhYTM4ZDUifQ.jtRQfeQxyDH1Bp84WSPmtsSpqnl0cZjl2nkigqzIMgy_H-qALSAd-Uci79aaeUhagQYIeuNf5z8WJ2OMoA-Xzk3x3JMw3eAOcnFeE6WEODqgtjHdhlScAgM2WBZYCYM3D9dJMTBxdHGYYmQ8stkk9qpv3z3K-2YySzI_xIUa6pn1Mt4htZ1bTPtPyXCWm6JjFHmgbnHgkgtD2PAW00mnBGjgMc6anJ_ac7qup44khF4bA5-spee-jC6SEqfJ-mQl7uwcVrBrcOh8FXI-KXff91tNsTYWp9jaTCuj1l8RCK6LAAtWKi5NwC33Y-xqjCgdi4PPD_QWy07PWSZr0iWEfA'

    try:
        #json_schema = utils.consultar_schema_registry(schema)  
        # avro_schema = utils.obtener_schema_avro_de_diccionario(json_schema)
        # async with aiopulsar.connect(f'pulsar://{utils.broker_host()}:6650') as cliente:
        async with aiopulsar.connect(f'pulsar+ssl://pulsar-aws-useast2.streaming.datastax.com:6651', authentication=pulsar.AuthenticationToken(token)) as cliente:
            async with cliente.subscribe(
                topico, 
                consumer_type=tipo_consumidor,
                subscription_name=suscripcion, 
                #schema=avro_schema
            ) as consumidor:
                while True:
                    mensaje = await consumidor.receive()
                    print(mensaje)
                    datos = mensaje.value()
                    print(f'Evento recibido: {datos}')
                    eventos.append(str(datos))
                    await consumidor.acknowledge(mensaje)    

    except Exception as e:
        print("Exepcion ", e)
        #logging.error(f'ERROR: Suscribiendose al tópico! {topico}, {suscripcion}, {schema}')
        logging.error(f'ERROR: Suscribiendose al tópico! {topico}, {suscripcion}')
        traceback.print_exc()