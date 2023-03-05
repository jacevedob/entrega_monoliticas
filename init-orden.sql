CREATE TABLE ordenesbase(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    fecha_creacion VARCHAR(10),
    id_cliente VARCHAR(255)
) COMMENT 'Tabla de ordenes';