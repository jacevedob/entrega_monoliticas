import pulsar
from pulsar import ConsumerType
import insert
import productor
import os
from dotenv import load_dotenv
import ruta
from pulsar import ConsumerType

load_dotenv()
token = os.getenv('PULSAR_TOKEN')
service_url = os.getenv('PULSAR_URL') 
topic_consumer = os.getenv('PULSAR_CONSUMER_TERCEROS')
topic_producer = os.getenv('PULSAR_PRODUCER_TERCEROS') 
client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
consumer = client.subscribe(topic_consumer, 'terceros-subscription-consumer', ConsumerType.Shared )

while True:
    msg_receive = consumer.receive()
    mensaje = str(msg_receive.data())
    insert.insert_db()
    msg_transmission = ruta.enviarRuta(mensaje)
    productor.send_topic(msg_transmission, topic_producer )
    consumer.acknowledge(msg_receive)

client.close()


