# Entrega #4
A continuación presentamos la entrega parcial o Entrega #4.

En esta entrega presentamos 3 microservicios con comunicación asincrona ( comandos y eventos) usando Apache Pulsar y usando un modelo clásico **CRUD**  para las bases de datos. 

El proposito de este es que los ingenieros puedan apreciar una prueba de concepto de la arquitectura solución para el proyecto Entrega Alpes, por medio de la validación de 3 escenarios de calidad para cada atributo de calidad en este caso ( Disponibilidad, Interoperabilidad, Escalabilidad).

### Disponibilidad

![image](https://user-images.githubusercontent.com/78766013/223620518-609538bb-f69f-479e-93ab-24d639a36716.png)


### Interoperabilidad

![image](https://user-images.githubusercontent.com/78766013/223620560-cb7b4ad2-63df-4cdb-b053-9592237532e3.png)


### Escalabilidad

![image](https://user-images.githubusercontent.com/78766013/223620584-817fb7d0-b346-4b26-bbac-4ac1f8bd2603.png)




Para lograr lo anterior, planteamos la siguiente arquitectura modelo para llevar a cabo el objetivo.

![image](https://user-images.githubusercontent.com/78766013/223618412-346bb8fc-3f1d-44b3-9525-28c5d604d73c.png)



Además seguimos los siguientes lineamientos. 
1. Para este ejercicio seguimos los principios de microservicios basados en eventos. Por tal motivo la comunicación entre los servicios **se realizó usando comandos y eventos **
2. Definimos los eventos de acuerdo a los escenarios de calidad a satisfacer en este caso usamos eventos de integración. Adicionalmente diseñamos el esquema en formato **Json** y usamos el sistema de versionamiento que nos provee el broker de pulsar en su estrategía **Full compatibilty ** ,


## Intrucciones de ejecución del proyecto
1. Clonar repositorio
2. Agregar al repositorio el archivo .env, enviado al canal de slack y al correo del tutor.

3. Iniciar las bases de datos

![image](https://user-images.githubusercontent.com/78766013/223617903-72ab9da0-765a-4c71-9175-e306e9f3893f.png)

4. Construcción de imagen del docker compose


![image](https://user-images.githubusercontent.com/78766013/223620785-f57d7f75-961b-4c85-838a-fc06ed59b732.png)


5. Iniciar servicios 


![image](https://user-images.githubusercontent.com/78766013/223620743-496fb964-7832-4224-a264-4dd79b9022de.png)


6. Enviar mensaje para inicio del flujo


![image](https://user-images.githubusercontent.com/78766013/223618174-95d220dc-e5f1-4ac0-8671-a68b7dab5ee2.png)



## Enlace video entrega parcial

## Descripción de actividades por integrante
A continuación se describe por integrante el aporte individual y como contribuyó al equipo.

### Cesar Chembi
- Construcción del microservicio de "Servicio de Recogida"
- Construcción lógica de hoja de ruta
- Construcción de peristencia para el servicio de Recogida
- Construcción de server mock para la simulación de respuesta de los centros de distribución externos.

### Giovani Briceño
- Construcción microservicios Ordenes.
- Adaptación lógica de consumo y producción de mensajes al broker.
- Refactor y adaptación de código de tutoriales para proyecto.
- Construcción de REST API, para la invocación de llamados al servicio de ordenes y traducción a eventos a esquema EDA. 
- Construcción de persistencia para el servicio de ordenes.

### Albeiro Cuadrado
- Diseño de arquitectura de experimentación.
- Configuración y manejo del broker apache pulsar
- Configuración de georeplicación en el broker para favorecer atributo de Disponibilidad
- Configuración y definición del particionamiento para favorecer atributo de Escalabilidad
- Definición de esquemas y evolución de mensajes.
- Apoyo al equipo en códificación de microservicios en python.

### Juan Camilo Acevedo
- Construcción del microservicio  de almacenamientos a terceros
- Construcción de SideCar Adaptador para centros de distribución externos para favorecer atributo Interoperabilidad.
- Construcción lógica de creación de hoja de rutas.
- Construcción base de datos de microservicio de almacenamiento terceros.
- Gestión de subscripciones del broker.

## Comandos útiles

### Listar contenedoras en ejecución
```bash
docker ps
```

### Listar todas las contenedoras
```bash
docker ps -a
```

### Parar contenedora
```bash
docker stop <id_contenedora>
```

### Eliminar contenedora
```bash
docker rm <id_contenedora>
```

### Listar imágenes
```bash
docker images
```

### Eliminar imágenes
```bash
docker images rm <id_imagen>
```

### Acceder a una contendora
```bash
docker exec -it <id_contenedora> sh
```

### Kill proceso que esta usando un puerto
```bash
fuser -k <puerto>/tcp
```

### Correr docker-compose usando profiles
```bash
docker-compose --profile <pulsar|aeroalpes|ui|notificacion> up
```
