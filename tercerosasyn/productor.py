
def publicarPedido(msg, topic):
    load_dotenv()
    token = os.getenv('PULSAR_TOKEN')
    service_url = os.getenv('PULSAR_URL') 
    producer_pulsar = topic 
    try:
        client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
        producer = client.create_producer(producer_pulsar)
        producer.send((msg).encode('utf-8'))
        client.close()
    except Exception as e:
        print("Error , ", e)

def publicarSaga(msg, topic):
    load_dotenv()
    token = os.getenv('PULSAR_TOKEN')
    service_url = os.getenv('PULSAR_URL') 
    producer_pulsar = topic 
    try:
        client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
        producer = client.create_producer(producer_pulsar)
        producer.send((msg).encode('utf-8'))
        client.close()
    except Exception as e:
        print("Error , ", e)        