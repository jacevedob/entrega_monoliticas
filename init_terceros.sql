CREATE TABLE hoja_ruta(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    producto VARCHAR(255),
    cantidad VARCHAR(255),
    bodega_centro VARCHAR(255),
    id_orden VARCHAR(255)
) COMMENT 'Tabla hoja de ruta';
CREATE TABLE ordenes(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    fecha_creacion VARCHAR(10),
    id_cliente VARCHAR(255)
) COMMENT 'Tabla de ordenes';
