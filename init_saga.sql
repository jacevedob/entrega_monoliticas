CREATE TABLE saga(
    identificador int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    source VARCHAR(100),
    status VARCHAR(100),
    id VARCHAR(100)
) COMMENT 'Tabla saga log';


