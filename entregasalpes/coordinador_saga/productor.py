import json

import pulsar
import os
from dotenv import load_dotenv
from pulsar import ConsumerType

def send_topic(message):
    load_dotenv()
    token = os.getenv('PULSAR_TOKEN')
    service_url = os.getenv('PULSAR_URL')
    producer_pulsar = os.getenv('PULSAR_COMPENSACION')
    client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
    producer = client.create_producer(producer_pulsar, 'producer-saga')
    producer.send(message.encode('utf-8'))
    client.close()