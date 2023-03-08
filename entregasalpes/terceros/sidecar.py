import requests
import json
import random

def bodegas():

    bodega = random.randrange(1, 4, 1)

    if bodega == 1:
      r = requests.get('https://97d4ae2f-6ee2-456e-8967-17dca9f75ba2.mock.pstmn.io/bodega1')
      posts = r.json()
      datos = json.loads(json.dumps(posts))
      datos_retorno = [datos['nombre'], datos['cantidad'], datos['descripcion'], datos['id_orden'], '1']
      print(datos_retorno)
      return datos_retorno
    
    elif bodega == 2:
      r = requests.get('https://97d4ae2f-6ee2-456e-8967-17dca9f75ba2.mock.pstmn.io/bodega2')
      posts = r.json()
      datos = json.loads(json.dumps(posts))
      datos_retorno = [datos['producto'], datos['disponibilidad'], datos['detalle'], datos['id_orden'], '2'] 
      print(datos_retorno)
      return datos_retorno

    elif bodega == 3:
      r = requests.get('https://97d4ae2f-6ee2-456e-8967-17dca9f75ba2.mock.pstmn.io/bodega3')
      posts = r.json()
      datos = json.loads(json.dumps(posts))
      datos_retorno = [datos['nombre_producto'], datos['cantidad_productos'], datos['descripcion_producto'], datos['id_orden'], '3'] 
      print(datos_retorno)
      return datos_retorno
