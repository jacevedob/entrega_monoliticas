import pulsar
from pulsar import ConsumerType
import insert
import productor_01
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('PULSAR_TOKEN')
service_url = os.getenv('PULSAR_URL') 
pulsar_consumer = os.getenv('PULSAR_CONSUMER_TERCEROS') 
client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
consumer = client.subscribe(pulsar_consumer, 'test-subscription', ConsumerType.Shared )

while True:
    msg = consumer.receive()
    print(msg.data())
    insert.insert_db()
    productor.send_topic('enviar_recogida')
    consumer.acknowledge(msg)

client.close()