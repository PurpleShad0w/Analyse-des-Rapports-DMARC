import mysql.connector

with open('root.txt', 'r') as file:
    user, pwd = file.read().split('\n')

create_db = """
    CREATE TABLE LICENSES (
    record_id INTEGER,
    mac VARCHAR(255),
    email VARCHAR(255),
    type VARCHAR(255),
    feature VARCHAR(255),
    until DATE,
    key_ VARCHAR(255),
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