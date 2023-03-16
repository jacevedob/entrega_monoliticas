from faker import Faker

fake = Faker()

def enviarRuta(mensaje, id):

    #id = "id=" + str(fake.random_int(0, 100))
    id = "id=" + str(id)
    direccion_recogida = "direccion_recogida=" + fake.address()
    direccion_entrega = "direccion_entrega=" + fake.address()
    fecha_recogida = "fecha_recogida=" + fake.date()
    fecha_entrega = "fecha_entrega=" + fake.date()
    estado = "estado=True"
    posIni = mensaje.find("productos=")
    productos = "productos="  + mensaje[posIni + 11: -3]

    cadena = "( " + str(id) + "," + direccion_recogida + " ," + direccion_entrega + " ,"
    cadena = cadena + fecha_recogida + " ," + fecha_entrega + " ," + estado + " ," + productos + ")"

    return cadena