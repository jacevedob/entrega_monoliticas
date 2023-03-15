from entregasalpes.config.db import db

Base = db.declarative_base()

unificacion_pedidos_productos = db.Table(
    "unificacion_pedidos_productos",
    db.Model.metadata,
    db.Column("unificacion_pedidos_id", db.Integer, db.ForeignKey("unificacion_pedidos.id")),
    db.Column("serial", db.String(10)),
    db.Column("descripcion", db.String(50)),
    db.Column("precio", db.Integer),
    db.ForeignKeyConstraint( [ "serial", "descripcion", "precio"], ["productos.serial", "productos.descripcion", "productos.precio"] )
)
class Producto(db.Model):
    __tablename__ = "productos"
    serial = db.Column(db.String(10), nullable=False,primary_key=True)
    descripcion = db.Column(db.String(100),  nullable=False, primary_key=True)
    precio = db.Column(db.Integer, nullable=False, primary_key=True)
    fecha_vencimiento = db.Column(db.String(10), nullable=False, primary_key=True)

class UnificacionPedidos(db.Model):
    __tablename__ = "unificacion_pedidos"
    id = db.Column(db.Integer, primary_key=True)
    direccion_recogida = db.Column(db.String(100), nullable=False)
    direccion_entrega = db.Column(db.String(100), nullable=False)
    fecha_recogida = db.Column(db.String(10), nullable=False)
    fecha_entrega = db.Column(db.String(10), nullable=False)
    estado = db.Column(db.String(20), nullable=False)
    productos = db.relationship('Producto', secondary=unificacion_pedidos_productos, backref='unificacion_pedidos')

class EventosUnificacionPedidos(db.Model):
    __tablename__ = "eventos_unificacion_pedidos"
    id = db.Column(db.String(40), primary_key=True)
    id_entidad = db.Column(db.String(40), nullable=False)
    fecha_evento = db.Column(db.DateTime, nullable=False)
    version = db.Column(db.String(10), nullable=False)
    tipo_evento = db.Column(db.String(100), nullable=False)
    formato_contenido = db.Column(db.String(10), nullable=False)
    nombre_servicio = db.Column(db.String(40), nullable=False)
    contenido = db.Column(db.Text, nullable=False)