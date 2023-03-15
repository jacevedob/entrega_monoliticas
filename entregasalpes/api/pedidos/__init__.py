import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))


def importar_modelos_alchemy():
    import entregasalpes.modulos.unificacion_pedidos.infraestructura.dto

def registrar_handlers():
    import entregasalpes.modulos.unificacion_pedidos.aplicacion

def comenzar_consumidor(app):
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener 
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """

    import threading
    #import entregasalpes.modulos.ordenes.infraestructura.consumidores as ordenes    
    import entregasalpes.modulos.unificacion_pedidos.infraestructura.consumidores as pedidos

    # Suscripción a eventos
    # threading.Thread(target=ordenes.suscribirse_a_eventos, args=[app]).start()


    # Suscripción a eventos
    threading.Thread(target=pedidos.suscribirse_a_eventos, args=[app]).start()

    # Suscripción a comandos
    # threading.Thread(target=ordenes.suscribirse_a_comandos, args=[app]).start()



def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = 'TESTING' #configuracion.get('TESTING')

     # Inicializa la DB
    from entregasalpes.config.db import init_db, database_connection_pedidos

    app.config['SQLALCHEMY_DATABASE_URI'] = database_connection_pedidos(configuracion, basedir=basedir)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    init_db(app)

     # Inicializa la DB
    from entregasalpes.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    comenzar_consumidor(app)

    with app.app_context():
        db.create_all()
        #comenzar_consumidor(app)
        #if not app.config.get('TESTING'):
        #    comenzar_consumidor(app)

     # Importa Blueprints
    #from . import ordenes

    # Registro de Blueprints
    #app.register_blueprint(ordenes.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)


    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
