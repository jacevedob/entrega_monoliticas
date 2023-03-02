# Importa la librería de Apache Pulsar para Python
from pulsar import Client

# Crea una conexión al broker
client = Client('pulsar://localhost:6650')

# Crea un productor que envía mensajes a un topic
producer = client.create_producer('my-topic')

# Envía un mensaje al topic
producer.send('Hola Mundo')

# Crea un consumidor que recibe los mensajes del topic
consumer = client.subscribe('my-topic')

# Recibe un mensaje del topic
message = consumer.receive()

# Muestra el mensaje
print(message.data())

# ACK del mensaje
consumer.acknowledge(message)

# Cierra el productor y el consumidor
producer.close()
consumer.close()