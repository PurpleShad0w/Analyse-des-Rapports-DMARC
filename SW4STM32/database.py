import mysql.connector

with open('root.txt', 'r') as file:
    user, pwd = file.read().split('\n')

create_db = """
    CREATE TABLE LICENSES (
    record_id INTEGER,
    mac_address VARCHAR(255),
    client_name VARCHAR(255),
    client_email VARCHAR(255),
    license_type VARCHAR(255),
    license_features VARCHAR(255),
    expires DATE,
    currently_effective BOOLEAN,
    PRIMARY KEY (record_id))
    """


mydb = mysql.connector.connect(host="localhost", user=user, password=pwd)
mycursor = mydb.cursor(buffered=True)
mycursor.execute('CREATE DATABASE LICENSE')
mydb.close()

mydb = mysql.connector.connect(host="localhost", user=user, password=pwd, database='LICENSE')
mycursor = mydb.cursor(buffered=True)

mycursor.execute(create_db)
mydb.commit()