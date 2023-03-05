from entregasalpes.config.db import db

Base = db.declarative_base()

ordenes_productos = db.Table(
    "ordenes_productos",
    db.Model.metadata,
    db.Column("orden_id", db.String, db.ForeignKey("ordenes.id")),
    db.Column("serial", db.String),
    db.Column("descripcion", db.String),
    db.Column("precio", db.Integer),
    db.ForeignKeyConstraint(
        [ "serial", "descripcion", "precio"],
         ["productos.serial", "productos.descripcion", "productos.precio"]
    )
)
class Producto(db.Model):
    __tablename__ = "productos"
    serial = db.Column(db.String(10), nullable=False,primary_key=True)
    descripcion = db.Column(db.String(100),  nullable=False, primary_key=True)
    precio = db.Column(db.Integer, nullable=False, primary_key=True)
    fecha_vencimiento = db.Column(db.String, nullable=False, primary_key=True)

class Orden(db.Model):
    __tablename__ = "ordenes"
    id = db.Column(db.String, primary_key=True)
    id_cliente = db.Column(db.Integer, nullable=False)
    fecha_creacion = db.Column(db.String, nullable=False)
    productos = db.relationship('Producto', secondary=ordenes_productos, backref='ordenes')

class EventosOrden(db.Model):
    __tablename__ = "eventos_orden"
    id = db.Column(db.String(40), primary_key=True)
    id_entidad = db.Column(db.String(40), nullable=False)
    fecha_evento = db.Column(db.DateTime, nullable=False)
    version = db.Column(db.String(10), nullable=False)
    tipo_evento = db.Column(db.String(100), nullable=False)
    formato_contenido = db.Column(db.String(10), nullable=False)
    nombre_servicio = db.Column(db.String(40), nullable=False)
    contenido = db.Column(db.Text, nullable=False)