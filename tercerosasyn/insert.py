import mysql.connector
import os
from . import sidecar
from dotenv import load_dotenv

load_dotenv()
#hostname = os.getenv('BODEGAS_ADDRESS')
hostname = 'localhost'
user = os.getenv('USER_DB')
password = os.getenv('PASSWORD_DB')
database = os.getenv('DATABASE')

def insert_db(id_orden):
  try:
    mydb = mysql.connector.connect(
      host = hostname,
      user = user,
      password = password,
      database = database,
      port=3307
    )
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

  datos = sidecar.bodegas()
  mycursor = mydb.cursor()
  sql = "INSERT INTO hoja_ruta (producto, cantidad, bodega_centro, id_orden, id_bodega ) VALUES (%s, %s, %s, %s, %s)"
  val = (datos[0], datos[1], datos[2], id_orden, datos[4])
  print(val)
  mycursor.execute(sql, val)
  mydb.commit()

  print(mycursor.rowcount, "registro insertado")