import pulsar
from pulsar import ConsumerType
import insert
import productor
import os
from dotenv import load_dotenv
import ruta


load_dotenv()
token = os.getenv('PULSAR_TOKEN')
service_url = os.getenv('PULSAR_URL') 
pulsar_consumer = os.getenv('PULSAR_CONSUMER_TERCEROS') 
client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
consumer = client.subscribe(pulsar_consumer, 'test-subscription', ConsumerType.Shared )

while True:
    msg = consumer.receive()
    mensaje = str(msg.data())
    #topic = (str(msg.data())[2:-1])
    insert.insert_db()
    topic = ruta.enviarRuta(mensaje)
    productor.send_topic(topic)
    consumer.acknowledge(msg)

client.close()


