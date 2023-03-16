import mysql.connector
import os
from dotenv import load_dotenv
from entregasalpes.modulos.unificacion_pedidos.dominio.entidades import UnificacionPedidos
from entregasalpes.modulos.unificacion_pedidos.aplicacion.dto import ProductoDTO, UnificacionPedidosDTO

load_dotenv()
hostname = os.getenv('DB_HOSTNAME', default="localhost")
user = os.getenv('USER_DB', default="localhost")
password = os.getenv('PASSWORD_DB')
database = os.getenv('DATABASE_PEDIDOS', default="pedidos")

def registra_unificacion_pedidos(unificacion_pedidos: UnificacionPedidosDTO):
  try:
    mydb = mysql.connector.connect(
      host = hostname,
      user = user,
      password = password,
      database = database,
      port=3308
    )
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
    return "error"

  print("------------------ingreso al metodo-------->",unificacion_pedidos.id, '',unificacion_pedidos.direccion_entrega, '',unificacion_pedidos.estado)
  try:
    mycursor = mydb.cursor()
    sql = "INSERT INTO unificacion_pedidos (id, direccion_recogida, direccion_entrega, fecha_recogida, fecha_entrega, estado ) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (unificacion_pedidos.id, unificacion_pedidos.direccion_recogida, unificacion_pedidos.direccion_entrega, unificacion_pedidos.fecha_recogida, unificacion_pedidos.fecha_entrega, unificacion_pedidos.estado )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "registro insertado unificacion_pedidos")

    print(mycursor.rowcount, "registro insertado")
    print("mis prod - - - - -", unificacion_pedidos.productos)
    respuesta = 'success'

  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
  respuesta = 'error'

  if respuesta != 'error':
    try:
      for producto in unificacion_pedidos.productos:
        print ('sxxxxxxxxxxxxxxxxxxxxxx Serial xxxxxxxxxxxxxx ', producto[0].serial)
        sql = "INSERT INTO productos (serial, descripcion, precio, fecha_vencimiento ) VALUES (%s, %s, %s, %s)"
        val = (str(producto[0].serial), str(producto[0].descripcion), int(producto[0].precio), str(producto[0].fecha_vencimiento) )
        mycursor.execute(sql, val)
        mydb.commit()
        respuesta = 'success'

    except mysql.connector.Error as err:
      print("Something went wrong: {}".format(err))
    respuesta = 'error'
    enviaSagas(self, unificacion_pedidos.id, respuesta)


def enviaSagas(self, id: str, status: str):
        print('Enviando a sagas ', id)
        data = '{"id":'+str(id)+', "status": "'+str(status)+'", "source":"pedidos"}'
        load_dotenv()
        token = os.getenv('PULSAR_TOKEN')
        service_url = os.getenv('PULSAR_URL') 
        producer_pulsar = os.getenv('PULSAR_CONSUMER_SAGA') 

        client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
        producer = client.create_producer(producer_pulsar)
        print('Enviando a sagas - - -- - >', data)
        
        producer.send((data).encode('utf-8'))
        client.close() 
