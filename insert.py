import mysql.connector
import requests
import json

def insert_db():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="adminadmin",
    database="terceros"
  )


  r = requests.get('https://97d4ae2f-6ee2-456e-8967-17dca9f75ba2.mock.pstmn.io/')
  posts = r.json()
  print(posts)

  datos = json.loads(json.dumps(posts))


  mycursor = mydb.cursor()

  sql = "INSERT INTO hoja_ruta (producto, cantidad, bodega_centro, id_orden ) VALUES (%s, %s, %s, %s)"
  val = (datos['nombre'], datos['cantidad'], datos['descripcion'], datos['id_orden'])
  mycursor.execute(sql, val)
  mydb.commit()

  print(mycursor.rowcount, "registro insertado")