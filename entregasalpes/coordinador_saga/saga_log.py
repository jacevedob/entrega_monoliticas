import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
hostname = os.getenv('SAGA_ADDRESS', 'mysqldb_saga')
user = os.getenv('USER_DB')
password = os.getenv('PASSWORD_DB')
database = os.getenv('DATABASE')

def insert_db(source, status, id):
  try:
    mydb = mysql.connector.connect(
      host = 'mysqldb_saga',
      user = user,
      password = password,
      database = 'saga',
      port=3309
    )
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
  mycursor = mydb.cursor()
  sql = "INSERT INTO saga (source, status, id ) VALUES (%s, %s, %s)"
  val = (source, status, id)
  print(val)
  mycursor.execute(sql, val)
  mydb.commit()

  print(mycursor.rowcount, "registro insertado")