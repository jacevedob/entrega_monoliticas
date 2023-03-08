CREATE TABLE unificacion_pedidos(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    direccion_recogida VARCHAR(100),
    direccion_entrega VARCHAR(100),
    fecha_recogida VARCHAR(10),
    fecha_entrega VARCHAR(10),
    estado VARCHAR(20)
) COMMENT 'Tabla de unificacion pedidos';


