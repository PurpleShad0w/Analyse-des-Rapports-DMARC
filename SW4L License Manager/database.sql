CREATE DATABASE LICENSE;
CREATE TABLE LICENSES (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    mac_address VARCHAR(255),
    license_feature VARCHAR(255),
    license_type VARCHAR(255),
    license_key VARCHAR(255),
    valid_until DATE,
    status VARCHAR(255)
)