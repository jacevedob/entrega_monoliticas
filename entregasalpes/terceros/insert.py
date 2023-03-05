import mysql.connector
import os
import sidecar
from dotenv import load_dotenv

load_dotenv()
hostname = os.getenv('BODEGAS_ADDRESS')
user = os.getenv('USER_DB')
password = os.getenv('PASSWORD_DB')
database = os.getenv('DATABASE')

def insert_db():
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

  datos = sidecar.bodegas()
  mycursor = mydb.cursor()
  sql = "INSERT INTO hoja_ruta (producto, cantidad, bodega_centro, id_orden, id_bodega ) VALUES (%s, %s, %s, %s, %s)"
  #val = (datos['nombre'], datos['cantidad'], datos['descripcion'], datos['id_orden'])
  val = (datos[0], datos[1], datos[2], datos[3], datos[4])
  print(val)
  mycursor.execute(sql, val)
  mydb.commit()

  print(mycursor.rowcount, "registro insertado")