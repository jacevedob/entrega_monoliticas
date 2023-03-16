import entregasalpes.seedwork.presentacion.api as api
import json
from entregasalpes.modulos.ordenes.aplicacion.servicios import ServicioOrden
from entregasalpes.modulos.ordenes.aplicacion.dto import OrdenDTO
from entregasalpes.seedwork.dominio.excepciones import ExcepcionDominio
from entregasalpes.modulos.ordenes.aplicacion.comandos.crear_orden import CrearOrden

from flask import redirect, render_template, request, session, url_for
from flask import Response
from entregasalpes.modulos.ordenes.aplicacion.mapeadores import MapeadorOrdenDTOJson
from entregasalpes.seedwork.aplicacion.comandos import ejecutar_commando
from entregasalpes.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('compra', '/compra')

@bp.route('/ordenes', methods=('POST',))
def ordenar():
    try:
        print('ingreso')
        orden_dict = request.json

        map_orden = MapeadorOrdenDTOJson()
        orden_dto = map_orden.externo_a_dto(orden_dict)

        #sr = ServicioOrden()
        #print(orden_dto)
        #dto_final = sr.crear_orden(orden_dto)
        print (orden_dict.get('fecha_creacion'))

        comando = CrearOrden(orden_dict.get('fecha_creacion'), int(orden_dict.get('id_cliente')), int(orden_dict.get('id')), orden_dto.productos)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)




        return Response(json.dumps("Probando"), status=200, mimetype='application/json') #map_orden.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/orden', methods=('GET',))
@bp.route('/orden/<id>', methods=('GET',))
def dar_orden(id=None):
    if id:
        sr = ServicioOrden()
        
        return sr.obtener_orden_por_id(id)
    else:
        return [{'message': 'GET!'}]


@bp.route('/ordenQ', methods=('POST',))
def ordenar_usando_comando():
    try:
        # NOTE Asignamos el valor 'pulsar' para usar la Unidad de trabajo de Pulsar y
        # no la defecto de SQLAlchemy
        session['uow_metodo'] = 'pulsar'

        orden_dict = request.json

        map_orden = MapeadorOrdenDTOJson()
        reserva_dto = map_orden.externo_a_dto(orden_dict)

        comando = CrearOrden(reserva_dto.fecha_creacion, reserva_dto.fecha_actualizacion, reserva_dto.id,
                               reserva_dto.itinerarios)

        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
