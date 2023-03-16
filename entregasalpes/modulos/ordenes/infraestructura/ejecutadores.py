import mysql.connector
import os
from dotenv import load_dotenv
from entregasalpes.modulos.ordenes.dominio.entidades import Orden
from entregasalpes.modulos.ordenes.aplicacion.dto import ProductoDTO, OrdenDTO
import json

load_dotenv()
hostname = os.getenv('DB_HOSTNAME', default="localhost")
user = os.getenv('USER_DB', default="localhost")
password = os.getenv('PASSWORD_DB')
database = os.getenv('DATABASE_ORDENES', default="ordenes")

def registra_orden(orden: OrdenDTO):
  try:
    mydb = mysql.connector.connect(
      host = hostname,
      user = user,
      password = password,
      database = database,
      port=3306
    )
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

  print("------------------------------------------------------->",orden.id, '',orden.id_cliente, '',orden.fecha_creacion);

  try:
    mycursor = mydb.cursor()
    sql = "INSERT INTO ordenes (id, id_cliente, fecha_creacion ) VALUES (%s, %s, %s)"
    val = (orden.id, orden.id_cliente, orden.fecha_creacion)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "registro insertado orden")
  except mysql.connector.Error as e:
    print("----------------------------------- >Error", e)
    return "error_o"

  print(mycursor.rowcount, "registro insertado")
  print("mis prod - - - - -", orden.productos)

  try:
    for producto in orden.productos:
      print ('sxxxxxxxxxxxxxxxxxxxxxx valuyes  xxxxxxxxxxxxxx ', producto[0].serial)
      sql = "INSERT INTO productos (serial, descripcion, precio, fecha_vencimiento ) VALUES (%s, %s, %s, %s)"
      val = (str(producto[0].serial), str(producto[0].descripcion), int(producto[0].precio), str(producto[0].fecha_vencimiento) )
      mycursor.execute(sql, val)
      mydb.commit()
    

    print(mycursor.rowcount, "registro insertado productos")
    return "success"
  except mysql.connector.Error as e:
    print("Error", e)
    return "error"

def compensacion_orden(dato):
  try:
    mydb = mysql.connector.connect(
      host = hostname,
      user = user,
      password = password,
      database = database,
      port=3306
    )
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
  valor = json.loads(dato)
  
  print("----------------------------valor------------------------->",valor);
  
  try:
    mycursor = mydb.cursor()
    sql = "DELETE from  ordenes WHERE id =  "+ str(valor['id'])
    val = ()
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "registro borrado")
    return "success"
  except mysql.connector.Error as e:
    print("----------------------------------- >Error", e)
    return "error"
#
#  print(mycursor.rowcount, "registro insertado")
#  print("mis prod - - - - -", orden.productos)
#
#  try:
#    for producto in orden.productos:
#      print ('sxxxxxxxxxxxxxxxxxxxxxx Serial xxxxxxxxxxxxxx ', producto[0].serial)
#      sql = "INSERT INTO productos (serial, descripcion, precio, fecha_vencimiento ) VALUES (%s, %s, %s, %s)"
#      val = (str(producto[0].serial), str(producto[0].descripcion), int(producto[0].precio), str(producto[0].fecha_vencimiento) )
#      mycursor.execute(sql, val)
#      mydb.commit()
#    
#
#    print(mycursor.rowcount, "registro insertado productos")
#    return "success"
#  except mysql.connector.Error as e:
#    print("Error", e)
#    return "error"
#