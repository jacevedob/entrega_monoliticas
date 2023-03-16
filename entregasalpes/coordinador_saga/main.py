import json

import pulsar
import saga_log
import productor
import os
from dotenv import load_dotenv
from pulsar import ConsumerType

load_dotenv()
token = os.getenv('PULSAR_TOKEN')
service_url = os.getenv('PULSAR_URL')
pulsar_consumer = os.getenv('PULSAR_CONSUMER_SAGA')
client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
consumer = client.subscribe(pulsar_consumer, 'terceros-subscription-consumer', ConsumerType.Shared )

while True:
    msg = consumer.receive()
    mensaje = msg.data()
    try:
        mensaje_decodificado = json.loads(mensaje)
        print(mensaje)
        saga_log.insert_db(mensaje_decodificado['source'], mensaje_decodificado['status'], mensaje_decodificado['id'])
        if (mensaje_decodificado['status'] == "error"):
            productor.send_topic('{"id":"' + mensaje_decodificado["id"] + '"}')
    except Exception as e:
        print("error parseando json")
    consumer.acknowledge(msg)


