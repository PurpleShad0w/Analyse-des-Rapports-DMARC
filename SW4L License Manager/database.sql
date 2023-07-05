CREATE DATABASE LICENSE;
CREATE TABLE LICENSES (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    created_at DATETIME,
    updated_at DATETIME,
    mac_address VARCHAR(255),
    email_address VARCHAR(255),
    license_type VARCHAR(255),
    license_feature VARCHAR(255),
    valid_until DATETIME,
    license_key VARCHAR(255)
)