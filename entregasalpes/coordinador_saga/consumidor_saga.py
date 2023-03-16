import pulsar
import os
from dotenv import load_dotenv
from pulsar import ConsumerType

load_dotenv()
token = os.getenv('PULSAR_TOKEN')
service_url = os.getenv('PULSAR_URL')
pulsar_consumer = os.getenv('PULSAR_CONSUMER_SAGA')
client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
consumer = client.subscribe(pulsar_consumer, 'saga-subscription-consumer', ConsumerType.Shared)

while True:
    mensaje = consumer.receive()
    datos = mensaje.data()
    print(f'Evento recibido SAGA: {datos}')
    consumer.acknowledge(mensaje)

