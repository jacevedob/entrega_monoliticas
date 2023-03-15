import pulsar
import os
from dotenv import load_dotenv
from pulsar import ConsumerType

def send_topic(topic):
    load_dotenv()
    token = os.getenv('PULSAR_TOKEN')
    service_url = os.getenv('PULSAR_URL') 
    producer_pulsar = os.getenv('PULSAR_PRODUCER_TERCEROS') 
    client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
    producer = client.create_producer(producer_pulsar, ConsumerType.Shared)
    producer.send((topic).encode('utf-8'))
    print('Mensaje de compensación enviado')
    client.close()