import pulsar
from pulsar.schema import *


class Despachador:
    def __init__(self):
        ...

    async def publicar_mensaje(self, mensaje, topico, schema):
        json_schema = utils.consultar_schema_registry(schema)  
        avro_schema = utils.obtener_schema_avro_de_diccionario(json_schema)

        #cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        cliente = pulsar.Client(f'pulsar+ssl://pulsar-aws-useast2.streaming.datastax.com:6651')
        publicador = cliente.create_producer(topico, schema=avro_schema)
        publicador.send(mensaje)
        cliente.close()


    async def publicarPedido(self, mensaje, topico):
            load_dotenv()
            token = os.getenv('PULSAR_TOKEN')
            url = os.getenv('PULSAR_URL') 
            cliente = pulsar.Client(url, authentication=pulsar.AuthenticationToken(token))
            publicador = cliente.create_producer(topico)
            publicador.send((mensaje).encode('utf-8'))
            print("Mensaje publicado ", mensaje)
            cliente.close()

    async def publicarSaga(self, mensaje, topico, schema):
            json_schema = utils.consultar_schema_registry(schema)  
            avro_schema = utils.obtener_schema_avro_de_diccionario(json_schema)

            #cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
            cliente = pulsar.Client(f'pulsar+ssl://pulsar-aws-useast2.streaming.datastax.com:6651')
            publicador = cliente.create_producer(topico, schema=avro_schema)
            publicador.send(mensaje)
            cliente.close()