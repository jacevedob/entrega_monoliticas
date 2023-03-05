CREATE TABLE hoja_ruta(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    producto VARCHAR(255),
    cantidad VARCHAR(255),
    bodega_centro VARCHAR(255),
    id_orden VARCHAR(255),
    id_bodega VARCHAR(255),
) COMMENT 'Tabla hoja de ruta';